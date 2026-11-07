## MATH.Reference:6 - Checks and common failures - Preserve what the next construction needs

For a use spanning several patterns, check the following relations at the joins:

1. The next operation receives objects in its domain, with every enabling condition it uses.
2. An identification retains the operation or answer that will be applied to the classes.
3. A change of representation carries the relevant operations and quantities, including the rule for returning the answer.
4. A consequence has the scope supplied by its argument: for example, impossibility, a necessary condition, a constructed witness or a minimum.
5. A computation has the data, branch decisions and termination properties claimed for its use.
6. A changed premise is followed through the constructions that depend on it.

Use the corresponding local pattern's argument where it already answers the question. A small direct use needs only its relevant conditions. A larger claim can require more: obtaining a minimum over one orbit does not by itself settle a minimum over every solution, and a physical conservation statement requires the dynamics under which the quantity is conserved.

The movement example shows why a representation must be judged against the question it answers. Accumulated displacement answers the final-position question; it loses information needed for some visit questions. MATH.2 supplies the test for retaining an answer when cases are identified. In symmetry-dependent choice, MATH.8 and MATH.9 ask how the answer must change with the data; an invariant quantity and a choice that transforms with the input need different constructions.

Another failure arises when mathematical equality is used to reorganize work without examining execution. MATH.12's split-and-join example returns equal values for a fixed function, while repeated evaluation can cost more. If a call changes hidden state, repeated calls can also return different values. Restore the relevant state and use C.29.3 for the execution correspondence before transferring that mathematical transformation.
