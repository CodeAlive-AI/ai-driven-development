## MMP.10 - Construct and Revise a Mathematical Constraint Formulation

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative within the stated use

### MMP.10:1 - Problem frame

Use this pattern when you know conditions that a possible object or situation must satisfy, but still need to express its possibilities mathematically. You may be looking for an arrangement, a quantity, a shape or a rule of action. Choosing variables already makes decisions: a number can express an amount, but an ordered list, a set of members and an unknown function permit different operations and different possible answers.

Start by describing one candidate object and what would make it admissible. Choose a way to represent it, then distinguish two kinds of condition: those needed for the representation to denote such an object, and those expressing the requirements on that object. This produces a mathematical problem that can be reasoned about or handed to an appropriate computational method.

The result consists of variables with their domains, joint conditions, the requested operation on their solutions and a way to interpret the answer. It can be enough to find one feasible case; another question may require all possible values, a preferred case or a count. The chosen representation must support that particular result.

You need to understand the objects and requirements in the original question, elementary logical conditions and the mathematics used to express them. A mathematical collaborator can construct the expressions while you resolve their intended meaning. When a suitable formulation already exists, use it. When the missing contribution is a physical relation, an observation law or a rule of change, obtain that relation through the relevant method before translating it. B.5.FM supplies the broader first-model construction; MMP.7 and MMP.9 develop observation and reduced-evolution constructions.

### MMP.10:2 - Problem

A convenient variable can leave out the possibility that matters. A single interval cannot represent an activity that may pause. A membership bit cannot record repeated membership. Coefficients of a straight line cannot describe every continuous curve. These restrictions may be useful, but they change which cases the formulation can answer for.

Representation can also add possibilities. A table intended to describe a function can allow two values for one argument unless its conditions exclude that case. Extra fields can create several records of the same object. A calculation over those records can then answer a different counting or probability question.

The difficulty is to construct the mathematical expression of the intended possibilities, including their joint restrictions and the requested result. Solving the resulting equations addresses the problem only after that construction has been made.

### MMP.10:3 - Forces

| Force | Consequence for the construction |
| --- | --- |
| Faithful possibilities and useful operations | A familiar representation may make calculation easy while excluding an intended case or hiding a useful relation. |
| Structured objects and scalar tools | A function, set or sequence may need several scalar variables and additional conditions to represent its structure. |
| Shared restrictions and local descriptions | Separate bounds on individual variables can lose a condition on their combination. |
| Simple answer and rich solution set | A single witness needs less from the representation than counting, sampling or claiming that no witness exists. |
| Reuse and changed requirements | A derived constraint that helped an earlier formulation may exclude valid cases after the requirement changes. |

### MMP.10:4 - Solution

**Describe the possible object → choose its representation → derive the representation conditions → express the requirements and question → obtain and interpret a result → revise the affected construction.**

#### MMP.10:4.1 - Recover what varies and what the question asks

Describe a candidate before choosing scalar variables. Is it an amount, a collection, a sequence, an assignment, a function or another mathematical object? Which distinctions can change the answer? A set retains membership; a multiset also retains multiplicity; a sequence retains positions. Choose among them from the question.

Separate supplied quantities from unknowns. Among unknowns, distinguish what is to be inferred, what can be chosen and what can vary independently of that choice. If a choice uses an observation, specify when the observation becomes available; MMP.8 constructs the resulting information-dependent requirement. An unknown value does not become a freely selectable design variable merely by appearing in the same equation.

State the requested result. Existence asks whether at least one admissible object can be constructed. Inference asks what a quantity can be across admissible objects. Selection adds a preference among them. Counting and sampling depend on how individual objects are distinguished. Keep those requests separate while choosing the representation.

#### MMP.10:4.2 - Construct variables that represent the object

Choose an expression from which a candidate can be recovered. Give each variable a domain and any unit or reference point needed by its operations. A machine label ranges over names; arithmetic on the label requires a separate meaning. A count ranges over nonnegative integers; an amount may be divisible. State a finite bound when the task supplies one. Adding a bound solely to finish a search restricts the question to that bound.

For a structured object, compare representations by the operations you need. A function on a finite set can use one output variable for each input. Alternatively, a table of Boolean indicators can say which input-output pairs belong to its graph. The first expression makes function evaluation easy to state. The second makes some relations among pairs visible, but needs conditions to make the table a function. For a partial function, represent undefinedness as well as defined values.

Keep a shared quantity shared. If several equations use the same unknown offset, one offset variable must occur in all of them. Introducing a separate offset in each equation creates additional possibilities. Conversely, equating genuinely separate values can remove possibilities.

For a function or shape over an infinite domain, choosing finitely many coefficients also chooses a family. Identify that family and whether it expresses the intended possibilities or is a deliberate restriction. For example, the conditions on a continuous function may allow curved solutions even when no affine function satisfies them. A useful restricted family can be sufficient for finding a witness; failure inside it leaves the larger family unresolved.

#### MMP.10:4.3 - Derive structural conditions and translate requirements

Ask what must hold for a variable assignment to describe one candidate of the intended kind. With Boolean entries `r_ij` describing the graph of a total function, require `sum_j r_ij = 1` for every input i. For a partial function, replace this with `sum_j r_ij <= 1`; an all-zero row then means undefined at that input. For an injective function, additional conditions on columns express the extra requirement.

These conditions have different reasons. One value per input comes from choosing a total function. Injectivity comes from the particular problem, if it requires injectivity. Keep their reasons recoverable so that a later change from total to partial or from injective to unrestricted has a local repair.

Express the original requirements using the represented objects. Conjoin conditions that must hold for the same assignment. Use disjunction for allowed alternatives and implication when choosing an option imposes a condition. An implication alone supplies no timing; use time quantities or an explicit sequence when order matters. Preserve a coupled condition such as `x+y=1` rather than replacing it by separate bounds on x and y.

When a bijection between representations is established, MATH.7 supplies transport of operations, relations and compound expressions. For a representation with several records per object, C.29.1 supplies the more general correspondence. Use the decoding of a record to express the requirement on its object. If a condition is rewritten to fit the receiving notation, derive that expression from the original relation and the structural conditions. This is where a missing index, an undefined value or a lost alternative can change the formulation.

Additional constraints can expose consequences and help the obtaining method. Derive them from the retained requirements, and preserve that dependence. Fewer variables or more constraints do not alone establish a faster method; compare the actual resulting work when efficiency matters.

#### MMP.10:4.4 - Make the answer correspond to the question

Define how to recover the requested object or quantity from a satisfying assignment. Then work in both directions: represent an intended admissible case, and interpret an allowed assignment. Use the construction and its conditions to establish the reach of this correspondence. A small case can expose a mistake; a claim about every case needs the corresponding argument.

Match that reach to the requested result:

- To use a witness, its recovered object must satisfy the original requirements.
- To conclude that no intended object exists from inconsistency of the formulation, every intended object must have a representation in it.
- To infer all possible values, translate the quantity as well as the admissible cases; C.16.IR supplies the projection question.
- To optimize, translate the objective and preference as well as feasibility. Distinguish a bound from a value attained by an object.
- To count or sample objects, account for multiple representations of the same object. One representation per object is one solution; weighting or grouping representations can be another.

Auxiliary variables can change what a returned number means. Suppose a finite nonempty set of finish times `f_i` is determined by the other variables. Introduce a real auxiliary T used only in `T >= f_i` and the objective of minimizing T. Lowering T to `max_i f_i` then preserves feasibility, so at an attained optimum T equals the latest finish. If T must instead be an integer and the latest finish is 1/2, its minimum is 1. A merely feasible intermediate T can also exceed the latest finish. Recover the actual latest finish as `max_i f_i`; infer equality with T only when its domain and other conditions permit that lowering.

Choose an obtaining method for the constructed question. Manual substitution may suffice; another problem needs a numerical method, symbolic derivation or search. C.29.2 separates the required mathematical result from the procedure and its execution. Use that method's actual conclusion: finding no case within a time budget differs from establishing inconsistency. Preserve any restriction or approximation when returning the result to the original question through C.29.1.

#### MMP.10:4.5 - Revise the formulation from the changed requirement

Locate the changed participant, domain, relation or requested result. Changing a supplied amount can retain the same representation. Allowing interruptions changes what an activity description must express. Changing a total function to a partial one changes structural conditions. Changing existence to counting can make duplicate records material.

Revisit constraints derived from the old requirement as well as the original formula. Reconstruct the affected expressions and answer interpretation, retaining the unaffected ones. If a solving tool cannot support the needed object, construct a suitable representation or choose another obtaining method; keep any deliberate restriction visible in the returned conclusion.

Stop with a usable formulation and interpretation, an adequate answer, or a named missing relation or operation. Choose further derivation, observation or computation according to what it can change in the work and its cost; C.11.DUA supplies that decision. When the formulated object is itself a working method, use MMP.22 when the mathematical transformation still needs to be reconstructed as a working rule, then return the candidate to C.32.MWA.PP for practical comparison and A.3.1.MV where it changes a reusable Method. The mathematical model supplies a reason for the change; the working method still has to be performed under its stated conditions.

### MMP.10:5 - Archetypal Grounding

#### MMP.10:5.1 - Construct an unknown rule from requirements on its repetitions

A device has three labeled modes A, B and C. The required rule changes the mode on every use and returns to the starting mode after three uses. The question is to construct a deterministic rule, with no additional internal state. The rule itself is the unknown object.

Let `S={A,B,C}`. Choose one output variable `p_i in S` for each input i. The requirements become `p_i != i` and `p_(p_(p_i)) = i` for every i. Function composition gives the meaning of the repeated application. MATH.1 constructs composable paths; MATH.5 extends an interpretation of their elementary steps to the compounds.

To express the rule by selected pairs instead, choose `r_ij in {0,1}`. Add `sum_j r_ij=1` for each row, `r_ii=0`, and, for all i,j,k, `(r_ij=1 AND r_jk=1) implies r_ki=1`. The row condition makes a function. The implication expresses the return after three uses: the first two selected transitions determine a required third.

Recover p by taking the unique selected column in each row. Conversely, p creates the table by selecting exactly its output pair in each row. These constructions are inverse. The triple-application requirement is therefore the same in both formulations, with MATH.7 carrying that relation. A rule A→B→C→A and its reverse both satisfy it.

There are precisely two such rules. From `p^3=id`, p is invertible with inverse `p^2`. Its cycles have lengths dividing three. Since a one-element cycle is forbidden, the three modes form one three-element cycle, with two possible orientations. This reasoning proves completeness; listing two examples alone would not.

Change the device to four modes, retaining the three-use return and no unchanged mode. A permutation of four elements cannot partition them into cycles all of length three, so no rule exists under these conditions. Change instead to a return after two uses. The conditions become `p_(p_i)=i` and `p_i!=i`; the indicator formulation requires symmetry `r_ij=r_ji`. It admits three pairings of four modes. Remove the former three-use implication: leaving it in the formulation would make the new, feasible requirement appear impossible.

The result is a rule that can be implemented and its stated scope: deterministic changes of the visible mode without hidden state. A proposal with additional state describes a different device and needs a new account of its operation.

#### MMP.10:5.2 - Preserve existence while repairing a count

An optional assignment gives each of two named requests either no selected option or one of options 0 and 1. Different requests may select the same option. This is a partial function from the two requests to `{0,1}`. Each request has three possibilities, so there are nine assignments.

Suppose the storage format gives each request two bits: d says whether an option is defined, and q gives its value when defined. When `d=0`, q is ignored. All sixteen four-bit records denote valid partial assignments. Every assignment has a record, so the representation can support an existence query with translated requirements.

It does not preserve the count. The empty assignment has four records, each of the four assignments defined on exactly one request has two records, and each of the four total assignments has one record. Thus `4 + 4*2 + 4 = 16`. Uniform selection among records gives probability `4/16` to the empty assignment and `1/16` to each total assignment, rather than the `1/9` obtained by uniform selection among assignments.

For a count or uniform assignment sample, one repair is the structural condition `d=0 implies q=0` for each request. There are now three admissible bit pairs per request and nine records, one per assignment. Another is a single variable with domain `{absent,0,1}` per request. If the sixteen-record storage representation must remain, group or weight its records using the multiplicities instead. To sample the nine assignments uniformly, give each record of an assignment with m records probability `1/(9*m)`. The probabilities of all m records then sum to `1/9` for that assignment. Thus each record of the empty assignment receives `1/36`, each record of a one-request assignment `1/18`, and each total-assignment record `1/9`. C.29.1 supplies the required correspondence; MMP.7 supplies a probability law when sampling is the intended operation.

The original existence use can remain sufficient. The new count or sampling question exposes the need for the additional construction. No change in the underlying possible assignments is intended.

#### MMP.10:5.3 - Keep quantities and domain restrictions together

A preparation requires one litre containing 35 percent solute by volume, using solutions A and B at 20 and 80 percent. Assume solute is conserved and component volumes add in this preparation. Those subject assumptions supply the relations. Let x and y be the respective volumes in litres; choose nonnegative real domains because the amounts can initially be divided freely.

The joint conditions are `x+y=1` and `0.2*x+0.8*y=0.35`. Substitution gives `x=0.75`, `y=0.25`. Both the total and solute requirements hold for those amounts. Separate bounds `0<=x<=1` and `0<=y<=1` would lose their required total.

Now only whole half-litre doses may be used. Change the representation to `x=m/2`, `y=n/2`, with nonnegative integers m and n. The volume equation becomes `m+n=2`. Its possibilities `(m,n)=(2,0),(1,1),(0,2)` give solute amounts 0.2, 0.5 and 0.8 litre. None supplies 0.35 litre. Rounding the former solution changes the preparation; it does not satisfy its original condition.

If the required concentration changes to 50 percent, one dose of each solution works. The subject relations and unit remain, while the requirement and feasible assignment change. If mixing changes volume or solute, obtain the replacement subject relation before revising its mathematical expression.

### MMP.10:6 - Bias-Annotation

Tool familiarity can make scalar variables appear inevitable and conceal a different object or useful operation. Begin with the candidate object and its requirements. Compare representations when that comparison can change the answer or obtaining effort.

Compactness can hide duplicate records or omitted possibilities. Judge the representation by the requested result and the work needed to obtain it.

### MMP.10:7 - Conformance Checklist

- Can the reader identify a candidate object before interpreting the variables, including what is supplied, unknown or selectable?
- Do domains, units, shared quantities and definedness express the intended possibilities?
- Which conditions make the representation denote an object, and which express requirements on it?
- Do conditions that must hold together refer to the same assignment? Are alternatives and conditional restrictions preserved?
- Can intended cases be represented and satisfying assignments be interpreted at the reach required by the question?
- Does the requested value, preference, count or probability survive the representation, including auxiliary values and duplicate records?
- What does the obtaining method actually establish, and which changed requirement reopens which construction?

### MMP.10:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Why it changes the result | Repair |
| --- | --- | --- |
| Use separate bounds in place of a joint relation. | The same assignment can violate the lost total or coupling. | Retain the relation with its shared variables. |
| Number labels and use their arithmetic as a subject law. | Addition or order on the labels may describe no operation on the labeled objects. | Supply the intended operation or use names as names. |
| Read an empty restricted search as absence in the original problem. | Intended cases may lie outside the chosen bound or family. | Return the restricted conclusion or extend the representation. |
| Count records as objects after adding auxiliary fields. | Multiple records can describe one object and alter the count or sampling law. | Canonicalize, group or weight by the needed correspondence. |
| Keep a consequence of a replaced requirement. | It can remove the newly allowed cases, as in the changed rule in :5.1. | Re-derive the affected constraints. |

### MMP.10:9 - Consequences

The mathematical problem becomes available for reasoning, computation and revision without leaving the interpretation of its variables implicit. A solver result can be returned as the arrangement, quantity or unresolved distinction that the work needs.

Constructing and maintaining a second representation has a cost. Direct formulation is often sufficient when the objects and their restrictions already have a clear expression. A structured intermediate formulation becomes useful when it preserves meaning across several receiving notations, helps revise requirements or exposes a calculation that the first representation hid. Any efficiency advantage depends on the resulting obtaining method.

### MMP.10:10 - Architectural Rationale

Mathematical modeling often starts with choosing how possible objects will be expressed. The choice determines which restrictions must be added and which results can be recovered. Separating representation conditions, subject requirements and the operation on solutions makes revisions local: a changed requirement need not replace the representation, and a new representation need not change the intended possibilities.

An operation can itself be the unknown object. The finite-rule case therefore treats repeated action as a requirement on a function and uses composition to express it. The same organization applies to other structured objects, while their mathematics supplies the needed constructions and proofs. MATH.7 explains reversible transport after the maps are available; this pattern develops the modeling choice and construction of those expressions, including cases that need a many-to-one correspondence.

The connection to computation runs in both directions. A mathematical formulation supplies the problem a procedure must answer. The operations supported by a procedure can suggest a different expression of that problem. Meaning is retained through the representation conditions and answer interpretation, while performance is judged on the resulting work.

### MMP.10:11 - SoTA-Echoing

The [MiniZinc Handbook 2.10.1, modeling and efficiency sections](https://docs.minizinc.org/en/stable/efficient.html) develops alternative models, derived constraints and interactions with solving methods. Adopt comparison of the resulting work; a smaller variable count alone does not settle it. A direct scalar formulation remains economical when its meaning is already clear.

[Akgun and colleagues, Conjure (2023), sections 2-4](https://www.ijcai.org/proceedings/2023/0765.pdf) separates representation selection from expression refinement and introduces structural constraints during refinement. Adopt this construction when structured objects would otherwise disappear into unexplained scalar choices. Conjure's finite combinatorial scope and model-selection heuristic remain specific to that approach. They do not establish a general best representation or performance guarantee.

The [Essence language reference, function and relation domains](https://conjure.readthedocs.io/en/latest/essence.html) makes such choices as partiality and cardinality explicit. This informs :4.2-4.3; its particular syntax is optional. The ordinary alternative is to express those conditions directly in a familiar mathematical notation.

For infinitely many possible objects, a finite parameterization needs its own coverage or approximation argument. Consider continuous nonnegative functions f on `[0,1]`, with `f(0)=f(1)=0` and integral one. An affine parameterization permits only the zero function after the endpoint conditions, so it fails. The quadratic `f(t)=6*t*(1-t)` satisfies every requirement. This authored countercase explains why the finite structured-model sources do not settle general parameterization. C.29.1 supplies the interpretation of a restriction; the relevant mathematical method supplies a suitable larger family or approximation.

To apply the formulation in another subject, obtain the relations and mathematical operations needed to express its requirements. Reconsider the representation when a new requirement, result kind or obtaining method changes what it needs to preserve or make affordable.

### MMP.10:12 - Relations

MMP.21 uses the formulation to compare connected operations, preserved observations and shared capacity. MMP.22 uses a mathematical transformation to construct the changed reusable working rule and its necessary conditions.

- **B.5.FM and B.5.TU:** construct a first account and connect a subject theory to the encountered problem. This pattern translates its candidate objects and conditions into a mathematical formulation.
- **MATH.1 and MATH.5:** construct composable paths and extend an assignment on elementary steps to compounds while preserving operations and equations. MATH.16 chooses a mathematical construction from the maps it must support. MATH.7 transports structure when the required bijections have been constructed.
- **C.29.1 and C.29.2:** supply correspondence, answer recovery and the separation of a mathematical result from its obtaining procedure and execution.
- **C.16.IR:** determines what a compatible set permits one to infer through projection and constancy of the requested quantity.
- **MMP.7 and MMP.8:** construct observation probabilities and information-dependent choices. A formulation's variables retain those probabilistic and temporal meanings.
- **MMP.9:** derives a reduced evolution law when retained quantities depend on eliminated contributions. The resulting law can supply relations used here.
- **C.11.DUA, E.22 and E.23:** choose worthwhile further inquiry and organize evaluation and improvement of a formulation or its obtaining work.
- **MMP.22** constructs a working-rule candidate from a mathematical transformation; **C.32.MWA.PP** compares practical arrangements and **A.3.1.MV** maintains a consequential Method variant. Its performance in the subject remains distinct from the formal properties of its description.

### MMP.10:End
