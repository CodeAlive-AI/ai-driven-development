## MATH.22 - Change Axioms and Trace Their Consequences

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### MATH.22:1 - Problem frame

Use this pattern when a mathematical assumption excludes a construction you need, a theorem uses a stronger premise than its intended application supplies, or two accounts differ in what they assume. The work is to change the assumptions and establish what the changed theory permits.

An **axiom** is a statement taken as a premise of the theory being developed. A **model of those axioms** is a mathematical structure in which they hold under a stated interpretation. For example, an ordered set interprets an order relation; a collection of permutations interprets composition. This use of model concerns mathematical satisfaction. Applying the structure to an observed subject requires the additional correspondence work in C.29 and MMP.

**First useful move:** isolate one assumption and one construction or conclusion affected by it. Try to derive that conclusion from the remaining assumptions, or construct a case where they hold and the conclusion fails. The result identifies what can be retained and what must change.

The reader needs elementary reasoning about sets, operations, relations and their laws. The examples introduce the group, order and arithmetic assumptions they use. A change of logical inference rules needs the corresponding knowledge of that logic.

If a supplied theorem already works under the available assumptions, apply it. MATH.6 suffices for refuting one proposed consequence. Use the present method when the receiving work needs a revised theory, its changed constructions and its surviving results.

### MATH.22:2 - Problem

A familiar axiom set can make a useful construction impossible or unnecessarily restrictive. Dropping a premise admits more structures, but a familiar proof may then fail. Adding a convenient operation can conceal an existence assumption, and adding a desired law can conflict with laws already retained.

There are different outcomes to establish. A proof might survive unchanged, admit a new proof, need an extra condition, or have a counterexample. A stopped proof search leaves these possibilities unresolved. The revised theory must expose the difference because later reasoning and computation consume its consequences.

### MATH.22:3 - Forces

| Force | Tension |
| --- | --- |
| Generality | Fewer assumptions can cover more structures while supporting fewer conclusions. |
| Stronger constructions | Added axioms can supply an object or simplify a proof while excluding intended cases. |
| Familiar notation | A new symbol can abbreviate an existing construction or introduce a new assumption. |
| Proof reuse | A theorem may remain valid even when its familiar proof uses a removed axiom. |
| Useful metatheory | A small countermodel can settle a local question; a consistency claim about a foundation can require much stronger work. |
| Computational use | An existence principle can support a mathematical argument while leaving an obtaining procedure to be supplied. |

### MATH.22:4 - Solution

**Local mantra:** isolate the assumption and wanted construction; choose the change; build or interpret the changed structures; trace the affected arguments; establish what the comparison warrants; return the revised theory to use.

#### MATH.22:4.1 - Identify the assumption and its mathematical job

State the objects, operations and laws currently used. Find the step where the disputed assumption enters. It may justify rearranging operations, comparing two objects, choosing an element, taking a limit, or introducing an object with a required property.

Distinguish a law about the objects from a logical rule used to infer statements about them. Removing commutativity changes the structures being studied. Restricting proof by contradiction can change the permitted arguments even when the question concerns the same objects.

State the desired gain. Examples include admitting noncommuting operations, retaining incomparable alternatives, obtaining a missing limit, or preserving the computational content of a proof. This gain guides which consequences to examine first.

For a local question, the relevant definitions and proof dependencies are enough. Reconstruct a whole formal foundation only when the conclusion being sought depends on it.

#### MATH.22:4.2 - Choose the change and what stays fixed

With a fixed language and logic, removing axioms weakens the theory: every old model still satisfies the retained axioms, and additional models may become possible. Adding axioms strengthens it: every new model must satisfy the old axioms as well, so some old models may be excluded. Replacing an axiom combines removal and addition; neither direction of inclusion follows automatically.

Name the fixed assumptions and the changed one. If the vocabulary changes too, give the interpretation used to compare the accounts. MATH.18 develops that comparison.

When introducing a symbol for an operation, ask how the operation is obtained. An abbreviation such as d(x,y)=x+(-y) expands into operations already available. If a proposed definition instead asks for the unique object satisfying a property, establish existence and uniqueness on its intended inputs. Calling it a definition does not complete that construction. In :5.2, a least upper bound exists in one order and is absent in another.

An added operation can also require a larger collection of objects. In that case construct the extension and the map from the earlier structure, then establish which old operations and relations the map preserves. MATH.1/.2/.16 supply construction methods for objects and operations. An extension by limits also requires specifying convergence and establishing that the needed limiting objects exist.

#### MATH.22:4.3 - Construct models and separating cases

Give the objects and the interpretation of every operation and relation needed by the claim. Establish each retained axiom. For an infinite family, use a general argument; enumerated cases suffice only when they exhaust the admitted possibilities.

Choose a case that distinguishes the changed theories. To investigate an axiom A relative to retained assumptions T, a model of T in which A fails shows that A is not a consequence of T. A model where A holds shows that adding A is compatible with that model. These are different results, and both can matter.

Use MATH.6 to construct a countermodel. Finite structures are often a cheap first attempt because their operations and relevant failures can be displayed completely. An existing infinite structure with a short argument may be simpler.

If the changed account uses different objects or primitives, an interpretation can carry its constructions into an established theory. Check the translated axioms and the translated steps of inference needed for the result. A picture suggesting an analogy is a starting point for this work.

#### MATH.22:4.4 - Trace the consequences that the receiving work uses

For each required result, locate the affected proof step.

- Retain a proof when its steps use only assumptions that remain.
- Try another proof when the old one uses the removed assumption. A dependency of one proof need not be a necessary premise of the theorem.
- Keep a conditional result when the receiving use can supply the additional premise.
- Return a countermodel when the conclusion fails under the revised assumptions.
- Leave a particular consequence unresolved when neither an argument nor a countermodel has been obtained.

Apply the same reasoning to constructions. Check whether their inputs are still admitted, the operations remain defined, and the properties used by the next step still follow. For example, :5.1 retains cancellation after dropping commutativity but loses unrestricted rearrangement of factors.

When a proof is formalized, its recorded dependencies can help find affected steps. They report what that proof uses. A claim that no proof can avoid an axiom requires an additional argument.

If the result will generate data or a program, trace what the new principle supplies operationally. An existence argument and an effective construction support different next uses. MATH.12 handles extraction; the relevant computational method handles execution and cost.

#### MATH.22:4.5 - State what the model or proof establishes

In a sound interpretation of a deductive system, a proof preserves truth in every model of its premises. Therefore a model of T where A fails rules out a proof of A from T. If another model of T satisfies A, it likewise rules out a proof of not-A. Together these establish that A is independent of T, relative to the logic and semantics being used.

A model also supports consistency: a sound derivation of a contradiction from its axioms would have to make a contradiction true in that model. The construction of the model relies on background mathematics. Keep that dependence when reporting a consistency result, especially when comparing foundations. A failure to find a contradiction supplies no such construction.

For a definitional extension, expand the new symbols in the affected claims and arguments. When all new operations are definable in the old theory and the definitions can be eliminated, conclusions stated wholly in the old language retain their old justification. If an existence principle or inference rule has been added, examine its consequences separately.

The preceding model arguments use their stated semantics. A change to intuitionistic, dependent-type or another logic requires an interpretation sound for its own rules; an arbitrary transfer of classical model arguments could answer the wrong question.

#### MATH.22:4.6 - Use the revised theory

Return the changed assumptions together with the construction, theorem or obstruction needed by the receiving work. Carry the conditions under which it can be used. An unresolved consistency or consequence question can be handed to a collaborator without presenting it as settled.

Choose between revised theories by the work they enable and the costs they impose. One can admit more objects, another can make a needed construction available, and another can retain an effective procedure. FPF's ordinary characterization and choice methods apply when these alternatives must be compared; the present method supplies their mathematical consequences.

Use the changed result to reformulate a model, modify a method, or pose the next mathematical problem. For a new conjecture, state which further relation might hold under the retained assumptions. A later failure reopens the assumption or inference on which the failed use depends.

### MATH.22:5 - Archetypal Grounding

#### MATH.22:5.1 - Drop commutativity while preserving invertible composition

Suppose a collection has an associative operation, an identity e and an inverse for every element. These are the group assumptions. Add commutativity, xy=yx, and familiar rearrangements become available. For example, MATH.19's argument proves `(xy)^n=x^n y^n`.

The intended new use composes invertible operations whose order matters. Remove commutativity and retain the group assumptions.

Cancellation survives, although its proof may change. A commutative proof multiplies `ax=ay` on the right by the inverse of a, then rearranges `axa⁻¹` and `aya⁻¹` to obtain `x=y`. This uses commutativity. A replacement proof multiplies on the left: `a⁻¹(ax)=a⁻¹(ay)`. Associativity gives `(a⁻¹a)x=(a⁻¹a)y`, hence `x=y` by the inverse and identity laws. The theorem therefore survives after removing commutativity.

Unrestricted rearrangement fails. Consider all permutations of {1,2,3}, composed with the rightmost permutation acting first. Composition is associative, the identity leaves each element fixed, and each bijection has an inverse. Let f swap 1 and 2, and let g swap 2 and 3. Then fg sends 1 to 2 to 3 to 1 as a cycle, while f² and g² are identities. Thus (fg)² sends 1 to 3, but f²g² sends 1 to 1.

This is a model of the group assumptions with noncommuting elements. The two-element group {e,h}, with h²=e, is a model where every pair commutes. Under ordinary classical group logic, the two models show that commutativity is independent of the retained group axioms.

The revised theory now admits ordered compositions. It retains cancellation and inverses. Rearrangement remains usable for particular pairs whose commutation is established; it has ceased to be a general permission.

#### MATH.22:5.2 - Remove total comparability and inspect a proposed new operation

A partial order is reflexive, antisymmetric and transitive. A total order additionally compares every pair: x<=y or y<=x. Suppose the work needs to retain pairs for which neither direction holds.

Remove total comparability. On pairs of natural numbers, define (a,b)<=(c,d) when a<=c and b<=d. The three partial-order laws follow coordinate by coordinate. The pairs (1,0) and (0,1) are incomparable. The ordinary order on natural numbers supplies a model with total comparability; the pair order supplies a model without it.

Now ask for a least common upper bound of two objects. In the pair order, it is the coordinatewise maximum. It is above both inputs, and any common upper bound is above each coordinatewise maximum. This proves both the construction and its leastness.

The partial-order axioms alone do not supply that operation. Take four distinct objects a,b,u,v. Besides reflexive comparisons, require a<=u, a<=v, b<=u and b<=v, and no others. This is a partial order. Both u and v are upper bounds of a and b, but neither is below the other; a and b are not upper bounds. There is no least upper bound of the pair.

Consequently, writing "x join y" for every pair in an arbitrary partial order adds an existence requirement unless a construction has already supplied it. The work can select an order where joins exist, add the join assumption and accept its narrower class of models, or undertake a construction that enlarges the objects. Choosing one of u or v alone supplies an upper bound, not the missing least one.

This separates two changes that a generic instruction to "relax the order" would hide: allowing incomparability and requiring a combining operation. A model of alternatives can use the resulting order; any decision to prefer one alternative remains a separate choice.

#### MATH.22:5.3 - Introduce total reciprocal notation without retaining a false law

Suppose arithmetic uses field laws, including `0!=1` and distributivity, and the reciprocal law `x*inv(x)=1` for `x!=0`. The proposed change makes inv a total operation and asks that same law to hold at zero.

The retained laws already imply `0*y=0`. Indeed, `(0+0)*y=0*y+0*y` by distributivity, and cancelling one `0*y` from `0*y=0*y+0*y` leaves `0=0*y`. The proposed new reciprocal law at zero would therefore imply `0=1`. The retained assumptions and the new law conflict.

A different change works: over the rational numbers, define `inv(0)=0` and `inv(x)=1/x` for `x!=0`. This gives a total operation, retains the nonzero reciprocal law, and leaves the field operations unchanged. It has not made cancellation of a zero factor valid.

For a use involving the equation `x*y=x*z`, cancellation still requires `x!=0`. At `x=0`, all rational y,z satisfy the equation. A calculation using total reciprocal notation must retain that condition or inspect the zero case.

The result is a consistent construction within rational arithmetic and a revised law with its condition, rather than the initially requested unconditional inverse law. Total notation and stronger algebraic permission have been separated.

### MATH.22:6 - Bias-Annotation

Familiar structures can make their extra laws feel unavoidable. The permutation and partial-order cases expose assumptions that integers with addition or a single numerical scale can conceal.

The examples use elementary classical structures so that the changed laws can be inspected directly. They demonstrate the method without deciding between competing foundations of mathematics. A foundational change needs its own interpretation and consequences, including any change in constructive use.

### MATH.22:7 - Conformance Checklist

For the change being made:

- The altered axiom, definition or inference rule and the assumptions retained are identifiable.
- The desired construction or consequence explains why the change is useful.
- A claimed model supplies the required objects and interpretations and satisfies every retained axiom.
- A definition has its required existence and uniqueness, or the additional assumption is stated.
- Reused proofs survive at the steps that matter; a lost proof is distinguished from a refuted theorem.
- Independence, consistency and non-derivability claims have the appropriate model or argument and retain their background assumptions.
- The receiving use gets the revised consequence with its applicability and any obtaining procedure still needed.

### MATH.22:8 - Common Anti-Patterns and How to Avoid Them

**Removing a premise while retaining its rewrite permission.** Dropping commutativity in :5.1 permits noncommuting operations. Reordering their factors requires a local commutation argument.

**Defining an object that need not exist.** The four-object order in :5.2 has common upper bounds but no least one. Supply a construction or change the assumptions before using join as a total operation.

**Extending notation and silently strengthening a law.** Total reciprocal notation in :5.3 is available with a conditional inverse law. The unconditional law contradicts the retained arithmetic.

**Treating a failed proof as independence.** The proof may need a different lemma. Establish non-consequence through a separating model or a suitable metatheoretic argument. For the model route in :4.5, establish both directions of separation before claiming independence.

### MATH.22:9 - Consequences

The result exposes which generalizations preserve a useful conclusion, which additions buy a new construction, and which changes require a different problem. A small separating structure can prevent repeated attempts to derive a false consequence.

Changing axioms can also open a family of new questions. Which maps preserve the revised structure? Which previous constructions still work? Can a missing operation be supplied by extending the objects? These questions continue the mathematical development and give modeling or methodological work new usable constructions.

### MATH.22:10 - Architectural Rationale

A proof states what follows from assumptions. A model makes their simultaneous satisfaction and separating consequences inspectable. Using both permits directed theory change: follow a needed construction to its assumptions, change them, and return the consequences to that construction's use.

MATH.6 constructs countermodels, MATH.18 compares accounts through interpretations, and MATH.19 constructs missing arguments. Here these methods support a revised theory whose consequences can be used deliberately.

Logical consistency, mathematical fruitfulness and correspondence to an observed subject answer different working questions. The first controls what the axioms jointly permit; the second concerns the further constructions and questions they open; the third requires subject knowledge and observation. Their connection supports mathematical modeling without making one stand in for the others.

### MATH.22:11 - SoTA-Echoing

The working question is how to change mathematical assumptions while retaining justified and useful consequences. The selected line combines proof-dependency analysis, construction of models and interpretations, and explicit separation of definitional change from added principles.

**Adopt the model-and-consequence method.** The Open Logic Project's [Models and Theories](https://builds.openlogicproject.org/content/first-order-logic/introduction/models-theories.pdf) makes the relation between axioms and satisfying structures explicit. [Logic and Proof, §§10.1-10.5](https://leanprover-community.github.io/logic_and_proof/semantics_of_first_order_logic.html) supplies interpretation and soundness for the first-order branch. These are method sources for :4.3/:4.5. Their use defeats an inference from unsuccessful proof search to non-consequence: a separating structure supplies the needed reason. A known theorem or short existing interpretation is cheaper when it already settles the same question. The chosen branch accepts the cost of constructing a model when that difference remains unresolved.

**Adapt dependency analysis to the required return.** [Theorem Proving in Lean 4, Axioms and Computation](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/) explains how added principles affect proof and computational interpretation, and how axiom dependencies can be inspected. This changes :4.1/:4.4: trace the principle actually used and what a later construction can obtain. Reading a proof's dependencies is a useful alternative to rebuilding it. That inspection alone does not settle whether another proof avoids the principle. A non-derivability claim needs a separate argument, such as a separating model under the stated soundness assumption. The source describes one formal system; Lean use is optional, and its evaluation mechanisms are not generalized to all mathematics.

Retain these approaches while their constructions answer the local question at acceptable effort. Reopen the comparison when the logic changes, a proposed interpretation fails, another proof removes the alleged dependency, or the receiving use needs computational content that the revised theory has not supplied.

### MATH.22:12 - Relations

- **MATH.6** constructs a countermodel; **MATH.18** compares accounts through interpretations.
- **MATH.19** constructs or replaces affected arguments; **MATH.12** recovers their constructive output.
- **MATH.1/.2/.16** supply construction methods when a changed theory needs different objects or operations.
- **B.5.FM, B.5.TC and C.29** use the resulting assumptions and structures in reformulation, theory change and correspondence to a subject.
- **MMP and the relevant CMP methods** use the revised mathematical construction, adding subject interpretation or an executable procedure when required.
- **Core's Method-development family** can use this mathematical account to change formal descriptions of methods; the behavior of the described work still needs its own justification.

### MATH.22:End
