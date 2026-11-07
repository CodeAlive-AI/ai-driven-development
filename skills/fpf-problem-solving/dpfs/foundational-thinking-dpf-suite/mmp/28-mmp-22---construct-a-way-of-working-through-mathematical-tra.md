## MMP.22 - Construct a Way of Working through Mathematical Transformation

> **Status:** Stable

> **Type:** Method pattern
>
> **Normativity:** Normative within the stated use

### MMP.22:1 - Problem frame

Use this pattern when a mathematical transformation suggests a different way of doing recurring work. Factoring a repeated operation may let several contributions share preparation. Changing a decision rule may avoid unnecessary work. Replacing an operation by a different construction may make a previously unavailable result obtainable.

Begin with the working difficulty, the proposed transformation and the consequence that matters. Recover what the mathematical objects describe in the work. Derive the changed construction, then turn its operations and conditions into a candidate way of working.

The result is a candidate with a stated practical change, its mathematical grounds and the conditions still needed in the work. A useful result can also be a changed description of the existing method, or a reason that the proposed transformation cannot supply the desired improvement. Such a conclusion can finish the present question.

This method designs through a mathematical model. C.39.RQ supplies the situated requirements, C.32.MWA.PP and MMP.21 compare arrangements, and B.1.5.CM distinguishes a proposed way of working from a Method whose relations obtain. The mathematics is supplied by MATH or the relevant mathematical practice. The additional work here is to construct a practicable change from that mathematical result.

The reader needs an account of the work and enough mathematics to interpret the chosen transformation, or a collaborator who can explain its assumptions and consequence. Use mathematics that expresses the needed dependency; a small equation can be sufficient.

Use an already suitable method without deriving another. When the candidates are already constructed, compare them through C.32.MWA.PP. When only one execution's dates or assignments change under an unchanged rule, the result belongs to planning that Work; it does not yet establish a changed reusable method.

### MMP.22:2 - Problem

A transformed mathematical description can look like an improved method while omitting the action that would realize it. Conversely, a useful transformation may remain an equation because nobody reconstructs the resulting work.

The main difficulty is that mathematical preservation has a chosen scope. Two constructions may produce the same final value while requiring different information, changing intermediate results or using the same resource at incompatible times. A mathematical improvement can also depend on a preparation, capability or permission the performers do not have.

The method engineer must recover the proposed working change and determine which conclusions follow from the mathematics, which depend on its correspondence to the work, and which remain unresolved.

### MMP.22:3 - Forces

| Force | Tension |
| --- | --- |
| Mathematical freedom and working constraints | A mathematically valid transformation of an expression may require an unavailable operation or a prohibited change of order. |
| Preserved result and changed means | Output agreement can coexist with different effort, intermediate access or failure behavior. |
| Reuse and independence | Sharing a contribution saves work but can introduce a common failure or stale information. |
| General rule and particular execution | A new reusable procedure differs from moving one task in a schedule. |
| Formal derivation and situated judgement | Mathematics exposes a consequence under assumptions; actual feasibility needs its own grounds. |
| Further assurance and useful completion | A conditional design can answer the current question without an obligatory trial. |

### MMP.22:4 - Solution

MATH.17 and MATH.18 supply the actual operation transformation and its preservation or recovery relation. MMP.10 supplies a constraint formulation where one is needed, and MMP.18 keeps shared contributions and dependence truthful. The construction here returns from those mathematical results to a reusable working rule: what performers now do, which intermediate contributions remain necessary, and which new inputs, capabilities or support make the change obtainable. Use a supplied correct transformation directly; an equal expression alone is not the changed work.

Relate the existing way of working to its mathematical account. Transform that account, then reconstruct the proposed working operations and their conditions. Establish the claimed mathematical consequence and the correspondence needed to use it. Return the candidate at the strength those grounds support.

#### MMP.22:4.1 - Choose the working change and what must survive it

Take the difficulty and requirements from the receiving work. State the gain sought and the properties that the change must retain. For example, the recipient may need the same acceptance decision with less effort, a result before a deadline, or a new result the incumbent cannot produce. These are different transformation questions.

Retain requirements about intermediate contributions when they matter. An early indication, an independent assessment or an explanation of every failure can be part of the needed result. Equality of a final number does not include them automatically.

Recover the allowed variation. The method may permit a different order or performer while requiring an independent second observation. A proposed change of that requirement is a separate decision under C.39.RQ; omitting it from the model does not amend it.

#### MMP.22:4.2 - Recover the mathematical operations and their working meaning

Represent the contribution to be changed at the detail the transformation uses. Recover each operation's input, result and relevant state, including information available when it is performed. If an operation alters its input or the surroundings, include that effect in the account used for the transformation.

MATH.17 lets operations themselves be constructed and transformed; MATH.18 compares what different accounts preserve. MMP.21 constructs the comparison with actual work requirements.

Distinguish several transformations that can look alike on a diagram. Copying a value can differ from obtaining a second observation. Commuting two pure functions can differ from interchanging actions on a shared object. Parallel branches in a mathematical representation do not provide two available performers.

Choose a richer account only when the omitted distinction can change the candidate or its use. A deterministic function can be sufficient for transforming a fixed-data calculation. Stochastic observations need their dependence; shared-state actions need their effects.

#### MMP.22:4.3 - Perform the transformation and derive its scope

Apply the mathematical construction with its conditions. A transformation may preserve an answer, establish a one-way refinement, give a bounded approximation or construct a new family of operations. State which of these conclusions is obtained.

For a preservation claim, compare the original and transformed constructions over the admitted inputs. If R extracts the required result from a construction's outcome, the condition may be:

~~~
R(new(x)) = R(old(x)) for every admitted x.
~~~

The equality concerns that result. Expand R or the compared behavior when intermediate responses, errors or resource interactions also matter. For a bounded approximation, derive the bound and the inputs on which it holds. For a new capability, establish what the new construction can produce and which old requirements it still satisfies.

Derive the gain separately. A reduction in the number of operations can imply less work under a supplied cost model. It may leave elapsed time unchanged, or increase storage and communication. Use the existing characterization and comparison methods when those trade-offs affect the choice.

A familiar algebraic rule is usable when its assumptions fit. If a proposed rewrite fails, return the failed condition; do not present the transformed expression as a viable candidate. Consider another construction when a promising alternative remains.

#### MMP.22:4.4 - Construct the changed way of working

Translate the transformed construction back into operations that performers can carry out. Name the change to the reusable rule: what is obtained once or repeatedly, what information is retained, when a branch is selected, or how a contribution is allocated.

Recover the resulting dependencies. Shared preparation needs a usable result, access for its consumers and a rule for when that result ceases to apply. An earlier decision needs its inputs earlier. A removed operation may have supplied a useful intermediate result even if the final-value model ignored it.

Keep the Method question separate from surrounding changes. The candidate may require a tool, capability, permission or assignment; those are conditions for using it. Changing only such a condition can enable the same Method rather than create a new one. A.3.1 determines Method identity; B.1.5.CM constructs and qualifies a claimed Method whole.

Write the proposed rule in the language of the work, with the mathematical account available for deriving or revising it. An engineer should be able to explain what a performer would do differently without repeating a formalism they cannot interpret.

#### MMP.22:4.5 - Compare the candidate and return what is supported

Compare the candidate with the incumbent and any serious alternatives under the same working requirements. MMP.21 supplies a mathematical comparison where useful; C.32.MWA.PP and the existing worth and portfolio methods handle the broader decision.

Separate the derived consequence from its working assumptions. A formula can establish the expected number of operations under a supplied distribution. It cannot by itself establish the distribution, actual preparation time or a performer's capability. Retain only the unresolved conditions that matter to the receiving decision.

Choose further work through C.11.DUA. An existing result may support retaining the incumbent, adopting a bounded change where authorized, or keeping a conditional candidate for later use. When a trial can change the decision enough to warrant its cost, A.3.1.WT and A.3.1.FT supply the appropriate trial and fit judgement. A.3.1.MI handles a selected introduction.

A.3.1.MV preserves the candidate and its consequential changes when later comparison needs that lineage.

Reopen the affected transformation when an input, dependency, required result or realization condition changes. Retain the parts of the argument and the work that the change leaves valid.

### MMP.22:5 - Archetypal Grounding

These constructed cases demonstrate changes to reusable procedures. Their numerical assumptions are supplied for the calculation; using the candidates in a project requires the corresponding working facts.

#### MMP.22:5.1 - Share preparation while preserving the receiving results

Two engineering analyses use the same fixed set of measurements. Each first converts the source into a common unit and coordinate convention, then derives its own result. Let f be the deterministic conversion, g the first analysis and h the second. The required pair is:

~~~
old(x) = (g(f(x)), h(f(x))).
~~~

The transformation obtains y=f(x) once and distributes that unchanged value:

~~~
new(x) = let y=f(x) in (g(y), h(y)).
~~~

The required results agree for every admitted x when the same conversion and input apply and neither consumer changes y. The proposed working rule is to prepare one shared converted dataset for this pair of analyses, identify the input and conversion used, and let both consumers read that result.

Suppose conversion takes 12 minutes, the two analyses take 3 and 5 minutes, and preparing access to the shared result takes 1 minute. Summed effort changes from 12+3+12+5=32 minutes to 12+1+3+5=21 minutes under those assumptions. This is an effort calculation; it does not determine calendar completion when people and tools can work concurrently.

Now change the situation. The second analysis receives corrected measurements. Reusing y from the old input no longer computes h(f(x_new)). The candidate's reuse rule must identify an unchanged input and conversion, or recompute the affected preparation. The factorization remains correct; its former working precondition has failed.

In another use, the two original preparations were independent measurements rather than repeated deterministic conversion. Sharing one measured value removes that independence. If the measurement errors are independent and each has variance s^2, averaging the two measurements has error variance s^2/2. Copying one measurement twice and averaging it retains variance s^2. The apparent duplication cannot be eliminated under a requirement for the former error variance. MMP.18 recovers the shared dependence; the mathematical function account must be changed before the work is redesigned.


#### MMP.22:5.2 - Change the order of checks without changing the required decision

An administrative procedure accepts a case only if checks A and B both pass. The checks do not change the case or each other's outcomes. Either may be performed first, and the current requirement permits stopping after the first failure. A takes 6 minutes and passes 90% of cases; B takes 2 minutes and passes 50%. These are supplied proportions for the same incoming population, unaffected by check order. Times are fixed.

With A first, expected effort is 6+0.9\*2=7.8 minutes. With B first it is 2+0.5\*6=5 minutes. Both return the same acceptance decision for every case. The candidate rule is to do B first and run A only after B passes.

For two such checks i and j with fixed costs c_i,c_j and pass probabilities p_i,p_j, placing i first has no greater expected cost when:

~~~
c_i + p_i*c_j <= c_j + p_j*c_i,
equivalently c_i*(1-p_j) <= c_j*(1-p_i).
~~~

For this two-check comparison, independence of their outcomes is unnecessary: the second check is incurred exactly when the first passes. Extending one fixed ordering rule to many checks needs the conditional probabilities among cases reaching each position; marginal ratios alone can fail when those probabilities change.

Now require the procedure to report every failed condition so that the applicant can correct the case in one return. Stopping after the first failure no longer supplies the required result. Both checks must then be completed, taking 8 minutes of summed effort under the same assumptions. A changed order may still affect the time of an early indication, but it no longer produces the claimed effort saving.

If the requirement instead remains the first-failure decision but A supplies information needed to perform B, the proposed order is unavailable. Add the preparation that would make B independently executable and recompute its cost, or retain A first. A lower algebraic value is not a usable method while its required input is unavailable.

The changed reusable screening rule belongs to method design. Scheduling a particular person's A check on Tuesday under the unchanged rule would be a Work-planning result.

### MMP.22:6 - Bias-Annotation

Algebra makes repeated calculation easy to see, which can hide the distinct contributions of people, instruments and organizations. Recover whether repetition provides independence, learning, accountability or access before treating it as duplicate computation.

The small cases use fixed costs and simple outputs. In continuing work, feedback, queues and changing inputs can alter the comparison. Use the corresponding modeling and computational methods when those interactions change the selected transformation.

### MMP.22:7 - Conformance Checklist

The proposed transformation supports its stated use when:

- the working difficulty and desired change are recognizable;
- the mathematical operations have recoverable meanings in the work;
- the transformation's assumptions and retained or changed result are stated;
- the claimed gain follows under a supplied comparison basis;
- the candidate specifies a changed reusable operation or rule that performers could carry out;
- required information, capabilities and other realization conditions are available or remain visibly unresolved;
- a derived model consequence is distinguished from an observed working consequence;
- a changed requirement or dependency has a usable return to the affected argument.

These conditions recognize a constructed candidate. Acceptance for a particular use follows from the evidence and decision appropriate to that use; the construction imposes no trial on every proposal.

### MMP.22:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| Treat an equal expression as an implemented change | No performer has a different reusable rule | Reconstruct the changed work or return a redescription |
| Preserve only the final value | An early result, explanation or independent contribution can disappear | Compare the full result needed by the recipient |
| Remove a repeated operation without recovering its role | Shared failure or stale input replaces an independent or updated contribution | Distinguish reusable calculation from renewed observation |
| Read a parallel expression as available capacity | The candidate assumes resources that cannot perform the work together | Supply or revise the allocation and its burden |
| Choose a smaller model cost with missing inputs | The preferred ordering cannot be performed | Recover the prerequisite and recompute the alternative |
| Demand a new trial for every conditional design | Further evidence can cost more than it changes the decision | Use C.11.DUA and return the supported candidate or incumbent |

### MMP.22:9 - Consequences

Mathematical reasoning can produce new method candidates rather than merely describe established practice. It also makes a rejected candidate useful: the failed transformation condition identifies what would have to change.

The method can reduce repeated work, change information timing or expose an unavailable operation. It may also require new support or transfer burden to another participant. A transformed rule becomes useful only at the scope where its correspondence and realization conditions hold.

For human and AI work, a candidate may redistribute operations between agents. The mathematical construction exposes the required contribution; capability and authority still determine who can provide it.

### MMP.22:10 - Architectural Rationale

Methods are the subject of this design activity. Mathematical operations supply a studied way to represent, transform and reason about them. A working operation and its mathematical representation therefore remain connected without becoming the same object.

The construction has two returns that must remain distinguishable. A mathematical transformation can improve the description or computation of an existing method. It can also suggest changed working operations. Reconstructing those operations, dependencies and conditions is what turns the latter into a method candidate.

This method complements comparison: MMP.21 derives consequences of supplied arrangements, while this pattern creates a candidate through a mathematical transformation. MATH retains the mathematical constructions; C.39.RQ supplies situated requirements, C.32.MWA.PP compares practical arrangements, and A.3.1.MV preserves a consequential variant and its evidence.

### MMP.22:11 - SoTA-Echoing

**Situated construction and reuse.** Ralyté's account of assembly-based Situational Method Engineering describes constructing a context-specific method from selected contributions. This supports retaining the working requirements and the receiving contribution while constructing a candidate. The mathematical branch here is a conceptual synthesis with transformation methods, not a claim that every method component must already be a formal mathematical object. [Author's research account](https://cui.unige.ch/~ralyte/research.html).

**A redesign heuristic needs its applicability conditions.** Reijers and Limam Mansar's historical review, *Best practices in business process redesign* (2005), §§4.3.1–4.3.3, discusses reordering, early rejection and parallelism, including their cost and elapsed-time trade-offs. The adopted move is to derive a particular redesign's consequence instead of applying a slogan such as “parallelize” universally. The two-check construction above retains its output and input conditions; it is not a claim that one ordering optimizes every workflow. [Source](https://hreijers.win.tue.nl/H.A.%20Reijers%20Bestanden/BPRpractices.pdf).

**Transformations can construct different families.** In *On the Anatomy of Attention* (2024, v2), §§2–5, Khatri and colleagues distinguish equational diagram transformations from refinements of parameterized function families and explore recombinations of attention components. This contributes the distinction in :4.3 between equality, refinement and a changed family. Equality within one representation does not establish equal training behavior, learned parameters or performance on another task. The paper's computational setting demonstrates a possible mathematical design method; applying the same idea to other work needs its own interpretation and constraints. [Paper](https://arxiv.org/pdf/2407.02423v2).

**Operational constraints remain part of the question.** Dijkman's *Business Process Optimization* (BPM 2025) frames redesign and execution choices around resources, timing, uncertainty and competing objectives. Its published summary supports the breadth of that question; it is not used here as a proof of a particular optimizer. This pattern uses mathematical transformations to obtain candidates, then retains the existing Core comparison and decision Methods rather than prescribing universal optimization. [Publication and summary](https://research.tue.nl/en/publications/business-process-optimization/).

The serious alternative is to adapt a familiar method directly or use a redesign heuristic without a mathematical model. Keep that cheaper route when it settles the consequence. Mathematical construction earns its effort when it exposes a consequential dependency, establishes a useful preserved result or produces a candidate otherwise difficult to obtain. A new source or technique reopens this choice when it changes those possibilities under the working conditions.

### MMP.22:12 - Relations

- **MMP.10** supplies a constraint formulation and its answer interpretation; **MMP.18** supplies a joint model when component exchange or shared dependence is unresolved. Reuse either result at its actual scope.
- **C.39.RQ** supplies situated requirements and appraises a disputed criterion.
- **C.32.MWA.PP** compares arrangements; **MMP.21** constructs and interprets their mathematical comparison.
- **B.1.5.CM** distinguishes a candidate account from obtaining Method relations.
- **MATH.17** constructs operations and transformations of them; **MATH.18** compares accounts and preserved consequences.
- **C.29** supplies correspondence between a mathematical account and its subject. **C.29.1** transfers the consequence at the justified scope.
- **MMP.11** supplies a family for an unknown relation; **MMP.8** formulates information-dependent choices.
- **CMP.12** constructs transformations of computations, and **CMP.14** constructs interactions between them when those are the operations being changed.
- **A.3.1.WT and A.3.1.FT** supply a selected trial and fit judgement; **C.11.MV** evaluates worth, **A.3.1.MV** maintains consequential candidate lineage, and **A.3.1.MI** handles introduction.
- **C.11.DUA** chooses worthwhile further inquiry; the existing portfolio and improvement methods retain complementary candidates and their development.

### MMP.22:End
