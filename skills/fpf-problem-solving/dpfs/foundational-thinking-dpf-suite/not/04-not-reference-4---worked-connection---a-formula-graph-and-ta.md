## NOT.Reference:4 - Worked connection - A formula, graph and table must change together

### NOT.Reference:4.1 - Construct the expressions and their interpretation

A group uses a simple rule, `r(q,b) = q + q + b`, over real numbers. Here q is one supplied input value and b is a shared parameter. The immediate work is to obtain values, inspect dependence on b and change that parameter. This stipulated mathematical example supplies its own interpretation; applying it to a price, measurement or other subject would require a separate account of that subject.

NOT.1 makes the operations explicit. A list of output values supports lookup at listed inputs. It does not necessarily support changing the rule or obtaining an answer at an unlisted input. NOT.2 fixes the references: both q occurrences use the same supplied value; b denotes the same parameter throughout this use. Parentheses or graph connections determine which operands each addition consumes.

For an operation graph, connect the input q to both inputs of one addition, then connect its result and b to a second addition. NOT.3 interprets those connections as addition of the supplied real values. With b=1 and q=0, 1 and 2, the outputs are 1, 3 and 5. A reader can obtain them by following the graph without a software implementation.

NOT.4 permits the transformation `q + q + b` to `2*q + b` under that interpretation. The arithmetic identity supplies preservation for every admitted q and b. A shorter inscription may be useful for changing or explaining the rule, but its symbol count does not establish that every reader will find it easier.

### NOT.Reference:4.2 - Translate only as far as the receiving question allows

NOT.5 translates the rule at b=1 into the table `(0,1), (1,3), (2,5)`. Lookup at those three inputs survives. The table alone does not determine the value at q=3: both `2*q + 1` and `2*q + 1 + q*(q-1)*(q-2)` agree on its rows, but give 7 and 13 respectively at q=3.

If the receiving work needs the general rule, retain that rule or a sufficient construction of it alongside the table. If it only needs the three listed values, the table can suffice.

### NOT.Reference:4.3 - Interpret an edit before propagating it

Now a participant asks that the output at q=1 become 4 while the coefficient 2 remains fixed. NOT.6 treats this as a constraint on the rule, not as an isolated replacement of a displayed cell. It gives `2*1 + b = 4`, hence b=2. The graph receives the new parameter; the table becomes `(0,2), (1,4), (2,6)`. Its former values were derived outputs, so they are recalculated.

If another participant also requires the old output at q=0 to remain 1, that requirement gives b=1. It conflicts with b=2 under the retained rule. The useful result is the conflicting pair of requirements and the assumption on which it depends. Silently choosing one edit would conceal the decision that the group must make.

An independent measurement record is different again. If its row says that an observed output was 3, a parameter change does not change that past observation. Keep the record and updated prediction separately so that the difference can inform the subject inquiry.

### NOT.Reference:4.4 - Change the operation and revisit the affected construction

Suppose a later description replaces each occurrence of q with a fresh sensor read. This changes the operation assumed in :4.1. If consecutive reads return 4 and 5 while b=1, `read() + read() + b` returns 10; `2*read() + b` using the first reading returns 9. The former rewrite is still correct for a single supplied q, but it cannot be transferred to this new interpretation merely by replacing the printed name.

NOT.3 restores what an occurrence now does; NOT.4 reopens the transformation's condition. If the intended operation is to take one sample and reuse it, explicitly bind that sample once. If two observations are required, retain them. CMP.12 provides the algorithmic interpretation when implementing those instructions. The physical measurement method supplies what each read obtains and under which conditions.

Finally, NOT.7 can compare the group’s editing arrangements. A single named b avoids separately editing every derived row, while a table remains useful for direct lookup. Keeping both requires the correspondence already constructed in NOT.6.

The connected result is a usable rule, its complementary expressions and an account of what the change affects. An adequate answer may be the new table, the conflict, or the need for a different reading operation. This combination also applies to other expression families: the arithmetic and sensor supply the worked conditions, while the transferable work is to recover references, interpretation, loss and intended change.
