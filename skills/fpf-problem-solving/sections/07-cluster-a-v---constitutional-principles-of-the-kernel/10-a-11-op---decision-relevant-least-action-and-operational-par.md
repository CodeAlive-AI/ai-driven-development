## A.11.OP - Decision-Relevant Least Action and Operational Parsimony

> **Type:** Part A pragmatic principle pattern
> **Class:** `Prag`
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain name.** Keep only work that changes a substantive choice or result, or protects a condition on which the use relies.

**Primary reader.** A practitioner or designer deciding whether one proposed action or supporting apparatus should be mandatory.

### A.11.OP:1 - Problem frame

**Use this when.** Use this pattern when someone proposes making an action or apparatus mandatory and a plausible question remains: does this requirement change the subject work, or does it only make the route look controlled?

The primary `EntityOfConcern` is one proposed mandatory requirement under one declared use and one substantive horizon. The pattern governs only that admission decision; *action*, *apparatus*, *requirement*, and *horizon* keep their ordinary meanings.

**First useful result.** Return one of two short answers:

- retain the requirement for this use and horizon because it changes a named substantive branch, realizes an already selected result, or preserves a named assurance or recovery condition on which the use relies; or
- remove the requirement or leave it optional because none of those conditions changes when it is removed.

Ordinary use needs no score or separate record. Name the receiving decision, result, reliance, or recovery condition in the same sentence as the disposition.

**Three recognition cases.**

- A team has added a second status update before a repair decision. Every possible status leaves the same repair action, and no later user relies on the duplicate update.
- A laboratory considers a bounded probe that leaves today's setup unchanged but can determine which of two methods will be used next week.
- A release route contains both a deterministic build step that creates the selected publication and an assurance check whose evidence is consumed by the release decision.

These are one recurring problem across unlike situations: mandatory effort can be ceremonial, immediately productive, decision-relevant only later, or necessary because another use relies on the assurance or recovery condition it preserves.

**What goes wrong if missed.** Requirements accumulate because each sounds prudent in isolation, while their possible results change no substantive choice and produce no selected result. The opposite error removes exploration, deterministic realization, safety evidence, recovery support, or a small discriminating cue merely because it does not change the next administrative state.

**What this buys.** The practitioner can remove ceremony without treating the fewest steps as the goal. Useful exploration, realization work, assurance, option preservation, and recovery remain when their receiving use is named.

**Not this pattern when.**

- When an applicable direct authority already establishes the obligation, use that authority. Apply A.11.OP only to discretionary apparatus inside the space it leaves.
- When several already qualifying alternatives need comparison, use their direct choice, apparatus, architecture, or Method Engineering pattern.
- When the question is whether a new durable ontology value should exist, use `A.11`.
- When the question is how to use an already selected pattern, use `E.11.PUA` or `E.11.PUR`.
- When ongoing Work needs one next action chosen from current facts, use `A.15.7`.
- When an available direct-kind apparatus is already being configured for a declared use, use `C.19.2` for that application question.

### A.11.OP:2 - Problem

Methods and their administrative or support arrangements can accumulate apparatus, such as duplicate reads, checks, and handoffs. Each addition can be defended by a possible future benefit. If hypothetical usefulness is enough, every requirement survives. Attention and elapsed time then move from the subject result to the route's own states and receipts.

Simple minimization fails in the other direction. A deterministic assembly step may have no rival outcome yet still create the selected result. A decision maker may use new information to change a later policy while leaving the immediate action unchanged. A safety check may return the expected result while supplying evidence on which release reliance depends. A practitioner may use a recovery cue to avoid continuing from the wrong place. Counting branches, steps, documents, or minutes does not distinguish those cases.

The problem is therefore not how to minimize action in general. It is how to admit one proposed mandatory requirement only when a materially plausible difference reaches a named substantive use, without weakening the direct authority that governs the action.

### A.11.OP:3 - Forces

| Force | Tension |
| --- | --- |
| Economy versus result production | Removing ceremony saves effort, but a deterministic action can be the work that realizes the selected result. |
| Immediate economy versus delayed information value | A probe can leave the next action unchanged while changing a later decision inside the relevant horizon. |
| Light use versus assurance | Ordinary decisions should stay conversational, but a relied-on exposure, release, rollback, or recovery condition may need evidence. |
| Local closure versus open-world reuse | A declared horizon makes action possible; unspecified future reuse cannot justify every precaution. |
| Parsimony versus authority | A burden screen can expose ceremony, but it cannot override law, regulation, Guard-Rails, assurance floors, or direct duties. |
| One general rule versus direct owners | The recurring admission question should be easy to find, while Method, choice, apparatus, evidence, assurance, and Work claims retain their own patterns. |
| Plain guidance versus theory laundering | Use epistemic and counterfactual distinctions without importing a universal engineering objective from free-energy or physical least-action formalisms. |

### A.11.OP:4 - Solution

Apply one bounded admission question before making the proposed action or apparatus mandatory.

> **Admission rule.** An author or method designer **MUST NOT** make a proposed action or apparatus mandatory unless at least one materially plausible result can change a named substantive decision or branch within the declared horizon, the action realizes an already selected transformation or required subject result, or removing it changes a named assurance or recoverability condition on which the declared use relies.

Passing one branch establishes only that the requirement is non-ceremonial for this use and horizon. Every stronger claim remains with its direct owner.

#### A.11.OP:4.1 - Name the use and nearest substantive horizon

1. Name the proposed requirement and the declared use for which mandatory status is being considered.
2. End the horizon at the nearest named substantive decision, receiving use, selected transformation result, assurance use, or recovery use that can justify the requirement.
3. Name the possible result or removal consequence that reaches that horizon. Do not use the requirement's own status, completion flag, receipt, or other administrative transition as its receiver.

The nearest substantive horizon is not necessarily the next event. It may include a later decision when the dependency from the present result to that decision is stated. End it before any further use whose receiver and dependency have not been named.

#### A.11.OP:4.2 - Compare keeping and removing through three branches

| Admission branch | Passing condition | Boundary of the result |
| --- | --- | --- |
| **Decision-changing result** | At least one materially plausible result changes a named subject branch or selection among named alternatives inside the horizon. An information-gathering action passes when one of its possible results changes a later policy even if the immediate action stays the same. | The passing basis is the result-to-decision dependency; likelihood and the eventual branch remain open. |
| **Selected realization** | The action performs a required part of an already selected transformation or obtains the required subject result. A deterministic step needs no fabricated rival outcomes. | This branch admits only the realizing action; it presupposes selection and leaves authorization, actual Work, and result status to their direct owners. |
| **Assurance or recoverability preservation** | Removing the action changes a named assurance or recoverability condition on which the declared use relies. | This branch preserves that condition; its required level and evidential basis come from the direct assurance or recovery owner. |

Compare the concrete situation with and without the requirement. If one branch passes, retain the requirement at no more formality than its direct owner and named reliance need justify. If several proposed actions or apparatus configurations pass, return their comparison to the pattern that directly governs those alternatives.

If no branch passes, remove the requirement or leave it as an optional convenience. Convenience and prior investment do not supply the missing receiving difference.

#### A.11.OP:4.3 - Judge material plausibility through the subject claim

*Materially plausible* means more than logical possibility and less than certainty. The direct owner of the claimed consequence supplies its standard of evidence. A low-probability result can remain material when its consequence changes exposure or the admissible policy. A large information volume is material only when some possible result changes a named receiving use.

When the branches cannot be distinguished, name the exact claim and missing basis and return them to that claim's direct owner. Alternatively, run a bounded experiment whose possible results can genuinely change the named decision. Unresolved usefulness does not create permanent mandatory status.

#### A.11.OP:4.4 - Return authority and claims to their direct owners

Apply this screen only inside the space left by every applicable direct authority. The direct owner establishes the obligation or floor and resolves disputes about its basis or applicability.

A passing branch establishes only that the requirement is non-ceremonial for the named use and horizon. Every downstream claim remains with the direct pattern named in Relations; obtain that result by value instead of treating this admission as its substitute.

#### A.11.OP:4.5 - Keep the result light and reopenable

For ordinary use, say:

> Keep `<requirement>` for `<declared use>` until `<nearest substantive horizon>` because `<named branch and receiving difference>`.

or:

> Remove or demote `<requirement>` for `<declared use>` because keeping and removing it produce the same substantive decision and result and change no relied-on assurance or recovery condition.

A named later use that must cite, compare, audit, or rely on the disposition records it in the existing record kind appropriate to that use. Otherwise the one-sentence result is complete.

Reopen the disposition when the horizon, plausible results, selected transformation, direct duty, assurance floor, recovery reliance, or burden-bearing alternative changes.

#### A.11.OP:4.6 - Keep framework layers distinct

FPF owns this cross-domain admission principle. A Method Engineering DPF may use it when deciding which requirements should be mandatory in a named Method situation; that DPF still owns the Method-specific design. A local practice framework may bind the principle to its own execution and assurance mechanisms. Those mechanisms retain local scope, and the FPF admission condition must still be established for the declared use.

### A.11.OP:5 - Archetypal Grounding

#### A.11.OP:5.1 - Duplicate status update and deterministic publication build

A publication repair route asks for a second status update immediately before the repair decision. The update has the same possible values as the first one. None changes `repair`, `stop`, or `publish`, no receiver cites it, and removing it changes no assurance or recovery condition. The second update passes no branch, so the route removes it or leaves it as an optional convenience.

The same route runs a deterministic build after the sources and publication form have been selected. The build has no decision-changing outcome by design, but it assembles the selected sources into the required publication. It passes selected realization and remains. Any claim about the assembled publication or its release still needs its direct owner.

#### A.11.OP:5.2 - Exploration whose value appears in a later decision

A maintenance team must choose next week between Method A and Method B for a recurring seal failure. A bounded probe performed today can return one of three observations: evidence favoring A, evidence favoring B, or an unresolved result that triggers a hold. Today's immediate action is unchanged, but every possible probe result has a named effect on the later Method-selection decision.

The probe passes the decision-changing-result branch. Its horizon ends at that named selection and its stated window, not at the probe's completion flag. If the team later shows that every possible observation leads to Method A, the probe no longer passes for that use and is removed, redesigned, or made optional.

#### A.11.OP:5.3 - Assurance evidence with an unchanged operating decision

A pressure-system release check is expected to confirm the current operating decision. The release authority nevertheless relies on its evidence, and omission changes the accepted exposure for release. The check passes assurance preservation even when its most likely result leaves the operating branch unchanged.

`B.3`, the applicable evidence pattern, and the release authority set the assurance floor and disposition. A.11.OP returns only that the check is non-ceremonial for this named release reliance. A candidate check qualifies here only when the relying condition, exposure change, and direct owner are known.

#### A.11.OP:5.4 - Recovery cue and discriminating language

After an interrupted multi-part analysis, a small progress marker identifies the last closed item and the next item. Removing it can cause the practitioner to repeat completed work or resume from the wrong branch. The marker passes recovery preservation while that continuation use relies on it. If the task is short and the next item is already unambiguous, the marker becomes optional.

In another case, a sentence must distinguish a reusable Method from dated Work that enacted it. The distinction changes whether the practitioner repairs a description claim or a performance claim. The requirement to preserve that distinction passes the decision-changing-result branch for this use. Other terminology remains informative unless a named interpretation or action depends on it.

#### A.11.OP:5.5 - Speculative compliance without a receiver

A team proposes generating a compliance packet for possible future reuse. No applicable authority or named receiving use has been established for the packet, so it passes no branch and is not mandatory.

If an applicable duty or relying receiver is later established, reopen the disposition under that direct authority. The earlier speculative possibility was not evidence that the duty already existed.

### A.11.OP:6 - Bias-Annotation

Scope: **Universal** for the cross-domain admission question governed by this pattern.

| Lens | Likely bias | Countermove |
| --- | --- | --- |
| **Gov** | Parsimony language is used to bypass an instituted duty, safety rule, or assurance floor. | Return authority and applicability to the direct law, duty, Guard-Rail, evidence, gate, or assurance owner. |
| **Arch** | Every special case receives another owner, or this pattern absorbs Method, choice, Work, evidence, and assurance decisions. | Keep one three-branch admission screen and return every downstream claim to its direct pattern. |
| **Onto/Epist** | An author declares ordinary words such as *action*, *apparatus*, or *horizon* as new kinds, or treats information volume as decision relevance. | Keep the words ordinary and name the exact receiving decision, result, reliance, or recovery condition. |
| **Prag** | “Less is better” deletes exploration, deterministic realization, prevention, or recovery; “might help” preserves ceremony forever. | Compare keeping and removing at the nearest named substantive horizon through all three branches. |
| **Did** | The branch table becomes a mandatory form that costs more than the judgement it supports. | Keep ordinary use to one disposition sentence and introduce durable evidence only for a named relying use. |

### A.11.OP:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-A11.OP-1` Governed requirement | One proposed mandatory requirement, one declared use, and one nearest substantive horizon are recognizable. |
| `CC-A11.OP-2` Substantive receiver | The justification reaches a named subject decision, receiving use, selected result, assurance use, or recovery use; the requirement's own route state is not its receiver. |
| `CC-A11.OP-3` Three-branch comparison | Keeping and removing the requirement have been compared through decision-changing result, selected realization, and assurance or recoverability preservation. |
| `CC-A11.OP-4` Material plausibility | Each claimed difference has the basis appropriate to its subject, evidence, risk, causal, decision, or assurance claim; bare logical possibility and information volume are insufficient. |
| `CC-A11.OP-5` Deterministic realization | A required deterministic step is retained when it realizes the already selected result without fabricated outcome branches. |
| `CC-A11.OP-6` Delayed decision value | Information is retained only when at least one materially plausible result can change a named later decision inside the stated horizon. |
| `CC-A11.OP-7` Assurance boundary | A retained assurance or recovery action names the relied-on condition and its direct owner; that owner establishes the floor and evidential basis. |
| `CC-A11.OP-8` Disposition boundary | Passing a branch is reported only as non-ceremonial admission for the named use and horizon; every stronger claim is returned to its direct owner. |
| `CC-A11.OP-9` Light result | Ordinary use ends in the direct one-sentence disposition; a durable result uses an existing record kind required by a named later use. |
| `CC-A11.OP-10` Direct-owner return | Each downstream claim remains with the direct pattern named in Relations and is obtained from that pattern by value. |
| `CC-A11.OP-11` Reopen condition | The disposition names or makes recoverable which change in horizon, result, transformation, duty, reliance, or alternative can reopen it. |
| `CC-A11.OP-12` Theory boundary | Epistemic value and a counterfactual horizon may inform the comparison. Expected free energy, variational free energy, and Hamiltonian least action do not supply a universal engineering admission rule. |

### A.11.OP:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| **Fewest steps wins** | Deterministic realization, exploration, assurance, or recovery is deleted because it adds work. | Apply all three branches and compare substantive consequences, not step count. |
| **Next-click horizon** | A probe is judged useless because it changes a later decision rather than the next administrative action. | End the horizon at the nearest named substantive receiver and state the dependency. |
| **Infinite downstream usefulness** | Any requirement survives because it might help an unnamed future user. | Require a named receiver, decision, reliance, or recovery use; otherwise remove or demote it. |
| **Administrative self-receiver** | A receipt is justified because it updates the route state that exists only to carry the receipt. | Name a subject decision or reliance outside the requirement's own administration. |
| **Fabricated alternatives for deterministic work** | A build or transformation step must invent outcome branches to look decision-relevant. | Retain it through selected realization when it performs the already selected result. |
| **Precaution label as assurance** | Calling a step “safety” or “compliance” creates an unsupported floor. | Name the direct authority, evidence, exposure, and relied-on condition; return their disposition to the direct owner. |
| **Branch passage as authority or optimum** | Admission is substituted for the stronger claim governed elsewhere. | Report only non-ceremonial admission; obtain authority or comparison from its direct owner. |
| **Mandatory parsimony record** | The screen creates the same ceremony it is meant to remove. | Use one ordinary disposition sentence unless a named later use needs a durable episteme. |
| **Free-energy or physics laundering** | Expected free energy, variational free energy, or Hamiltonian least action is presented as proof of a universal engineering rule. | Keep only the bounded epistemic, pragmatic, horizon, and risk distinctions; reject mathematical equivalence and mandated scalarization. |

### A.11.OP:9 - Consequences

The pattern changes practice before a requirement is installed. A designer names the receiving horizon and checks what keeping or removing the requirement changes. Duplicate status work becomes removable without making “less paperwork” a universal argument. Deterministic transformations remain because they produce the selected result. Exploration, assurance, recovery, and small cues remain when their delayed or relied-on consequence is explicit.

| Benefit | Cost or boundary |
| --- | --- |
| Mandatory effort is tied to a decision, result, reliance, or recovery use. | The designer must name that receiving use instead of appealing to generic prudence. |
| Immediate and delayed value are distinguished without a universal calculation. | Material plausibility still depends on the applicable subject, evidence, risk, or assurance basis. |
| Ordinary application stays conversational. | Consequential or disputed use may need an existing claim-bearing episteme for its relying consumer. |
| Direct owners remain intact. | The screen decides only whether the requirement is non-ceremonial for the declared use and horizon. |
| Local closures can remove speculative work and still reopen. | A changed horizon, duty, result, reliance, or alternative can legitimately reverse the earlier disposition. |

### A.11.OP:10 - Rationale

Operational parsimony is about relevance, not abstract minimization. The fewest-step method can be wrong when one additional action realizes the chosen result, changes a later policy, or preserves a relied-on condition. The longest method can also be wrong when its extra actions have no substantive receiver. Comparing keeping and removing one proposed requirement makes that difference visible without inventing a global cost function.

The three branches cover distinct reasons for mandatory status. Decision-changing result preserves exploration and discrimination. Selected realization preserves deterministic work. Assurance or recoverability preservation protects a named relied-on condition. Each reason justifies only mandatory status for the declared use and horizon; its direct owner establishes every downstream claim.

The horizon must be substantive and bounded. A next-event horizon hides delayed information value; an indefinite horizon lets hypothetical future usefulness justify everything. The nearest named receiver is the smallest horizon that can carry the reason and the smallest reopen boundary when the use changes.

The rule coordinates existing decisions, transformations, results, evidence, assurance, and recovery uses. Keeping these objects under their direct patterns preserves FPF layering while giving practitioners one discoverable admission question.

### A.11.OP:11 - SoTA-Echoing

| Practice question | Best-known line and serious alternative | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- |
| How should a process designer recognize information-seeking action whose value appears in a later decision rather than the immediate result? | The selected line distinguishes epistemic from pragmatic value and evaluates present action across counterfactual future policies. The serious default is an immediate-result screen that calls a probe useless when the next action stays unchanged. | The default deletes useful exploration. **Adapt:** the decision-changing-result branch admits a probe only when a materially plausible result changes a named later policy inside the substantive horizon. | Friston et al., [“Active Inference: A Process Theory”](https://direct.mit.edu/neco/article/29/1/1/8207/Active-Inference-A-Process-Theory) (2017), supplies the epistemic/pragmatic distinction; Friston et al., [“Sophisticated Inference”](https://direct.mit.edu/neco/article-abstract/33/3/713/97487) (2021), supplies the counterfactual policy horizon. They are best-known-line candidates for these discriminators, not evidence of a universal engineering threshold, FPF ontology, or effectiveness claim. At comparable use effort, naming the receiving decision preserves delayed value that the immediate-result default loses. | Reopen if stronger current evidence changes the epistemic/pragmatic distinction, defeats the receiving-decision test, or supplies a lower-effort discriminator that preserves the same exploration boundary. |
| Can expected free energy or physical least action serve as a universal scalar rule for admitting engineering actions? | The selected critical line shows that expected free energy is not obtained merely by projecting variational free energy forward, while least-action results in the free-energy principle depend on a particular random-dynamical and Bayesian construction. The serious alternative is to transplant EFE, VFE, or Hamiltonian “least action” as a general engineering objective. | The transplant launders model-dependent mathematics into authority and can hide the actual receiving use. **Reject:** no EFE/VFE/Hamiltonian equivalence or mandatory score enters the Solution. **Adapt:** judge information-seeking work by a named receiving decision and counterfactual horizon, with risk and ambiguity supplied by their direct owners. | Millidge, Tschantz, and Buckley, [“Whence the Expected Free Energy?”](https://direct.mit.edu/neco/article/33/2/447/95645/Whence-the-Expected-Free-Energy) (2021), supplies failure evidence against the simple VFE-forward account. Friston et al., [“The free energy principle made simpler but not too simple”](https://www.sciencedirect.com/science/article/pii/S037015732300203X) (2023), supplies the model-dependent least-action construction. Neither source establishes an engineering duty, assurance floor, scalar optimum, or universal process law. The selected qualitative rule is cheaper to apply and keeps direct authorities visible. | Reopen if a current primary result establishes a transferable engineering admission rule with explicit scope and lower decision error at comparable effort, or if a governed use requires a quantitative comparator under its own direct pattern. |

### A.11.OP:12 - Relations

- **Classified by:** `E.3` as one `Prag` principle. It primarily advances P-1 Cognitive Elegance, P-7 Pragmatic Utility, P-10 Open-Ended Evolution, and P-11 State-of-the-Art Alignment while respecting the other Pillars.
- **Coordinates with:** `A.11`, which governs admission of ontology additions. Namespace adjacency makes the two parsimony questions discoverable; their EntitiesOfConcern remain distinct.
- **Coordinates with:** `E.11.PUA` and `E.11.PUR`, which govern use, recommendation, coordination, and reuse after a pattern has been selected. A.11.OP asks whether an extra mandatory requirement belongs in the first place.
- **Coordinates with:** `C.11`, `C.19.2`, `A.19`, and Method Engineering for comparison or configuration of qualifying alternatives under their own conditions. Those owners decide the application threshold and choose among alternatives.
- **Coordinates with:** `E.13` for proxy-to-value repair and `E.23` for operations inside repeated evaluated improvement. A.11.OP retains the initial action-admission question.
- **Coordinates with:** `A.3.1` and `A.3.2` for Method and MethodDescription identity, `A.15.1` for dated Work, and `A.15.7` for next-action choice during ongoing Work. A.11.OP governs design-time admission of the requirement.
- **Constrained by:** applicable law and regulation, `E.5` Guard-Rails, `A.10` reliance boundaries, `B.3` assurance floors, and any other direct subject or authority pattern for the use.
- **Consumed by:** Method Engineering and other DPFs when they decide whether domain-specific requirements or support apparatus deserve mandatory status. Those frameworks retain their domain decisions and evidence.
- **May be specialized by:** local practice frameworks for concrete execution and assurance. Their local arrangements remain local rather than FPF authority.

### A.11.OP:End
