## CMP.15 - Compose Independent Extensions of Data Variants and Operations

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### CMP.15:1 - Problem frame

**Use this when** different contributors must add new forms of data and new operations on those forms without repeatedly changing one another's modules. An expression language may gain a binding construct while an independently developed analysis gains an operation for finding free variables. Each addition works with the old core; using the analysis on the new construct still needs a meaning and an implementation.

Start by choosing the combinations the receiving application must support. Find the first required combination whose implementation is absent or whose selection is unclear, and provide the joining contribution that knows both additions. The useful result is a composed set of operations with explicit coverage, selection rules and preservation conditions. A small composition can be assembled and examined directly; a promise about arbitrary future additions requires stronger interfaces and checking.

This method concerns computational data variants and operations. The reader can follow a recursive function and distinguish a data constructor from an operation that processes it. CMP.12 explains how to derive an interpretation and its correspondence with the intended meaning. The construction here keeps independently supplied additions composable.

Keep a closed representation and ordinary functions when one owner can maintain the required cases affordably. If only the data variants change, methods attached to those variants may suffice. If only the operations change, functions over a stable closed data type may suffice. Independent extension on both axes earns its additional machinery when those simpler arrangements obstruct actual changes.

### CMP.15:2 - Problem

How can independently added data variants and operations be used together while preserving established combinations, detecting unsupported or conflicting combinations, and keeping the cost of extension bounded?

A new data variant and a new operation create a possible intersection that neither author knew. An automatic loader can connect an existing implementation, but that intersection may have no implementation yet. A generic traversal can return a value of the right type while computing the wrong meaning. A new dispatch rule can also redirect an old call without changing any old source file. The construction must address these different failures instead of treating successful registration as sufficient composition.

### CMP.15:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Independent contribution and shared meaning | Contributors can avoid editing one another's modules, but someone must understand both sides of each required new intersection. |
| Openness and coverage | A receiving application needs known behavior for its admitted inputs; future contributions can introduce cases outside that promise. |
| Reuse and recursive reach | An old handler should remain reusable when a new form occurs below it, while recursive calls must reach the assembled implementation. |
| Early checking and late composition | Static interfaces can expose missing capabilities before execution; late selection permits further combinations and introduces visibility and loading conditions. |
| Extension and preservation | Adding a body is easy; showing that old calls still select equivalent behavior depends on the dispatch and effect model. |
| Flexibility and total cost | Generic interfaces, joining bodies, diagnostics and deployment can cost more than maintaining a closed set of cases. |

### CMP.15:4 - Solution

Construct the semantic intersection before relying on the mechanism that binds it. Use the same required combinations to choose a representation, assemble contributions, qualify their guarantees and compare a simpler alternative. CMP.15:5 develops one binding example in executable and typed forms; these are alternative realizations of the method.

#### CMP.15:4.1 - Select the two extension axes and required combinations

Name the data variants and the operations separately. For an expression language, `Literal`, `Variable`, `Add` and `Let` are variants; evaluation and free-variable analysis are operations. A variant description gives its fields and their meaning, including which fields contain further expressions and where a name is bound. An operation description gives its inputs, result and intended meaning.

Choose the receiving application before requiring every conceivable combination. An evaluator may accept `Let` while an exporter intentionally accepts only arithmetic expressions. That restriction can be adequate if inputs are checked before export and the unsupported case is reported. If the exporter promises the full language, the missing `Let` case is an unfulfilled obligation.

For finite sets of variants `V` and operations `O`, let `R` be the required pairs drawn from `O × V`. Obtain `R` from admitted inputs and reachable calls, not just the constructors seen at the roots of sample expressions. An old `Add` can contain a new `Let`. An operation can invoke another operation, so its dependencies may enlarge the required set. For mutually recursive operations, continue following these dependencies until no new required pair appears.

A conservative complete set is often cheaper than proving that a difficult pair is unreachable. When reachability depends on arbitrary program behavior, a small collection of successful runs does not settle it. Restrict the admitted input language, require an explicit capability before the call, or retain a checked failure before consequential effects. State which choice bounds the use.

Reuse adequate constructor meanings and operation rules. If these remain unclear, use CMP.12:4.1–4.2 to construct the interpretation; NOT.2 and NOT.3 supply expression structure and meaning when the notation itself is being designed. Return the resulting rules to this composition rather than inferring them from a dispatch key.

#### CMP.15:4.2 - Assign and provide the joining contribution

A data-extension author supplies the new variant and the operations that the extension promises. An operation-extension author supplies that operation for the variants it promises. For a required intersection unknown to both, one contributor who understands both agreements supplies the missing body. This can be either author or the application's integrator. The application must have a way to obtain that body; merely naming a future contributor leaves the combination unsupported.

The joining contribution contains an implementation and the grounds for using it: the accepted variant, operation meaning, required context, dependent operations and a case that distinguishes it from a plausible wrong implementation. Place it in a module that can depend on both additions without making either old module depend on its future users. The original contributions remain independently usable on their established cases.

Shared construction can replace many individually written bodies when its law applies. A structural fold, for example, combines results already obtained for children. It is useful when that summary suffices for the operation. Binding, control, object identity or effects can require additional information or a different recursion. Establish what the generic rule preserves before deriving a new intersection from it.

Check whether the implementation environment permits the intended contribution. Some languages restrict implementation of an externally defined interface for an externally defined type. A local wrapper, an explicit object containing the operations, or a contribution maintained by one interface owner can then provide the join. These choices change representation, calling conventions or maintenance; they do not remove the semantic obligation.

When the contributions will be supplied as independently maintained extensions, use SYSE.27 to arrange a reproducible contribution, its dependencies and its support. Bring that obtainable implementation back here. Package availability is necessary for execution but does not establish the meaning of its operations.

#### CMP.15:4.3 - Derive the new operation from the variant's meaning

Consider the nonrecursive lexical construct `Let(name, value, body)`. The value is evaluated in the incoming environment; the name is then bound locally while evaluating the body. The binding does not govern occurrences inside its own value expression.

Free-variable analysis returns the names with lexically free occurrences. It is not, in general, the smallest set of external values on which a particular execution depends. For the old forms its rules are:

```text
FV(Literal(k)) = {}
FV(Variable(n)) = {n}
FV(Add(a,b)) = FV(a) union FV(b)
```

To derive the missing rule, divide the occurrences by field. Every free occurrence in `value` remains free in the whole `Let`, because the new binding does not reach that field. In `body`, the new binding captures free occurrences of its own name; other free occurrences remain free. Therefore:

```text
FV(Let(n,v,b)) = FV(v) union (FV(b) minus {n})
```

For `let x = 2 in x + y`, the value contributes no free names and the body contributes `{x,y}`; removing the body's bound `x` leaves `{y}`. Unioning every child's result would return `{x,y}`. Both results are sets of names, so an ordinary result-type check cannot choose between them.

The location of the subtraction matters. For `let x = x + 1 in x + y`, the `x` in the value refers to the incoming environment. The whole expression has free names `{x,y}`. Subtracting `x` after unioning both fields would incorrectly return only `{y}`.

For another constructor, repeat this derivation from its rules. A recursive binding has different scope; a branch may require preserving which child is evaluated; a graph analysis may require identity and a fixed-point computation. Use the relevant CMP.12 interpretation or other supplied operation to obtain those facts, then implement the intersection. A common syntax shape alone does not justify copying this `Let` rule.

#### CMP.15:4.4 - Bind one applicable body and keep recursion open

Assemble contributions under an explicit selection rule. The simplest rule uses an exact pair `(operation, variant)`. Reject two bodies for the same pair unless the composition explicitly selects one before assembly. Silently letting the last loaded body win makes loading order a semantic decision.

If selection uses subtyping or predicates, determine which bodies apply and how one is chosen. No applicable body means missing support. Several applicable bodies can be acceptable when one is uniquely more specific under the declared rule; incomparable best candidates leave ambiguity. An explicit body for their intersection, a restriction of applicability or an explicit composition-level choice can resolve it. Each repair still needs a semantic justification.

For recursive data, pass recursive requests through the assembled operation. One simple interface is:

```text
run(operation, expression, context):
    body = select(operation, expression.variant)
    return body(run, expression, context)
```

The body receives `run` as its recursive entry. Thus an old `Add` handler can process a `Let` child using the new body selected by this composition. Calling a private old evaluator from that handler would close recursion over the old cases and defeat the extension. For an algebraic construction that receives already interpreted children, the parameterized algebra performs the corresponding composition during term construction; CMP.15:5.3 shows that alternative.

Connect dependencies between operations in the same manner. If an analysis calls a printer, choose which printer it uses, its required variants and the result it returns. Do not leave that dependency bound to an obsolete private implementation merely because a newer printer is present elsewhere in the application.

Keep the composed selection stable for the execution being qualified. With a copied exact-key table, later additions to a source collection need not alter that table. Shared mutable state inside a handler still can alter behavior. If the application replaces methods during an execution, qualify visibility and interaction through CMP.14 rather than assuming that a successful assembly settles them.

#### CMP.15:4.5 - Choose checking and binding conditions separately

Choose when contributions become connected and when the required obligations are checked. These are distinct decisions: dynamic composition can carry static constraints, and early registration can still leave semantic errors until execution.

| Needed guarantee | What must support it |
| --- | --- |
| Old source modules remain unchanged | The extension and joining modules use published interfaces; composition happens outside the old modules. |
| Modules can be checked and compiled separately | The language and build arrangement expose sufficient interfaces, constraints and dependency information without requiring all implementation sources together. |
| A required missing body is found before execution | A static capability requirement or a complete composition check covers the admitted combinations and their dependencies. |
| Old behavior is preserved | Old calls retain suitable bodies and assumptions, with an argument over the observations actually promised. |

A static realization can express each operation as an implementation of a constructor signature. A term using `Let` requires that extended signature. An implementation of only the old signature cannot be supplied to it without failing the relevant type requirement. CMP.15:5.3 gives the bodies and the rejected combination. This establishes availability and type compatibility only to the extent enforced by the chosen language; an unchecked cast can conceal the missing obligation. Correctly typed but wrong `FV(Let)` remains possible.

A dynamic realization can collect explicit bodies, reject conflicts and compare their keys with `R` before running any handler. Missing pairs then fail during composition rather than halfway through an effectful operation. The check is complete for `R`; it covers the application only if `R` covers its reachable uses. Guard calls outside that scope. Loading another extension requires constructing or qualifying another composition.

Keep three failures distinct:

| Failure | Diagnosis and useful repair |
| --- | --- |
| No applicable implementation | Supply the missing body, make an existing body available, or narrow the admitted use explicitly. |
| No unique selected implementation | Resolve the conflict or ambiguity by a stated selection, applicability or intersection rule. |
| One selected implementation returns the wrong meaning | Repair its semantic rule and dependent uses; availability and ordinary types have not established correctness. |

Malformed input, an unbound variable and a language-defined arithmetic error are errors of the represented language or its inputs. A loaded method that is not visible to the running computation is a binding or visibility issue. Diagnose those conditions separately from a missing semantic implementation.

The historical *expression problem* asks for stronger properties than practical plug-in loading alone, including static type safety and extension without recompiling existing code. [Wadler's formulation](https://homepages.inf.ed.ac.uk/wadler/papers/expression/expression.txt) supplies those comparison criteria. Use the name as a search cue; state which properties the actual construction achieves.

#### CMP.15:4.6 - Establish preservation on the promised old uses

Preserve the old meanings as well as the old files. For each established operation, compare which body an old input selects after extension and which dependencies that body invokes. A new, more specific method can redirect an old call in a subtype-based dispatcher. Disallow that override, explicitly retain the earlier selection, or treat it as a behavior change requiring its own correspondence.

For a pure tree interpreter with exact keys, a useful preservation argument is available. Suppose the old keys still select the same bodies, the old expressions contain only old constructors, and primitives, environments and dependent operations retain their meaning. A leaf obtains the same result. At a compound old node, induction gives the same child results, and the unchanged body combines them in the same way. Every finite old expression therefore retains its result. This argument depends on those premises; unchanged source text alone does not prove them.

Test a new form beneath an old constructor as a different obligation. It was not an old expression, so the preservation argument does not establish its new meaning. This case checks whether open recursion reaches the supplied intersection and whether the resulting composition obeys the new rules.

When effects, failures or concurrent replacement matter, use the observations and correspondence from CMP.12 and the interaction method in CMP.14. Preserving a returned number may leave an extra effect or a changed failure observable. Selected tests can expose such differences; a promise for an entire class of executions needs an argument at that scope.

#### CMP.15:4.7 - Bound the cost and retain the simplest adequate composition

Count the work that the architecture moves as well as the work it removes. Independent authors avoid editing a central list, but someone still writes or derives the required intersections, connects dependencies, diagnoses rejected compositions and supports the result. A generic derivation can reduce the number of bodies; its applicability and exception handling still have a cost.

For an exact-key table with `H` supplied bodies and `Q` required pairs, assembly and coverage checking take expected order `H + Q` dictionary operations and order `H` table storage. Each recursive dispatch adds an expected constant-time lookup under the hash-table assumptions. Count the bodies separately: free-variable analysis copies or unions sets, and evaluation may copy environments. With `N` visited nodes and at most `K` names in intermediate sets, straightforward set operations can cost order `N K`, rather than merely `N`. Large-integer arithmetic and representation conversion have their own costs.

A static representation can move selection into compilation or construct terms through operation dictionaries, but it can introduce interface complexity, generated instances, code size, specialization and build dependencies. A dynamic representation adds assembly, visibility, possible runtime failures and often indirect calls. Measure or derive the relevant total for the actual workload; neither label guarantees the cheaper execution.

Compare a closed alternative using the same required cases. For four stable variants, two fixed operations and one maintainer, two exhaustive functions may be easier to understand and maintain than a registry and its coverage description. They still need the correct `Let` rule. Conversely, repeatedly editing another team's module for each new operation or variant gives independent composition a concrete benefit. Use SYSE.23 when the broader engineering choice needs comparison of anticipated changes and their complete cost.

Stop with the smallest construction that provides the receiving application's operations under its admitted inputs and extension conditions. Retain explicit unsupported cases rather than implying a complete open world. Reopen the selection when a new required pair, operation dependency, binding rule, loading condition or change workload invalidates it.

### CMP.15:5 - Archetypal Grounding

#### CMP.15:5.1 - Find the absent intersection before connecting it

Start with integer expressions `Literal`, `Variable` and `Add`, together with evaluation. Contributor A adds nonrecursive lexical `Let` and its evaluation. Contributor B independently adds free-variable analysis for the original forms.

| Variant | Evaluation after A's extension | Free-variable analysis after B's extension |
| --- | --- | --- |
| Literal | Return its integer. | Return the empty set. |
| Variable | Look up its name in the incoming environment. | Return its name as a singleton set. |
| Add | Evaluate both children and add their values. | Union the children's free-name sets. |
| Let | Evaluate the value in the incoming environment, then the body with one local binding. | Not yet supplied. |

If the application accepts all four variants for both operations, seven available bodies leave one required pair absent. The joining contributor derives the eighth body as in CMP.15:4.3. For `let x = 2 in x + y`, evaluation under `y = 4` is 6 and free-variable analysis is `{y}`.

Changing the question to evaluation alone makes the seven-body composition sufficient for that operation. This is a legitimate narrower use, not a repair of the still-unsupported analysis. Changing the binding to recursive `Let` reopens both its evaluation and free-variable rule.

#### CMP.15:5.2 - Assemble and run the contributions with exact keys

The following Python 3 example is a complete small realization for finite, well-formed expression trees. Tuple tags stand for already parsed constructors. It has no parser, effects, method replacement or static type checking. Environments are maps from names to integers; missing names raise `UnboundName`. Set-valued results are compared by membership.

Each contribution is a sequence of explicit bodies. The assembler copies them into a private table, rejects repeated keys and checks any declared required pairs before invoking a handler.

```python
class MissingCase(Exception):
    pass

class MissingCoverage(Exception):
    pass

class ConflictingCase(Exception):
    pass

class UnboundName(Exception):
    pass

def lookup(environment, name):
    if name not in environment:
        raise UnboundName(name)
    return environment[name]

def compose(*contributions, required=()):
    bodies = {}
    for contribution in contributions:
        for operation, variant, body in contribution:
            key = (operation, variant)
            if key in bodies:
                raise ConflictingCase(key)
            bodies[key] = body
    missing = set(required) - bodies.keys()
    if missing:
        raise MissingCoverage(frozenset(missing))

    def run(operation, expression, environment=None):
        key = (operation, expression[0])
        if key not in bodies:
            raise MissingCase(key)
        context = {} if environment is None else environment
        return bodies[key](run, expression, context)
    return run

base = [
    ("eval", "lit", lambda r, e, env: e[1]),
    ("eval", "var", lambda r, e, env: lookup(env, e[1])),
    ("eval", "add",
     lambda r, e, env: r("eval", e[1], env) + r("eval", e[2], env)),
]
data_extension = [
    ("eval", "let",
     lambda r, e, env:
         r("eval", e[3], {**env, e[1]: r("eval", e[2], env)})),
]
operation_extension = [
    ("free", "lit", lambda r, e, env: set()),
    ("free", "var", lambda r, e, env: {e[1]}),
    ("free", "add",
     lambda r, e, env: r("free", e[1]) | r("free", e[2])),
]
joining_contribution = [
    ("free", "let",
     lambda r, e, env: r("free", e[2]) | (r("free", e[3]) - {e[1]})),
]
wrong_join = [
    ("free", "let",
     lambda r, e, env: r("free", e[2]) | r("free", e[3])),
]

old = ("add", ("lit", 2), ("var", "x"))
term = ("let", "x", ("lit", 2),
        ("add", ("var", "x"), ("var", "y")))
required = {
    (operation, variant)
    for operation in ("eval", "free")
    for variant in ("lit", "var", "add", "let")
}

baseline = compose(base)
partial = compose(base, data_extension, operation_extension)
assert baseline("eval", old, {"x": 3}) == 5
assert partial("eval", term, {"y": 4}) == 6

try:
    partial("free", term)
except MissingCase as error:
    assert error.args[0] == ("free", "let")
else:
    raise AssertionError("The absent body was not reported.")

try:
    compose(base, data_extension, operation_extension, required=required)
except MissingCoverage as error:
    assert error.args[0] == frozenset({("free", "let")})
else:
    raise AssertionError("Coverage checking admitted an absent pair.")

incorrect = compose(base, data_extension, operation_extension,
                    wrong_join, required=required)
assert incorrect("free", term) == {"x", "y"}

complete = compose(base, data_extension, operation_extension,
                   joining_contribution, required=required)
assert complete("free", term) == {"y"}
assert complete("eval", term, {"y": 4}) == 6
assert complete("eval", old, {"x": 3}) == baseline("eval", old, {"x": 3})

embedded = ("add", term, ("var", "x"))
assert complete("eval", embedded, {"x": 10, "y": 4}) == 16
assert complete("free", embedded) == {"x", "y"}

outer_name = ("let", "x",
              ("add", ("var", "x"), ("lit", 1)),
              ("add", ("var", "x"), ("var", "y")))
assert complete("eval", outer_name, {"x": 10, "y": 4}) == 15
assert complete("free", outer_name) == {"x", "y"}

shadowed = ("let", "x", ("lit", 2),
            ("let", "x", ("add", ("var", "x"), ("lit", 1)),
             ("add", ("var", "x"), ("var", "y"))))
assert complete("eval", shadowed, {"y": 4}) == 7
assert complete("free", shadowed) == {"y"}

try:
    compose(base, data_extension, operation_extension,
            joining_contribution, wrong_join, required=required)
except ConflictingCase as error:
    assert error.args[0] == ("free", "let")
else:
    raise AssertionError("Two bodies for one pair were accepted.")
```

The absent pair can be found at use or, when `required` is supplied, during assembly. The wrong join passes coverage and returns a set, yet fails the semantic requirement. Supplying both joins fails before any handler runs. These are three different outcomes.

An operation can also depend on another operation rather than only on its own recursive calls. Suppose `IsClosed(e)` asks whether `FreeVariables(e)` is empty. For each admitted variant, its body calls the assembled free-variable operation: `lambda r, e, env: not r("free", e)`. The required set for this use contains both `IsClosed` and `FreeVariables` on all four reachable variants; evaluation is unnecessary. Supplying every `IsClosed` body without `FreeVariables(Let)` must therefore fail coverage before execution. This dependency closure is chosen from the bodies' calls; the assembler does not infer it.

For `let x = 2 in x`, the correct free-variable join returns the empty set, so `IsClosed` returns true. The wrong union returns `{x}`, so `IsClosed` returns false even though all required bodies are present. Both the missing dependency and the wrong meaning propagate into the receiving operation. Calling a private older analysis would evade the selected join instead of repairing either failure.

The `embedded` case sends a new `Let` through an unchanged `Add` body. Its sibling variable `x` still reads the outer value 10 because the `Let` handler extends a copy of its incoming environment. The `outer_name` and `shadowed` cases distinguish the binding rules: the value expression sees the incoming binding, while the body sees the new one.

For this grammar, all recursive calls stay within the declared eight pairs. Coverage checking therefore settles absence for these two operations over well-formed trees of the four constructors. It establishes neither the meaning of a body nor static type safety. Arbitrary supplied Python functions could mutate external state or call other operations; those would need an enlarged dependency account and preservation conditions. The induction in CMP.15:4.6, rather than the finite assertions alone, explains preservation for all old trees under the stated pure semantics.

#### CMP.15:5.3 - Express the same obligation through a typed signature

A static alternative represents a term by its use of constructor operations. Instead of first constructing a stored tree and then dispatching on it, the term receives an algebra: a collection of constructor functions whose common result type `R` is chosen by the interpretation.

The notation below is typed pseudocode. `Base<R>` and `LetPart<R>` are records of functions; `&` requires both sets of fields. It specifies the constraints a realization must enforce.

```text
Base<R> = {
    literal: Integer -> R,
    variable: Name -> R,
    add: (R, R) -> R
}
LetPart<R> = {
    let_: (Name, R, R) -> R
}

old<R>(a: Base<R>): R =
    a.add(a.literal(2), a.variable("x"))

extended<R>(a: Base<R> & LetPart<R>): R =
    a.let_("x", a.literal(2),
           a.add(a.variable("x"), a.variable("y")))

withLet<R>(base: Base<R>, part: LetPart<R>):
        Base<R> & LetPart<R> =
    {literal = base.literal, variable = base.variable,
     add = base.add, let_ = part.let_}
```

For evaluation, choose `R = Environment -> Integer`. The result of constructing each subexpression is a function awaiting its environment. This delays lookup until the expression's binding context is known. Let `extend(env,n,k)` return a new environment that maps `n` to `k` and otherwise agrees with `env`.

```text
evalBase: Base<Environment -> Integer> = {
    literal = k -> (env -> k),
    variable = n -> (env -> lookup(env,n)),
    add = (f,g) -> (env -> f(env) + g(env))
}
evalLet: LetPart<Environment -> Integer> = {
    let_ = (n,v,b) -> (env -> b(extend(env,n,v(env))))
}
```

For free-variable analysis, choose `R = Set<Name>`:

```text
freeBase: Base<Set<Name>> = {
    literal = k -> {},
    variable = n -> {n},
    add = (a,b) -> a union b
}
freeLet: LetPart<Set<Name>> = {
    let_ = (n,v,b) -> v union (b minus {n})
}

old(freeBase) = {"x"}
extended(withLet(freeBase, freeLet)) = {"y"}
extended(withLet(evalBase, evalLet))({y = 4}) = 6
```

The expression `extended(freeBase)` lacks the required `let_` field and is rejected in a realization that enforces these record constraints. The operation author can keep `freeBase` unchanged; the joining contributor supplies `freeLet`, and the application assembles them with `withLet`. A wrong `freeLet` returning `v union b` has the required type, demonstrating the same semantic limit as the dynamic example.

Here `withLet` copies only the old constructor functions and supplies one new field, so it does not silently override an old field. A richer composition with overlapping signatures needs its own explicit selection rule. Interface union alone does not combine implementations. The chosen language must also support any promised separate compilation; satisfying these mathematical signatures does not establish how a build system handles dependencies.

This representation suits operations expressible through the supplied constructor algebra. Context-sensitive evaluation works because its result is an environment-taking function. An operation needing raw child identity, multiple interacting analyses or cyclic data can need richer results, additional operations or a different representation. Previously serialized trees require a reader that recognizes the extended syntax and applies the right constructor functions; adding `LetPart` does not update an old parser.

#### CMP.15:5.4 - Stop when independent extension has no useful payoff

Suppose a private calculator has the same four constructors and two operations, and one maintainer changes them together. A closed tagged data type with an exhaustive evaluation function and an exhaustive free-variable function makes every required case visible. Adding `Let` means editing those two functions, deriving exactly the same binding rule and checking the new cases.

That arrangement loses independent addition without edits, but the application does not require it. A registry, separate contribution interfaces and loading rules would add work without removing an actual obstacle. Keep the closed design.

If a separately maintained analyzer must later add an operation while another team extends the expression language, repeat the comparison. The new independent change requirement can justify interfaces and an external joining module. It still leaves that module's semantic body to be supplied.

### CMP.15:6 - Bias-Annotation

The worked construction favors explicit finite syntax and pure operations because their dispatch and preservation can be inspected directly. Opaque foreign data, cyclic structures, effects and live method replacement need additional representation or interaction arguments. Do not transfer the tree induction to them solely because their implementation also uses handlers.

The method also makes integration work visible. Contributors who each test only their own extension can underestimate the cost of intersections that appear only in the receiving application. Conversely, anticipated openness can be overvalued when stable requirements make a closed representation adequate.

### CMP.15:7 - Conformance Checklist

- The data variants, operation meanings and admitted receiving uses determine the required combinations, including nested forms and dependent operations.
- Every required new intersection has an obtainable body or an explicit unsupported-use boundary; its supplier understands both sides.
- Generic derivation is justified by the operation's meaning, with binding, control or identity distinctions retained where material.
- The composition defines selection, reports missing support and rejects or resolves conflicts without accidental loading-order semantics.
- Recursive and dependent calls reach the implementation selected for the composition.
- Unchanged sources, separate checking and compilation, early coverage and behavior preservation have distinct stated grounds.
- A semantic counterexample can distinguish a present, uniquely selected but wrong body from a correct one.
- Old-use preservation covers the promised observations and assumptions; a new form below an old constructor is exercised separately.
- The full cost is compared with an adequate closed alternative, and a changed required pair or binding condition has a clear return.

### CMP.15:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Useful correction |
| --- | --- | --- |
| Register first, assume the new intersection exists | Neither independent author necessarily supplied the joint case. | Identify and obtain the joining body before qualifying the combination. |
| Fold every child by default | Binding or control can change how child results contribute. | Derive the rule from the constructor and operation meanings. |
| Recurse through the old private evaluator | A new form works at the root but fails under an old constructor. | Route recursive calls through the assembled operation. |
| Let import order select behavior | Deployment changes can silently change meaning. | Reject duplicate keys or make selection explicit. |
| Treat a successful lookup as correctness | A unique body can return a well-typed wrong result. | Use distinguishing semantic cases and a scope-appropriate argument. |
| Equate unchanged files with unchanged behavior | New dispatch rules or dependencies can redirect old calls. | Compare selection and observations on established uses. |
| Promise arbitrary future combinations from today's coverage check | Future variants and operation dependencies were not included. | Qualify the declared set and reassemble when it changes. |
| Buy openness for an unchanged closed problem | The extra interfaces and support have no receiving benefit. | Retain the exhaustive closed construction while it suffices. |

### CMP.15:9 - Consequences

Independent additions can remain useful without edits to their original modules, while the receiving application chooses the combinations it supports. Missing and conflicting combinations become diagnosable at a stated point. Semantic joining work has an explicit location instead of being hidden in a loader or left to each user.

The price is additional interfaces, composition and qualification. Static checking can move some failures earlier; dynamic composition can admit later choices. Neither removes the need to establish the operation's meaning. A closed design remains a valid result when its total change cost is lower for the actual use.

### CMP.15:10 - Architectural Rationale

The two-axis construction separates knowledge that can evolve independently from knowledge that must meet. A variant author knows the new form's structure; an operation author knows the analysis or transformation. Their future intersection becomes implementable when one contribution can use both. Keeping that contribution outside the old modules preserves their original dependency direction without pretending that the new meaning follows automatically.

The receiving composition bounds the promise. Requiring every possible pair would overstate some applications and make useful partial support expensive. Checking only examples would understate applications that admit arbitrary trees. The required set and its recursion dependencies connect those alternatives to the actual input language.

Exact-key dispatch is the simplest realization in the executable example because it makes absence, conflict and preservation easy to inspect. Subtyping and algebraic interfaces can remove other burdens but require their own resolution or typing conditions. The method therefore selects guarantees independently of binding time.

The semantic rule remains necessary under every realization. The wrong free-variable body passes ordinary type, presence and uniqueness checks in both examples. The explicit derivation and binding variations supply what those checks omit. CMP.12 remains the source of interpretation construction; this method organizes independently supplied extensions of that construction. CMP.14 becomes necessary when effects or changing visible methods alter the composed observations.

### CMP.15:11 - SoTA-Echoing

**How can both axes extend while missing capabilities remain visible?** For a language representable through constructor functions, **adapt** object algebras and typed tagless-final interpretation as the static line used in CMP.15:5.3. [Oliveira and Cook, 2012, sections 5 and 7](https://www.cs.utexas.edu/~wcook/Drafts/2012/ecoop2012.pdf), supplies parameterized constructor signatures and explicit combination of implementations; [Kiselyov, sections 2.2–2.3](https://okmij.org/ftp/tagless-final/course/lecture.pdf), exposes the missing interpretation through constraints and treats deserialization separately. A closed data type with exhaustive functions is the serious cheaper alternative when independent changes are unnecessary. The selected construction removes obligatory edits to a central case definition while retaining explicit new bodies. Reconsider it when raw structure access, cyclic data or interface complexity defeats the chosen representation.

**Can later composition retain static guarantees?** **Adapt** the separation of binding time from checking time in modern compositional programming. [Ye, Sun and Oliveira, 2024](https://yzsun.me/files/ICP-paper.pdf), develops operation dependencies and explicitly supplied extensions for imperative analyses. [Sun, Huang and Oliveira, 2025, sections 3.4 and 6.6](https://yzsun.me/files/CPC-paper.pdf), combines dynamic inheritance through merging with static checking and an implementation of separate compilation through interfaces. These are current research alternatives to treating every late-bound registry as the only open design. They motivate the independent guarantees in CMP.15:4.5; their language proofs do not prove arbitrary user operations correct, and the latter paper distinguishes the core formalization from further implementation features. Reopen a concrete realization when tool support, required effects or compilation obligations differ from those the chosen language supplies.

**How should overlapping bodies be resolved?** **Adopt** explicit resolution rather than import-order selection in CMP.15:4.4. The [Julia method documentation](https://docs.julialang.org/en/v1/manual/methods/) supplies a practical comparator: incomparable applicable methods need a disambiguating method, and newly defined methods have execution-visibility conditions. The exact-key table deliberately uses the simpler rule of rejecting duplicates. [Xu, Huang and Oliveira, 2025](https://sec-r.github.io/papers/oopsla25apartness.pdf), supplies a serious research alternative to rejecting all overlap: apartness and guarded subtyping permit overlap that remains distinguishable at use. Those mechanisms still require supplied behavior. Compare again when useful compositions are rejected by the simpler rule or when a new method changes an established call.

**How does an independent join become available?** **Adapt** explicit extension modules from the current [Julia package-extension mechanism](https://pkgdocs.julialang.org/v1/creating-packages/#Conditional-loading-of-code-in-packages-(Extensions)) as a dynamic realization of CMP.15:4.2 and CMP.15:4.5: dependency triggers load already authored code. This improves availability; it does not construct a missing semantic intersection. A static application assembly remains a cheaper alternative for a fixed set. The [Rust coherence rules](https://doc.rust-lang.org/reference/items/implementations.html#trait-implementation-coherence) supply a limiting comparator: foreign-interface and foreign-type combinations are restricted, so a wrapper, explicit dictionary or owner-supported contribution may be necessary. Reopen the packaging choice when ownership, compatibility or visibility changes. These sources describe mechanisms, not production guarantees for an arbitrary assembled application.

### CMP.15:12 - Relations

- **CMP.12:** use its interpretation rules and correspondence argument when deriving a body or qualifying preserved behavior; return those results to the chosen composition.
- **CMP.14:** use its interaction construction when handlers share state, produce effects or change visibility during execution. Pair coverage alone leaves those observations unresolved.
- **CMP.2 and CMP.10:** supply recursive construction and representation cost analysis when the extension changes decomposition, storage or access.
- **NOT.2, NOT.3 and NOT.4:** supply expression structure, meaning and permitted transformations when a notation is being designed; the computational implementation here consumes those rules.
- **SYSE.23:** compares the engineering value and full cost of changeability when choosing an open architecture.
- **SYSE.27:** supplies the reproducible extension contribution and support arrangement when separately maintained modules are needed; the joining semantics remains the computational work described here.

### CMP.15:End
