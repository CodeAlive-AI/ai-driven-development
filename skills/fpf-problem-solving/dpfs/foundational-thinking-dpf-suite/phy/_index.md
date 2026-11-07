# Physical Thinking DPF

**DocID:** `PHY` within **FPF Library**.

> A pattern language for forming physical accounts, deriving usable consequences, constructing observations and revising the physical assumptions.

- **Author:** Anatoly Levenchuk, with AI-assisted development and review
- **Version:** 24 October 2026
- **Status:** Eternal alpha: a usable repertoire that remains open to correction and extension.
- **License:** © 2026 Anatoly Levenchuk. Original framework text: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Cited sources retain their own terms.
- **Publication:** [FPF Library repository](https://github.com/ailev/FPF)

Begin with the physical question in your work. Use the Table of Contents to find a relevant method, then open its Problem frame, Solution, worked cases and checklist. The Readme follows worked connections between methods; the Architectural Reference explains how the methods connect, which knowledge they require and how to revise a physical account.

The reference code **PHY** names this DPF. Its numbers are stable pattern addresses; § shows position within a Part. The methods can be used separately or in longer routes with mathematical and computational contributions.

This publication belongs to the [Foundational Thinking DPF Suite](../_index.md). Its [Reference (Foundational)](../suite-reference/_index.md) explains those connections and the available publications. References such as B.5.MPC and C.29 name patterns in [FPF Core](../../../sections/03-first-principles-framework-readme/_index.md). Open the cited body when its contribution is needed; revisit a receiving conclusion when that contribution changes.

To cite this edition: Anatoly Levenchuk, *Physical Thinking DPF*, [FPF Library repository](https://github.com/ailev/FPF). Include the version date shown above.

# Table of Contents

## Public units

| Unit | Title | Use |
| --- | --- | --- |
| Readme | [Physical Thinking - Readme](_index.md#physical-thinking---readme) | Follow worked connections between physical methods. |
| Architectural Reference | [Physical Thinking DPF Architectural Reference](_index.md#physical-thinking-dpf-architectural-reference) | Understand the connected methods, their rationale, sources and limits. |
| PHY.Reference:1 | [Problem frame - Construct a physical account you can use and change](01-phy-reference-1---problem-frame---construct-a-physical-accou.md) |  |
| PHY.Reference:2 | [Problem and forces - Keep the physical question through the calculation](02-phy-reference-2---problem-and-forces---keep-the-physical-que.md) |  |
| PHY.Reference:3 | [Solution - Connect physical methods through their results](03-phy-reference-3---solution---connect-physical-methods-throug.md) |  |
| PHY.Reference:3.1 | [Construct and constrain the account](03-phy-reference-3---solution---connect-physical-methods-throug.md#phyreference31---construct-and-constrain-the-account) |  |
| PHY.Reference:3.2 | [Compare, observe and construct another use](03-phy-reference-3---solution---connect-physical-methods-throug.md#phyreference32---compare-observe-and-construct-another-use) |  |
| PHY.Reference:3.3 | [Constituent actions in ongoing work](03-phy-reference-3---solution---connect-physical-methods-throug.md#phyreference33---constituent-actions-in-ongoing-work) |  |
| PHY.Reference:4 | [Worked connection - From an unknown resistance to a useful comparison](04-phy-reference-4---worked-connection---from-an-unknown-resist.md) |  |
| PHY.Reference:5 | [Bias, use checks and recurring failures](05-phy-reference-5---bias-use-checks-and-recurring-failures.md) |  |
| PHY.Reference:6 | [Consequences and Architectural Rationale](06-phy-reference-6---consequences-and-architectural-rationale.md) |  |
| PHY.Reference:7 | [Shared sources, alternatives and relations](07-phy-reference-7---shared-sources-alternatives-and-relations.md) |  |

## Part A - Construct and constrain a physical account

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [PHY.4 - Constrain an Unknown Physical Law by Transforming the Situation](09-phy-4---constrain-an-unknown-physical-law-by-transforming-th.md) | Stable | unknown law; symmetry; physical transformation; dimensions; balance; dissipation. What can be concluded before a full response law is known? | MATH.13 for a symmetry consequence; MMP.11 for an unknown response family. |
| 2 | [PHY.5 - Choose an Effective Physical Description by Scales and Couplings](10-phy-5---choose-an-effective-physical-description-by-scales-a.md) | Stable | scale separation; coupling; memory; fluctuation; transient; effective description. Which physical effects can be omitted for the consequence and duration of interest? | MMP.9 for mathematical elimination; PHY.6/.8 when evolution or collective preparation matters. |
| 3 | [PHY.6 - Construct Physical Evolution from Balances and Response Laws](11-phy-6---construct-physical-evolution-from-balances-and-respo.md) | Stable | participants; exchange; balance; constitutive response; preparation; boundary condition. Which physical laws and conditions close the proposed evolution? | C.29.BB for balances; MMP.10 for coupled equations; C.29.2 for computational formulation. |
| 4 | [PHY.7 - Obtain Motion from a Physical Variational Principle](12-phy-7---obtain-motion-from-a-physical-variational-principle.md) | Stable | physical action; admissible history; constraints; boundary freedom; variation. What physical grounds permit a variational construction, and what motion follows? | MATH.10 for mathematical variation; PHY.6 for the direct balance alternative. |
| 5 | [PHY.8 - Infer Macroscopic Physical Behavior from Microscopic Alternatives](13-phy-8---infer-macroscopic-physical-behavior-from-microscopic.md) | Stable | microstates; preparation; ensemble; correlation; fluctuation; relaxation. Which physical distribution and dynamics support a collective prediction? | MMP.7 for probability composition; MMP.9 for reduction; PHY.6 for the required physical evolution. |

## Part B - Compare, observe and act

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [PHY.1 - Construct Physical Similarity Across Changed Conditions](14-phy-1---construct-physical-similarity-across-changed-conditi.md) | Stable | scaling; similarity; dimensionless groups; prototype; changed regime. When does a physical result transfer to a different size, material or condition? | PHY.5 for consequential omitted effects; mathematical methods for the resulting comparison. |
| 2 | [PHY.2 - Construct a Physical Analogue from Interactions](15-phy-2---construct-a-physical-analogue-from-interactions.md) | Stable | physical analogue; mechanism; interaction; preparation; readout. How can another physical arrangement supply a wanted consequence? | PHY.5/.6 for physical description and evolution; PHY.9/.10 for observation and comparison; C.29.3 for computing realization. |
| 3 | [PHY.9 - Construct a Measuring Interaction for a Physical Distinction](16-phy-9---construct-a-measuring-interaction-for-a-physical-dis.md) | Stable | measuring interaction; transduction; reference; calibration; disturbance; ambiguity. How can the needed property be made to affect an observable indication? | C.16.MR for the measurement relation; C.16.IR for inference from indications; PHY.10 for competing physical accounts. |
| 4 | [PHY.10 - Construct a Physical Test That Separates Rival Accounts](17-phy-10---construct-a-physical-test-that-separates-rival-acco.md) | Stable | rival accounts; physical contrast; preparation; apparatus; parameter freedom; noise. Which feasible comparison separates the consequences that matter? | PHY.9 for a needed readout; PHY.6 for evolution; B.5.TC for theoretical comparison. |
| 5 | [PHY.3 - Derive a Physical Limit from Permitted Transformations](18-phy-3---derive-a-physical-limit-from-permitted-transformatio.md) | Stable | physical limit; impossibility; reversible reference; complete exchanges; changed premise. What can a proposed transformation achieve under the physical laws and resources supplied? | C.29.BB for balances; MATH.11/.20 for invariants or bounds; PHY.2 for another physical construction. |

# Physical Thinking - Readme

## Practical entries

Bring the physical question from your work. A useful answer may need a physical account, a consequence derived from it, and an observation that distinguishes what remains unresolved. The worked connections below show how one method's result becomes another's input, where an existing result lets you enter, and which changed condition sends you back.

Use the Table of Contents and each pattern's title and Problem frame for other questions or direct help. The bodies explain their methods, prerequisites, examples and return conditions. The physical theory and mathematics stated for a case belong to that application, not to every method.

You can ask an assisting agent: “Explain this and give me your comments in the language of my work, without framework jargon.” Ask it to show what the quantities and operations mean, where the physical premises enter, and what the result lets you do next.

### PH-PREDICT-AND-DISTINGUISH - Develop a physical prediction and the test it needs

- **Situation:** Several physical accounts fit what is known but imply different consequences for the work.
- **Question:** How can we construct the consequences and resolve only the difference that matters?
- **First useful result or blocker:** A conditional prediction that answers the working question, or a consequential difference and a feasible comparison that could resolve it.
- **Start with:** [PHY.4](09-phy-4---constrain-an-unknown-physical-law-by-transforming-th.md) when the law is unknown; [PHY.6](11-phy-6---construct-physical-evolution-from-balances-and-respo.md) consumes a supplied response to construct evolution; [PHY.10](17-phy-10---construct-a-physical-test-that-separates-rival-acco.md) is needed when rival consequences remain worth distinguishing.
- **Stop or return:** Stop at a sufficient consequence. Return to the affected law, preparation or observation when its premise changes.

#### From an unknown resistance to a useful comparison

**1. Carry the remaining freedom into candidate laws.** The work needs the distance a body travels while slowing from 1 m/s to 0.5 m/s through a medium. Stipulate an effective inertia of 1 kg, no other force along the motion, and an instantaneous resistance at fixed material conditions. PHY.4 uses an isotropic comparison and a passive response to constrain the resistance's direction. Those conditions leave its speed dependence unresolved. A force magnitude of 1 N at 1 m/s admits both `D=b*v`, with b=1 N·s/m, and `D=c*v²`, with c=1 N·s²/m². These are two candidate laws, not all possibilities allowed by that information.

**2. Consume each law in the requested prediction.** PHY.6 combines resistance with `m*dv/dt=-D(v)` and `dx/dt=v`. MMP.10 formulates those relations with the preparation; C.29.2 obtains the requested consequence. Eliminating time gives `dx/dv=-m*v/D(v)`. Over the stated speed interval, the linear law gives a distance of 0.5 m, while the quadratic law gives `ln(2)` m, about 0.693 m. With only 0.6 m available, the two accounts give different answers. With more than 0.7 m available, both satisfy this requirement under their premises, so this difference alone supplies no reason for another test.

**3. Make a consequential difference observable.** If the 0.6 m question still matters, PHY.10 consumes the two response laws to select a comparison at maintained speed 0.5 m/s. They predict 0.5 N and 0.25 N. A supplied calibrated force arrangement with indication error bounded by 0.02 N gives non-overlapping ranges [0.48,0.52] N and [0.23,0.27] N. An indication of 0.25 N would be compatible with the quadratic candidate and incompatible with the linear candidate under these conditions. If the required readout is unavailable, [PHY.9](16-phy-9---construct-a-measuring-interaction-for-a-physical-dis.md) takes the predicted force difference as the distinction its measuring interaction must expose; the distance result remains conditional meanwhile.

**4. Check the physical transfer, then reopen only what changed.** The maintained-speed comparison informs coasting only if the instantaneous-response and material premises cover both preparations. [PHY.5](10-phy-5---choose-an-effective-physical-description-by-scales-a.md) examines a consequential wake or relaxation time if that transfer is doubtful; memory can require another state in the evolution rather than a changed coefficient. If the medium's material condition changes between force comparisons, recover its effect before treating the later indication as a test of the original candidates. Their conditional integrals remain correct; their applicability to the changed run has reopened. Neither result establishes behavior at zero speed or in a new physical regime.

[PHY.Reference:4](04-phy-reference-4---worked-connection---from-an-unknown-resist.md) gives the connected account and division of physical, mathematical and computational work. The same dependence can arise in an unfamiliar transient, a collective response or a physical analogue. The physical laws and observable change with the situation; the contributions still have to support one interpreted answer.

### PH-COLLECTIVE - Choose a collective description for the time that matters

- **Situation:** A simpler collective law may answer a late-time question while losing a response needed soon after preparation.
- **Question:** Which microscopic behavior survives into the requested observable, and does the proposed reduction retain it accurately enough?
- **First useful result or blocker:** A collective prediction with an adequate error for the requested time, or the state or preparation that must remain.
- **Start with:** [PHY.8](13-phy-8---infer-macroscopic-physical-behavior-from-microscopic.md) for the microscopic alternatives and preparation; PHY.6 connects their transport and transitions into evolution; PHY.5 chooses which physical response a reduced account may omit.
- **Stop or return:** Use a sufficient conditional prediction. A changed time, observable or preparation returns to the part of the account that supplied it.

#### From persistent motion to a justified diffusion calculation

**1. Keep the preparation with the microscopic law.** In [PHY.8:5.3](13-phy-8---infer-macroscopic-physical-behavior-from-microscopic.md#phy853---derive-transport-from-persistent-microscopic-motion), particles start at the origin on an unbounded line, with either direction equally likely. Each moves at speed v>0 and reverses direction at independent Poisson events of rate alpha>0. These are supplied physical premises; a fitted position histogram would not establish the reversal mechanism or its time scale.

**2. Turn those premises into the collective evolution.** PHY.6 balances transport and transitions between the two directions. With n the total position-probability density and j its current, the resulting relations are

`partial_t n = -partial_x j`,

`partial_t j = -v²*partial_x n - 2*alpha*j`.

The ideal point preparation leaves probability atoms at x=±v\*t for particles that have not yet reversed; these density equations are understood in the distributional sense. PHY.8 connects their solution to the observable needed here: mean-square displacement at a specified time. The current carries directional persistence even though the mean position stays zero.

**3. Decide whether the faster response can be omitted.** PHY.5 compares the observation time with the current's relaxation time `1/(2*alpha)` and checks the spatial variation. When the reduction is justified, [MMP.9](../mmp/23-mmp-9---derive-a-reduced-mathematical-model-of-state-evoluti.md) supplies the mathematical reduction: replace the relaxed current by `j approximately -D*partial_x n`, with `D=v²/(2*alpha)`, to obtain a diffusion equation. The question still decides whether its consequence is accurate enough.

For v=2 cm/s and alpha=1/s, PHY.8's full account gives

`E[x(t)²] = (v²/alpha)*(t-(1-exp(-2*alpha*t))/(2*alpha))`,

while diffusion gives `2*D*t`. At 20 s these are about 78 and 80 cm². The relative overestimate is about 2.56%, so a 3% allowance for this observable permits the reduced result under the supplied premises. This is a comparison with the microscopic model, not an experimental validation of it.

**4. Return through the consequence that changed.** Ask instead for the spread at 0.1 s. The full result is about 0.03746 cm²; diffusion gives 0.4 cm². Restore the current response for this early question. A finer computation of the same diffusion equation cannot recover what its reduction removed. A question about arrival at a boundary would need the corresponding boundary conditions and its own comparison; agreement on mean-square displacement does not supply that answer.

A simulation used to obtain these timed predictions must implement the stated reversals and their physical time. An artificial sampler that reproduces a position distribution supplies a different result. If the conditional prediction already serves the work, no new measurement is mandatory; if the physical mechanism or preparation is the consequential uncertainty, that becomes the next physical question.

### PH-LIMIT - Use a physical bound before designing a mechanism

- **Situation:** A proposed cyclic device promises 60 J of work from 100 J of heat taken from a 600 K reservoir, rejecting heat only to a 300 K reservoir.
- **Question:** Can a different mechanism achieve this with the same resources and restoration conditions?
- **First useful result or blocker:** The stated second-law comparison bounds net work by 50 J, excluding the 60 J proposal within these conditions.
- **Start with:** [PHY.3:5.1](18-phy-3---derive-a-physical-limit-from-permitted-transformatio.md#phy351---bound-a-proposed-engine-without-designing-its-mechanism), which constructs the comparison from complete exchanges.
- **Stop or return:** Use the exclusion without designing every possible engine. Reopen the exchange account if an extra resource or a different end condition is allowed.

The reservoirs have fixed absolute thermodynamic temperatures, the device returns to its initial state, and no other resource is consumed. Under the supplied classical second-law account, `W <= (1-300/600)*100 J = 50 J`. Energy balance alone would allow the proposed 60 J and therefore would not settle the question. The bound restricts net work; it neither supplies an attaining design nor its power or cost. External work, a nonthermal resource or an unrestored auxiliary changes the account to be compared, not the arithmetic of the original bound.

---

## Files of this publication

Generated by the skill's splitter: one file per section, in reading order.


### Physical Thinking DPF Architectural Reference

- [PHY.Reference:1 - Problem frame - Construct a physical account you can use and change](01-phy-reference-1---problem-frame---construct-a-physical-accou.md) (12 lines)
- [PHY.Reference:2 - Problem and forces - Keep the physical question through the calculation](02-phy-reference-2---problem-and-forces---keep-the-physical-que.md) (17 lines)
- [PHY.Reference:3 - Solution - Connect physical methods through their results](03-phy-reference-3---solution---connect-physical-methods-throug.md) (34 lines)
- [PHY.Reference:4 - Worked connection - From an unknown resistance to a useful comparison](04-phy-reference-4---worked-connection---from-an-unknown-resist.md) (22 lines)
- [PHY.Reference:5 - Bias, use checks and recurring failures](05-phy-reference-5---bias-use-checks-and-recurring-failures.md) (18 lines)
- [PHY.Reference:6 - Consequences and Architectural Rationale](06-phy-reference-6---consequences-and-architectural-rationale.md) (12 lines)
- [PHY.Reference:7 - Shared sources, alternatives and relations](07-phy-reference-7---shared-sources-alternatives-and-relations.md) (16 lines)
- [PHY.Reference:End](08-phy-reference-end.md) (2 lines)

### Part A - Construct and constrain a physical account

- [PHY.4 - Constrain an Unknown Physical Law by Transforming the Situation](09-phy-4---constrain-an-unknown-physical-law-by-transforming-th.md) (220 lines)
- [PHY.5 - Choose an Effective Physical Description by Scales and Couplings](10-phy-5---choose-an-effective-physical-description-by-scales-a.md) (242 lines)
- [PHY.6 - Construct Physical Evolution from Balances and Response Laws](11-phy-6---construct-physical-evolution-from-balances-and-respo.md) (252 lines)
- [PHY.7 - Obtain Motion from a Physical Variational Principle](12-phy-7---obtain-motion-from-a-physical-variational-principle.md) (238 lines)
- [PHY.8 - Infer Macroscopic Physical Behavior from Microscopic Alternatives](13-phy-8---infer-macroscopic-physical-behavior-from-microscopic.md) (263 lines)

### Part B - Compare, observe and act

- [PHY.1 - Construct Physical Similarity Across Changed Conditions](14-phy-1---construct-physical-similarity-across-changed-conditi.md) (239 lines)
- [PHY.2 - Construct a Physical Analogue from Interactions](15-phy-2---construct-a-physical-analogue-from-interactions.md) (234 lines)
- [PHY.9 - Construct a Measuring Interaction for a Physical Distinction](16-phy-9---construct-a-measuring-interaction-for-a-physical-dis.md) (230 lines)
- [PHY.10 - Construct a Physical Test That Separates Rival Accounts](17-phy-10---construct-a-physical-test-that-separates-rival-acco.md) (229 lines)
- [PHY.3 - Derive a Physical Limit from Permitted Transformations](18-phy-3---derive-a-physical-limit-from-permitted-transformatio.md) (210 lines)
