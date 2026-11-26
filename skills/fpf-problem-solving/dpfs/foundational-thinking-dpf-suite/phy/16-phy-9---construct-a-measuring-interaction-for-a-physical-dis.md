## PHY.9 - Construct a Measuring Interaction for a Physical Distinction

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### PHY.9:1 - Problem frame

Use this pattern when a physical difference matters to the work, but the available arrangement does not make that difference observable. You may need to choose a sensing effect, prepare a reference, separate a wanted response from another influence, or change a probe that disturbs its subject.

The first result is a proposed measuring interaction with a usable response: what to prepare, what to couple, what to observe, and which physical differences the response can resolve. It can remain conditional on an identified coupling, calibration or operating range.

C.16.MR constructs the relation between a sought property and an indication. This method develops its physical realization when that realization is missing or inadequate. You can design the interaction before taking measurements or revise it after obtaining them. Changing a preparation or comparison can suffice with the existing instrument.

You need to interpret the relevant physical theory and the conditions under which its effect occurs. For a measurement design, establish which physical distinction matters and what observation could reveal it under attainable conditions. Determine who can choose the distinction, design the interaction or make the observation when that contribution is entrusted or the feasibility of the design depends on its provider. A laboratory may be entrusted to decide which temperature matters for a reading and how the sensor response can establish it. If the commission calls for the learner’s own choice of the quantity, leave that choice to the learner with the agreed help. The examples supply their additional mechanical, fluid and quantum premises.

Use an existing arrangement and calibration when they resolve the question. If the physical arrangement is suitable and only inference from its records remains, use C.16.IR or MMP.7.

### PHY.9:2 - Problem

A property can affect a physical system without appearing in the chosen readout. Mass occurs in the force and inertia of a falling body but cancels from ideal gravitational acceleration. A field can change a quantum state's phase while the selected measurement remains insensitive to it.

A responsive instrument can also confuse the sought property with its own interaction. A capillary responds to pressure through a liquid column, but surface forces contribute to the height. Repeating the same reading more precisely does not separate those contributions.

The difficulty is to construct a physical comparison that exposes the wanted difference under the available conditions.

### PHY.9:3 - Forces

| Force | Tension |
| --- | --- |
| Coupling and selectivity | A strong response can amplify an unwanted influence as well as the target. |
| Preparation and observation | The same interaction can be informative for one prepared state and uninformative for another. |
| Reference and portability | A comparison can remove an unknown contribution while depending on shared physical conditions. |
| Signal and disturbance | The probe can make a difference visible while changing the quantity whose earlier value was wanted. |
| Local sensitivity and usable range | A steep response can improve a local estimate while leaving distant possibilities indistinguishable. |
| Improved measurement and effort | Another interaction is useful only when its added distinction matters enough to the receiving work. |

### PHY.9:4 - Solution

**Choose the wanted distinction → select a responsive physical effect → construct the preparation and comparison → derive the readout and its disturbance → determine what can be resolved → revise the arrangement where needed.**

#### PHY.9:4.1 - Specify the physical distinction and conditions

Name two physical possibilities that the work needs to distinguish, or a quantity range within which an estimate is needed. State where and when the property is sought. A pressure before connecting a probe and the pressure maintained during readout can be different targets.

Choose the needed consequence. Detecting a change, estimating a value and deciding which side of a limit applies place different demands on the same arrangement. C.16 provides the characteristic and scale; C.16.IR determines what a given indication can resolve.

Include the conditions the work permits you to change. A prepared reference, imposed force, interrogation time or detector orientation is a potential experimental choice only when it can be controlled.

#### PHY.9:4.2 - Choose an effect that carries the distinction into a response

Find a physical interaction through which the sought difference changes a state, transition, force, flow or other observable response. Derive that dependence far enough to see whether the proposed readout retains it. PHY.4 can constrain an unknown law; PHY.6 or PHY.7 can construct the relevant physical evolution.

For a proposed arrangement, ask what differs in the predicted readout between the selected physical possibilities under the same preparation. Reject an insensitive arrangement for this question even if it uses a well-established effect. When another available arrangement could change the choice, compare the distinctions it can resolve and the resources it requires. The falling-body case in :5.1 shows why the occurrence of a quantity in one equation is insufficient.

Identify what supplies a reference. A known imposed quantity, a second preparation or a stable response can make the comparison interpretable. State the physical relation that allows the reference to be transported into this measurement. Numerical labels on two devices do not establish that relation.

If the coupling is unknown, keep the proposed response conditional. An available bound or calibration may settle the question. Select new characterization only when it can change the intended use.

#### PHY.9:4.3 - Construct the preparation and comparison

Specify how the subject, probe and reference are prepared before coupling. Then choose what is held fixed, what is varied and what is read. Include the order when the first interaction changes the next state.

Use a differential, reversed, ratio or null comparison when its physical invariance removes a consequential influence. Derive the cancellation from the arrangement. For example, reversing a known applied force while preserving a common force offset changes the wanted response but leaves the offset shared. A reversal that also changes the offset does not support that subtraction.

For a quantum probe, choose a prepared state, the parameter-dependent interaction and the measurement together. The physical interaction may be described by a channel taking rho to rho_theta; measurement operators E_k give outcome probabilities `P(k|theta)=Tr(rho_theta E_k)`. Here rho is the prepared state, theta the sought parameter, and the positive operators E_k sum to the identity. If those probabilities do not change with theta, that preparation and readout supply no information about it.

A reference can also select which part of a response is read. A phase-sensitive measurement needs a phase reference; a differential displacement needs a reference position. Preserve the conditions that make this reference stable during the comparison.

#### PHY.9:4.4 - Include the effect of measuring on the subject

Construct the coupled subject-probe account for the duration that matters. Determine whether connecting the probe changes the sought quantity, changes only another quantity, or leaves its relevant value effectively unchanged. Use the physical coupling rather than a universal claim that measurement must disturb the target.

If the wanted value precedes coupling, derive how it can be recovered from the disturbed response, or change the arrangement to reduce the consequential disturbance. Keep uncertainty in that recovery. When correction is poorly determined, a different interaction or a conditional range can be more useful than more decimal places.

Compare the retained effect with the allowed error or decision margin. Loading, finite response time and backaction matter through their consequences for this question. PHY.5 helps justify an approximation.

A nondestructive or non-demolition measurement protects a specified property under particular conditions; it does not establish that every later use of the subject is unaffected. Preserve any disturbance that changes the receiving experiment or work.

#### PHY.9:4.5 - Determine the distinctions the readout supports

Compose the physical response with the actual recording procedure through C.16.MR. Use MMP.7 when the conclusion requires a probability law for those records. Retain common influences, saturation, timing and finite resolution when they affect the conclusion.

Ask whether different target values can actually produce the same record under the stated preparation. With bounded errors, two feasible cases can demonstrate ambiguity. If only an outer bound crosses the decision limit, sharpen the calculation before concluding that a new instrument is needed. For random records, consider how likely each observation is under the competing accounts. A local slope describes the response near one setting and can leave a periodic ambiguity or a shared unknown unresolved.

Use the uncertainty or error model appropriate to the inference. Strongly nonlinear conversion can change both an estimate and its uncertainty; do not assume that converting an average is equivalent to averaging the converted quantity. Apply the necessary mathematical propagation or inference method, rather than treating a sensitivity coefficient as a complete answer.

When the order asks for several results from one preparation, determine which observations can be made on that preparation and in what order. Trace any disturbance or shared uncertainty into the later readings. A relation or an earlier record can already determine a value within its conditions. If the order also calls for making the measurement on this preparation, obtain the reading from that preparation and keep the conditions under which it was made. If separate preparations are allowed, establish why each answers its assigned use and, where the answer depends on a relation between them, what connects them. Compare feasible combinations under the available resources through C.16 and C.11.

#### PHY.9:4.6 - Obtain a first result and revise the physical arrangement

Work an admissible preparation through to its predicted readout and interpretation. This can establish possible operation and reveal a missing contribution before an instrument is built. For a reading already received, consider the states compatible with that reading and the other information the recipient has. A decision can be justified when it is acceptable in all those states. For an instrument promised to support decisions over a range, establish a usable rule for every readout possible in that range. Different readouts may call for different decisions. One ambiguous readout can defeat a guarantee while leaving another readout decisive. For an error-probability requirement, use the appropriate record laws and error criterion. Return the supported resolution and its range.

Change a condition that could defeat the intended use. Check the shared premise of a subtraction, the range of an inverse, the time available for a response or the disturbance caused by the probe. Return to the smallest implicated part of the arrangement.

Use available observations where they can change confidence or selection. C.11.DUA helps choose between another measurement, a conditional result and proceeding with uncertainty. A statistical comparison or a calibration certificate does not substitute for a missing physical response.

Return the proposed arrangement, its preparation and readout, the result it supports and the conditions that would change that use. The next work may be implementation, calibration, inference or a different measuring interaction. PHY.10 constructs a physical test when the purpose is to separate rival accounts.

### PHY.9:5 - Archetypal Grounding

#### PHY.9:5.1 - Make mass affect the observation

Two bodies fall in a sufficiently uniform gravitational field with negligible drag. The equation `m a=m g` gives a=g. Timing their fall cannot distinguish their masses in this idealization, even though gravity exerts different forces.

Choose instead a known horizontal applied force F whose generation does not depend on the unknown mass. Track the body's acceleration under that force. With other horizontal forces negligible, `m a=F` gives `m=F/a` for nonzero a. The physical change is from a force proportional to the unknown mass to an independently supplied force.

Now a constant horizontal force offset b matters during the short observation. Use two otherwise identical preparations with applied forces +F and -F. Assume the same b and the same mass in both, and measure their initial accelerations:

`m a_+=F+b`, `m a_-=-F+b`.

Subtracting gives

`m=2F/(a_+-a_-)`.

With F=6 N, a_+=4 m/s² and a_-=-2 m/s², the mass is 2 kg and b=2 N. Using only F/a_+ would give 1.5 kg. The controlled reversal made mass distinguishable from the shared force offset.

The two preparations must preserve that offset. Velocity-dependent drag need not do so after the trajectories diverge. Measuring comparable initial responses, including the changed drag law, or selecting another arrangement can repair that use. Taking more samples of two physically different offsets does not justify the shared-b subtraction.

The acceleration readout and the force reference retain their own calibration and uncertainty. A decision whose margin exceeds those effects can use the mass estimate; a tighter use returns to the consequential contribution.

#### PHY.9:5.2 - Separate pressure from the probe's surface force

A large liquid reservoir maintains an unknown gauge pressure p during a small probe's readout. A vertical circular capillary opens to the atmosphere. Let rho be liquid density, g gravitational acceleration, r the tube radius and h the meniscus height above the pressure reference. Assume hydrostatic equilibrium and a capillary regime in which the meniscus curvature is described by the wetting angle theta.

Hydrostatic pressure and the surface-pressure jump give

`p=rho g h - s/r`, where `s=2 gamma cos(theta)`

and gamma is surface tension. The height responds to the wanted pressure and to the capillary surface force.

If s is unknown but the same surface condition can be prepared in two narrow tubes of radii r_1 and r_2, use

`rho g h_1=p+s/r_1`, `rho g h_2=p+s/r_2`.

For distinct radii,

`p=rho g (r_1 h_1-r_2 h_2)/(r_1-r_2)`.

Take rho g=10000 Pa/m, r_1=0.1 mm, r_2=0.2 mm, h_1=0.20 m and h_2=0.15 m. The inferred pressure is 1000 Pa and s=0.10 N/m. Interpreting the first height as p=rho g h_1 would give 2000 Pa. Both narrow radii must remain within the chosen capillary approximation.

Now suppose the two surfaces have different, unknown wetting conditions. The equations contain separate s_1 and s_2. The cancellation no longer determines p: two readings with three unknown quantities leave a consequential freedom. Restore the common surface condition, use useful bounds on the surface terms, or select another pressure-sensitive interaction.

The reservoir premise also matters. If filling the capillary changes the pressure whose earlier value was wanted, include the reservoir-probe volume and pressure relation through PHY.6 and C.16.MR. The maintained-pressure calculation cannot by itself recover that earlier value.

#### PHY.9:5.3 - Prepare a probe whose phase difference can be read

An ideal two-level probe couples to a constant classical field B through

`H=(hbar gamma B/2) sigma_z`,

where gamma is a known coupling coefficient and sigma_z has eigenvalues +1 and -1 for states |0> and |1>. Treat the field as unchanged by this probe during the interrogation time t. The wanted quantity is B within a supplied range.

Prepare |0>. Evolution multiplies it by a global phase; measurements of this state cannot reveal that phase. Increasing t alone does not create a readable field dependence.

Instead prepare `|+>=(|0>+|1>)/sqrt(2)`. Evolution produces a relative phase `phi=gamma B t`. Reading sigma_z still gives equal probabilities and is uninformative about phi. A controlled rotation before detection permits a sigma_x or sigma_y measurement. The model predicts means cos(phi) and sin(phi). Together their exact values determine phase modulo 2 pi. Repeated preparations give a finite series of outcomes for each readout from which those means can be estimated.

For gamma=1 rad/(s·field-unit), t=1 s and B=pi/3 field-units, the ideal means are 1/2 and sqrt(3)/2. They select phi=pi/3 modulo 2 pi. On the supplied range `-pi < gamma B t <= pi` those ideal responses identify a unique field. A finite run can give the same outcome sequence at nearby field values in that range. For a conclusion about the measured field, infer the supported precision or uncertainty from the outcomes and their sampling law.

If the field may instead lie between -4 pi and 4 pi field-units, several fields give exactly the same pair of ideal means, however often the readout is repeated at this time. Shorten the initial interrogation, for example to t=0.1 s with the same gamma: the whole supplied range then lies inside the unambiguous phase interval. A later longer interrogation can refine a value once the remaining range supports its interpretation.

Coherence loss, imperfect rotations or an uncertain gamma change the response law. They can be included or constrained where the required estimate needs them.

### PHY.9:6 - Bias-Annotation

The examples use controllable idealized arrangements to expose the construction. A field situation may limit access, preparation, reversibility or repeated sampling. Use those limits in choosing the interaction rather than treating the ideal case as an available apparatus.

Quantum sensing is one implementation of a wider physical move. Classical comparisons, chemical response and mechanical probes can serve the same construction when their physical relations and receiving use fit.

### PHY.9:7 - Conformance Checklist

- The target distinction includes the physical conditions under which it is sought.
- The proposed interaction makes that distinction affect the selected readout.
- Preparation, reference and comparison operations are physically interpretable.
- A cancellation or transferred calibration retains its shared physical premises.
- Disturbance and finite response are included when they change the wanted result.
- Local sensitivity is not substituted for resolution over the required range.
- The result states what the available observations and physical premises resolve, what remains ambiguous and when to revise the arrangement. If several observations must be made on the same preparation, their timing and disturbance allow the required combination.

### PHY.9:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| The quantity appears, so it is measured | Mass cancels from ideal falling acceleration. | Derive the complete response and choose a coupling that retains the wanted dependence. |
| Responsive interaction, insensitive readout | A relative phase changes while a population measurement stays constant. | Choose preparation and readout together with the interaction. |
| Common offset by notation | Two preparations use one symbol for physically different influences. | Establish the shared condition or retain separate contributions. |
| More readings resolve every ambiguity | Repetition improves a statistic without separating compatible target values. | Change the interaction or use the sufficient compatible range. |
| Correction without the coupled arrangement | Probe loading is removed by a formula from another physical setup. | Derive the effect for the actual target and probe conditions. |
| Maximum local slope means best measurement | A periodic response leaves widely separated possibilities indistinguishable. | Compare the required range, resources and attainable distinctions. |

### PHY.9:9 - Consequences

The measurement can be improved by changing how information is physically produced. Better inference remains useful, but its contribution is tied to an interpretable preparation and response.

Different contributors can construct the coupling, calculate the response, prepare the reference and infer the result without losing the common physical question. When an existing arrangement suffices, the method ends with its use.

### PHY.9:10 - Architectural Rationale

The measurement relation and the measuring interaction solve connected difficulties. A relation can be derived for a fixed setup that is incapable of resolving the wanted difference. Constructing a different coupling, preparation or reference changes what the relation can supply.

This physical construction links theory to observation and intervention. It also links physical computing to readout: a physical state can carry a computed result that the chosen observation does not distinguish. Use the interaction and its conditions as inputs to the mathematical or statistical interpretation.

### PHY.9:11 - SoTA-Echoing

The [VIM definitions of measurement principle](https://jcgm.bipm.org/vim/en/2.4.html) and [measurand](https://jcgm.bipm.org/vim/en/2.3.html) distinguish the phenomenon supporting a measurement from the quantity sought under specified conditions. [JCGM GUM-6:2020](https://www.bipm.org/documents/20126/2071204/JCGM_GUM_6_2020.pdf/d4e77d99-3870-0908-ff37-c1b6a230a337?download=true&t=1775224426559&version=1.15), especially sections 7.2 and 9, explains theoretical, empirical and hybrid response models and effects of realizing a measurement.

Compare the two mass procedures in :5.1. Timing ideal free fall is simpler but supplies no mass distinction. A known-force comparison supplies it at the cost of a force reference and acceleration readout. Reversal adds another preparation only when separating the force offset matters. Neither a more accurate clock nor more identical falls supplies the missing physical dependence.

[Degen, Reinhard and Cappellaro, *Quantum Sensing*](https://arxiv.org/abs/1611.02427), Reviews of Modern Physics 89 (2017), is a foundational synthesis of preparation, coupling, control and readout. [Pezzè and Smerzi, *Advances in multiparameter quantum sensing and metrology*](https://arxiv.org/abs/2502.17396), 2025, extends the selection question to several parameters, incompatible optimal measurements and finite resources. The adopted contribution is the joint choice of probe, encoding and readout; a quantum sensitivity bound needs its own estimation and attainability assumptions.

For the phase question in :5.3, the same Hamiltonian with an eigenstate probe gives no observable phase, while a superposition and suitable readout do. Short interrogation resolves the wider range; longer interrogation can improve local sensitivity while requiring range information and adequate coherence. More complex entangled or adaptive arrangements require a comparison under the resource and uncertainty conditions of the intended measurement.

The [2026 amendment to JCGM 100](https://doi.org/10.59161/PPDI3267) explicitly addresses significant nonlinearity in both a measurement estimate and its uncertainty. It supports returning from a local sensitivity approximation when the receiving calculation depends on curvature. The applicable mathematical inference remains separate from construction of the physical coupling.

The numerical cases are constructed demonstrations under stated laws and idealizations. A changed material, interaction, preparation or readout range reopens the corresponding physical premise.

### PHY.9:12 - Relations

- **C.16.MR:** constructs and composes the relation from the sought property and measuring arrangement to an indication.
- **C.16.IR:** determines which target distinctions a supplied indication or response relation can resolve.
- **PHY.4, PHY.6 and PHY.7:** constrain a physical law or construct the evolution needed to derive a response.
- **PHY.5:** determines whether an interaction, disturbance or response time can be neglected for the intended consequence.
- **PHY.8 and MMP.7:** construct physical statistics and the probability law of recorded outcomes when variation and recording affect the result.
- **PHY.10:** uses a measuring interaction in a physical test separating rival accounts.
- **C.29.2** formulates the needed computation; **B.5.MPC** connects what it produces with the mathematical claim and the physical question.
- **C.16 and C.11:** characterize attainable performance and resource combinations, then choose among available arrangements.
- **C.11.DUA:** selects further measurement or inquiry by what it can change and the effort it requires.

### PHY.9:End
