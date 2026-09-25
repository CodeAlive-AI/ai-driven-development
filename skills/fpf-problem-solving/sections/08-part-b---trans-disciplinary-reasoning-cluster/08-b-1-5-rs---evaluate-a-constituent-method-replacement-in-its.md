## B.1.5.RS - Evaluate a Constituent Method Replacement in Its Encompassing Uses

> **Type:** Method pattern
> **Status:** Candidate

### B.1.5.RS:1 - Problem frame

Use this pattern when a constituent Method could be replaced, simplified or implemented differently and you need to know which encompassing uses remain possible. A faster check returns the same answer on familiar inputs but no longer exposes information another part needs. An approximation is adequate for ranking options but unsuitable for deciding whether a limit is exceeded.

Start with the direction of replacement and the practical gain sought. Ask: **“What do the receiving wholes rely on, and does this candidate still supply it under their conditions?”**

The first useful result is a bounded substitution decision: the uses preserved, uses needing adaptation or restriction, and uses for which the replacement is incompatible or unresolved. One decisive comparison may be enough. Do not perform a new trial when an available argument or known counterexample settles the decision.

Use B.1.5.EW first if the constituent and its encompassing uses are unclear. If only the wording or diagram changes and the performed Method remains unchanged, check that representation's correspondence instead. If the replacement supplies an entire standalone Method, use the relevant fit and choice Methods; this pattern contributes only the constituent-in-whole question.

### B.1.5.RS:2 - Problem

Local adequacy does not establish substitutability. The whole can depend on output meaning, intermediate interactions, order, timing, recoverability or resource demand that a local comparison omitted. A shared constituent can satisfy one whole and fail another.

The opposite failure is to demand that every internal detail remain identical. This prevents useful replacement even when the receiving work does not depend on that detail. The preservation question must come from the actual use.

### B.1.5.RS:3 - Forces

- A local gain can remove a contribution needed elsewhere.
- Several uses may require different guarantees from the same constituent.
- Simplification saves effort when its lost detail is irrelevant to the receiving action.
- Strong evidence can be expensive; a bounded argument or counterexample may already settle the next move.
- A common replacement reduces maintenance, while separate variants can preserve otherwise incompatible uses.
- Method identity, description correspondence and performance evidence answer different questions.

### B.1.5.RS:4 - Solution

Compare the candidate against what the encompassing work needs, then carry the changed contribution through that work. State the direction and conditions of the result.

#### B.1.5.RS:4.1 - Name the proposed change

Identify the current constituent, its candidate replacement and the gain: for example, reduced delay, effort or dependence on a scarce specialist. State what changes in the operation, its inputs, outputs, interactions or realization.

Keep a proposed replacement separate from one already performed. Use A.3.1 to settle any needed identity claim: exposing a hidden step, changing an implementation within an admitted variation and proposing another Method need not have the same answer.

#### B.1.5.RS:4.2 - Recover the receiving wholes

Identify the encompassing Methods or work arrangements whose use can change. Follow an indirect use through the intermediate whole while it affects the decision. Include a second receiving use when the constituent is shared; local success in the first use is not evidence for the second.

This is a search bounded by the intended replacement. If the actual users cannot be recovered, restrict adoption to the known uses or return the missing use information that prevents a broader decision. Do not require an inventory of all imaginable uses.

For each relevant whole, recover:

- what it supplies or assumes at the constituent's entry;
- what result or interaction it needs from the constituent;
- timing, ordering, coordination and resource conditions that affect this use;
- what variation or loss it can tolerate.

Plain statements are sufficient when they make the comparison executable. Use an existing interface or formal contract when it already states these conditions.

#### B.1.5.RS:4.3 - Compare the contribution under those conditions

Apply the proposed constituent to the receiving conditions. Follow what it supplies through the affected part of the whole, including an interaction before final output when the whole relies on it.

Choose an argument, available observations, calculation or trial that can discriminate the decision at proportionate cost. A known violation can reject a general replacement without testing every possible input. A successful example can reveal a usable construction but does not automatically support all inputs.

When an approximation is proposed, state the property preserved for the receiving use: a bound, ordering, feasible action, specified error or other needed consequence. Equal rounded answers on one example do not establish preservation of a different property.

If the same implementation must serve several wholes simultaneously, examine their joint demands. Separate success under incompatible settings is not one shared implementation. Compare retained variants or changed coordination where that is useful.

#### B.1.5.RS:4.4 - Classify the replacement by use

| Comparison result | What can follow |
| --- | --- |
| The needed contribution and conditions are preserved. | Adopt the replacement for that use at the supported scope. |
| Preservation holds only under a narrower condition. | Restrict use to that condition and retain a suitable alternative elsewhere. |
| An adapter or changed combination can restore the needed contribution. | Treat that adaptation as part of the candidate and check its full burden and behavior. |
| A required contribution is lost. | Reject the replacement for that whole, change the requirement through the relevant decision, or choose another candidate. |
| Information does not distinguish compatibility from failure. | Keep the uncertainty bounded and obtain more only if it can change a worthwhile next action. |

This is a directed conclusion. Replacing A by B in one use does not show that A can replace B, that they are the same Method, or that B is preferable in all uses.

#### B.1.5.RS:4.5 - Adopt or retain alternatives

Choose at the supported scope, accounting for adaptation, learning, operation and maintenance costs. Retain separate variants when their different strengths justify the burden; a single universal replacement is not required.

For an ongoing operation, use its ordinary rules for introducing change and retaining continuity. State the condition that would require reconsideration: changed inputs, another receiving whole, a tighter timing limit, lost support or a newly relevant result property. No separate certificate or trial is required merely to record that an existing basis was sufficient.

Return the decision in the form its receiver needs. Where the conclusion is only recognition of a plausible substitute, say so. A claim of guaranteed preservation needs the argument or assurance appropriate to that claim under B.3; a local decision under uncertainty uses C.11 and C.11.DUA.

### B.1.5.RS:5 - Archetypal Grounding

#### B.1.5.RS:5.1 - Faster ordering in two encompassing uses

A team proposes replacing a stable sorting Method with a faster one that need not preserve the input order of equal keys.

One whole prepares a table showing how many records occur at each key. Internal order among equal keys does not affect those counts. Subject to the remaining input and performance conditions, the candidate can supply that contribution.

Another whole schedules requests by priority while retaining arrival order among requests of equal priority. Its method first orders records by arrival and then stably orders them by priority. Replacing the second sort with the candidate can reverse equal-priority requests. The earlier arrival ordering no longer survives the composition.

An allowed reversal of two equal-priority records with different arrival times exposes the incompatibility with the required guarantee. This is a counterexample to unrestricted replacement, not a prediction that this implementation reverses every such pair; repeated random benchmarks cannot restore the missing guarantee. Options include retaining the stable Method or sorting by an explicit compound key of priority and arrival. The compound-key candidate has changed the operation; compare its behavior and cost before using it. The same “sorted by priority” description concealed different requirements of the two wholes.

#### B.1.5.RS:5.2 - A bounded estimate and a threshold decision

A constituent estimates a quantity with absolute error at most 2. A receiving whole only needs to distinguish alternatives separated by more than 4; the bound can support their ordering when both estimates satisfy it.

Another whole must decide whether the quantity exceeds 100. An estimate of 99 is insufficient: the admitted interval is 97 to 101 and crosses the threshold. A more accurate estimate or another decision rule is needed for that case. At an estimate of 95, the same error bound puts the whole interval below 100 and can settle that particular decision.

The change from “estimate the quantity” to “support this decision” makes the scope of replacement explicit. The threshold is stipulated in this constructed example; the pattern does not supply a rule for choosing it.

#### B.1.5.RS:5.3 - A quicker observation during coordinated work

A group performs a movement sequence in response to a leader. A proposed observation Method uses occasional snapshots rather than continuous observation. It can suffice for an exercise in holding a static pose, but miss the cue that starts a coordinated transition.

Recover the timing actually needed by the encompassing sequence. If the snapshot interval exceeds the available response window, better interpretation of each snapshot cannot restore the missed cue. Keep more frequent observation, redesign the cue so it remains available, or change the coordinated sequence. Each proposal has a different burden and requires its own bounded comparison.

### B.1.5.RS:6 - Bias-Annotation

The participant proposing a replacement often sees its local saving more clearly than the costs borne by other users. Recover the receiving requirements before choosing. A demand to preserve everything can conceal the opposite bias: treating familiar implementation detail as necessary even when no receiving use depends on it.

### B.1.5.RS:7 - Conformance Checklist

- Are the constituent, candidate, replacement direction and intended gain clear?
- Have the relevant receiving wholes and their relied-on contributions been recovered?
- Does the comparison carry the changed contribution through each affected use?
- Are joint requirements examined when one realization must satisfy several uses together?
- Does the conclusion preserve its conditions and evidence reach?
- Are adaptation costs and a useful reconsideration condition included where they change adoption?

### B.1.5.RS:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| One matching output stands in for preserved behavior. | Recover the timing, interaction or property actually used by the whole and test that contribution. |
| Compatibility in one whole is exported to every user. | Separate receiving uses and restrict the conclusion accordingly. |
| Every implementation detail must remain unchanged. | Preserve what the declared use relies on; permit changes outside that dependence. |
| An adapter is omitted from the candidate's cost or failure analysis. | Include the adapter in the candidate arrangement and follow the combined behavior. |
| A successful trial becomes an unconditional guarantee. | State its supported scope and establish stronger claims only when required. |

### B.1.5.RS:9 - Consequences

Useful replacements can be adopted where they work without silently breaking other wholes. An incompatibility can also expose a better architecture: different variants, an explicit interface or a changed combination.

The method requires knowledge of receiving uses. Its cost grows with meaningful differences among them, not necessarily with the number of documents or callers. Reuse one comparison across uses only when their relevant conditions and relied-on contribution match.

### B.1.5.RS:10 - Architectural Rationale

Substitution is a relation to a receiving use. A constituent's attractive property does not establish that relation. Recovering the whole's dependence avoids both unrestricted replacement and unnecessary preservation of detail.

When the receiving uses are already understood, the practitioner can begin with their requirements and compare the replacement directly. The result is a directed substitution decision across one or several uses, including a candidate that changes the whole to accommodate the new constituent.

### B.1.5.RS:11 - SoTA-Echoing

[Mazo, Compton, Cohen and Ames](https://arxiv.org/html/2409.14902v1) formulate compositional contracts for layered control systems. Their contribution supports checking what adjacent functions assume and supply, including their different signal and timing models. This pattern uses that conditional-composition idea beyond the paper's system class; its formal guarantees are not generalized.

The stable-sort case illustrates contextual preservation by an elementary algorithmic counterexample. The bounded-estimate case applies ordinary interval reasoning. These are constructed cases of the common Method, not evidence that every constituent requires a formal contract or a numerical error bound.

For the practical question of substituting a constituent, a local performance benchmark is a serious alternative: it can reveal speed, cost and errors on its tested inputs. It does not establish that a replacement preserving totals also preserves arrival order, or that its error bound supports the required threshold decision. Sections 4.2–4.4 therefore select receiving-use conditions first, then derive or test only the preservation those uses need. The worked counterexample or an available bound can settle the stated question at less effort than an additional benchmark; an unresolved performance question can still justify a targeted trial.

Formal compositional contracts offer a stronger alternative where the constituent, interfaces and encompassing system fit their mathematical assumptions. The cited control theory makes those assumptions and guarantees explicit. This Method adapts that conditional comparison into ordinary statements of inputs, interactions, results and permitted losses; it keeps the formal proof when its additional assurance is useful and attainable. It does not treat every professional practice as a control-system instance. Reopen the selected comparison when an unmodeled interaction, shared realization, changed receiver or unsupported adaptation defeats the preservation claim. If one constituent cannot satisfy the relevant uses together, retain different variants or change the encompassing arrangement instead of declaring one universally better Method.

### B.1.5.RS:12 - Relations

- B.1.5 and A.3.1 define Method composition, identity and replacement-claim distinctions.
- B.1.5.EW recovers constituent and encompassing work when those connections are not yet understood.
- B.5.RA and B.5.RR reconstruct and revise the argument on which preservation depends.
- C.29 governs a mathematical correspondence used in the comparison.
- C.30.LCA supplies control-specific conditions; C.30.ILC addresses resulting cross-scope architecture conflicts.
- C.11 and C.11.DUA govern the local decision and whether further investigation is useful.

### B.1.5.RS:End
