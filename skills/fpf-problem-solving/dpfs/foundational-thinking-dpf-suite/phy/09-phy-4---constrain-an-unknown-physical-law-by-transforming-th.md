## PHY.4 - Constrain an Unknown Physical Law by Transforming the Situation

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### PHY.4:1 - Problem frame

Use this pattern when an observed or proposed physical effect needs an account, but the interaction law is not supplied. A detailed mechanism may be unresolved and a familiar analogue may be inadequate. You can still ask how the situation could be changed, what would remain physically equivalent, and which responses those comparisons allow.

Start with one physical response or relation needed by the work. Describe its participants, preparation and relevant surroundings. Construct one comparison that could rule out a proposed dependence or restrict its form. A conditional restriction, together with the dependence it leaves unresolved, is a useful first result.

The method uses transformations justified for the physical situation: changes of position, orientation, scale, preparation, participant assignment or other relevant conditions. It combines their consequences with applicable dimensions, balances and dissipation. The question selects which of these contributions is useful.

You need enough physical understanding to propose the comparison and explain its conditions. Obtain an unfamiliar physical premise from a suitable account or collaborator. A qualitative comparison can already change the next move. The vector example additionally uses rotations and dot products; the chamber example uses elementary algebra and particle balance. Their branch-specific preparation belongs to those examples.

If an established interaction law already answers the question under the intended conditions, apply it. PHY.1 develops physical similarity across changed conditions, PHY.2 constructs a physical analogue, and PHY.3 derives a performance limit from permitted transformations. Return here when the unresolved contribution is the form of the interaction law itself.

### PHY.4:2 - Problem

A formula can be easy to calculate with while admitting a physically impossible direction, an unjustified dependence or an omitted influence. Choosing the formula first can hide those differences.

Conversely, an appeal to symmetry or conservation can appear to determine a law while leaving important functions or parameters free. The task is to obtain the restriction that follows from the physical comparison and carry its remaining freedom into the next construction or inquiry.

### PHY.4:3 - Forces

| Force | Tension |
| --- | --- |
| Unknown mechanism and usable physical grounds | Partial knowledge can constrain the law, while a premise about an omitted influence can invalidate the constraint. |
| Changed description and changed experiment | Coordinates can change without changing the situation; changing the apparatus alone can alter its relation to the surroundings. |
| Strong restriction and remaining freedom | A direction, sign or balance can be established while the magnitude law remains unknown. |
| Idealized comparison and intended use | A conditional law family can guide work before all its physical premises have been resolved for an application. |

### PHY.4:4 - Solution

**Local mantra:** recover the physical situation; construct its transformations; justify the comparison; restrict the relation; retain its unknown part; use the consequence or revise the premise.

#### PHY.4:4.1 - Recover the participants and the relation being sought

Name what interacts, what is prepared, what can be exchanged and what response matters. Include surrounding bodies, material state, fields or boundaries when they can change that response. An omitted orientation or stored state may matter more than an additional numerical parameter.

Choose candidate quantities from that physical account. Explain how each quantity describes a participant, preparation or interaction. A.3.3.TR supports constructing a state that distinguishes different possible continuations; here the physical account supplies what retains and changes that state.

Decide what kind of relation is being proposed. An instantaneous mean response `y=F(x)` assumes that the chosen current inputs determine that mean. Memory, unresolved states or several possible responses can require a history, additional state, a probability law or a relation admitting several outputs. MMP.10 and MMP.11 express those mathematical choices after the physical conditions are identified.

Retain the status of the premises. A studied physical law, an idealization and a proposed hypothesis can all support reasoning, with different conditions on its use. Use the resulting conditional consequence when it already answers the present question.

#### PHY.4:4.2 - Construct the transformation of the situation

Describe what happens to every relevant participant and condition under the proposed change. If an apparatus is rotated, what happens to gravity, nearby surfaces, an applied field and its preparation? If two participants are exchanged, which material properties and connections move with them?

Separate two comparisons:

- **Changed coordinates:** the same physical situation is expressed with different components or labels. Transform every quantity representing that situation consistently.
- **Changed physical situation:** participants or conditions are changed. Explain which physical premise predicts corresponding behavior in the new situation.

For an isotropic material, all spatial directions are physically equivalent under the stated conditions. An oriented material can also be described in rotated coordinates; its material direction must then rotate in the description. These are different premises for restricting a response.

Select the actual transformation class. A justified rotation condition supplies rotation consequences. Reflection, time reversal, scaling or exchange requires its own physical grounds when used. PHY.1 supplies the detailed work for a scaling comparison.

A thought comparison can be enough. When a physical premise is unsettled, identify a rival case that could make the responses differ. C.11.DUA helps decide whether resolving that difference is worth the work needed now.

#### PHY.4:4.3 - Turn the comparison into a constraint on the unknown relation

Specify how inputs and responses transform. If x changes by T and y by U, a proposed response function has the comparison condition:

`F(T(x))=U(F(x))`.

For a reversible symmetry of a relation R, the corresponding condition is `R(x,y) iff R(T(x),U(y))`. This permits constraining an account before choosing a direction in which to solve it.

Derive the restriction. One useful move is to hold the input fixed under some allowed transformations. The output must then remain fixed under its corresponding transformations. Another is to compare inputs related by a transformation: a value chosen at one constrains the value at the other. MATH.13 develops these mathematical consequences once the physical action has been supplied.

For example, in three-dimensional space, rotations about a nonzero vector w leave w fixed. A vector response determined only by w and unchanged physical conditions must therefore lie along w: any perpendicular component would turn. Rotations between equal-length velocities then make the scalar coefficient depend only on their length. The physical work is establishing that no additional direction or state must also be supplied; :5.1 makes those assumptions explicit.

If a proposed input was held fixed even though the physical transformation changes it, restore that input and repeat the derivation. The anisotropic case in :5.2 shows how the changed argument opens additional response directions.

#### PHY.4:4.4 - Combine applicable dimensions, balances and dissipation

Use the physical restrictions relevant to the requested consequence:

- **Dimensions:** terms added together as one physical quantity need compatible units. Determine the dimensions of remaining coefficients and arguments. PHY.1 supplies dimensionless similarity groups when scale is part of the question.
- **Balance:** account for the relevant quantity retained, transferred, supplied or lost across the chosen boundary. A flux entering and leaving a region can differ when the region stores the quantity.
- **Dissipation or passivity:** identify the exchange whose sign is constrained and the regime in which the constraint holds. For an instantaneous passive resistive force at relative velocity w, the mechanical power condition is `F(w) dot w <= 0`.

Derive each condition at its stated scope. A storage element can temporarily return energy that it received earlier; its instantaneous power need not satisfy the memoryless resistance condition. Including storage changes the applicable balance and inequality.

Combine the constraints and examine whether any candidate remains. If they conflict, return to the assumptions or allowed class that caused the conflict. If they leave several laws, express the unresolved function, parameter or state dependence. Symmetry and dimensions often narrow a family without selecting one member.

#### PHY.4:4.5 - Obtain the needed consequence and choose the next use

Use the constraint for the original question. It may reject an impossible response direction, locate a missing input, restrict a learned or symbolic model, bound a consequence, or identify a condition under which competing laws disagree.

MMP.11 supplies a mathematical family respecting the physical constraints. When a quantitative value is needed, an interaction theory, interpreted observations or another appropriate method can constrain its remaining freedom. C.16.IR handles inference from interpreted indications; MMP.7 formulates a probability law for recorded data when the inference uses that form. C.29.2 supplies a computational formulation.

Choose further work from the unresolved consequence. A direction or family-wide bound may already suffice. If a missing magnitude changes the decision, obtain the needed contribution at a useful range and precision. A proposed experiment or simulation should discriminate something that matters to that next move.

When a changed situation gives a response outside the family, inspect the physical comparison before adding arbitrary terms. A preferred direction, external drive, stored state or different regime can change the family itself. Retain earlier consequences where their premises still hold.

### PHY.4:5 - Archetypal Grounding

These are constructed physical accounts. They illustrate how physical premises constrain an unknown law and how a changed premise changes the result.

#### PHY.4:5.1 - Restrict an unknown resistive force

Seek the instantaneous mean resistive force on a body moving through a homogeneous isotropic medium at a fixed material state, in a classical three-dimensional regime. Assume the body and preparation introduce no preferred direction, relevant memory is negligible, and relative velocity w is the only varying input. These assumptions define the proposed comparison; their adequacy in a particular experiment remains a physical question.

Rotating the entire relevant situation rotates w and the force together. Because there is no further directional input, `F(Qw)=QF(w)` for every spatial rotation Q. For nonzero w, rotations about w rule out a perpendicular force component. Equal-length velocities are related by rotation, so write:

`F(w)=-a(|w|^2)*w` for w different from zero.

At w=0, rotational symmetry gives `F(0)=0`. The coefficient a is an unknown scalar function at the fixed material conditions. Its dimension is mass divided by time. Memoryless passive resistance gives:

`F(w) dot w=-a(|w|^2)*|w|^2 <= 0`,

so `a(s)>=0` for s>0.

The result determines a direction and sign while leaving the speed dependence unresolved. Both `a(s)=a0` and `a(s)=b0*sqrt(s)` with suitable nonnegative dimensional constants satisfy these restrictions. They predict different force magnitudes when speed changes. The comparison alone therefore provides neither a linear nor a quadratic drag law.

For a direction-only question, use the result directly. To predict stopping time, supply further information about a over the speeds involved, or obtain a sufficient bound over the admissible family. MMP.11 keeps that unresolved relation visible instead of inserting a familiar drag coefficient.

#### PHY.4:5.2 - Add a physical direction

Now the body is oriented or the environment has an aligned surface. Include its unit direction n in the input. Under a rotation of the complete situation, both w and n change, so the condition becomes:

`F(Qw,Qn)=QF(w,n)`.

A rotation fixing w can now change n. The earlier argument that fixed all inputs while rotating a perpendicular output component is no longer available.

For example, one admissible linear resistive family is:

`F(w,n)=-alpha*w-beta*(n dot w)*n`.

For unit n, its power is `-alpha*|w|^2-beta*(n dot w)^2`. Resolving w into parts parallel and perpendicular to n shows passivity for every w when `alpha>=0` and `alpha+beta>=0`. This is a possible family, not an exhaustive determination of the changed law.

With consistent units, take alpha=1, beta=3, `w=(1,1,0)` and `n=(1,0,0)`. The force is `(-4,-1,0)` and power is -5. The force resists motion while pointing in a direction different from -w. This possibility is excluded by the earlier isotropic account and allowed by the additional physical input.

If n is fixed in the laboratory while only the body motion changes, retain that fixed n in the experiment's account. Rotating the coordinate system changes the components of both quantities; it supplies no premise that removes the material or environmental direction.

#### PHY.4:5.3 - Exchange two participants

Two identical chambers at the same temperature exchange one kind of particle through a symmetric passage. Let a and b be their current concentrations and let `J(a,b)` be the instantaneous mean transfer rate from the first chamber to the second. Assume the proposed regime needs no additional passage state, and the surroundings introduce no directional bias.

Keep the chamber labels and the positive counting direction fixed, and exchange the concentrations in the two preparations. Because the chambers and passage are symmetric and the surroundings supply no bias, this physical exchange predicts a reversed measured transfer rate:

`J(b,a)=-J(a,b)`.

At equal concentrations, `J(a,a)=0`. A proposed law `J(a,b)=k*(a-b)^2` with k>0 fails the interchange condition: it gives a positive rate in the same counted direction after the preparations are exchanged.

Both `J(a,b)=k1*(a-b)` and `J(a,b)=k3*(a-b)^3` satisfy the interchange condition when their constants have the corresponding units. Symmetry has not chosen between them or determined their coefficients. Directional thermodynamic claims would additionally use the physical driving potentials and the applicable dissipation law.

If the passage stores no particles, the chamber particle numbers satisfy `dN1/dt=-J` and `dN2/dt=J`, preserving their sum. If appreciable particles accumulate in the passage, include its particle number and separate inlet and outlet rates. The earlier two-chamber balance then omits a relevant participant.

This comparison uses exchange and balance rather than rotation. It opens the same kind of result: an admissible law family and the physical condition that would require revising it.

### PHY.4:6 - Bias-Annotation

A familiar formula can conceal a missing physical premise. An elegant symmetry argument can conceal the same omission. Recover the participants, preparation and surroundings before deciding which transformations the situation admits.

A conditional family is useful when its remaining freedom is stated. Supplying an unexplained familiar coefficient would replace an unresolved physical question with apparent precision. Obtain further information only for the consequence that needs it.

### PHY.4:7 - Conformance Checklist

For the restriction being used:

- The physical response or relation, participants, preparation and relevant surroundings are recoverable.
- The transformation states what changes and what remains physically comparable.
- The mathematical input and output transformations follow that physical account.
- Each dimensional, balance or dissipation constraint has applicable physical premises.
- The derived consequence distinguishes what is constrained from what remains unknown.
- The result changes a construction, interpretation, prediction or next inquiry.
- A changed physical condition returns to the affected premise and constraint.

### PHY.4:8 - Common Anti-Patterns and How to Avoid Them

**Dropping the surroundings from the transformation.** Rotating a body relative to a fixed material direction can change its response. Transform the complete relevant account and distinguish that experiment from a coordinate change.

**Selecting a magnitude law from direction symmetry.** The linear and quadratic resistance possibilities in :5.1 satisfy the same directional restriction. Carry the unknown scalar function until a further physical contribution constrains it.

**Applying an instantaneous dissipation inequality to an energy-storing interaction.** Recover stored energy and the exchange balance. Temporary return of stored energy changes the instantaneous power without establishing an active energy source.

**Using a balance with an omitted participant.** Accumulation in the passage changes the two-chamber balance in :5.3. Include the storage and its exchanges before computing the chamber changes.

### PHY.4:9 - Consequences

Useful physical restrictions become available before a complete mechanism or fitted law is known. They can guide formulation, reject an incompatible model or direct a discriminating inquiry. The remaining freedom also becomes a specific task rather than an implicit assumption.

The result is conditional on the physical comparison. An added direction, stored state or changed regime can reopen the law family. This makes the dependence of the conclusion inspectable and supports retaining the portions that still apply.

### PHY.4:10 - Architectural Rationale

The physical construction precedes the mathematical symmetry calculation. MATH.13 can derive what a supplied transformation preserves; the present method supplies and criticizes the physical grounds for choosing that transformation and its inputs.

The unknown relation remains explicit through the work. This supports relational formulations as well as response functions, and allows later symbolic, numerical or learned models to use the same physical restrictions.

Similarity, analogy and performance bounds remain separately usable methods. Their results may settle the physical question directly. When a law is still missing, this method constrains its form and identifies the remaining contribution without requiring a detailed mechanism first.

### PHY.4:11 - SoTA-Echoing

Feynman's [discussion of symmetry in physical laws](https://www.feynmanlectures.caltech.edu/I_52.html), especially §52-2, is a historical methodological anchor for transforming an experiment together with its relevant surroundings. The adopted contribution is the physical construction of the comparison. The particular transformation and its regime are selected from the physical account being used.

Villar and colleagues' [Scalars are universal](https://arxiv.org/html/2106.06610v4), Proposition 4 and Appendix H, provides a contemporary constructive connection between specified symmetry actions, scalar invariants and equivariant response families. Its distinctions between rotation and reflection groups and between different input quantities matter when selecting a model. The paper's mathematical representation results are used under their hypotheses; the present physical method establishes which input and transformation account is appropriate.

When formulating an unfamiliar interaction law, a common alternative is to select a familiar constitutive formula and fit its coefficients. With only the physical premises in :5.1, that choice would insert a speed dependence the premises do not determine. The transformation method in :4.2-:4.4 first establishes the allowed direction and sign, leaving the scalar function open. For a direction-only question, this supplies the needed answer without obtaining a detailed law or fitting its coefficients. For a stopping-time prediction, :4.5 requires further information about that function or a sufficient bound; the restriction alone leaves the prediction unresolved.

An established constitutive account or reliable analogue is preferable when it applies to the intended regime and supplies the needed consequence with less work. The present method then helps inspect its physical assumptions or a proposed change of conditions. Reopen this choice when a new physical input or regime invalidates the comparison, an improved account changes its grounds or offers an easier answer, or the receiving question requires information that the constrained family leaves open.

### PHY.4:12 - Relations

- **PHY.1** constructs physical similarity and scale-dependent comparisons.
- **PHY.2** constructs a physical analogue or proposed mechanism from interactions.
- **PHY.3** derives a physical performance limit from the permitted transformations.
- **MATH.13** derives mathematical consequences of a supplied symmetry.
- **MMP.10 and MMP.11** formulate compatible conditions and relations with unresolved dependence.
- **A.3.3.TR** supplies common state and joint-change construction.
- **C.29.1, C.29.2 and C.29.3** connect correspondence, computational formulation and physical realization.
- **C.16.IR and MMP.7** support interpreted indications and the probability law used for recorded observations.
- **C.11.DUA** compares the value and effort of resolving a remaining physical question.

### PHY.4:End
