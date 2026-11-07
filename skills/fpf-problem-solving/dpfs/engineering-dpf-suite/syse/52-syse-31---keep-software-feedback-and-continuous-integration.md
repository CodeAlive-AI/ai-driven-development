## SYSE.31 - Keep Software Feedback and Continuous Integration Fast and Trustworthy

> **Status:** Stable

> **Normativity:** Guidance within the stated software-engineering use; examples are illustrative.

### SYSE.31:1 - Problem frame

Use this pattern when developers wait too long to learn whether a change works, rerun failures until they disappear, or receive green checks that do not answer the current engineering question. Start with one change and the decision its feedback must support. Identify what each check can establish, on which source or artifact, under which conditions, and who can act on failure.

The first result is a usable feedback arrangement: maintained checks, interpretable outcomes and a bounded response to a failed or missing result. It is not a target number of tests or a universal time limit. The application team supplies the expected behavior; a software platform can make the feedback available without inventing that behavior or owning the release decision.

If adequate build and tests already exist and only integration of a small change is missing, go directly to the DORA continuous-integration Method in section 4.5. Do not redesign adequate feedback first. If the build inputs themselves cannot be recovered, use SYSE.30; if the conditions cannot be reconstructed, use SYSE.33.

### SYSE.31:2 - Problem

A slow result arrives after the developer has changed context or several changes have accumulated. An unreliable result makes repetition cheaper than understanding. A fast but irrelevant result is equally dangerous: the suite can pass on one branch, one fixture or one old artifact while the integrated application fails.

The aim is not merely quicker execution. It is earlier useful discrimination between a usable change, an actual regression, a broken test or environment, and a question for which evidence is still absent.

### SYSE.31:3 - Forces

| Force | Practical tension |
| --- | --- |
| Speed and reach | Small checks give early feedback; some behavior needs a running application, real integration or human exploration. |
| Stable tests and real variation | Controlled fixtures aid diagnosis; removing genuine concurrency or environment variation can remove the defect being sought. |
| Local ownership and cooperation | Developers need to repair feedback quickly while testers and domain specialists contribute different acceptance knowledge. |
| Availability and maintenance | Keeping every test forever increases burden; dropping a test can remove the only evidence for an important claim. |

### SYSE.31:4 - Solution

#### SYSE.31:4.1 - Connect a check to the decision

Name the changed behavior, the assertion under test and the result consumer. Recover the application team's acceptance meaning rather than deriving it from current implementation. A test that repeats the implementation's mistaken assumption is not an independent answer to the user question.

Bind each result to the source or artifact actually exercised, relevant configuration, test input and conditions. Distinguish a test description from a completed run. A missing run, lost observation or wrong artifact cannot be reported as a pass.

Begin with checks that discriminate the consequential failures for the current change. When necessary behavior is not specified well enough to judge, return that precise question to its owner. Do not hide it behind a large existing test count.

#### SYSE.31:4.2 - Put feedback where it can change the next action

Use fast focused tests for failures they can detect. Retain integration, acceptance, performance and exploratory work where their distinct results affect reliance. Choose the execution arrangement from those dependencies, not from a fixed proportion of test types.

Run relevant checks close enough to a change that the result remains actionable. Recover the actual waiting, execution and diagnosis time before choosing an improvement: a faster test does not repair a long queue or an unintelligible failure report. Parallel execution is useful only when isolation and capacity preserve the test's meaning.

A slower test can remain necessary. Make its unresolved result visible to the decision that needs it instead of presenting early fast checks as full acceptance.

#### SYSE.31:4.3 - Make a failure reproducible and interpretable

Retain the tested revision/artifact, inputs, relevant environment and failure observation. Compare a suspected regression with the previous qualified behavior under matching conditions when that comparison can distinguish the cause.

Investigate variable outcomes. Shared mutable fixtures, uncontrolled clocks, order dependence and unavailable services can corrupt feedback. A nondeterministic product race is still a product defect; calling a test “flaky” does not settle which object failed.

Control a suspected source of interference and repeat a discriminating case. Change only what the comparison can account for. A rerun may help diagnosis, but a later pass does not erase an earlier failure under supported conditions.

#### SYSE.31:4.4 - Decide who repairs which failure

| Observed problem | Immediate response |
| --- | --- |
| The tested product violates the agreed behavior. | Return the failing case to the application team and withhold the reliance that required it. |
| The test asserts an obsolete or incorrect expectation. | Resolve the expectation with its owner, repair the test and re-exercise the behavior. |
| The environment or provider failed before the behavior could be observed. | Return that failure for environment/platform repair; retain the missing product evidence. |
| The result cannot be attributed to the candidate or conditions. | Recover attribution or rerun the right case; do not transfer the old pass. |

Use the actual maintainers and their permissions. Platform operators can repair provision; they do not acquire authority to change application behavior, withdraw a source change or approve release merely because they operate the test service.

If a test must be quarantined, identify the claim whose evidence was lost, its current consequence and a usable temporary replacement or stop. Name the repair responsibility and the condition for restoring the check. Quarantine is not an unlimited exemption or a way to improve the displayed pass rate.


#### SYSE.31:4.5 - Construct a stream of small integrations into the current mainline

Continuous integration is a way of keeping separately developing changes usable together. A server that builds isolated branches supplies feedback but does not create that combined result. The [DORA CI Method](https://dora.dev/capabilities/continuous-integration/) is a directly usable starting treatment; the construction here explains its joins with the artifact, environment and recovery Methods in this framework.

First choose the integration boundary that matters to the application. Name the shared mainline and the components whose combination must work. One repository can contain independently deployable components, and several repositories can still contain a tightly coupled application. Use the actual compatibility relation to choose the integration checks. A repository boundary is not evidence that two changes can be released independently.

Break a large change into increments that leave the mainline usable under its existing supported behavior. A preparatory increment may add an unused adapter; a later increment may switch one caller to it; removal waits until no supported caller needs the old route. Each increment should preserve the agreed behavior or openly change it under its acceptance conditions. A feature flag can separate installation from activation only if the disabled state really preserves the required behavior and the enabled path can be qualified. A dormant flag does not make an incompatible schema change harmless.

For one increment, take a current mainline base, construct the intended combined change, and run the relevant fast feedback against that combination. Resolve its actual incompatibilities before integration. When another change advances the mainline, update the candidate combination and re-establish the affected feedback. A merge queue is one possible implementation: it serializes or rebuilds candidate combinations against the base that will actually be used.

After integration, build and exercise the resulting shared revision through the authoritative path. Associate its produced artifact with that combined revision and its own results. An earlier artifact from the branch can be reused only when it is actually the same qualified subject under the needed conditions. The team must be able to find the current mainline result and its unresolved checks without reconstructing several private branch histories.

When the integration breaks, protect other development from treating the broken state as a usable base. Make restoration the immediate shared task. If a narrow repair can promptly restore the intended combination, integrate and check it. Otherwise the authorized team can withdraw the offending change and verify the resulting mainline. Withdrawing source changes does not undo an already executed external effect or data migration; those returns have their own state boundary. Keep the failed observation and unresolved business conflict so that a later attempt does not repeat it.

Choose integration frequency and feedback latency together. If a team accumulates several days of interacting changes because every run takes hours, asking for more merges alone creates a queue of unresolved combinations. First find the constraining feedback and improve its execution, split a genuinely independent check, or redesign the change so that each smaller increment remains useful. Slow necessary evidence can run separately while its affected release claim stays open. The sought gain is a short interval to a trustworthy combined result, not a mandated merge count.

For the range example in section 5, A and B are individually small but incompatible in business meaning. No branch strategy can choose whether a minimum of 8 or a maximum of 5 is intended. CI makes that conflict visible while it is still bounded. By contrast, adding a disabled new form with a lossless old-format adapter can be a legitimate preparatory increment, because the old behavior and storage contract remain usable while the new form is being developed.

#### SYSE.31:4.6 - Keep the complete feedback path usable as changes accumulate

Arrange checks by what they need and which decision they can change. A source-level invariant may run before packaging. A binary compatibility check consumes the produced package. An interaction with a real database needs a qualified running environment. A user-interface task can need browser behavior and human interpretation that a backend check cannot supply. Put the cheaper informative failure first where these dependencies permit; preserve the later question even when the early stage is green.

Use a small representative change to build this path before multiplying its variants. Give each stage a way to identify the candidate, obtain its actual inputs and return an actionable failure. When the first stage passes and a later stage is waiting, the current result is partly qualified. Do not let a single green label erase the pending contribution. Nor should every slow stage unnecessarily block unrelated editing or an independently qualified artifact.

Derive test selection from affected behavior and dependency reach. If a shared schema generator changes, all consumers of its changed output may be affected even if their hand-written files are untouched. If a test-selection mechanism cannot recover that reach, include a wider check or leave the conclusion narrower. Inspect escaped regressions for missing reach as well as missing assertions. Reducing test time by assuming unproven independence simply moves detection to a later, more expensive use.

For example, ParcelWorks can check lossless address split/join quickly with boundary values; check its write adapter and trigger in the actual supported database arrangement; then exercise display and save in the browser. These are complementary observations. Passing the first does not make the other two redundant. A new runner that halves unit-test time but starves the database stage has not necessarily shortened time to a releasable result; include queue and diagnosis delay when choosing that change.


#### SYSE.31:4.7 - Verify that the arrangement improves useful feedback

Exercise a known passing case, a meaningful failing change and a failure of the feedback mechanism. Check that the responsible person can distinguish them and recover the tested subject. Inspect late-discovered defects: did the arrangement omit a needed question, use the wrong conditions, or fail to deliver its result in time?

Return the checks, their supported questions and conditions, remaining evidence gaps, and the actual failure-response arrangement. Improve from useful detection and repair, not from test count or green percentage alone.

### SYSE.31:5 - Archetypal Grounding

In a constructed ParcelWorks case, two address-service tests share the same fixture row. One test removes it during cleanup while another still reads it. The second test sometimes fails on unchanged application bytes; rerunning the suite merely changes the timing.

The developer first preserves the failing order and row identity. The fixture is then made independent for each attempt, with cleanup limited to that attempt's data. Repeating the conflicting order no longer destroys another test's input. A deliberately broken address transformation still fails its assertion. The repaired feedback therefore removed fixture interference without deleting the behavior check.

Now consider a different failure: an application permits parcel weights between a minimum and maximum, with the declared invariant minimum <= maximum. Mainline M0 has the range 1..10. Change A raises the minimum to 8; change B, developed from M0, lowers the maximum to 5.

| Tested state | Range | Feedback and consequence |
| --- | --- | --- |
| M0 | 1..10 | The invariant passes. |
| A on M0 | 8..10 | A's branch passes. |
| B on M0 | 1..5 | B's branch passes. |
| B combined with already integrated A | 8..5 | The invariant fails despite no textual merge conflict. |
| Withdraw B while retaining A | 8..10 | The rebuilt integrated result passes the invariant again. |

Testing B against the actual current mainline would reject it before integration. If stale branch feedback was nevertheless used, the post-integration check finds the bad combination and blocks artifact qualification. The authorized application team withdraws B and verifies the restored result. The team must resolve the conflicting business intent about the permitted parcel-weight range before B is attempted again.

Finally, fast data-transformation tests can pass while a new address form hides a non-empty display line. The application-level acceptance or exploratory result remains necessary for that user behavior. Running more fast unit tests cannot substitute for the missing observation.

What changes in practice is that a failed result has a usable owner and meaning, and a green result stays bound to the change and behavior it actually exercised.

### SYSE.31:6 - Bias-Annotation

Teams can optimize the measured feedback time by excluding slow but necessary questions, or optimize pass rate by suppressing real failures. Developers may also assume that a familiar fixture represents all supported use. Inspect escaped defects and missing observations, including the perspective of application users and testers.

### SYSE.31:7 - Conformance Checklist

- Each relied-on check has a concrete question, subject and applicable conditions.
- The arrangement retains distinct slow or human evidence where the decision needs it.
- Product, test, environment and missing-observation failures receive different responses.
- Quarantine exposes the lost assurance and a replacement or stop.
- Integration feedback concerns the current combined mainline, not only isolated branches.
- Repair work has an assigned maintainer; source withdrawal and release require the applicable authorization.

### SYSE.31:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Repair |
| --- | --- |
| Rerun until green. | Preserve and explain the failed observation; use repetition diagnostically. |
| Delete the slowest test to meet a time target. | Recover the claim it answered and retain an adequate result or explicit limitation. |
| Two green branches imply a green mainline. | Exercise the current combined revision and restore it when the integration fails. |
| Infrastructure failure is reported as product success because no assertion failed. | Mark the product observation missing and repair the feedback mechanism. |

### SYSE.31:9 - Consequences

Useful feedback can shorten the interval between a change and an informed response. It requires continuing test and environment maintenance and can expose missing acceptance knowledge. Faster feedback is not always less testing; sometimes the gain is a clearer failure or a smaller integrated change.

### SYSE.31:10 - Rationale

Feedback is useful only when it helps answer the current question and arrives where someone can act on it. Subject attribution, credible failure meaning and repair ownership protect that connection. Mainline integration supplies an additional result that branch-local build and tests cannot establish.

### SYSE.31:11 - SoTA-Echoing

For prompt feedback and a usable combined mainline, **adopt and adapt** [DORA Test automation](https://dora.dev/capabilities/test-automation/) and [Continuous integration](https://dora.dev/capabilities/continuous-integration/). Their developed professional line already joins small integrations, maintained tests and rapid restoration. The [Continuous Delivery deployment pipeline](https://continuousdelivery.com/implementing/patterns/) arranges successive evidence across an integrated delivery path.

Sections 4.5–4.7 construct those joins for the actual shared base, artifact and environment. Compatible preparatory increments compete with a longer branch; fast scoped tests compete with broader slower checks. Select from interaction risk, feedback delay and recoverability, retaining a pending release question where necessary. A faster early stage that delays the whole useful result is not the intended gain.

Reopen test selection or integration structure when architecture, generated dependencies or supported behavior changes, regressions escape, or restoration no longer fits the working cadence.

### SYSE.31:12 - Relations

SYSE.30 supplies recoverable build inputs; SYSE.33 supplies development and test conditions. The DORA CI Method in section 4.5 supplies actual small-change integration when that is the missing result. SYSE.32 consumes artifact-specific evidence, SYSE.41 performs deployment, and SYSE.36 distinguishes observations of platform tasks from application tasks. SYSE.4 and SYSE.14 govern evidence reliance and release decisions respectively.

### SYSE.31:End
