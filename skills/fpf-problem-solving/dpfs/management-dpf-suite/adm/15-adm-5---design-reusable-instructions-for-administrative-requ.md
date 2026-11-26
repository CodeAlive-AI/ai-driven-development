## ADM.5 - Design Reusable Instructions for Administrative Requests

**Type:** Architectural

**Status:** Stable

### ADM.5:0 - Use this when

Use this pattern when a service owner has an administrative result to supply repeatedly and the policy that governs it, and handlers need a usable instruction for receiving, checking, deciding, providing and closing individual requests. A new reimbursement service, for example, needs more than a form and a list of approvers.

Return a service instruction that identifies what the handler, decision holder and provider do for an ordinary request and for a failed condition. Include specialist contributions where the case requires them. A representative request can expose a missing handoff. To design for the class, recover from the service terms which differences between permitted requests change the decision, the party who may act, the work due or its deadline.

Use an adequate existing instruction directly. This pattern is unnecessary for each later request and does not itself approve a request, appoint a provider or authorize an exception. Obtain missing policy from the authority responsible for it. A form field can collect an input once the applicable rule is known.

### ADM.5:1 - Problem frame

The designer is working on how a class of administrative requests will be handled. The enabled work and requested condition are already sufficiently clear, or ADM.1 can establish them. The supplied policy determines such matters as eligibility, permitted amounts, deciding authority and any mandatory evidence. Actual service participants supply the remaining operational constraints.

The reusable instruction and an individual case have different results. The instruction describes what the handler, decision maker and provider do under stated conditions. In a particular case, the responsible participants apply it to the case facts, make any required decision and perform the provision. A completed design cannot establish that any claimant has received a result.

The relevant scope may be small: reimbursing one category of travel expense for one employee population. Add a variant only when it changes the needed input, authority, action or result. A single instruction need not absorb every service that happens to share a portal.

### ADM.5:2 - Problem

A service often begins with an application form. Each department adds fields and approvals, yet nobody establishes how the approved request produces a usable result. Handlers then improvise missing evidence rules; applicants repeat information; providers close requests after issuing instructions whose effects remain unknown.

The opposite response leaves all handling discretionary. Skilled staff may resolve familiar cases, but a new handler cannot tell which decisions are already settled by policy, which require a competent decision holder and which information is actually needed.

### ADM.5:3 - Forces

| Force | Tension |
| --- | --- |
| Repeatability | An instruction should support consistent handling while retaining legitimate variations and exception conditions. |
| Minimum burden | Reuse known facts and decisions while obtaining the evidence the actual decision needs. |
| Institutional authority | A designer can describe a decision and its recipient without possessing the authority to make or delegate it. |
| Usable completion | A provider's intermediate activity is easy to record; the promised effect may require a different observation. |
| Practical size | One short instruction can be sufficient, while a diagram that omits refusal, uncertainty or recovery is incomplete for those cases. |

### ADM.5:4 - Solution

#### ADM.5:4.1 - Fix the supported result and governing inputs

Name the condition to be supplied, its recipient, applicable time and supported request class. Recover the applicable policy and who is authorized to decide, perform and correct each action. Distinguish a supplied rule from an assumption that still needs its competent source.

Keep the work enabled separate. A travel reimbursement service supplies an authorized reimbursement; it does not determine whether the traveller's negotiations succeeded. If the policy makes a business condition relevant, identify evidence that would establish it. A decision reserved to a particular party requires its effective act, which a suitable existing record may establish.

An unavailable policy, unassigned payment provider or missing qualified test is a design gap. State the exact missing contribution and who can supply it before promising the affected result.

#### ADM.5:4.2 - Work backwards to the minimum request

For each condition on which the handling or its conclusion depends, identify the fact, evidence or existing result that the handler needs. Reuse a sufficiently current assignment, permission or prior check within its actual scope. Ask the applicant only for information that cannot adequately be recovered and that matters to handling.

Specify how the handler relates the evidence to the claimant and request. A receipt must concern this expense; an assignment must cover the relevant participant and time. “Upload documents” leaves these questions unanswered. ADM.7 supplies the case check when the correspondence or support is disputed.

Specify where the request enters, how the applicant can correct an ordinary omission, and what the handler returns when the request is outside the supported class. Collect and expose personal information only for the stated handling need under the applicable information rules.

#### ADM.5:4.3 - Identify the actual decisions and actions

For each consequential branch, name who applies the rule or makes the decision, the conditions used, and what the next participant receives. A direct policy rule may already determine the required response. A case-specific approval remains a decision when the policy requires an authorized person to make it.

Keep the handler's preparation, a specialist's judgment, authorization by the competent holder and the provider's performance distinct. Completing a checklist neither transfers approval authority nor performs payment. ADM.8 resolves a permission question; OPS.5–OPS.6 can supply admission or situated continuation when actual handling needs one.

State which independent action may proceed while another condition is pending. An instruction for obtaining a price quote need not inherit the spending authorization required for a later booking unless the applicable rule makes that authorization a condition of the inquiry.

#### ADM.5:4.4 - Connect authorization to provision and completion

Identify the provider who will perform the authorized action and the input that provider needs. Define completion from the recipient's promised use: access that works under the grant, accommodation that can be occupied, or funds credited under the applicable payment terms.

Choose evidence adequate for that effect. An issued instruction may establish that the provider was asked to act; it may leave performance unknown. ADM.9 supplies the needed provision and recovery inquiry. ADM.10 reconciles a discrepancy among the obligation, performance and records.

Specify what each participant must receive about the decision, effect, effective conditions or remaining work. Use an existing case record where it suffices. Participants need enough correspondence to recover the same case; they need not adopt one universal description of every event.

#### ADM.5:4.5 - Describe ordinary correction and genuine exceptions

Give the handler the existing response for a correctable omission or an established negative condition. A missing receipt may receive the policy's correction request. A clearly excluded expense may receive its reasoned refusal and applicable challenge route. Use a separate decision only when the applicable policy or challenge requires it.

Use ADM.6 when an actual gap prevents ordinary handling: conflicting facts, an inapplicable rule, unresolved authority, incompatible requirements or provision whose effect cannot be established. Name the competent destination and the bounded question. A transfer to “support” without anyone assigned to resolve it is still a gap.

For potentially duplicate actions, include recovery of the earlier attempt before repetition. The instruction should state what remains permitted while the uncertain effect is investigated, rather than calling the entire service complete or restarting it blindly.

#### ADM.5:4.6 - Exercise and publish the usable instruction

Judge the instruction against the service it is meant to cover. Derive from the governing terms which differences can change the required response, who may decide or when a result is due. For each request the service undertakes to handle under those terms, the handler needs a permitted, timely way to act or to obtain the decision from the authority the policy designates. One rule can cover many requests when its premises hold across them. If two requests look alike to the handler at the time of choice yet require incompatible responses, give the handler a way to distinguish them in time or revise what the instruction promises. Where requests can be made together, check whether the permitted responses can also be provided together.

When a walkthrough is needed, use a representative case to check whether the instruction identifies each participant’s next action. A human handler can explain what they would do, and an automated handoff can be examined against its stated inputs and outputs. Repair missing handoffs and unnecessary requests. To establish that a person or service can perform the work and that the provider can deliver the promised condition, use applicable evidence of performance or a trial that covers the claimed result.

Return the instruction with the class of requests covered, its governing policy and the conditions it relies on. A decision on an individual case can remain open by design if the instruction reaches the party entitled to decide, with the means to reach a decision in time. For a panel, that can depend on whether the required members can examine the case and act under the applicable voting rule. If a promised class has no supported response, identify who must resolve that gap and the cases that can already be handled. A commission for a draft may allow such a choice to be returned to the service owner. To put an instruction into use for the whole class, cover each response the terms require. Publish it where handlers look for service instructions. Reopen its design when conditions or evidence of actual handling change the answer.

### ADM.5:5 - Archetypal Grounding

#### ADM.5:5.1 - A reimbursement instruction

Suppose policy P permits reimbursement of documented business-travel expenses up to 500 units for employees with an effective relevant assignment. P requires a named finance approver's case decision; treasury is authorized to pay approved claims. The payment terms define the promised effect as the approved amount credited to the claimant's designated account. These are supplied conditions for this example, not universal reimbursement rules.

The service owner and participants develop this instruction:

| Question | Instruction for the supported class |
| --- | --- |
| What enters? | Receive the claimant's identity, expense, amount, business purpose, receipt and relevant assignment reference. Recover adequate information already held. |
| What is checked? | The handler establishes claimant/assignment/expense correspondence, the applicable category and amount, and whether this expense has already been reimbursed. A disputed claim uses ADM.7. |
| What ordinary correction applies? | If the receipt is missing, ask the claimant for the correction P allows. Apply P's response to an established excluded category, including the available challenge route. |
| Who decides? | The finance approver applies P and makes the required decision for the exact claim and amount. The handler's completed preparation supplies input to that person. |
| Who performs? | Treasury receives the approved claim and the account information through the authorized channel, then issues the permitted payment. |
| When is provision complete? | Under P, the approved amount must reach the claimant's designated account. The credit date determines when provision occurred. A suitable bank statement or other reliable evidence can establish it later. An acknowledgement of the payment instruction leaves credit open. |
| What is returned? | The claimant receives the decision and actual provision result or precise remaining condition. Finance and treasury retain the corresponding evidence needed for their duties. |
| What requires resolution? | Conflicting assignment evidence, unclear approving authority or an unknown earlier payment effect goes to its competent resolver through ADM.6. Recover the earlier effect before a possible duplicate payment. |

Later an employee claims 200 units. The supplied assignment and receipt support eligibility, and adequate records establish no earlier reimbursement. The handler prepares the case, the finance approver approves it, and treasury performs payment. Evidence of the credit supports completion and the returned record.

#### ADM.5:5.2 - A variant outside the supplied policy

A contractor submits an otherwise identical receipt. P covers employees, and no contractor rule is supplied. The handler follows the instruction's outside-scope response and identifies the missing contractor-policy question to its competent source. The service owner cannot extend P by adding a contractor checkbox. If another applicable instruction already covers contractors, the request can use it.

### ADM.5:6 - Bias-Annotation

Designers tend to optimize the fields and handoffs they can see, while applicants bear repeated entry, waiting and inaccessible channels. Trace the recipient’s attempt to obtain the condition as well as the tasks performed by providers. Use evidence of repeated entry or inaccessible channels when examining the added burden.

The example assumes an explicit policy and identifiable decision makers. An informal service may use a short agreed instruction, but informality does not create missing authority. Where a question concerns the lawfulness or merits of the policy, obtain the applicable professional determination or policy decision.

### ADM.5:7 - Conformance Checklist

**Recognition.** The result is a reusable instruction for a bounded class. It connects entry and evidence to actual deciding and performing participants, a usable completion condition, the returned account and meaningful failure branches.

**Assurance for reliance.** Can the participants recover their next action for the variations the service promises to handle? Use a rule that covers the class, adequate evidence of the relevant branches, or both. An author walking through one request can find a missing handoff. When a handler works from the instruction with the support normally available, their choices show what that handler recovered in that situation. To rely on independent handling across the class, account for the variations in decisions, authority and available support. A promise to deliver the service also depends on the applicable policy, authority and timely provider capacity.

### ADM.5:8 - Common Anti-Patterns and How to Avoid Them

A **form presented as a service** specifies inputs but leaves the decision and actual provision unassigned. Follow one request through to the recipient's usable condition.

**Design on every request** repeats the architecture inquiry despite an adequate instruction. Apply the existing instruction; reopen only the defective or changed condition.

**Every refusal becomes an escalation** sends settled cases to another decider. Retain the policy's ordinary response and challenge route; reserve exception resolution for the actual unresolved question.

### ADM.5:9 - Consequences

Handlers can begin ordinary cases with less improvisation, while specialists receive specific questions and providers receive actionable decisions. Applicants can distinguish a correction request, a reasoned refusal and unfinished provision.

Design can require obtaining missing policy, checking correspondence and establishing how completion will be observed. Add detail when it helps participants handle cases or establish what happened. The instruction's successful construction does not establish service effectiveness; that requires evidence from actual cases and participants.

### ADM.5:10 - Architectural Rationale

The reusable object is the handling instruction. Authority remains with the actual participants, and successful provision remains an effect of their work. Keeping these distinct lets the service reuse its design without treating a model, approval or record as the beneficiary's result.

Apply a settled rule directly. When a potentially duplicate payment has an uncertain effect, obtain the specific recovery result needed before repeating it.

### ADM.5:11 - SoTA-Echoing

The working question is how to make an administrative service repeatable while keeping institutional decisions and actual provision connected. The June laboratory and ADM source pack distinguish developing a service from using it. Part of this question is how the service supports the participant's intended work and what effort it requires from them. The laboratory material supplies reported situations; assess service effectiveness from its actual use.

[OPS.5 through OPS.6][OPS] explain how to determine admission and continuation when those questions are open during handling. The administrative instruction specifies its evidence, authority and promised result. [CMMN 1.1][CMMN], §§4.1–4.3, supplies a case-model alternative: work toward an outcome can use evolving information and discretionary planning. Its model does not supply the local eligibility policy, appoint the decider or establish real provision.

Use an adequate existing service instruction directly. A process diagram or case model is also sufficient when it already carries the needed conditions and returns. Sections 4.2–4.5 become necessary where the representation omits those joins; no particular notation or CMMN conformance is required.

Reopen the affected design when policy, supported population, deciding authority, provider capability or a demonstrated handling failure changes it. A new form or software feature alone is not a new administrative result.

### ADM.5:12 - Relations

ADM.1 supplies the condition the service enables; ADM.2–ADM.3 supply participants and effective relations when those are unsettled. The handler uses ADM.7 for a needed claim check, ADM.8 for permission, ADM.9 for usable provision and ADM.10 for reconciliation. A genuine obstacle returns through ADM.6 to the source or authority able to resolve it.

[OPS.5 through OPS.6][OPS] help the handler determine which work may start or what a case needs next. [SYSE.26][SYSE] supplies the design of a supported interaction and its failure recovery when that engineering question is live. Neither return is a mandatory preliminary to using an adequate administrative instruction.

### ADM.5:End
