## MATH.Reference:5 - Worked use - Construct a choice after finding an obstruction

Four positions form a cycle, with costs (1,3,1,3). The required result is one cheapest position. Changing the numbering origin must rotate the selected position along with the input.

MATH.13 first establishes the transformation relation: rotation preserves the cost-minimization question. MATH.8 identifies the relevant transformed cases. A half-turn leaves this particular input unchanged but swaps its two cheapest positions.

Apply MATH.9's choice condition. An input-preserving transformation must also preserve the answer chosen from that input. Neither cheapest position is fixed by the half-turn, so the requested deterministic rule cannot choose one of them while meeting the rotation requirement.

This obstruction gives useful ways to change the problem. If the receiver can use all minimizers, return the set of the two cheapest positions. If one position is needed and a meaningful mark is available, include that mark in the input and choose the first cheapest position clockwise from it. A joint rotation preserves distances from the mark, so the selected position rotates as required. MATH.9 gives the construction and its reason.

A chosen lowest numeral would introduce a preferred origin. It is appropriate only when that added distinction belongs to the problem. A later request for continuity of the choice raises another condition; an equivariance argument alone has not addressed it.

The result identifies the missing input distinction or output change that permits a construction. The same pattern of work appears in mathematics used for geometric learning, cyclic schedules and other settings, with each setting supplying its own acceptable outputs and additional conditions.
