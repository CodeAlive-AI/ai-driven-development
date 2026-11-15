## SYSE.28 - Place Qualified Controls in a Supported Platform-Use Path

> **Status:** Stable

> **Normativity:** Guidance within the stated engineering use; examples are illustrative.

### SYSE.28:1 - Problem frame

Use this pattern when a justified constraint already exists but engineers must decide where and how a supported path will check or enforce it. Start with the constrained subject, applicable conditions, deciding authority and the reliance that would be prohibited if the constraint were not met.

The first result is a control-placement design: an applicable check or mechanism, the subject it observes, its point of use, the meaning of its outcomes and the response to failure or uncertainty. It is not a new policy or a release decision.

A software artifact can change after an early verification; a physical dimension can change after coating; an access decision can expire before a resource is used. Place the check or enforcement where it can establish whether the condition holds, or keep it in force, when the action relies on it. If the constraint, its justification or the authority is missing, return that question instead of inventing a platform rule.

### SYSE.28:2 - Problem

Controls placed too early can report a property that is later lost. Controls placed too late can discover a prohibited effect only after it occurs. Repeating the same check at every step can add delay without covering the actual point of loss.

A second failure is to merge different results: advice, an observed property, a technical block and an authorized decision. A successful mechanism does not create authority, while an authorized exception does not turn a failed observation into a pass.

### SYSE.28:3 - Forces

| Force | Practical tension |
| --- | --- |
| Early feedback | Early detection reduces rework, but later transformations can invalidate the result. |
| Reliance protection | A final check can protect a receiving action, but may arrive too late to explain a preventable failure cheaply. |
| Reuse and currentness | Reusing a matching result saves effort; stale subject or condition identity makes the reuse unsound. |
| Availability | A failed checker can block useful work; silently bypassing it can permit the exact reliance it was meant to prevent. |

### SYSE.28:4 - Solution

#### SYSE.28:4.1 - Recover the supplied constraint and decision

Name the property, the subject to which it applies, its effectivity and the action that depends on it. Identify the holder authorized to decide and any authorized exception conditions. Keep the constraint's justification separate from the proposed technical implementation.

Identify what evidence or qualified procedure can answer the property question. If the available evidence is insufficient and the necessary domain procedure is missing, identify the procedure still needed.

Use SYSE.4 for the relation between evidence and the engineering claim, and SYSE.14 when the consuming action is a release decision. This pattern determines where the supplied control can usefully act.

#### SYSE.28:4.2 - Find where the property can change or be lost

Follow the relevant input, construction, transfer, installation and use. Identify which operations can alter the property and where another subject can be substituted. Do not assume that one label denotes unchanged bytes, configuration or material.

Locate the last relevant change before the prohibited reliance. Place a decisive observation or enforcing mechanism so that it can still prevent that reliance. Add earlier feedback only when it can avoid meaningful rework or guide a correction.

If the property can continue to change during use, determine what continuing observation or enforcement is needed and under what conditions it remains effective. A historical check cannot guarantee an indefinitely changing subject.

Trace where the property can change and where it must hold. Mark where the relevant subject is produced, where a transformation or substitution can invalidate the observation, and where the dependent action first relies on it. Include alternative entry and recovery paths when they can reach that action. This exposes a bypass that a successful ordinary pipeline run would miss.

Distinguish a past observation from a condition that must hold at use. Earlier measurements can support a claim about the dimensions of a retained specimen while the preservation conditions keep those dimensions unchanged. An earlier observation can lose its force when authorization expires or a runtime condition changes. In those cases, either obtain a sufficiently current observation at the receiving action or supply a mechanism that preserves the condition through the reliance interval. If neither is available, the placement design cannot yet support that use.

#### SYSE.28:4.3 - Compare placements by the question they answer

Compare evidence reach, response time, user/provider burden, failure behavior and the remaining opportunity for change after each candidate placement. An input check, a provider check and a consumer check may answer different questions.

For an immutable artifact crossing a trust boundary, a producer's check can qualify its construction while a consumer-side identity/trust check concerns the bytes actually received. For a coated component, an earlier dimensional result may guide manufacturing but cannot by itself support reliance on the final dimension.

Reuse a result only while the subject, relevant configuration, criterion and qualification conditions still match. A preserved result may be sufficient through controlled steps that cannot change the checked property of the subject. Identify any change that would require rechecking before the result is reused.

Construct a sufficient combination from the candidate placements. An early advisory check may cheaply find a repairable error; a protected result transfer may let a later receiver reuse its evidence; a decisive control may prevent reliance after an unprotected change. Select each because it covers a distinct unresolved loss or avoids worthwhile rework. Remove duplicate work only after checking that the remaining combination covers the same subject and reliance.

Compare complete alternatives. A receiver-only check can suffice when it observes the actual subject in time and its qualification covers the question. An early check plus protected continuity can suffice where the protection preserves the relevant property and evidence. Early feedback plus a receiving check can be worth its extra effort when late failure is costly or the transfer is not trusted. Continuous observation may be necessary for a property that changes after entry.

Bind the result to what the action will actually consume. If the action reads a mutable name after verification, it can receive a different subject. Pass a stable identity, hold the relevant state under a qualified mechanism, or re-establish the condition at consumption. Also protect the governing expectation and the checker's authority to attest: an altered trust configuration can invalidate a previously reusable result even when artifact bytes are unchanged.

#### SYSE.28:4.4 - Define every consequential outcome

Specify the mechanism's input, how it obtains the observation, how the outcome is interpreted and what the user can do next. Distinguish at least the outcomes that change action: satisfied, failed, not applicable, insufficient evidence and unavailable mechanism.

A technical block should block the dependent action, not silently cancel unrelated work. When a decisive checker is unavailable, preserve the uncertainty and use only a separately permitted alternative or current matching result. Do not make “could not check” indistinguishable from “passed.”

Keep advice, enforcement and authority separate. An advisory warning informs a decision. A technical block can prevent an action. An authorized holder may permit a bounded exception under the applicable rule. Record that exception's real subject, extent and conditions where needed; the failed or missing factual result remains failed or missing.

Explain a rejected attempt in the user's terms: which required property was not established, for which subject, and which correction, evidence request or authorized alternative is available. Provide detail sufficient to correct the use without disclosing protected material. Repeated unintelligible rejection creates pressure to bypass the path without resolving the underlying condition.

Treat an exception as a different authorized continuation with its own scope and expiry. Decide how the dependent mechanism recognizes it and what continues to be observed. A later request must not inherit the exception simply because it shares a project label. If an emergency or checker outage needs a fallback, use a fallback already authorized for those conditions, or obtain authorization from the applicable holder before relying on it.

#### SYSE.28:4.5 - Exercise the control where it will be relied on

Establish how the control behaves for its receiving use. Use applicable existing evidence and select any further cases needed, such as normal use, violation, subject substitution or checker unavailability. Confirm that the intended dependent action receives the right outcome and explanation. Check the conditions and result of any authorized exception path.

For consequential reliance, also inspect whether the controlled property can change between observation and use. Bind the result to the actual subject or protect that interval with a qualified mechanism. A green check followed by an uncontrolled substitution does not protect the receiving action.

Return the placement, mechanism, outcome interpretation, applicable conditions and remaining gaps. Safety or compliance claims that rely on the control require their own domain evidence; placing the check is not that qualification.

Use qualified evidence for the checker and for the connection between its observation and the dependent action. For a condition that can change during use, establish whether the response arrives in time. If a material failure mode remains untested, choose an exercise that addresses it, such as a substitution after an early pass, a change in applicability or another permitted entry to the same action. Use trials permitted by the domain. Where a direct trial would be destructive or hazardous, use an adequate safe substitute when needed. A desk walkthrough can test the proposed logic. To rely on the implemented control, use evidence of its operation and the domain property it is meant to establish.

### SYSE.28:5 - Archetypal Grounding

A constructed software case supplies an existing requirement: before installing a service package, its receiver must establish that the actual artifact meets the configured provenance expectations. The applicable trust roots and expectations are provided by the responsible holder; the platform team does not invent them.

The build service has verified package h1. A later registry transfer returns different bytes h2 under the same human-readable version tag. A check performed only before that transfer cannot establish the property for h2.

The chosen placement keeps the early producer feedback and performs the receiving verification on the actual artifact before installation. SYSE.32 supplies the artifact-specific verification Method. If h2 has no matching qualifying provenance, installation receives a failed or insufficient result, not the old h1 success. If the verifier is unavailable, the same dependent installation waits or takes a separately authorized alternative; an unrelated already qualified test can continue.

Once the artifact is verified, a controlled transfer of those unchanged bytes can reuse that identity result under matching trust conditions. A newly downloaded package, altered artifact or changed relevant expectation reopens the affected check. None of these outcomes approves the application's production release.

Compare the complete designs. Receiving verification alone would answer the immediate artifact question, but in this example an early failure can prevent costly transfer or downstream preparation. The selected combination keeps that early feedback and the receiver's verification because they serve different uses. Rechecking unchanged protected bytes at every internal hop would add no further coverage under the stipulated trust conditions.

Now the responsible holder withdraws trust from the builder after a cached verification result was issued. The artifact identity is still h1, but the expectation used by the consuming decision has changed. The path reevaluates that affected result against the new trust basis before dependent installation. It neither rebuilds unrelated artifacts nor treats a matching digest as sufficient evidence of continuing trust. The holder may select a different qualified source or a bounded exception; the old verification claim keeps its original conditions.

In a physical case, the engineering requirement concerns a finished coated bore of 20.000 ± 0.020 mm. Assume a qualified measurement procedure is available for the finished part. Measuring the uncoated bore can guide machining, but coating can alter the final dimension.

The decisive final-dimensional check is therefore placed after coating and before the part is accepted for the dependent assembly. A pre-coating pass cannot be reused merely because the part number is unchanged. If the qualified finished-part measurement is unavailable, the result remains unestablished; faster transfer of the old report does not cure it. If no qualified measurement procedure is available for the finished part, identify that separate gap.

The receiver can identify which subject and interval the result concerns and what is stopped when that result is absent.

### SYSE.28:6 - Bias-Annotation

Teams often place controls where tools make them easy rather than where the property can be lost. A preference for early feedback or for one final approval can hide complementary needs. Inspect the actual transformation and reliance, including physical effects that no later software action can undo.

### SYSE.28:7 - Conformance Checklist

- The constraint, subject, applicability and deciding authority are supplied.
- The observation or enforcement Method is adequate for its particular property, or its gap is explicit.
- Placement accounts for the operations and substitutions that can invalidate the result.
- Reuse is conditional on matching subject, criterion and qualification conditions.
- Failed, missing and unavailable outcomes reach the dependent action with a usable explanation.
- An authorized exception leaves failed or missing factual results unchanged.
- A technical block stops only the dependent action and leaves unrelated work available.

### SYSE.28:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Repair |
| --- | --- |
| Check early and assume the property survives every later step. | Identify later changes and cover the actual receiving subject. |
| Run the same check at every step. | Separate distinct questions and reuse a matching result through protected transformations. |
| Checker failure means pass. | Preserve missing evidence and follow only an authorized fallback or stop. |
| A green badge grants release authority. | Return the bounded evidence to the actual decision holder. |

### SYSE.28:9 - Consequences

Checks can provide earlier repair feedback and a more credible basis for reliance. Some placements require additional observation or protected transfer, while others become unnecessary duplicates. Explicit unavailable-result behavior can delay the dependent action, but exposes the real constraint rather than disguising a bypass.

### SYSE.28:10 - Rationale

A property's truth at one time or location does not automatically survive transformation, transfer or substitution. Control placement is therefore a question about evidence reach and prevented reliance. Keeping that question separate from policy and authority makes the mechanism useful.

### SYSE.28:11 - SoTA-Echoing

**Adapt** [SLSA v1.2, Build: Verifying artifacts](https://slsa.dev/spec/v1.2/verifying-artifacts), particularly “How to verify,” “Forming Expectations” and “Architecture options.” It compares ecosystem, consumer and monitor verification, permits complementary placements and distinguishes the threats they address.

For engineering uses beyond artifact verification, trace where the required property can change and where an action relies on it. Choose a sufficient combination of observations, protected continuity and responses. For software provenance, SYSE.32 and SLSA supply the specialized verification. For the finished bore, the qualified measurement procedure is a separate supplied premise.

The alternatives differ by what they protect and what they cost. A receiving check can be enough for one use; early feedback is worth retaining when it avoids substantial rework; controlled continuity can support reuse; a changing property can require continuing observation. The selected combination accepts only the added burden that changes those results. Reopen when the subject, trust basis, invalidating operations, checker qualification, protected interval or consuming action changes.

### SYSE.28:12 - Relations

SYSE.26 supplies the supported interaction and failure feedback. SYSE.4 governs evidence reliance, SYSE.13 identifies configurations and SYSE.14 supplies release decision-making. SYSE.32 supplies software artifact verification and SYSE.41 supplies deployment observations. For a missing justification, authorization or specialist qualification, identify the source or holder that can supply it.

### SYSE.28:End
