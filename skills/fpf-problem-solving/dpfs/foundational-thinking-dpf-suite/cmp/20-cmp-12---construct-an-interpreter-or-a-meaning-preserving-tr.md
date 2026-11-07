## CMP.12 - Construct an Interpreter or a Meaning-Preserving Translation

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### CMP.12:1 - Problem frame

**Use this when** a calculation, rule language or program description has an intended meaning, but an effective way to execute it is missing, too costly or must change. You need to construct evaluation rules, translate the description into another executable form, or repair a translation that changes the result or behavior on which its user relies.

The reader can distinguish the admitted expressions and the operations they describe. The task is to turn those distinctions into an algorithm for evaluation or translation. Programs become inputs and outputs of that algorithm: a reader can examine how a rule is executed and change the rule's representation without silently changing its use.

The result is an interpreter or effective translation, with the correspondence needed to use its output. Depending on the question, the preserved observation may include returned values, state changes, interaction, failure or termination. A compiler for a programming language, an evaluator for symbolic expressions and an interpreter for a decision language are different applications of this method.

Use an existing suitable evaluator or translator when it already provides the needed behavior affordably. Designing the notation's useful distinctions is a separate question when those distinctions are still unknown. Choosing a physical realization follows the computational construction and its actual resource requirements.

### CMP.12:2 - Problem

How can expression meaning be turned into effective evaluation and translation rules, so that the resulting computation preserves the observations needed by its user?

A mathematical interpretation can assign a meaning without providing an algorithm for obtaining it. A text substitution can preserve printed names while changing what they refer to. A translation can return the right value on a simple test while evaluating an unwanted branch, capturing another binding or failing to terminate on a previously terminating input.

### CMP.12:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Meaning and obtaining | Knowing what answer an expression denotes leaves the effective evaluation work to be constructed. |
| Local syntax and surrounding bindings | The same expression can refer to different values in different environments. |
| Equal final values and observable behavior | Order, effects, failure and termination can matter even when a returned number agrees. |
| Repeated interpretation and prior translation | Translation can save later dispatch work while adding construction time and retained code. |
| Compositional reasoning and execution context | A correct component must retain its meaning when combined with neighboring components. |
| Abstract operations and finite resources | Arithmetic range, stack capacity and foreign operations can change the admitted execution. |

### CMP.12:4 - Solution

**Recover expression structure and observations → construct evaluation rules → make control and binding effective → construct the translation → establish the needed correspondence → execute and revise the changed rule.**

#### CMP.12:4.1 - Recover the expression structure and the intended observations

Identify the constructors of admitted expressions and how their parts bind and compose. Work with a parsed structure when precedence, grouping or scope matters. A name occurrence must reach the declaration or external input intended by the language. If the supplied text admits different parses that change the answer, resolve that difference before constructing one evaluator.

Specify what evaluation receives and what its user can observe. Inputs can include the expression, name bindings, stored state and external responses. Outputs can include a value, changed state, a sequence of interactions or a failure. Distinguish a language-defined error from the absence of a defined operation; a translator can be required to preserve the former without being required to assign a meaning to the latter.

Choose the required relation between source and target observations. Equal returned values may suffice for a terminating pure expression. An interactive program may require the same ordered events. A source with several permitted behaviors may allow the target to choose among them; retaining every source possibility is a stronger requirement. Timing, memory use or a probability law belongs in this relation only when the receiving question uses it.

#### CMP.12:4.2 - Derive effective evaluation rules for each constructor

Construct the evaluator by cases on expression structure. For a literal, return its value. For a name, obtain its binding. For an operation, evaluate the required operands in the specified order and apply the available primitive. For a conditional, evaluate its test and then only the selected branch when that is the language's rule.

Give binding an explicit operation. In an immutable lexically scoped language, evaluating `let x=a in b` first obtains a's value in the current environment, then evaluates b in an environment extended with that binding. The extension's scope ends with b. Nested use of the same printed name need not change the earlier binding.

For a function expression, construct an applicable value containing the parameters, body and the bindings its later execution needs. Such a value is a **closure**. To apply it under lexical scope, extend its saved environment with the argument bindings and evaluate its body there. If variables can change, distinguish names, storage locations and current contents so that a captured reference continues to designate the intended location.

Expose the primitive's actual operation. An instruction to select an element satisfying a condition needs a search or other obtaining procedure. An unbounded search must retain its possible nontermination. If the implementation language has different arithmetic, truth values or evaluation order, translate those operations deliberately rather than inheriting its defaults.

#### CMP.12:4.3 - Make control, progress and resource use executable

Decide what remains to be done after the current subexpression returns. A recursive evaluator can retain that continuation in its own call stack. An explicit evaluator can instead store pending operations, environments and return destinations as data. Construct the transition that resumes the pending work with the obtained result.

Distinguish the termination of translation from the termination of the translated program. A compiler that traverses a finite syntax tree can terminate even when the generated program runs indefinitely. A step limit can return a suspended computation; reaching that limit does not establish divergence. CMP.1 supplies the limit on general termination decision when that question arises.

Count consequential dispatch, environment lookup, retained continuations, arithmetic and storage. Removing repeated syntax analysis may repay compilation for repeated execution. For a rarely used or frequently changing expression, direct interpretation may be the cheaper choice. Retain the existing algorithmic cost and comparison methods rather than assuming compilation always improves the work.

#### CMP.12:4.4 - Construct translation from the evaluation structure

Choose a target instruction or expression language with defined execution rules. For each source constructor, generate the target operations that perform its required evaluation. Construct the translation of subexpressions and then their combination, retaining temporary results until their consumers use them.

Preserve binding and control at this construction step. Allocate fresh temporary names or use addresses whose scopes cannot capture unrelated bindings. Place conditional branches behind the appropriate control transfer. Pass arguments and return results through agreed locations. An operator with effects requires the relevant order and number of executions; algebraic reassociation alone does not supply that permission.

State how source values, environments and observations correspond to target ones. A target representation may require encoding inputs and decoding outputs. Check that admitted values fit its arithmetic and storage operations. If one representation deliberately approximates another, use CMP.8 for the qualified relation instead of claiming unchanged values.

When several translation passes are used, connect their actual input and output relations. Each pass's output must satisfy the next one's premises. MATH.17 and MATH.18 supply composition and interpretation reasoning; the computational work additionally provides the terminating conversion and executable target operations.

#### CMP.12:4.5 - Establish the correspondence at the scope needed

For a structurally recursive translation of a terminating expression language, use induction on expression construction. Include the context that surrounding code can supply: an arbitrary admitted environment, earlier stored values and the continuation after the translated fragment. A claim that works only with an empty stack may fail as soon as two fragments are composed. Section :5.1 derives the stronger usable claim.

For stateful or interacting languages, relate source and target states and the observations their transitions produce. Explain how matching transitions reestablish the relation. If several internal steps implement one visible step, account for their completion; an infinite internal loop must not masquerade as successful preservation of a terminating computation. Choose the simulation direction or behavior relation that supports the requested conclusion. Showing that one source run has a target counterpart alone leaves other target behavior unresolved.

An alternative is to describe sets of terminating, diverging, failing or interacting behaviors and show that translation preserves the selected relation between them. Use this when the language's semantic operations and composition laws make the argument simpler. Preserve the distinctions that the use needs when choosing this mathematical representation.

Separate a general preservation claim from a check on selected translations. A small comparison can expose a defective rule or settle a bounded receiving case. A claim covering every admitted expression needs an argument covering that class. Use C.11.DUA to choose further testing, translation-specific validation or a general proof according to what the receiving decision requires.

#### CMP.12:4.6 - Run the construction and revise the failed correspondence

Evaluate or translate a meaningful input and use the resulting value or behavior. Return the construction together with the input, binding, execution and recovery conditions needed by its recipient. When comparison fails, locate the changed constructor, binding, primitive, control rule or value correspondence.

A changed language feature or execution context reopens its dependent translations. Preserve unaffected rules. Adding assignment requires revisiting captured bindings; changing integer arithmetic requires revisiting arithmetic correspondence; allowing externally supplied code requires examining the contexts with which translated components interact.

### CMP.12:5 - Archetypal Grounding

#### CMP.12:5.1 - Derive an arithmetic interpreter and stack translation

Expressions are integer literals, names and binary addition, subtraction or multiplication. An environment ρ supplies every free name. Both source and target use unbounded integers. The source evaluator returns a literal, looks up a name, or evaluates the left operand and then the right operand before applying the operator.

The target stack is written from bottom to top. `PUSH n` appends n; `LOAD x` appends ρ(x). For `ADD`, `SUB` or `MUL`, pop the right operand b and then the left operand a, and append respectively `a+b`, `a-b` or `a*b`.

Construct the compiler C:

- `C(n) = PUSH n`.
- `C(x) = LOAD x`.
- `C(a op b) = C(a); C(b); OP`, where OP is the matching target operation.

The useful induction claim is: for every admitted ρ and every initial stack S, running `C(e)` leaves `S · [eval(e,ρ)]`, with earlier entries unchanged. Literals and names append the required value. For a binary expression, the induction hypothesis for a gives `S · [eval(a,ρ)]`; applying the hypothesis for b to that whole stack appends `eval(b,ρ)`. OP replaces just those two entries by their required combination. This proves the claim and supplies the composition condition.

With ρ(x)=5, compile `(x+1)*(x-2)` to:

```text
LOAD x; PUSH 1; ADD; LOAD x; PUSH 2; SUB; MUL
```

Starting above an earlier stack value 99 gives successive added values 5, 1, then 6; next 5, 2, then 3; multiplication leaves `[99,18]`. Each syntax-tree node produces one instruction. Integer operation costs and peak live stack values still depend on the values and expression structure.

**Changed arithmetic:** suppose the target uses unsigned eight-bit wraparound. For `x+1` at x=255 it returns 0, while the source returns 256. Preserve the source by using a wider or multiword representation, restrict the admitted inputs by a valid range argument, or deliberately change the source meaning to modular arithmetic. A successful parse and a preserved instruction order do not fix the arithmetic mismatch.

#### CMP.12:5.2 - Preserve a function's binding when its call site changes

Extend the evaluator with immutable lexical bindings, function values and function application. Evaluate:

```text
let x = 2 in
  let f = (lambda y: x + y) in
    let x = 100 in f(3)
```

Creating f saves its body, parameter y and the environment in which x is 2. Calling f extends that saved environment with y=3, so the body returns 5. Looking up free x in the caller's environment would return 103 and implement a different binding rule.

The closure makes a rule available as a value without discarding its needed surroundings. A procedure can return it, receive it as an argument or construct a new closure that composes it with another rule. Each later application follows the saved bindings and the new arguments.

**Changed feature:** now permit assignment to the original captured x before calling f. If the language specifies capture of that variable's location, assigning it 7 makes `f(3)` return 10. Keeping a copied value 2 would instead return 5. Represent the environment as names mapped to locations and obtain current values from the store; a later shadowing declaration must allocate a different binding. Revise the capture and lookup rules without changing the arithmetic rule.

#### CMP.12:5.3 - Preserve which operation is executed

Let `ifzero(test,a,b)` evaluate test and then only a when the result is zero, otherwise only b. Let division by zero be a defined execution error. The expression `ifzero(x,0,10/x)` returns 0 at x=0 and 5 at x=2.

A translation that evaluates all three parts and then selects a value raises the unwanted division error at x=0. Instead generate fresh labels and conditional control:

```text
LOAD x
JZ zero
PUSH 10; LOAD x; DIV
JMP end
zero: PUSH 0
end:
```

`JZ` pops the test and jumps when it is zero; otherwise execution continues. `JMP` transfers control unconditionally. `DIV` pops right then left and divides left by right, using rational values here. Resolve each fresh label to its instruction position before execution. At x=0 the division instructions are skipped; at x=2 they append 5. Either path preserves earlier stack entries and appends one result.

If the branches instead emit commands, the same construction retains which command occurs. If the source is deliberately changed to evaluate both branches, the preservation claim and translation must change with it. The control rule, rather than a particular programming language's spelling, determines this choice.

#### CMP.12:5.4 - Preserve completion through internal steps

The source instruction is `return 7`; the receiving use requires that return. A target first takes k internal steps and then returns 7, where k is a supplied nonnegative integer. Use a remaining-step counter: each internal step reduces it by one, and at zero the target returns. For every finite k the counter proves that the internal phase finishes, so the target supplies the required result.

Change the target to `loop: goto loop`, leaving `return 7` after this loop. Each internal step goes back to `loop`, so the return is unreachable. A correspondence that allows arbitrarily many silent steps without a completion argument would hide this failure. Restore a finite internal phase to meet the required return.

### CMP.12:6 - Bias-Annotation

A familiar implementation language can silently supply truth tests, numeric limits, scope or evaluation order. Recover the intended operation before reusing that default. The arithmetic, closure and conditional cases each show a different observation lost by an apparently straightforward implementation.

### CMP.12:7 - Conformance Checklist

- Expression formation, binding and needed observations are recoverable.
- Every required evaluation step has an available operation and an explicit control rule.
- Translation terminates on its admitted descriptions; execution progress has its own stated scope.
- Source and target values, bindings, states and observations have the correspondence required by the use.
- The preservation argument includes the surrounding state or context needed for composition.
- Cost includes translation and execution under the actual arithmetic and storage assumptions.
- A changed rule or failed comparison leads to a specific reconstruction.

### CMP.12:8 - Common Anti-Patterns and How to Avoid Them

| Tempting move | Failure | Useful repair |
| --- | --- | --- |
| Copy the implementation language's defaults | The interpreted language acquires unintended arithmetic, scope or order. | Implement the source operation and its conditions explicitly. |
| Substitute names by spelling alone | A new binder captures an unrelated occurrence. | Preserve binding through fresh names, locations or scoped addresses. |
| Evaluate every child before choosing a branch | An unselected operation fails or produces an unwanted effect. | Compile the language's conditional control. |
| Prove a stack fragment only from an empty stack | The result cannot justify embedding after another fragment. | Establish its effect above any admitted earlier stack. |
| Treat a timeout as a divergence result | A terminating run may simply require more steps. | Return suspension or use an applicable termination argument. |

### CMP.12:9 - Consequences

Descriptions of computations become material for further computation. A reader can construct an evaluator, remove repeated interpretation work, combine translated fragments and diagnose a changed result through its binding, control or representation rule.

Preservation is relative to the observations and contexts selected. A useful translation may leave a reverse translation unavailable, select among allowed behaviors, or preserve values while having different resource costs.

### CMP.12:10 - Architectural Rationale

An expression, its mathematical meaning, an evaluator and one execution are different objects in this work. Keeping their correspondence visible lets operations themselves become inputs to constructive transformation. MATH.17 and MATH.18 provide the mathematical composition and interpretation; algorithmics supplies an effective evaluator or converter and explains its execution.

The preservation claim includes composition because translated fragments are normally used together. The arbitrary earlier stack, captured environment and selected branch are three forms of context that change what a local construction must retain. State-based and behavior-based descriptions offer different ways to carry that argument across a larger language.

### CMP.12:11 - SoTA-Echoing

How should expression meaning become executable? **Adopt** the constructor-based evaluation and saved-environment application in [SICP's evaluator](https://sicp.sourceacademy.org/chapters/4.1.1.html) for :4.2–4.3. Its historical contribution is exposing operations otherwise hidden in a host language. A direct evaluator is a serious cheaper choice for changing or infrequently executed expressions. **Adapt** [SICP's compilation construction](https://sicp.sourceacademy.org/chapters/5.5.html) when prior analysis repays its cost over subsequent runs: construct operations instead of repeatedly selecting them during execution. Keep binding and control semantics while comparing conversion, code storage and later execution. A changed execution frequency, primitive or language feature reopens that choice.

Which preservation claim supports actual reuse? **Adopt** the explicit behavioral scope in the current [CompCert manual, section 1.2](https://compcert.org/man/manual001.html), for :4.1 and :4.5. Matching final values is sufficient only for uses governed by those values; interaction and termination can require more. CompCert's theorem has its own language-defined behavior and undefined-behavior treatment, and excludes time and memory consumption from its observed trace. A translator for a language with a defined division error therefore needs the error policy chosen in :5.3, not an imported C-specific permission to remove it. A changed observation or admitted execution context reopens the relation.

For larger compositions, **adapt** the choice between operational simulation and denotational behavioral refinement examined in [*Denotation-based Compositional Compiler Verification*](https://arxiv.org/html/2404.17297v1). The latter uses algebraic composition of behavioral sets to reduce proof duplication, while retaining termination, divergence, failure and interaction distinctions that simpler final-state accounts can lose. Use it when those operations fit the language and simplify the actual preservation argument; a direct structural or state correspondence remains sufficient for the small constructions here. Changed control features, module interaction or proof-maintenance cost can reverse the selection.

### CMP.12:12 - Relations

- **MATH.5, MATH.17 and MATH.18:** supply extension through expression construction, operations on operations and interpretation/composition arguments.
- **CMP.1:** supplies effective conversion and answer recovery for computational reductions; interpretation here also retains the required execution behavior.
- **CMP.2, CMP.3 and CMP.10:** supply recursive construction, sharing and computational representation choices used by an evaluator or translator.
- **CMP.8:** qualifies deliberate approximation of represented values.
- **CMP.15:** composes independently added expression variants and operations when new required combinations need their own implementation and preservation conditions. A sufficient closed interpreter does not require that extension architecture.
- **C.29.2 and C.29.3:** supply the surrounding computational formulation and physical realization questions.
- **C.11.DUA:** selects additional validation or proof by the conclusion it can change.

### CMP.12:End
