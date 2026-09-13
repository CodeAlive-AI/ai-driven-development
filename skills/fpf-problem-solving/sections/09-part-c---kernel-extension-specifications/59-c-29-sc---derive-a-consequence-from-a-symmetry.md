## C.29.SC - Derive a Consequence from a Symmetry

> **Type:** Method
> **Status:** Draft
> **Normativity:** Normative

### C.29.SC:1 - Problem frame

Use this pattern when a transformation appears to preserve the structure relevant to a problem, and you need to turn that observation into a useful restriction, a transferred solution or a reason that a requested answer cannot be selected from the available information.

A symmetric allocation problem can constrain its unique optimum before a full calculation. An anonymous arrangement can make a unique choice impossible under a stated selection rule. A rotationally symmetric physical law can relate motions with different initial states. The useful consequence depends on what the transformation actually preserves and how the required answer transforms.

A *symmetry* here is an invertible transformation preserving the stated structure. The object of the Method is that transformation together with the problem and answer it acts on. State the structure: preserving a shape, an equation, a criterion or a fully specified problem gives different premises.

The first result is a consequence with its reason: another valid solution, a restriction on possible answers, or a conflict between the input symmetry and the required output. This can reduce a search or identify the additional distinction a computation needs.

The reader needs the problem's conditions and enough subject mathematics to apply the transformation and test its effect. The allocation and selection examples need algebra and permutations. The dynamics example additionally needs differentiation and elementary state updates.

If no symmetry-related conclusion is needed, use the direct calculation. If the live problem is a general change of mathematical representation, C.29.1 supplies result transfer without requiring a symmetry.

### C.29.SC:2 - Problem

A suggestive symmetry can omit the feature that decides the problem. Equal-looking components can have different costs. A law can be unchanged while its boundary or initial data change. A function can require its output to rotate with its input rather than stay numerically identical.

A second error begins after a real symmetry is established: the solver assumes more than it implies. A symmetric problem can have several asymmetric solutions. A rotation-respecting numerical scheme can fail to conserve the physical angular momentum. To obtain a usable conclusion, follow the transformation through the actual solution condition.

### C.29.SC:3 - Forces

| Force | Tension |
| --- | --- |
| Structure of interest | A transformation can preserve one structure while changing a criterion, condition or distinction needed by the question. |
| Whole problem and law | Symmetry of a law can relate different input problems; a conclusion about one fixed problem needs its data preserved as well. |
| Solution multiplicity | A transformation preserves the solution set, but individual solutions can move within it. |
| Computational saving | Symmetry can reduce repeated work, while the output may need information lost by the reduction. |
| Physical use | A mathematical symmetry can suggest a conserved quantity; its conservation needs the relevant dynamics or theorem. |

### C.29.SC:4 - Solution

**Specify the transformation → follow every relevant condition → transform the answer → derive the consequence → use it within those premises.**

#### C.29.SC:4.1 - Name what must stay the same and what may transform

Recover the problem: admitted candidates, supplied data, conditions, criterion if there is one, and the required kind of answer.

Choose a transformation g and say how it acts on those participants. A permutation can exchange components; a rotation can change coordinates or rotate a physical configuration. Explain which operation is intended. For a symmetry claim, the transformation must be invertible on the relevant domain and retain the stated structure.

Several transformations may form a group: they include doing nothing, composing transformations and undoing each transformation. Name the action on the objects used by the problem. A familiar group name alone leaves that action unspecified.

Keep supplied data in the comparison. If swapping two components also swaps their different costs, the result can be an equivalent problem with transformed data. It is a symmetry of the fixed original problem only if the data required to remain fixed are preserved.

#### C.29.SC:4.2 - Establish the problem-to-solution relation

Apply the transformation to the conditions. Show that an admitted solution is taken to an admitted solution of the stated target problem.

For an optimization problem, check feasibility and the criterion. If g maps the feasible set onto itself and `J(g(x))=J(x)`, it maps every minimizer to a minimizer of that same problem.

For a rule `f:X->Y`, specify the input action g and the corresponding output action r(g). The relation

`f(g(x))=r(g)(f(x))`

is called *equivariance*: transforming the input and then computing agrees with computing and then transforming the output. *Invariance* is the case where the output stays unchanged. Classification of an object and prediction of its position can require these different relations.

For a dynamics law, transform the state, parameters and initial or boundary data. A transformed trajectory may solve the law with transformed data. Establish that correspondence before claiming anything about the solution with the original fixed data.

Use a mathematical argument for the range claimed. A few successful transformations can reveal or test a candidate symmetry; a conclusion covering an entire stated family requires the corresponding preservation argument.

#### C.29.SC:4.3 - Obtain the useful consequence

Follow the consequence needed by the question.

**Transfer a solution.** From a known solution x, obtain g(x) and use the preservation argument from :4.2 to establish what problem it solves. Compositions can generate further related solutions. These are distinct answers only when the transformed objects differ under the problem's equality.

**Restrict a unique solution.** If the fixed problem has exactly one solution x, every symmetry g of that problem must satisfy `g(x)=x`: g(x) is a solution, so uniqueness identifies it with x. Solve this fixed-point condition to restrict or find the candidate.

If uniqueness has not been established, retain the weaker result: symmetries move solutions within the solution set. A symmetric candidate may be worth testing, but the existence of asymmetric solutions remains possible.

**Test a requested deterministic answer.** Suppose an input x is fixed by g and the requested rule must be equivariant. Then `f(x)=r(g)(f(x))`. Check whether any permitted output can satisfy that condition for every transformation fixing x. If none can, the requested deterministic rule cannot answer that input under the stated requirements. The missing distinction or incompatible output requirement is a useful result.

These deductions use preservation and, where stated, uniqueness or equivariance. A conservation law along physical time evolution is a different conclusion. Obtain it from the dynamics or the applicable theorem, including its conditions.

#### C.29.SC:4.4 - Preserve the information needed for use

When symmetry reduces a calculation, state what the reduced answer means in the original problem.

An invariant output can often be calculated from a representative of a symmetry class. An equivariant output may need the transformation used to choose that representative so the answer can be returned to the original coordinates. If several transformations give the same representative, their different output actions must agree on the returned answer, or the result remains ambiguous.

For example, rotating an image to a standard orientation can help classify the object. Reporting a location in the original image additionally requires the corresponding inverse coordinate transformation. If the task distinguishes orientations, the normalization must retain that information.

Use C.29.1 when establishing this representation-and-return relation is itself the difficulty. Use C.29.2 to construct the actual computation; the existence of a symmetric formulation does not supply an efficient algorithm.

#### C.29.SC:4.5 - Return a failed symmetry to its decisive premise

When the comparison in :4.2 fails, identify what changed: an allowed candidate, supplied datum, criterion, output meaning or modeled law. Use that difference to revise the symmetry claim or the problem formulation.

An approximate symmetry can still help, but the allowed discrepancy must be related to the requested result. Establish the bound needed by that use. Small-looking changes are insufficient when they reverse a selection or destroy uniqueness.

After obtaining the consequence, continue with the reduced calculation, transferred solution or revised requirement. Stop when it answers the current question. Add observations or input distinctions only when they can resolve the remaining choice; C.11.DUA supplies the cost-sensitive decision about further work.

### C.29.SC:5 - Archetypal Grounding

#### C.29.SC:5.1 - A symmetric allocation and an asymmetric optimum

Let `x1,x2>=0`, `x1+x2=10`, and minimize `J=x1^2+x2^2`. Swapping x1 and x2 preserves both the feasible set and J.

The cost is strictly convex on this feasible segment, and a minimizer exists because the segment is compact and the cost is continuous. Hence the minimizer is unique. The symmetry condition requires `(x1,x2)=(x2,x1)`, so the only possible optimum is `(5,5)`. The direct calculation `J(5+h,5-h)=50+2*h^2` confirms it for every feasible h.

Now use `J=x1^2+2*x2^2` under the same resource constraint. Swapping the allocations changes the cost: `J(10,0)=100` and `J(0,10)=200`. The original exchange symmetry is gone. The optimum is `(20/3,10/3)`, as the admissible-variation construction in C.29.AV shows.

Symmetry alone also need not make individual solutions symmetric. If the original sum-of-squares criterion is maximized on the same segment, `(10,0)` and `(0,10)` are both maxima. The swap exchanges them. The midpoint is fixed by the swap but is the minimum, so selecting it from symmetry without the uniqueness and optimization premises would answer a different question.

#### C.29.SC:5.2 - A unique choice from an indistinguishable arrangement

A selector receives a three-vertex cycle with identical vertex attributes and equal edge attributes. Its output must designate exactly one vertex. Rotating the cycle is treated as a relabeling: the requested deterministic rule must rotate its selected vertex in the same way.

For this input, a one-step rotation leaves the supplied arrangement unchanged. Equivariance therefore requires the selected vertex to be fixed by that rotation. No vertex is fixed: each moves to the next vertex. The requested deterministic selector has no permitted output for this input.

One repair is to supply a distinguished attribute, such as an available unique priority, and let the rule use it. Another is to change the requested result to the set of all three equally admissible vertices. Random selection is another problem: a uniform distribution can be rotation-invariant even though a sampled vertex is not fixed. The construction of a coordinated random choice would need its own procedure.

This is a mathematical result about the given input and rule requirements. Extra identifiers, timing distinctions or other available attributes can change the input symmetry and therefore the conclusion. It does not establish that every real three-agent arrangement faces this obstruction.

#### C.29.SC:5.3 - A symmetry of motion and what a numerical step preserves

Consider the planar model `qdot=v`, `vdot=-q`. Applying the same planar rotation R to q and v preserves these equations. Thus a trajectory starting at `(q0,v0)` produces a rotated trajectory starting at `(R*q0,R*v0)`.

For `q0=(1,0)`, `v0=(0,1)`, a quarter-turn changes the initial data. The transformed trajectory solves another initial-value problem. Uniqueness for the original data therefore does not imply that its trajectory is fixed by every rotation.

In this model, `J=x*vy-y*vx` is angular momentum for unit mass. Direct differentiation gives

`Jdot = x*ay-y*ax = x*(-y)-y*(-x)=0.`

This establishes conservation along its trajectories. A radial law `vdot=-k(t)*q` gives the same cancellation. The proof uses the acceleration relation; the rotational description alone is not the argument.

Now compute with explicit Euler:

`q_next=q+h*v; v_next=v-h*q.`

The update is equivariant under the same rotations because R distributes over the linear combinations. Yet substitution gives

`J_next=(1+h^2)*J.`

Starting with J=1, h=0.1 and taking one hundred steps yields about 2.7048. Rotation equivariance of the scheme has survived while conservation of J has failed. If the question uses angular momentum, the computational construction must be changed or its error made acceptable for that use.

For this model, the update `v_next=v-h*q; q_next=q+h*v_next` preserves J by substitution. Its preservation of this quantity is one property of that scheme; questions about phase or other errors retain their own numerical analysis.

### C.29.SC:6 - Bias-Annotation

Visual sameness can distract from a cost, label meaning or boundary datum that distinguishes the cases. Transform those inputs explicitly.

A solver familiar with unique linear problems may carry uniqueness into a problem with several solutions. Keep the solution-set result available until uniqueness has its own basis.

A conserved-looking scalar can also invite the wrong inference from equivariance. Distinguish a quantity unchanged under a spatial transformation from a quantity unchanged as the system evolves. The oscillator computation exposes the practical difference.

### C.29.SC:7 - Conformance Checklist

| Question | Passing result |
| --- | --- |
| What structure is preserved? | The transformation, its domain, inverse and action on relevant participants are stated. |
| Which problem is related? | The argument identifies a fixed problem or a problem with transformed data. |
| How does the answer transform? | The solution condition, criterion or required input-output relation is preserved as claimed. |
| What follows from that relation? | The transferred solution, fixed-point restriction or output obstruction follows with its needed uniqueness or equivariance premise. |
| What information must return? | A reduced or normalized calculation can supply the output in the required interpretation. |
| What changes the conclusion? | The decisive datum, constraint, output requirement or law is identifiable when the symmetry fails. |

### C.29.SC:8 - Common Anti-Patterns and How to Avoid Them

| Text-invited mistake | Repair |
| --- | --- |
| Swap components but ignore their different costs. | Apply the transformation to the complete criterion and identify whether the data remain fixed. |
| Infer a symmetric individual solution from a symmetric solution set. | Establish uniqueness or retain the whole transformed family of solutions. |
| Rotate a law while silently keeping changed initial data as the same problem. | Track the transformed initial or boundary values. |
| Demand an invariant output when the task needs an equivariant position or direction. | Specify and apply the output action. |
| Normalize an input and lose the original coordinate relation. | Retain the transformation needed to return the answer or expose the remaining ambiguity. |
| Infer physical conservation from an equivariant update alone. | Derive the quantity's change along the actual dynamics or numerical step. |

### C.29.SC:9 - Consequences

Symmetry can reduce calculation, generate useful related solutions or expose an impossible selection requirement before implementing a solver. The preservation argument also locates what new information would make a choice possible.

The main cost is identifying the relevant structure and following the transformation through the whole problem. Large or continuous symmetry groups may require substantial mathematical methods. The direct consequence obtained here can make that further work worthwhile or show that the simpler calculation already suffices.

### C.29.SC:10 - Architectural Rationale

The Method follows a transformation through a problem and its answer. This keeps a visible symmetry from becoming an unrestricted claim about every quantity or every use.

The fixed-point argument is particularly useful because it converts invariance of the input into a restriction on the answer. Uniqueness and equivariance enter at the point where that conversion needs them. Keeping those premises explicit makes the same reasoning useful in optimization, mathematical construction and computational selection.

A dynamics symmetry, a conservation theorem and a numerical method can contribute to one physical answer while doing different work. The oscillator case retains that connection and exposes where a valid property is lost during computation. A specialized construction of Noether quantities or structure-preserving integrators is a further Method when that result is required.

### C.29.SC:11 - SoTA-Echoing

The selected approach defines the structure and input-output action before using symmetry. It supports direct algebra for a small problem and provides the premise for more specialized group, optimization or numerical constructions.

[Bronstein, Bruna, Cohen and Veličković, *Geometric Deep Learning*, draft chapter 3, §§3.1-3.2](https://geometricdeeplearning.com/book/algebraicpriors.html) develops symmetries as invertible structure-preserving maps and distinguishes invariant and equivariant outputs. Adopt that explicit action and output discipline. Whether a transformation preserves a label or target still comes from the modeled task. Architecture construction and learning-performance claims need the corresponding further Methods and evidence.

[Tong, *Classical Dynamics*, §2.4](https://www.damtp.cam.ac.uk/user/tong/dynamics/dynhtml/S2.html) derives conserved quantities from continuous symmetries of a Lagrangian using its equations of motion. The useful contribution is the extra argument connecting symmetry with time evolution. The simple oscillator calculation above performs that connection directly; it does not substitute for the wider Noether construction.

[Hairer, *Geometric Numerical Integration*, lecture 2, §1](https://www.unige.ch/~hairer/poly_geoint/week2.pdf) supplies the symplectic Euler formulas and their Hamiltonian conditions. The direct comparison above shows why a requested invariant must be examined under the actual numerical update. A different model or requested accuracy can favor a different scheme.

C.29.1 supplies the general result-transfer comparison. The fixed-point and selection constructions here make one specific consequence available without a full group-theory survey. Revisit the use when its structure, output meaning, uniqueness premise or transformation law changes.

### C.29.SC:12 - Relations

- **C.29** establishes the mathematical interpretation and its return to the working subject.
- **C.29.1** constructs the preservation and recovery of a result through a changed representation.
- **C.29.AV** derives consequences from changes that retain constraints; symmetry additionally preserves the specified structure or criterion.
- **C.29.2 and C.29.3** connect a computation with its represented operations and realization.
- **A.3.3.TR** constructs state change from the available laws. **B.5.MPC** connects that physical account with mathematical and computational contributions.
- **B.5.RR** revises reasoning after a premise changes. **C.39** helps obtain a missing construction or reformulate an obstructed result.

### C.29.SC:End
