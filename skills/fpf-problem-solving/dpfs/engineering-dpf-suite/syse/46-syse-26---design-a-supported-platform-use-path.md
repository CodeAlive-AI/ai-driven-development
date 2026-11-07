## SYSE.26 - Design a Supported Platform-Use Path

> **Status:** Stable

> **Normativity:** Guidance within the stated engineering use; examples are illustrative.

### SYSE.26:1 - Problem frame

Use this pattern when a practitioner knows the engineering result needed next but must repeatedly discover how to request it, which inputs are acceptable, what a delay or failure means, or how to recover. A developer asks for a test environment, a test engineer asks for a bench run, or a manufacturing engineer asks for an inspection result. The available tools may work while the interaction between their users and providers remains unreliable.

Start with one representative attempt and say what the user supplies, what usable result should return, and which conditions make the attempt supported. Construct a way of obtaining that result through the available operations and providers; then design its interaction through success, variation, waiting and failure. The first useful result is an explained supported path whose operations fit together, with a trial or a precise missing provision identified. A description supplies a design; actual support needs capable providers, effective access and evidence from the intended use.

The intended reader understands the professional task and can obtain its specialist results. The new work here is to organize their use through the platform: connect inputs and returned results, preserve the conditions needed by the whole attempt, and give users and providers a workable continuation. A catalogue of available services is insufficient when these connections remain to be designed.

Platform Engineering concerns Systems that enable their users' work. This pattern concerns one way of obtaining a result through those Systems and their providers, not every aspect of the platform. If the desired improvement is still unclear, use SYSE.25 to choose it. If complete alternative obtaining arrangements must be compared, use SYSE.24. If the interaction is already clear but the underlying professional operation is not qualified, address that operation rather than redesigning the entry form. An already sufficient one-off tool result needs no supported-path redesign. When the provider's offered result and conditions themselves are unclear, use SYSE.8 to develop that provider concept before making the promise.

### SYSE.26:2 - Problem

A user can submit a valid request yet receive only a job number, a generic error or a link to an obsolete result. A provider can report technical completion while the user still lacks the configuration, evidence or access needed for the next engineering action. Repeating the request may create a second environment or repeat a physical operation that cannot be undone.

The missing engineering work is to connect the user's undertaking to the actual accepted inputs, operations, returned result and support. The connection must survive the cases users really encounter, not only a provider's successful demonstration.

### SYSE.26:3 - Forces

| Force | Practical tension |
| --- | --- |
| Simple entry | Hiding irrelevant implementation detail helps; hiding a condition that changes the result makes use unsafe. |
| Supported variation | A common route reduces repeated effort, but one rigid template can exclude legitimate work. |
| Retry and recovery | Users need a next move after uncertainty; repetition can duplicate an already completed effect. |
| Low coordination | Self-service can reduce case-specific assistance, while maintenance and exception support still need capable providers. |

### SYSE.26:4 - Solution

#### SYSE.26:4.1 - Begin with the user's completed undertaking

Walk through an actual or explicitly constructed attempt with a representative user. Ask what they will do with the result: compare a model, test a change, release a configuration, or accept a manufactured item. Work backwards from that use to the input and returned result sufficient for that use.

Keep the user's result separate from intermediate provider activity. An accepted request, a booked slot, a running job and an inspected item are different results. A booking may be sufficient when the user is scheduling; it is insufficient when they are deciding whether a component passed a test.

Name the System or provider that supplies each indispensable operation. Recover existing configuration identities and conditions through SYSE.13. When a professional Method is missing, name its required result and supplier. A clear description of a missing operation is useful for design, but does not justify promising that operation to users.

Construct the path backwards from the receiving action. For an acceptance test, a running environment may be insufficient: the test also needs the intended package, a compatible data state, effective access and enough remaining lifetime. For each needed condition, ask which existing operation can establish it, what that operation requires and who can supply it. Continue only until the inputs are already obtainable or a missing operation is precise. This locates the actual work to design, including preparation that precedes the visible request.

Then follow a proposed attempt forwards. At a consequential join, establish that the preceding result is the right subject, configuration and state for the receiving operation. Convert representations where a known rule preserves meaning; obtain missing information where no conversion can supply it. A source revision does not identify built bytes; a credential issued to one principal does not establish access for another; a specimen number does not establish its current treatment. The join must deliver the needed condition, not just a field with the expected name.

Explain how the operations fit together. Preparation may proceed independently while waiting for a resource, but only if it does not depend on that resource's later identity or mutable state. Serialize the operations whose effects depend on each other. Reserve or sequence shared resources when simultaneous demand would defeat the result. For a provisional design, show the condition that must still be established; do not replace it with the word “integrated.”

Check conditions that span several operations. A result's validity must reach its use; data preparation must fit within the environment's available lifetime; the expected demand must fit the available capacity and support; two uses of the same resource must be compatible. Repair the specific mismatch by changing order, obtaining a longer window, reserving provision, changing a constituent or narrowing the supported attempt. A passing test of every component separately leaves these joint conditions open.

Keep the professional suppliers intact. SYSE.30 and SYSE.32 can supply an identified and appropriately verified software artifact; SYSE.33 supplies the environment construction; SYSE.34 supplies the relevant persistent-data compatibility or recovery result. Use only the contributions the task needs. The supported path explains what it receives from them and how their outputs become usable together; it does not replace their Methods with generic “build,” “deploy” or “restore” labels.

#### SYSE.26:4.2 - Bound the supported interaction

Choose a bounded, coherent class of supported attempts. Determine the required input, valid variants, applicable permissions, limits, return format and conditions under which the result is usable. Expose only the choices users need to make; derive safe defaults from known facts rather than guessing omitted engineering conditions.

For each material variation, choose a supported route, a provider-assisted route, an extension request or an explicit unsupported answer. An unsupported but legitimate request is not an invalid request. Do not coerce it into a template whose result answers a different question. Use SYSE.27 when contributors need a maintained extension path.

Use an interface already natural for these users when it suffices: a callable operation, a command, a workbench interaction or a short agreed request can provide the supported interaction. A new portal is justified only by an additional user result. Pass required credentials through the applicable protected authentication mechanism; keep its secret material out of task request and response payloads, displays and diagnostics. Determine which task information is necessary and permitted in the input, returned result and display, who may receive it, and how it is protected. Preserve necessary personal data within those permissions and protections; omit sensitive details that the receiving action does not need. Keep diagnostic detail to what its authorized recipient needs to understand the result or take the next action. If a necessary permission is unavailable, return that condition to the person authorized to grant it before the affected operation.

Generate more than one feasible form when the interaction arrangement is unresolved. An assisted path can have a practitioner submit the engineering question and a qualified operator supply the result. A self-service path can expose an understood, repeatable operation with appropriate observation and recovery. A hybrid can automate preparation and ordinary execution while returning a consequential exception to a specialist. Begin from existing tools, qualified operations and actual assignments; a new interface is only one possible change.

Compare these forms for the same supported task. Ask which decisions users must understand, how often assistance is needed, what happens under a legitimate variant, and what support must remain available. A documented procedure can be the thinnest sufficient path when its users can follow it and its providers can support it. An automated wrapper may be thinner in the user interface while moving considerable integration and recovery work into the provider. Include that work in the comparison.

Choose the abstraction boundary by the user's decisions. Hide provider-specific configuration that the path can derive reliably. Expose an operating range, data class, expiry or trade-off when users must select it to obtain the right result. Supply a safe default only where its applicability is known; keep a supported route for variations that cannot use the default. If experienced users compose the underlying capabilities differently, make clear which whole-use conditions they must re-establish and what support applies.

Place already justified controls through SYSE.28 while constructing the path. A required control is one of the conditions the receiving action needs; its unavailable result can change which continuation is possible. This may alter an otherwise convenient ordering. Treat a change to the control's constraint or authority as a separate decision, not as an interface convenience.

#### SYSE.26:4.3 - Make progress, result and uncertainty distinguishable

Decide what the user can observe at the points that change their next action.

| Situation | What the user needs to know | Admissible next move |
| --- | --- | --- |
| The request was not accepted | Which input or permission is missing, and whether any effect occurred. | Supply the required input or request the missing permission from the person authorized to grant it. |
| Work was accepted and is waiting or running | A retrievable attempt identity, present progress and the meaningful limit or support condition. | Observe the same attempt; cancel only under the stated cancellation semantics. |
| The operation completed | The returned result, its configuration and usable conditions, not merely the worker's exit status. | Use the result for the named next action. |
| The operation failed or its state is unknown | Observed partial effects, remaining uncertainty and the safe recovery or support return. | Reconcile actual state before a replay that might duplicate effects. |

These are semantic distinctions, not compulsory status labels or a universal workflow. A synchronous operation may need no persistent job record. An operation with uncertain external effects needs enough stable identity and observation to recover the same attempt.

Design reattempt and cancellation around the actual effects. If a provider can look up an earlier attempt, use that lookup before creating a replacement. If it cannot establish whether the effect occurred, return the uncertainty and restrict further action. Cancellation of a request does not necessarily cancel provider work or reverse a completed effect. Domain-specific state recovery remains with its qualified Method; software/data recovery uses SYSE.34.

#### SYSE.26:4.4 - Keep support connected to the failed use

Make the support return available where the user encounters the failure. Carry the attempt identity, relevant input/configuration, observed result and last safe action, subject to confidentiality. The user should not have to reconstruct a hidden chain of provider job numbers.

Determine who can actually investigate or repair the provision and which promise is in force. If the assignment is missing, ask the person authorized to assign support who will provide it; a support-link label does not appoint a provider. Keep the user's continued-work option visible, including a bounded manual route when it is usable and permitted.

Arrange support for the scope actually promised. Establish when diagnosis is available, which provider can observe or change each consequential effect, and how a case crosses provider boundaries without making the user rediscover them. A platform team need not operate every backing service, but a supported path needs an attainable continuation when one fails. If the named operator is available only during a shift, either arrange further support or bound the promise accordingly.

Explain the path's technical decisions to practitioners and contributors. Demonstrate an ordinary attempt and the failure where the next move differs: for example, retrieving an uncertain creation rather than creating a second resource. Let a user perform the attempt and explain the returned result. Repair the description or preparation when the missing knowledge belongs to supported use; retain necessary specialist assistance in the arrangement. This technical leadership develops shared understanding of the selected design. Assigning Work, granting rights and authorizing exceptions remain with their actual holders.

#### SYSE.26:4.5 - Exercise the interaction before relying on it

Try the supported case with a representative user and the intended result consumer. Select further cases from the supported variants and actual failure modes: a valid variation, an invalid or unsupported request, delay where timing matters, and interruption where an operation's effect may already have occurred. Check that each selected case leaves an intelligible next move and preserves the result's identity.

A desk walkthrough tests the description. A trial against the actual provision tests more: whether the request reaches the right System, the operation works under the stated conditions and the result can be used. Keep those evidence claims separate. SYSE.12 distinguishes a readiness assessment made before relying work from a later assessment of actual use; SYSE.36 helps observe software-service user tasks. Stop at the design result or bounded trial result that the current decision needs.

Select trial conditions from the design's actual failure modes. If short-lived access is the critical join, include a delayed preparation. If two operations share the only resource, exercise the intended overlap or its enforced exclusion. Observe what the practitioner can complete and what the provider must do, including any assistance supplied during the trial. Increase reliance only within the conditions that the evidence covers. A well-explained prospective path may be a useful design result while a capability or an unavailable provider still prevents its realization.

#### SYSE.26:4.6 - Adapt the affected construction

Start with the changed condition and identify the operation or join that relied on the old value. A longer data setup can require earlier preparation or a longer environment lifetime. A new user group may require a different entry or teaching arrangement while the construction remains valid. A changed provider response can require an adapter or a different recovery operation.

Compare the affected alternatives at the whole-task boundary. Extending a lifetime can solve the user's problem and exceed the shared resource budget; preparing earlier can solve the budget problem and use data that is stale at execution. Derive the supported continuation from both conditions. Reuse unaffected operations and evidence, exercise the changed join and its failure branch, and update the description used by the next practitioner. If no construction fits, return the precise missing provision or reconsider the desired result through SYSE.25. A broader change in obtaining arrangement returns to SYSE.24.

### SYSE.26:5 - Archetypal Grounding

A constructed ParcelWorks example begins with: “Give me an isolated preview environment for service change r17, so I can run the address-form acceptance test.” Developers already have a CI entry and a registry; a new user interface is not assumed necessary.

The supported request identifies r17, the chosen service variant, a versioned environment recipe and synthetic test-data set s4. The response must identify the created environment, its observed configuration, access instructions and expiry condition. The underlying environment-construction Method supplies the environment; this pattern supplies the interaction by which the developer obtains and interprets it.

Construct the whole attempt before choosing an interface. Working backwards, the test needs an identified artifact and matching runtime, synthetic data accepted by that runtime, effective access for the developer and an available test interval. The existing build/verification and environment Methods supply these professional operations. The platform design connects their results: the request preserves the artifact identity, the recipe fixes its compatible runtime, the data loader checks the supplied data version, and the response reports the observed environment and access state. Completing the environment operation alone is an intermediate result.

The first proposed construction starts a twenty-minute environment lease when creation begins. Data preparation takes fifteen minutes, environment preparation five and the acceptance test ten. In this illustrative case data preparation can run before allocation because it uses a fixed synthetic set independently of the environment; loading the prepared set takes two minutes. Preparing data after creation and then testing would require thirty-two minutes from creation to test completion under the stated serial order, so the twenty-minute lease cannot support that plan. Preparing it first requires seventeen minutes after allocation for the five-minute creation, two-minute load and ten-minute test, provided access is already effective.

Three alternatives are considered: extend the lease, prepare the synthetic data first, or use an operator-assisted reserved environment. The design assumes sufficient access and a qualified preparation operation, so the second alternative fits the twenty-minute lease without increasing reserved compute time. It accepts fifteen minutes of preparation before allocation. The user already works through CI, so a small interaction there is chosen. At higher uncertainty or low-frequency exceptional use, the assisted alternative could be preferable. These are stipulated design premises and arithmetic, not measured service guarantees.

In the first walkthrough, the provider accepts attempt q17 and creates environment e42, but the response is lost. A second click with a new request identity would create an unnecessary second environment. The revised interaction retains q17 at the caller, permits retrieval of that attempt and returns e42 only after checking its current state. If that lookup is unavailable, the response says that creation is uncertain and returns q17 to support; it does not invite an unqualified create-again action.

A later constructed trial finds the environment running but the acceptance-test connection denied. “Created” is therefore not the promised usable result. The trial returns the observed access failure and its repair route. After the permitted access configuration is repaired and the connection checked, the developer receives e42 with the matching recipe and data identity. This is still no approval to release the application.

A request for an unsupported build language receives a specific extension/support answer. It is not silently run through another language's recipe. Expiry is also visible: the user can retain the permitted test result before the disposable environment is removed, rather than treating access to a disappearing environment as permanent evidence.

Now change the data condition: the test needs a fresh environment-specific export that takes twenty-five minutes to prepare and cannot be prepared before that environment exists. Moving preparation earlier no longer preserves the input. Five-minute creation, twenty-five-minute preparation, two-minute loading and the ten-minute test require forty-two minutes under the stated serial dependencies. The old twenty-minute path is unsupported for this variant. Extending the lease to an agreed window or arranging a reserved assisted run can work only after checking shared capacity, access and the new data conditions. If neither is available, the user receives that precise limitation. The previously supported synthetic-data path remains usable.

The final description states that qualification is for obtaining and using the preview environment in this test. Its successful acceptance-test observation is returned with the artifact, recipe and data identity before expiry. Production deployment, exposure and release decisions retain their own authority and evidence. On actual implementation, the representative trial must also establish the assumed timings and access; the design arithmetic does not do that.

For a physical test bench, the same design question separates a reservation from a completed measurement. A request can name component configuration C4, the intended operating range and the measurement needed for an engineering decision. The returned booking confirms only a slot. The later measurement result also needs the actual specimen, setup and applicable measurement qualification. Software-style resubmission cannot safely repeat a destructive test, so an uncertain run returns to the operator before another specimen is consumed.

The practical change in both cases is that the user can distinguish what has been obtained and what is still missing.

### SYSE.26:6 - Bias-Annotation

Evidence from frequent expert users can hide the difficulties of infrequent users and unsupported variants. Include people who abandon the route or require assistance. Software examples also make replay look cheap; physical changes, consumed specimens and external commitments can make the same action irreversible.

### SYSE.26:7 - Conformance Checklist

- A representative user's next engineering result, supplied input and supported conditions are concrete.
- Acceptance, progress, intermediate completion and the usable returned result remain distinguishable.
- Valid unsupported use has an explicit return rather than a false success or coerced variant.
- Retry and cancellation preserve known effects and expose unknown ones.
- The support return reaches an actual capable provider without inventing an assignment or permission.
- Description, desk walkthrough, actual trial and later use support only their own evidence claims.

### SYSE.26:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Repair |
| --- | --- |
| A completed backend job is reported as the user's completed task. | Check the returned result with its intended consumer and expose any remaining condition. |
| A timeout offers “try again” without an attempt lookup or effect check. | Recover the earlier attempt and reconcile its effect before replay. |
| Every request is forced into the common template. | Distinguish invalid input from a legitimate unsupported variant and provide the corresponding return. |
| The support page lists a team that cannot repair the failure. | Recover the actual provider capability and assignment, or state that support is not yet supplied. |

### SYSE.26:9 - Consequences

Users can identify the decisions they need to make and a usable next move after failure. Providers gain evidence that connects a fault to a user undertaking. Designing and maintaining variant, feedback and recovery behavior costs effort.

### SYSE.26:10 - Rationale

An enabling System matters through the work people can complete with it. Designing only the successful technical operation leaves users to integrate configuration, interpretation and recovery themselves. Exposing the conditions that change their next action reduces that hidden integration work.

### SYSE.26:11 - SoTA-Echoing

**Adapt** the [CNCF Platforms White Paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/), especially “What is a platform,” platform attributes and provider relations. It already describes integrated capabilities, documentation, support, composability and a thin layer over real providers. A wiki or direct provider route can be sufficient in its terms.

This pattern develops a particular engineering construction within that line: work backwards from a usable result, connect the supplying operations forwards and resolve conditions that must hold across them. The preview example shows why an appropriate collection of services can still need an ordering or lifetime repair. A qualified existing provider composition can supply that construction without another platform layer.

**Adapt** the task-feedback guidance in [DORA Platform engineering](https://dora.dev/capabilities/platform-engineering/) for sections 4.3–4.5. Feedback becomes useful through the next action it supports, including uncertainty about an existing effect.

Assisted provision and self-service are serious alternatives. The selected design exchanges recurring human coordination for explicit interface, recovery and maintenance work only where the task warrants it. Reopen on changed use, provider behavior, shared capacity, validity windows or support. These software sources inform the design; the physical-bench transfer remains conditional on its own qualified operations and effects.

### SYSE.26:12 - Relations

SYSE.25 selects the task improvement; SYSE.24 compares whole obtaining arrangements. SYSE.12 develops the enabling System and separates readiness from later use. SYSE.13 supplies configuration identity. SYSE.27 develops contribution and compatibility paths; SYSE.28 places already justified controls. Software environment construction, state recovery and task measurement are supplied respectively by SYSE.33, SYSE.34 and SYSE.36. Use SYSE.14 for a required release decision; release authority remains with its applicable holder.

### SYSE.26:End
