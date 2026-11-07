## SYSE.25 - Decide Whether and How to Improve a Platform from Practitioner-Task Evidence

> **Status:** Stable

> **Normativity:** Guidance within the stated engineering use; examples are illustrative.

### SYSE.25:1 - Problem frame

Use this pattern when practitioners repeatedly wait, redo work or ask for help through a platform, but the next investment is justified only by a preferred tool, adoption target or loud complaint. Choose one user population and one engineering undertaking. Observe how people try to obtain its result, including attempts that fail, are abandoned or fall outside the supported route.

The first useful result is one task-grounded choice to retain or change provision, a discriminating probe or a named missing-premise return. The governed question is whether and how to improve the enabling System and its provision for that work.

A software developer waiting for reliable feedback, a test engineer reconstructing a bench setup and a manufacturing engineer chasing an inspection result can all face this question. Their professional operations differ. This pattern selects what enabling difficulty to address; it does not provide every missing professional Method. For a one-off missing credential, ask the person who can supply it. An already justified implementation can go directly to its supplying Method.

### SYSE.25:2 - Problem

Platform work can become a list of internal features while users still cannot complete the task that matters. A new interface may make submission pleasant without changing waiting, error or recovery. Conversely, a reduction in visible support tickets can mean that users gave up or transferred the work to another team.

The selection problem is to connect a proposed enabling change to a consequential user result and an observation that could prove the proposal wrong. Frequency, satisfaction and adoption can contribute evidence, but none alone establishes that connection.

### SYSE.25:3 - Forces

| Force | Practical tension |
| --- | --- |
| Representative use | Common tasks offer leverage; rare failures or excluded variants can still carry large consequences. |
| Local gain and transferred burden | Less developer work can require more provider work, and faster throughput can increase recovery cost. |
| Evidence and timely action | Waiting for exhaustive measurement delays useful repairs; selecting from anecdotes can fund the wrong mechanism. |
| Standardization and variation | A common improvement can serve many users without making every legitimate task identical. |

### SYSE.25:4 - Solution

#### SYSE.25:4.1 - Bound one population and undertaking

Name the users, task, required result, supported variants and interval being examined. Follow the work far enough to see whether its result is usable by the next consumer. Keep distinct, for example, submitting a build, obtaining an identified package and releasing an application.

Include unsuccessful and unsupported attempts. A sample drawn only from completed backend jobs misses people who could not enter the route. Record exclusions when they could change the choice. Use a short observation or an existing operational account when it suffices.

Recover the relevant current configuration and conditions. A difficulty in one environment, shift or service class does not automatically characterize every user.

Build the observation around the task rather than around a platform feature. Ask a practitioner to reconstruct the last attempt using its actual inputs, returned results and help received. Observe another attempt when the reconstruction leaves a consequential gap. Combine this with provider records for the same attempt. An interview can reveal why a user bypassed the path; backend timing can establish where a job waited. Neither replaces the other.

Select contrasting cases that can expose the suspected difficulty: a routine success and a failure, experienced and occasional users, an ordinary variant and the important exception. This is purposeful diagnosis, not a representative prevalence estimate. State which population is covered before reporting a rate. If an urgent rare failure already defeats an essential result, do not postpone it merely to collect more frequent minor complaints.

#### SYSE.25:4.2 - Locate the burden without inventing its cause

Separate active practitioner work, waiting, error, rework, diagnosis and assistance. Follow the burden across users and providers rather than optimizing one team's visible time. Preserve missing observations; do not turn an unobserved abandoned attempt into a success.

Ask what actually obstructed the result. Possibilities include an unavailable enabler, an unreliable technical operation, unclear interaction, inadequate capacity, a missing authorized decision, an invalid Method or an unsettled desired result. These lead to different work.

Ask the person authorized to grant the missing permission. Return a missing professional Method or acceptance meaning to the relevant engineering specialist. Consider platform repair when the enabling System or supported use can change the observed difficulty. Use SYSE.12 when the broader platform's actual participation, capability or provision must first be established.

Follow one obstruction through its dependencies. If developers wait for access, determine whether a decision is waiting, an already granted right has not taken effect, or the resource itself is unavailable. Changing the entry form cannot remove that obstruction unless it also changes the operation that creates it. If developers repeatedly ask which package was tested, connect the test result to its actual artifact before diagnosing a training need. These observations discriminate mechanisms; a complaint category alone does not.

Preserve the arrangement of time and work. Two concurrent waits should not be added as if they occurred in sequence; a fast operation that queues behind one shared specialist can still dominate the user's completion time. Compare the task's completion with the earliest point at which all its needed results are jointly usable. Ask whether removing the suspected obstruction would let the task finish, or merely expose the next missing input. This yields a bounded improvement hypothesis and its dependencies rather than a ranking of individually slow tools.

#### SYSE.25:4.3 - Construct competing improvement hypotheses

For each serious candidate, state the difficulty it should change, the proposed mechanism, the expected user result and the observation that would disconfirm it. Compare it with retaining or simplifying current provision and with attainable repairs to that provision, including each option's full burden.

Compare the same task, acceptance meaning, supported variation and evidence horizon. Include user and provider effort to use, maintain and support the changed provision, migrate to it, and restore operation after failure. Preserve constraints such as unavailable expertise, confidential data and an existing service commitment without treating a constraint label as proof of feasibility.

A disagreement about the whole obtaining arrangement—local provision, a shared service, an external provider or a mixture—uses SYSE.24's complete comparison. The present choice may identify a result worth improving while leaving that obtaining comparison tied.

Construct alternatives by changing the mechanism, not just the supplier's brand. For an access wait, plausible alternatives may activate an already granted right earlier, supply a supported standard request, reserve provider assistance, or alter resource provision. Retaining a qualified assisted route is a real alternative when demand is small or judgement is irreducible. Automation is a candidate when repeated, sufficiently understood operations can be performed and recovered under known conditions. A proposed standard path should state which variations it absorbs and which it deliberately leaves to assistance.

Follow each candidate through the whole bounded task. Include the work needed to prepare its inputs, learn its use, interpret failure and sustain its providers. Check shared constraints: saving ten minutes for each user may consume the only specialist hour needed for another supported task. Reject an option that cannot meet a necessary condition; compare the remaining options by their consequential differences. When neither dominates, expose the accepted trade-off or retain a tie. A weighted score is useful only if its scales and weights express the deciding participants' actual preferences.

Keep the implementation increment coherent. An artifact-identity repair may require a producer to return the identity and a consumer to preserve and display it. Funding only the first half would not deliver the improvement. Conversely, it need not wait for unrelated portal, deployment and training work. SYSE.26 develops the supported path through the affected operations; SYSE.20 supplies the reconciliation when shared Work or resources create a real conflict.

#### SYSE.25:4.4 - Select a justified next action

Retain current provision when the comparison supports it. Choose a bounded repair when evidence already distinguishes it and its conditions can be met. Choose a probe when its attainable result could change the choice enough to justify its cost and delay; use C.11.DUA when that comparison is unresolved. Specify what the probe will hold comparable, what it observes, and how its possible outcomes change the next action.

Do not conceal a tie with an arbitrary score. A useful probe can be a representative attempt, a comparison of two repaired interactions, or an exercise of one costly failure. Keep the chosen next result and its permission with the actual decision holder.

Stop with a missing-premise return when neither a justified action nor a worthwhile permitted probe is available. Continue independent work whose premises are already supplied.

Make the probe discriminate the competing explanations. Identify the same task outcome on both sides, the material conditions to hold comparable, the observation that distinguishes the mechanisms, and what each possible observation permits next. A guided demonstration may find an interface defect, but it cannot establish independent user success if the guide supplies missing operational knowledge. Record that assistance as part of the tested arrangement.

Use comparable attempts where attainable, including their failures. If the only affordable design is a before/after trial, inspect changes in workload, user preparation, configuration and provider availability that could also explain the result. Keep the causal conclusion conditional when those differences remain. A small trial can reject a broken join or support a bounded continuation without estimating a population-wide productivity effect.

#### SYSE.25:4.5 - Revisit the choice from actual use

After the permitted change or trial, compare the relevant task results under sufficiently matching conditions. Include unsuccessful attempts and provider burden. Keep observed improvement, a plausible causal explanation and an untested expectation distinct.

A local improvement can be retained while its broader rollout remains unqualified. New use can select a different next improvement, expose an unsupported variant or justify retirement through SYSE.29. Use this same Method when the question recurs.

For software-service task measurement, SYSE.36 supplies the subject, eligible attempts, good result and missing-observation distinctions. If the issue becomes actual adoption of a Method across a population or cultural continuation, use SYSE.21 rather than treating one successful task as a cultural change.

The return is selective. If only the implementation is defective, repair that operation and retain the task choice. If a new variant no longer fits the supported path, revisit its scope through SYSE.26 or its extension through SYSE.27. If results improve for users while provider recovery becomes unsustainable, reopen the complete arrangement. A changed need can make simplification or retirement preferable. Do not preserve the investment merely because the pilot once succeeded.

### SYSE.25:5 - Archetypal Grounding

ParcelWorks provides an invented example. In twenty service-release attempts, six require repeated infrastructure contacts, four include tests that pass on unchanged inputs after a rerun, two use different package bytes under the same source label, and one attempted rollback fails after a column rename. These counts overlap; they are not thirteen distinct failed releases.

The team initially proposes a portal, a shared delivery path and more developer training. It first selects a bounded question: can developers obtain and retain the identity of the package whose test result they intend to use? This question does not claim to repair the flaky tests or the data-recovery failure.

Two reconstructed attempts show that the visible source label already agrees while package bytes differ. Merely displaying that label more prominently cannot resolve the problem. The training hypothesis would need evidence that developers can already obtain the needed identity and fail to use it; that evidence is absent. Preserving and returning the exact artifact identity is a plausible different mechanism.

The chosen next result is a limited comparison of the current interaction with an identity-preserving repair for one supported service class. Both use the same source change, test question and result consumer. The probe observes whether the developer can identify the tested bytes without a separate reconciliation contact, including the case in which transfer fails. It also observes provider work; a new manual identity-reconciliation step hidden behind the interface would not be the intended gain.

This selects an improvement question and probe, not a shared-platform winner. The identity and environment repair can be implemented locally or through a thin shared provision. Without matched maintenance and failure evidence, those complete obtaining arrangements remain tied under SYSE.24. The unsupported language-specific variant remains outside the probe.

If the comparison removes identity confusion but slow or unreliable feedback remains, the next question goes to SYSE.31. A healthy artifact path does not repair the old rollback failure; that still needs the actual data construction in SYSE.34.

Suppose the bounded trial contains six matched attempts. On both routes, the same two artifact transfers fail once. The repair returns the tested artifact identity in all six outcomes, including the failures, and the developer can distinguish retrying a transfer from rebuilding a package. The existing route requires two manual identity reconciliations. The provider performs no new per-attempt reconciliation. This supports the functional result for the tested service class; a repair that merely hides the two failed transfers would fail the question.

To decide whether to retain this local repair, the provision owner compares twelve planned attempts over the next quarter. The following bounded estimates cover preparation, use, producer/consumer identity maintenance, assistance and recovery. Unchanged build and testing Work is equally supported in both arrangements. The provider's available windows can meet the task deadlines; the eight-hour allowance below is additional to its protected commitments.

| Local arrangement | Practitioner effort | Provider effort and provision |
| --- | --- | --- |
| Existing qualified route | Six hours, including identity reconciliation and failed-transfer handling. | Four hours for maintenance, assistance and recovery, including return from the trial to this route. |
| Retain the identity-preserving repair | Two hours for result use and failed-transfer handling. | Seven hours: one for completing the producer/consumer change, two for continuing identity-relation maintenance, and four for assistance and recovery. Qualified performers and the needed windows are available within the eight-hour allowance. |

The owner is authorized to allocate that allowance and accepts three more provider hours to save four practitioner hours while preserving identified outcomes. It retains the repair for this quarter and service class, with the prior route available as a qualified fallback. This local choice does not settle the separate local/shared obtaining comparison: matched maintenance and failure evidence for the shared alternative is still missing. Nor do the six trial observations establish faster testing or a general productivity effect.

Change only the provider allowance before that commitment: another protected undertaking leaves five hours available. The seven-hour repaired arrangement no longer fits, while the four-hour prior route does. The owner keeps the prior route for this period and returns the repair's additional provision need for reconsideration. The six functional observations remain valid. User-side improvement has not supplied the missing provider capacity or authority to displace the other undertaking.

A second team performs one exceptional inspection per quarter using a format for which no automated identity relation is available. The inspection and its result are already qualified. An authorized inspector can apply a qualified manual reconciliation that preserves specimen/configuration identity in the returned result. For the coming quarter, preparation and maintenance take fifteen minutes and the assisted task takes thirty; the inspector has an agreed one-hour window before the receiving deadline. The user's fifteen minutes and the available correction/return procedure are included. Extending the automated path instead requires three provider hours, unavailable in that window. The provision owner accepts the forty-five-minute assisted arrangement for this use. Identical interfaces are unnecessary for the two teams' identified results. If the inspector or the permitted source is unavailable, the team retains this as a candidate and returns that provision gap before using it; the ordinary software branch remains supported.

In an unlike physical example, engineers wait for inspection results after coating. An observation finds that the measurement setup is qualified but the returned report omits specimen configuration, so engineers repeatedly ask the inspector which item was measured. A bounded report/transfer repair may help. If instead coating changes the measurement relation and no valid procedure exists, the same complaint returns a metrology Method gap; faster report delivery cannot qualify the measurement.

### SYSE.25:6 - Bias-Annotation

Frequent users, articulate experts and platform maintainers can dominate observations. Sample abandoned and assisted attempts as well as successful ones. Avoid treating a task's frequency as its whole consequence, or treating a preferred tool as the cause of every observed difficulty.

### SYSE.25:7 - Conformance Checklist

- The user population, task, result and relevant conditions are bounded.
- Failed, abandoned and unsupported attempts are visible where they can change the choice.
- Waiting, work, error and transferred support burden are not collapsed into one favorable number.
- Each serious improvement has a mechanism and a disconfirming observation.
- Alternatives, including attainable repairs, share a comparison basis; whole obtaining choices use SYSE.24.
- The result is an actionable choice, informative probe or named missing-premise return, with a revision condition.

### SYSE.25:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Repair |
| --- | --- |
| Adoption proves value. | Observe whether the users' required results improve and what burden moves elsewhere. |
| All support requests justify automation. | Recover whether the missing element is provision, a Method, a fact or authority. |
| The favorite repair is compared with a broken incumbent while an attainable incumbent repair is omitted. | Include that repair and its full burden, then compare the options' remaining consequences on the same basis. |
| A small successful pilot is treated as universal coverage. | Preserve its population, variants and conditions; qualify wider use separately. |

### SYSE.25:9 - Consequences

Platform work gains an explicit connection to practitioner results. Some attractive features lose priority, and some real problems return outside the platform team's authority or expertise. Observation and comparison cost effort.

### SYSE.25:10 - Rationale

An improvement is useful through the result it changes, not through the amount of platform functionality added. A disconfirming observation makes that proposed connection testable. Comparing total burden and retaining ties prevents the selection process from rewarding invisible work transfer or a preferred architecture.

### SYSE.25:11 - SoTA-Echoing

**Adapt** task discovery and feedback from [DORA Platform engineering](https://dora.dev/capabilities/platform-engineering/), a software practice guide. This selects the user undertaking as the unit for sections 4.1–4.3.

The [2025 DORA report](https://dora.dev/research/2025/dora-report/), platform chapter, gives a different source contribution: observed capability ratings and model-dependent outcome estimates. Its association between clear task feedback and favorable experience motivates examining that mechanism. It does not prove that this local repair causes improvement. Its reported increase in delivery instability also warrants retaining recovery and downstream results in the comparison.

A developed product-discovery approach already connects research, hypotheses and small trials. This pattern adopts that strength. Its additional engineering work is to follow each candidate through identified outputs, shared provision and the conditions of the consuming action. A complete applicable product-discovery method can supply the research; use sections 4.2–4.5 only for the remaining engineering connection.

Compared with immediate delivery of a well-understood repair, the investigation costs time and is unnecessary when the relevant value and conditions are already established. Compared with an unresolved feature request, the bounded trial can reject the wrong mechanism before committing to the whole arrangement. Reopen on changed users, transferred burden, consequential unsupported variation or a better available obtaining way. Software observations do not qualify the physical-inspection example.

### SYSE.25:12 - Relations

SYSE.12 establishes the platform's relation to practitioner work. SYSE.24 compares complete obtaining arrangements; SYSE.26 designs the supported interaction. SYSE.31 addresses software feedback and SYSE.36 supplies software-service task measurement. SYSE.29 handles migration or retirement and SYSE.39 addresses repetitive platform work. SYSE.21 concerns actual Method enactment and cultural continuation, not adoption statistics alone.

### SYSE.25:End
