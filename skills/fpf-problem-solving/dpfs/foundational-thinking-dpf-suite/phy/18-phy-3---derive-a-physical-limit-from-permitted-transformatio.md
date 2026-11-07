## PHY.3 - Derive a Physical Limit from Permitted Transformations

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative within the stated use

### PHY.3:1 - Problem frame

Use this pattern when you need to determine what a physical process or device could accomplish before choosing its detailed mechanism, or when a familiar physical prohibition appears to rule out a proposed change. A candidate may have an acceptable energy balance yet require an unavailable preparation, consume a resource that was omitted, or perform differently on inputs that one device is supposed to handle.

The first useful result is a necessary condition on the requested performance, a conditional exclusion of a class of proposals, or a changed premise that opens a different construction. You obtain it by describing the complete physical transformation and constructing a comparison that the applicable physical laws constrain. “Permitted” here means allowed under those physical premises.

You need a working description of the requested effect, the resources and surrounding systems it may use, and the physical principles relevant to that effect. A qualitative argument can suffice. A quantitative result also needs the quantities and mathematical operations in its chosen comparison. The two worked cases require different preparation: energy exchanges and elementary ratios in the first, state vectors and inner products in the second. Obtain an unfamiliar physical premise or calculation from a suitable source or collaborator and retain the conditions on which its answer depends.

When an established bound already answers the same question under the same physical conditions, apply it directly. A measurement of a particular device, estimation of an unknown parameter and design of a mechanism have their own methods. Return here when their result changes the allowed transformation or the reach of a physical restriction.

### PHY.3:2 - Problem

A physical proposal usually names the desired effect more readily than the whole change needed to produce it. “Return the machine to service,” “copy an input” and “extract more work” can leave different resources, input families and end conditions implicit. Those differences determine which physical restrictions apply.

Detailed calculation of one design can reveal its failure while leaving other designs available. Conversely, a quoted limit can be applied outside its premises and suppress a useful construction. The difficulty is to derive a restriction whose physical description covers the proposals being considered, and then use it to decide what to change or investigate.

### PHY.3:3 - Forces

| Force | Tension |
| --- | --- |
| Reach across mechanisms | A bound can guide many designs, but its description must cover every design to which the conclusion is applied. |
| Complete physical change | Preparation, surroundings and restoration can determine the result; describing every microscopic detail would make the first inquiry unusable. |
| Admissible comparison | A simple reference can expose a strong limit, while a mathematically convenient inverse may require a physical operation that is unavailable. |
| Useful idealization | A larger class of ideal operations can yield a bound on real devices; an omitted physical contribution can invalidate that inference. |
| Continued construction | An obstruction can redirect work immediately, while removing that obstruction leaves further realization questions. |

### PHY.3:4 - Solution

Construct the complete proposed transformation, identify the physical restrictions shared by its candidate mechanisms, and use an admissible comparison to derive their consequence. Keep the requested performance and its physical conditions attached to the result. Revisit the premise that matters when the resources, input family or required performance changes.

#### PHY.3:4.1 - Specify the physical change and what must remain usable

Start with the proposed input and output. Include the range of inputs and the performance required on them. For a machine expected to handle an unknown input, ask whether one fixed arrangement must work throughout that range or whether the arrangement may be chosen after learning the input. For fluctuating processes, distinguish a guarantee on every run from an average or an allowed failure probability. MMP.8 supplies that formulation when the choice or information condition is difficult.

Follow the resources that can participate in the transformation: material, energy, prepared states, information about the input, external controls and connections to the surroundings. Describe their relevant initial and final conditions. A charged auxiliary, a memory that accumulates records and an initially correlated pair can be consumed resources even if the visible output is unchanged. Use the physical theory to decide which such differences matter to the proposed restriction.

For repeated operation, state what the device must remain able to do. Return to an identical state is needed only when the requested operation or the physical argument requires it. If the construction uses a reset, include its physical change and resource use. A device that still performs the next operation can have changed state; a device restored in one observed variable can have exhausted another needed resource. A.3.3.TR helps choose a sufficient state description where these cases are unresolved.

The result is a physical transformation with its allowed side effects and input conditions. Keep an unspecified preparation visible as an unresolved premise. It can be useful to derive a conditional bound before that premise is settled.

#### PHY.3:4.2 - Establish which physical restrictions cover the candidate mechanisms

Select the physical account that connects the requested change with a conserved quantity, an ordered change, a preserved relation or another necessary condition. State its regime and the systems to which it applies. A local balance law can require a larger boundary when something crosses it; a law for a closed process can require explicit surroundings when the proposed device exchanges matter or information.

Explain why every device in the proposed conclusion admits the chosen description. MMP.10:4.4 supplies this coverage requirement. Physically, it can mean including a reservoir and its controller, representing an unobserved auxiliary, or admitting all interactions allowed by the theory instead of only one circuit. Restrict the conclusion to the designs described if this coverage remains incomplete.

An enlargement of the allowed class can make exclusion easier: if even a class with additional resources cannot realize the requested transformation, its contained class cannot do so. Show that containment. An approximation chosen because it is easy to calculate does not automatically give such an enlargement; it can remove a coupling or noise source that changes what is possible. When only an approximate account is justified, propagate a suitable error allowance or retain a conditional result at that model's stated scope.

Use B.5.TU to recover the physical theory's premise and its consequence for the case. The output of this step is the applicable restriction and the reason it covers the proposed physical class. Further measurement is useful only if its possible result changes that premise or the next choice; C.11.DUA helps resolve a consequential uncertainty about that effort.

#### PHY.3:4.3 - Construct a comparison that exposes the restriction

Choose the operation that fits the available physical structure. The following two constructions address different situations and can be used independently.

**Compose with a reference and cancel selected changes.** Use this when an admitted reference process exchanges the relevant quantities or restores a needed condition. Choose the part of the proposal you want to eliminate from the combined account, then determine the reference's direction, amount and preparation that match it. Establish that the reference can perform that operation under the same connecting conditions. For example, two processes may exchange equal energy but require incompatible temperatures, pressures, phases or forms of delivery. Numerical equality alone cannot establish the physical connection.

Combine the proposed and reference operations, including their auxiliaries. Cancel only the matched exchanges or restored states; keep all remaining changes. C.29.BB supplies the accounting for additive quantities. Apply the physical restriction to the composite. If it would have a prohibited net effect, derive the inequality or condition on the original proposal that avoids that effect. A reference may be an ideal process admitted by the theory; building it in a laboratory is unnecessary for this conditional argument. Using the inverse in an equation still requires a reason that the needed physical reverse process is admitted.

**Compare inputs of the same operation.** Use this when one device must perform the requested transformation on a family of inputs and a physical law relates its actions on different inputs. Select inputs whose relation can expose the limitation. Write their proposed outputs, including allowed auxiliary outputs, while holding fixed the device and its input-independent preparation. Derive the relation the law requires between those outputs. If the requested outputs violate it, the common device cannot provide them under the stated conditions.

An auxiliary output may depend on the input even when the initial preparation cannot. Allow that dependence in the comparison. Requiring the auxiliary to return to a fixed state when the proposal permits a changed state would prove a narrower restriction. Conversely, choosing a different apparatus separately for each input would answer a different question from the fixed-device requirement.

These constructions can reveal a remaining physical premise rather than a bound. Name that premise and what supplying it would enable. Forcing either comparison when its connection conditions or input relation are absent adds no physical result.

#### PHY.3:4.4 - Derive the consequence with every remaining physical change included

Carry the quantities, signs, state conditions and input relations through the chosen comparison. Interpret each term by the physical contribution it represents. Check that the canceled effects have compatible units and conditions, and that the uncanceled effects describe the complete remaining process.

Obtain the requested inequality, an excluded transformation, or the unresolved condition on which either result depends. When using a mathematical invariant, MATH.11 supplies the derivation from the admitted transformation rules. When a numerical tool performs the algebra, retain the symbolic relation or a sufficient explanation that lets another participant inspect what the computation establishes. C.29.2 and C.29.3 govern a computation whose formulation or realization needs further work.

Distinguish a necessary bound from attainability. A proposed device can satisfy one physical restriction and still fail another, or approach a theoretical limit only as time or another resource grows. The useful output at this step says which candidates have been excluded, which remain under consideration, and which premise or construction controls the next question.

#### PHY.3:4.5 - Change the proposal at the premise that controls the result

Return the physical consequence in the terms of the working question. For a proposal outside the bound, identify a consequential change: supply a previously forbidden resource, allow a side effect, narrow the input family, relax precision or reliability, or change the condition for reuse. Derive the affected comparison again for the chosen change. Keep the original result for its original premises.

When the obstruction disappears, continue with a mechanism, an approximation or another limiting principle. PHY.2 can help construct a physical analogue for that inquiry; PHY.1 supplies physical similarity if transferring between regimes is the next difficulty. If the new question concerns an unfamiliar mathematical construction, obtain that contribution from Mathematical Thinking. B.5.MPC helps divide and reconnect those contributions across people and AI agents.

Stop the present derivation when its result is sufficient for the next decision. Further information or a physical trial is a separate action whose value depends on what remains unresolved. A concise explanation of the compared transformation and controlling premise is enough when it allows the intended user to continue.

### PHY.3:5 - Archetypal Grounding

#### PHY.3:5.1 - Bound a proposed engine without designing its mechanism

**Question.** A proposed cyclic machine takes 100 J from an ideal reservoir at 600 K and delivers 60 J as work. Its only other interaction is heat rejection to an ideal reservoir at 300 K. The machine returns to its initial state. Can a different mechanism make the proposal possible under these same conditions?

The physical preparation includes both reservoirs, the work store and restoration of the machine. It supplies no fuel, depleted auxiliary store or initially available nonthermal resource. The two temperatures are absolute thermodynamic temperatures. Energy balance gives 40 J rejected to the cold reservoir; that balance alone leaves the proposed output admissible.

Use the classical second-law account for these conditions. Its Clausius restriction excludes a composite process whose only net effect is transfer of heat from the colder reservoir to the hotter one. An admitted reversible reference between these reservoirs has `eta_ref = 1 - 300/600 = 1/2` and can run backward. This is a theoretical reference; no claim of a finite-power reversible laboratory device is needed.

Choose cancellation of the work exchange. A backward reference consuming the proposed 60 J extracts 60 J from the cold reservoir and delivers 120 J to the hot reservoir. The compatible exchanges combine as follows; positive entries increase the named store.

| Store or component | Proposed engine | Backward reference | Net change |
| --- | --- | --- | --- |
| Hot reservoir | -100 J | +120 J | +20 J |
| Cold reservoir | +40 J | -60 J | -20 J |
| Work store | +60 J | -60 J | 0 |
| Both devices | Each completes its cycle | Each completes its cycle | Restored |

The net process transfers 20 J from cold to hot with no other change. It violates the selected restriction. The argument uses only the proposed exchanges and cyclic condition, so changing the candidate's internal mechanism cannot repair it within this class.

For a general positive requested work `W`, the backward reference requires `Q_hot_ref=W/eta_ref`. If `W > eta_ref*Q_hot`, then `Q_hot_ref > Q_hot`; canceling work again produces the prohibited cold-to-hot transfer. Therefore:

~~~text
W <= eta_ref*Q_hot = (1 - T_cold/T_hot)*Q_hot.
For the stated inputs: W <= 50 J.
~~~

The practical result redirects the design question to work below this bound or to a change in the stated resources. It does not supply the design that attains a chosen value, its power or its operating cost.

**Change the allowed physical operation.** Suppose the proposed device may also receive 20 J of external work. A forward reversible reference producing 40 J from 80 J of hot-reservoir heat, together with routing those 20 J through the work store, can supply 60 J gross output. The net work produced is 40 J. The denominator and net exchange must now reflect the actual question; this construction supplies no engine producing 60 J net work from the original 100 J alone. If exactly 100 J must still be taken from the hot reservoir, an admitted additional transfer of 20 J from hot to cold accounts for the remainder. The total cold-reservoir gain is 60 J, and both laws permit the resulting exchanges. The changed resource condition opens a construction rather than altering the earlier bound.

For a microscopic proposal with initial correlations or a nonthermal auxiliary, use the physical account appropriate to those resources. A reservoir-only calculation leaves their contribution out. The source comparison in :11 identifies a current treatment; it does not prescribe the same generalized formula for every macroscopic device.

#### PHY.3:5.2 - Test copying across inputs while allowing auxiliary outputs

**Question.** Can one device take one input qubit in an unknown pure state and produce two perfect copies on every run? The device can use an auxiliary prepared independently of the input, and its final auxiliary state may depend on that input. Discarding an auxiliary is allowed.

Use the standard quantum description of a deterministic operation. Include the device's environment and any measurement records in the description of the complete process. A fixed mixed auxiliary preparation can be purified by adding a reference system. The total evolution can then be represented by one isometry `V`, which preserves inner products. This includes deterministic operations obtained by interaction and later discarding part of the system; it does not impose that the visible two-qubit map itself be unitary. If both required output copies are pure, their joint output factors from the remaining pure total state.

Choose two distinct nonorthogonal input states `|a>` and `|b>`. Let `|0>` be the blank second qubit and `|e>` the fixed initial auxiliary. Perfect copying would require:

~~~text
V(|a>|0>|e>) = |a>|a>|e_a>
V(|b>|0>|e>) = |b>|b>|e_b>.
~~~

The final auxiliary states are deliberately allowed to differ. Define `s=abs(<a|b>)`, with `0<s<1`, and `r=abs(<e_a|e_b>)`, with `0<=r<=1`. Taking inner-product magnitudes before and after the same isometry gives:

~~~text
s = s*s*r.
Dividing by s>0 gives 1=s*r.
But s*r <= s < 1.
~~~

The requirements are inconsistent. For the concrete pair `|a>=|0>` and `|b>=(|0>+|1>)/sqrt(2)`, `s=1/sqrt(2)` would require `r=sqrt(2)`. That exceeds the allowed overlap of normalized auxiliary states. More unobserved auxiliary output cannot make this deterministic perfect copier possible under the stated account.

This is a physical restriction on one operation across its input family. The mathematical step is preservation of an inner product; the physical work is establishing why the candidate devices admit that common description with the stated preparation. Showing failure of one guessed gate arrangement would leave this broader question unanswered.

**Change the input family.** Restrict it to the computational-basis states `|0>` and `|1>`, with a blank second qubit `|0>`. Controlled-NOT gives `|0>|0> -> |0>|0>` and `|1>|0> -> |1>|1>`. The same arrangement therefore copies every input in that restricted family. A different known orthogonal pair can first be mapped to that basis, copied, and mapped back on both outputs.

**Change the performance instead.** If failed runs may be discarded, the accepted operation is conditioned on an outcome and the all-runs argument no longer directly characterizes its normalized successful output. One must specify the allowed input set, success probability and failure output, then derive their restrictions. Allowing imperfect copies likewise changes the output relation and requires an accuracy question. The present result identifies why either revised problem differs; it supplies no unexamined claim that a desired success rate or accuracy is achievable.

### PHY.3:6 - Bias-Annotation

The method corrects two live errors: treating one device's failure as a prohibition on every mechanism, and applying a quoted prohibition after its resource or input conditions have changed. Its own principal risk is selecting a convenient physical description that omits an allowed device or contribution. Keep the coverage argument next to the conclusion and use a changed-condition return to expose what the result actually depends on.

The worked proofs assume established classical thermodynamics and standard quantum operations in their stated regimes. Their conditional strength should remain visible when a research question concerns the adequacy of those theories themselves. A formal contradiction identifies incompatible premises; it does not choose by itself which empirical premise to revise.

### PHY.3:7 - Conformance Checklist

- [ ] The requested physical effect includes its input family, performance criterion and relevant preparation.
- [ ] Consumed resources, surrounding systems and any required restoration or continued capability are included where they affect the restriction.
- [ ] The selected physical account has a stated regime and a reason to cover the device class in the conclusion.
- [ ] The comparison uses compatible admitted reference operations, or the same operation on inputs linked by the physical law.
- [ ] The derivation retains uncanceled changes and allowed auxiliary outputs.
- [ ] The result distinguishes the derived necessary condition or exclusion from the still-needed realization.
- [ ] The explanation shows which changed premise would require another derivation and what the current result enables next.

### PHY.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure in use | Repair |
| --- | --- | --- |
| A limit quoted without its physical preparation | A bound derived for two reservoirs is applied to a device consuming an additional resource. | Recover the complete transformation and derive the applicable restriction. |
| An algebraic inverse treated as an available apparatus | The comparison depends on a reverse process whose required preparation or control was never admitted. | Establish the physical reference operation before using its cancellation. |
| Failure of one construction promoted to impossibility | Another permitted coupling or auxiliary lies outside the calculation. | Give a covering physical description or restrict the conclusion to the analyzed class. |
| Input-specific devices hidden inside one-device wording | A calculation selects a separate operation after knowing each supposedly unknown input. | Hold the common device and allowed information fixed across the input comparison. |
| Reset or ancillary change omitted | Apparent cyclic performance consumes a stored resource or accumulates a consequential change. | Include that state change and the reset required by the actual repeatability condition. |

### PHY.3:9 - Consequences

A useful physical limit can be obtained before the internal mechanism is known. It can reduce unproductive design work, expose an omitted resource, or suggest a different input family or performance requirement. The derivation also gives collaborators a physical question to answer: a needed reference process, a covering law or an unsettled preparation.

The cost is obtaining a physical account whose reach matches the conclusion. Stronger exclusion usually needs broader coverage than failure of a candidate design. A conditional result is often sufficient to guide the next step while that coverage is developed. Near a limiting value, finite time, noise, size and implementation constraints can determine whether pursuing it is useful.

### PHY.3:10 - Architectural Rationale

The complete transformation is the shared object of the two comparison constructions. It makes hidden resources and restoration conditions available to reasoning, while leaving the internal mechanism open. Reference cancellation reduces a proposal to a constrained composite effect. Input comparison constrains what one operation can do across alternatives. These differences explain the choice in :4.3; neither construction is a compulsory stage of the other.

The physical premise gives the mathematical operation its bearing on a device. A conserved sum or preserved inner product can be studied mathematically without that interpretation. Conversely, knowing the name of a physical principle does not yet specify the permitted exchanges, preparation or input family. The method supplies this physical construction and uses the existing mathematical and common inquiry methods for their contributions.

An ideal reference helps bound real proposals when its admitted operations and the coverage relation are explicit. It serves a different purpose from a realistic simulation of one device. Both kinds of account can remain useful in the same inquiry: the bound directs construction, and the constructed mechanism reveals further practical restrictions. The explanation of a failed proposal can also generate the next problem by identifying a consequential change of premise.

### PHY.3:11 - SoTA-Echoing

**Reversible-reference comparison.** [David Tong, Statistical Physics, §4.3.1-4.3.2](https://davidtong.org/pdfs/teaching/statistical-physics/statphys4.pdf) gives the established Carnot comparison and the thermodynamic temperature ratio. It is a historical methodological anchor for composing processes and canceling exchanges. The pattern uses the construction beyond a particular working substance.

**Input comparison with auxiliaries.** [Peter Shor, Quantum Computation, lecture 5](https://math.mit.edu/~shor/18.435/oldlectures/lecture5.html) presents the no-cloning comparison and explicitly includes an input-dependent ancillary output. The present worked case spells out the total-process interpretation, overlap bound and changed-input return. The classical thermal and quantum arguments exemplify different physical restrictions and different comparison operations.

**Resource conditions in current thermodynamics.** [Aguilar and Lutz, Correlated quantum machines beyond the standard second law, version 2 (2025)](https://arxiv.org/html/2409.07899v2) analyzes initial correlations, nonthermal resources, interaction energy and changes remaining after a driving cycle. These contributions explain why a reservoir-only efficiency claim can need a different account. Its microscopic assumptions determine where its generalized expressions can be used.

**One occurrence and repeatable performance.** [Marletto, Deutsch and Vedral, Tests of constructor theory (2026), §1.4 and §3.2](https://arxiv.org/html/2606.07352v1) develops the distinction between an allowed evolution and a device able to repeat a specified transformation, including the difference between reversing dynamics and supplying a reusable inverse operation. The pattern adopts that problem distinction. The article's new constructor-theoretic principles are research proposals with their own tests; they are unnecessary premises for the two established arguments above.

The synthesis selects operations for constructing a physical limitation and reopening it under changed conditions. A new account of the permitted operations, an omitted resource or a changed performance condition is a reason to revisit the affected argument and its source premises.

### PHY.3:12 - Relations

- **B.5.TU and B.5.MPC** supply theory-to-case use and division and reconnection of mathematical, physical and computational work. **B.5.QD** helps develop the next question from an obtained limit or obstruction.
- **A.3.3.TR** supplies a sufficient state description and representation of interacting changes. **C.29.BB** supplies boundary accounting and cancellation for additive quantities.
- **MMP.8 and MMP.10** supply information-conditioned choice, constraint formulation and the coverage requirement for a class-wide conclusion. **MATH.11** supplies mathematical invariant construction and use.
- **PHY.1** supplies physical similarity when the comparison must cross regimes; **PHY.2** constructs a physical analogue for the continuing mechanism question.
- **C.29.1-C.29.3** govern mathematical correspondence, computational formulation and realization where those are unresolved. **B.1.5.CM** develops a proposed composition of the work method using the physical result; **A.3.1.CC** checks the claims in that account and its description. **C.11.DUA** helps decide whether an additional inquiry can change the useful next action.

### PHY.3:End
