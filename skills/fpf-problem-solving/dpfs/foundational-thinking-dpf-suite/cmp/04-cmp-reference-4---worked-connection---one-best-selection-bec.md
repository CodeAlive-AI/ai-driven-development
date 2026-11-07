## CMP.Reference:4 - Worked connection - One best selection becomes every best selection

Suppose a finite list contains individually identified options. Each may be chosen at most once. Costs are positive integers and values are nonnegative integers. A selection's cost and value are the respective sums for its chosen options; total cost must not exceed capacity W. The first request is the maximum value and one selection achieving it. These are stipulated model conditions; whether they describe an actual investment, experiment or production choice is a separate modeling question.

Use three options: A costs 4 and has value 7; B costs 3 and has value 5; C costs 2 and has value 3. Capacity is 5.

**Construct what a smaller problem must return.** CMP.2 defines R(i,b) as the best value using the first i options with remaining capacity b. The base is R(0,b)=0. If option i costs w_i and has value p_i, its recurrence is:

`R(i,b) = R(i-1,b)` when `w_i > b`;

`R(i,b) = max(R(i-1,b), p_i + R(i-1,b-w_i))` otherwise.

Every selection either excludes or includes option i, so these branches cover its possibilities. Both use a smaller i. Store a choice attaining the maximum when a witness is required. For A, B and C, the final values at capacities 0 through 5 are `0, 0, 3, 5, 7, 8`; recovering the choice at capacity 5 gives B and C.

**Share subproblems and compare cost.** CMP.3 computes each needed pair (i,b) once in dependency order. A full table has (n+1)(W+1) cells and O(nW) updates. This is a count of table operations; arithmetic cost depends on the size of the values. Since W is encoded with about log₂(W+1) bits, this procedure can still be expensive relative to input length. Keeping just two value rows reduces storage, but recovering the selection then requires retained decisions or recomputation. CMP.10 helps compare those operations for the actual workload.

**Use a cheaper bound when it settles the request.** CMP.5 allows fractional choices solely to obtain an upper bound. At capacity 5, take all of A and one third of B: the relaxed value is 26/3. The corresponding fractional optimum follows by considering value per unit cost, or by the bound derived in CMP.4's worked case. Original values are integers, so they are at most 8. The feasible B+C selection reaches 8. CMP.4 can therefore finish the optimality question without searching every remaining branch. When a bound does not settle it, the search retains the unresolved alternatives.

**Change the requested answer and a supplied option.** Add D, costing 4 with value 8, and request every optimal selection. The new final value row is `0, 0, 3, 5, 8, 8`. D and B+C both attain 8. D cannot be combined with another option within capacity; the earlier argument bounds all selections omitting D. The old fractional bound does not cover the changed list: the new relaxation can take D and one quarter of A, giving 39/4. That bound alone leaves the integer value 9 unresolved.

A search for one optimum can discard a branch whose best possible value equals the incumbent. A search for every optimum must retain a branch that may contain a different equal-valued witness. Similarly, a table storing only the minimum cost for each value keeps D at cost 4 for value 8 and can discard B+C at cost 5. Recovering all ties in that compressed table cannot recover a selection already discarded for being heavier.

Return to the original recurrence. After computing R, recover every optimal selection by following each branch whose value equals R(i,b), retaining the distinct choices. At (4,5), both exclusion, R(3,5)=8, and inclusion, 8+R(3,1)=8, qualify. They recover B+C and D. CMP.4 supplies the changed exclusion condition; CMP.3 supplies the retained dependencies or recomputation; CMP.10 exposes what a compressed representation lost. The value calculation survives, while the witness procedure changes. Enumerating all witnesses can require exponential output even if the value table is small.

If the work later permits a near-optimal value, CMP.8 can trade a quantified rounding loss for a smaller computation. That different request does not supply every optimizer of the unrounded problem. Select the answer the work needs before choosing the shortcut.

The same connected method can be used with other finite recurrences and search constructions. Independent additivity and integer capacity belong to this example. A different problem may require different state, recurrence and bounds while preserving the need to connect answer, construction, retained information and cost.
