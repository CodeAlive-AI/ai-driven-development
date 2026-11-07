## MATH.6 - Refute a Mathematical Claim with a Countermodel

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### MATH.6:1 - Problem frame

Use this pattern when a proposed mathematical implication might fail and you need a construction that settles the failure. Examples include a claimed property of every relation of a certain kind, a proposed inverse, or an interchange of quantifiers that would make a result more useful.

A *countermodel* gives mathematical objects, operations or relations in which the assumptions hold and the proposed conclusion fails. A counterexample to a statement about fixed objects supplies the particular values that make it fail. Both let you stop trying to prove the original claim and identify a useful change of question or assumptions.

Start by stating what must remain true and what would defeat the conclusion. Then construct one such case. Return the case and its decisive calculation or argument. A familiar counterexample already satisfying the present assumptions can finish the work immediately.

The reader needs elementary sets, relations, functions and quantified statements. The constructions below use ordinary mathematical truth and explicit witnesses; symbolic logic notation is explained where it changes the construction. A proof of a true claim, an estimate of how often a procedure fails, and an observation about a physical system require their corresponding methods. Countermodel construction answers whether the stated mathematical assumptions force the conclusion.

### MATH.6:2 - Problem

Several successful examples can hide the condition on which a conclusion depends. Conversely, an apparently failing example can violate an assumption, use different arithmetic, or assign inconsistent values to one object. It then leaves the proposed implication unanswered.

The working difficulty is to keep the assumptions and the failed conclusion in one construction. Quantifier order determines which choices may depend on which inputs. The carrier and operation rules determine whether the proposed objects are admissible. Search limits determine what can be concluded when no failure is found.

### MATH.6:3 - Forces

| Force | Tension |
| --- | --- |
| Small examples and the stated domain | A small construction is easier to understand, but the required failure may need a larger or infinite carrier. |
| Freedom to construct and retained assumptions | Changing a relation or operation can expose the failure while also destroying a premise. |
| Local witness and quantified failure | One input defeats a universal claim; defeating an existence claim can require a reason covering every candidate. |
| Criticism and continuation | Refutation removes one route to a result; its mathematical structure can suggest a different useful route. |

### MATH.6:4 - Solution

**State the implication → construct its failure condition → realize the objects and rules → establish assumptions and failure together → use the result or change the search.**

#### MATH.6:4.1 - Recover the mathematical claim

Name the carrier sets, constants, operations and relations that may vary. Retain the restrictions already given: total or partial operations, finite or infinite carriers, allowed values, and any equations or other assumptions. Expand a definition when its content determines the case you need to build.

Write the proposed implication in the form “under these assumptions, this conclusion holds.” Keep a definition or assumption separate from the conclusion being tested. For example, adding transitivity to the assumptions would remove all nontransitive relations from a test of whether reflexivity and symmetry imply transitivity.

If the claim comes from another practice, first recover its mathematical formulation and the intended interpretation through FPF C.29. The mathematical countermodel will test that formulation. Its consequence for the practice depends on that correspondence.

#### MATH.6:4.2 - Work out what failure requires

Keep the assumptions true and negate the conclusion. Preserve the order and permitted dependence of choices. The following ordinary forms cover common starting points; `P` and `R` denote the stated properties, and each variable keeps its declared domain.

| Conclusion to defeat | Construction or argument needed for failure |
| --- | --- |
| Every `x` has property `P(x)`. | One allowed `x` for which `P(x)` fails. |
| Some `y` has property `P(y)`. | A reason why `P(y)` fails for every allowed `y`. |
| For every `x`, some `y` satisfies `R(x,y)`. | One allowed `x` for which every allowed `y` fails. |
| Some `y` satisfies `R(x,y)` for every `x`. | For each allowed `y`, an `x` that defeats it; this `x` may depend on `y`. |

An equation between operations can often be defeated by one input tuple. Failure of transitivity requires three elements with the first two links present and the third absent. Start with those witnesses and use them to constrain the construction.

Where failure contains a universal requirement, give its argument or a complete finite case distinction. Finding one unsuccessful candidate for an existential conclusion leaves the other candidates open.

#### MATH.6:4.3 - Build objects that can realize the failure

Choose a familiar structure or a small carrier that has room for the required witnesses. Assign the constants and the critical relation entries or operation values first. Fill the remaining entries so that the assumptions continue to hold. Total operations need an output for every allowed input; partial operations retain their domains of definition.

For a finite relation, a table can make the critical choices visible. For a function, give its value at each element or give a defining rule. If the objects are classes of expressions, ensure the operation has the same value for equivalent representatives; MATH.2 supplies that construction.

Use the assumptions to reduce the choices. Symmetry determines the reversed relation entry; an identity law determines part of an operation table. After a forced assignment, return to any assumption that uses the changed entry. A conflict means this attempted construction needs revision.

Try a larger carrier or another kind of structure when the failure condition needs it. Smallness is useful for discovery and explanation; a smallest countermodel is required only when its minimality answers the question. A symbolic construction can cover an infinite carrier without listing its elements.

A model finder can supply assignments when the interacting constraints make manual construction expensive. Give it the assumptions together with the negated conclusion and the chosen search scope. Retain the meaning of its types, arithmetic and undefined values when interpreting the returned assignment.

#### MATH.6:4.4 - Establish that the construction defeats the claim

Evaluate every assumption used by the implication in the constructed case. Then exhibit the false conclusion with the witnesses or quantified argument from :4.2. These two parts establish the countermodel.

For a finite carrier, universal premises can be checked over all relevant tuples. For an infinite carrier, use a rule and an argument covering the required inputs. A program's finite output can help discover that rule; the argument determines the wider conclusion.

If a search tool used a restricted interpretation, substitute its proposed counterexample back into the intended mathematical definitions. For example, a truncated representation of the natural numbers needs its missing values accounted for. Repair an assignment that relies on an unavailable value or an altered operation before using it to refute the original statement.

Suppose the source claim is `n+1≠0` for natural numbers. An encoding instead uses addition modulo 2 and returns `n=1`. Its `1+1=0` becomes `1+1=2` in the source arithmetic, so this assignment fails to refute the source claim. Restore the source arithmetic before continuing that search, or prove the claim directly from `n+1≥1`.

Remove dispensable elements or assignments when that makes the reason easier to see. After such a simplification, repeat the affected assumption and failure checks. Keep a larger readable case if further minimization adds work without helping its use.

#### MATH.6:4.5 - Interpret an unsuccessful search

State what the search covered. Exhaustive failure to find a countermodel establishes absence only in the fully searched class and under the encoded semantics. A timeout or a partial enumeration leaves even that class unresolved.

When this absence is unexpected, compare the encoded assumptions with the intended ones. A contradictory or overrestrictive premise set can exclude the very cases under examination. Constructing one model of the assumptions alone can help distinguish that problem from an unsuccessful search for failure.

Choose the next move from what could answer the question: a different carrier, a symbolic infinite construction, a proof of the proposed claim, a weaker conclusion, or stopping with the searched-scope result. FPF C.11.DUA helps decide whether further inquiry is worth its cost. Enlarging the search is one option.

#### MATH.6:4.6 - Use the failure to revise the mathematical work

Return the assumptions that survived, the failed consequence, and the construction that separates them. This can reject an identification, stop an invalid proof attempt, expose a needed input, or identify an operation for which a proposed representation is unsuitable.

A repair is a new mathematical question. Restrict the domain, strengthen a justified premise, weaken the requested conclusion, or change the construction according to what the receiving work needs. Establish the revised claim on that scope; merely excluding the exhibited case can leave other failures.

Use B.5.RR to follow the effect through an existing argument. Use MATH.2 or MATH.5 when the affected step forms classes or interprets generating operations. Stop once the countermodel and its intended consequence are usable.

### MATH.6:5 - Archetypal Grounding

#### MATH.6:5.1 - A relation that cannot serve as the proposed equivalence

The claim is that every reflexive, symmetric relation is transitive. On `X={a,b,c}`, assign the following relation; 1 means the pair is in the relation.

| R | a | b | c |
| --- | --- | --- | --- |
| a | 1 | 1 | 0 |
| b | 1 | 1 | 1 |
| c | 0 | 1 | 1 |

The diagonal establishes reflexivity. Matching entries across the diagonal establish symmetry. But `a R b` and `b R c` hold while `a R c` fails. This is a countermodel with the required three witnesses.

With at most two elements, every reflexive symmetric relation is transitive: in a two-link sequence `x R y R z`, either `x=z`, or one adjacent pair is an equal pair and the other link already supplies `x R z`. The third element makes the failure possible.

If the work needs the smallest equivalence relation containing this R, its transitive closure adds the missing pairs and gives the single class `{a,b,c}`. It answers whether elements are connected through R-links. A question about the original direct relation still needs the original table. For classes on which further operations must be defined, continue with MATH.2's operation-preservation condition.

#### MATH.6:5.2 - A left inverse and the elements it does not recover

Consider the claim: if `f:A→B` has `g:B→A` with `g(f(a))=a` for every `a`, then `f(g(b))=b` for every `b`.

Choose `A={u}`, `B={0,1}`, `f(u)=0`, and `g(0)=g(1)=u`. Both maps are total. The premise holds at the only element of A, but `f(g(1))=0`. The claim fails because the left-inverse condition constrains recovery of source elements while B also contains an element outside the image of f.

Now require A and B to be the same finite set. The premise makes f injective: equality `f(a)=f(a')` gives `a=a'` after applying g. An injective self-map of a finite set is surjective. Write any `b` as `f(a)`; then `f(g(b))=f(g(f(a)))=f(a)=b`. This supplies a proof for the changed domain.

For the same infinite set `N={0,1,2,...}`, take `f(n)=n+1`, `g(0)=0`, and `g(n+1)=n`. Then `g(f(n))=n` for every n, but `f(g(0))=1`. Every finite self-map search can miss this failure because the finite claim is true. The symbolic construction locates the lost premise: finiteness supplied the step from injection to surjection.

A receiving construction can retain the original left inverse for source recovery, require surjectivity for recovery of every target element, or restrict the target to the image. Which result is useful depends on the proposed representation.

#### MATH.6:5.3 - A separate answer for each input and one answer for all inputs

Let `X=Y={0,1}` and let `R(x,y)` mean `x≠y`. For every x there is a y satisfying R: choose `y=1-x`. The proposed stronger conclusion is that one y works for every x.

To defeat that conclusion, take any proposed y and choose `x=y`. Then R fails. This gives the required argument for both possible choices of y. It does not replace the premise's input-dependent choice with a uniform one.

The useful result can instead be a function `h(x)=1-x`, satisfying `R(x,h(x))` for every x. MATH.4 supplies inductive witness construction when a comparable task has finite inductively formed inputs and suitable base and constructor clauses. The countermodel identifies which input dependence the requested result must retain.

### MATH.6:6 - Bias-Annotation

Small finite structures are prominent here because they expose the construction and make universal checks affordable. That preference can conceal infinite-only failures, as :5.2 demonstrates. The quantified claims also presuppose the stated mathematical interpretation; a probabilistic failure rate or empirical prevalence requires another question and method.

### MATH.6:7 - Conformance Checklist

- The construction uses the domains, operation rules and assumptions of the claim being tested.
- The failure condition retains quantifier order and the allowed dependence of each choice.
- The proposed objects satisfy the assumptions and defeat the conclusion in the same interpretation.
- A finite search result states its covered scope; any wider conclusion has its own argument.
- The result changes the receiving proof, construction or question, with any proposed repair stated separately.

### MATH.6:8 - Common Anti-Patterns and How to Avoid Them

**Put the desired conclusion among the assumptions.** This excludes countermodels by construction. Keep the conclusion outside the retained assumptions, and inspect an unexpected empty search.

**Use a failing case outside the stated domain.** The infinite shift in :5.2 refutes the unrestricted self-map claim while the finite claim remains true. Carry the actual domain into the returned conclusion.

**Keep one witness while reversing quantifier order.** The witness in :5.3 depends on the input. Preserve that dependence, or establish a uniform witness as a different result.

**Treat a search limit as the theorem's limit.** Recover which mathematical cases were represented. Change the construction or retain the bounded result when the desired claim reaches beyond them.

### MATH.6:9 - Consequences

A countermodel gives a conclusive failure of the stated implication and a concrete object for further work. It can reveal a useful narrower theorem, a needed distinction, or a replacement construction. Its direct result is refutation on the stated interpretation; choosing and proving the repair remains further work.

An unsuccessful attempt can still identify an incompatible set of assignments or a limited class with no failure. Its usefulness depends on how that result changes the next mathematical move.

### MATH.6:10 - Architectural Rationale

The method joins logical failure conditions with mathematical construction. Negating the conclusion tells the worker what to build; satisfying the assumptions makes the constructed case relevant; carrying the result back into the argument makes the criticism usable.

Separating these operations exposes two different errors: an inadmissible example and a failure condition that does not defeat the actual quantified claim. The finite and infinite inverse cases show how the same question can move between refutation and proof as the domain changes.

B.5.RA recovers an available argument, and B.5.RR revises reasoning when its premises or question change. This pattern supplies the mathematical countermodel they can consume. MATH.2's failed-identification witness is a direct use, while the relation and inverse cases give this construction independent mathematical entries.

A known case or a short direct construction is preferable when it already settles the implication. Constraint solving helps when the assumptions interact enough to make that construction difficult. Neither route requires finding a smallest example unless its size matters to the receiving question.

### MATH.6:11 - SoTA-Echoing

**Question:** how can a mathematical claim be refuted by a constructed interpretation while preserving its assumptions and quantifier dependencies?

Blanchette's [*A User's Guide to Nitpick for Isabelle/HOL*, 18 January 2026](https://isabelle.in.tum.de/doc/nitpick.pdf), §§3.2-3.5, demonstrates carrier search, recovery of assigned constants, dependent witnesses and the treatment of infinite number types. **Adopt** those distinctions. The manual's use of finite subsets for infinite types makes interpretation of a returned assignment important. The hand constructions here make the decisive reasoning accessible without requiring Isabelle.

The [Alloy language reference, Commands](https://alloytools.org/spec.html#command-section) specifies assertion checking as assumptions and declarations together with the negated assertion, within a scope. **Adapt** that construction to mathematical relations and operations; retain its distinction between assumptions, asserted consequences and search bounds. An empty search can expose an overrestricted formulation as well as an absence of counterexamples.

Direct construction, a supplied counterexample and a proof are meaningful alternatives at comparable effort. A model finder is useful when it supplies a difficult assignment, while symbolic reasoning remains important for quantified or infinite constructions. Reopen the chosen approach when a changed domain, equation or search interpretation changes what its result can establish.

### MATH.6:12 - Relations

- **Uses MATH.1 and MATH.2 when operations or classes are involved:** construct permitted combinations and test whether the proposed identification preserves them.
- **Connects with MATH.4:** retain the dependence of a constructed witness on its input.
- **Connects with MATH.5:** a failed source equation can refute the proposed extension to identified expressions.
- **Supplies B.5.RA and B.5.RR:** use a mathematical failure in criticism and in revision of the affected argument.
- **Uses C.29 for an external subject:** establish what the mathematical failure means for that subject.
- **Uses B.5.QD or C.11.DUA when continuation is the question:** choose a worthwhile new problem or further inquiry from the result.

### MATH.6:End
