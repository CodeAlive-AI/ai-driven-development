## Engineering.Reference:27 - Construct and reuse an exchange for a receiving decision

**Start from the result the next operation needs → agree what an exchange means → obtain or build its interpretation → perform it and use the return → revise the affected connection when its conditions change.**

Use this application when participants can send messages but their replies still require repeated reconstruction, or when a reusable adapter risks preserving the wrong meaning. The useful result is a contribution that enters the receiving operation under the conditions of that use. If an existing interface supplies that result, use it. For an occasional exchange, a checked interpretation can cost less than developing a reusable routine.

To work through the example, inspect the structured messages and run the small function, or obtain help with either task. The replenishment calculation assumes one product, site and period, with no incoming supply or other inventory-policy constraints. The 10 units are remaining demand additional to orders already covered by reservations. Compare that demand with stock free for it at the same snapshot. Here 7 units are free, so `max(0, demand - available)` proposes 3. Placing the order requires the receiving organization's separate conditions.

### Engineering.Reference:27.1 - Work backward from the needed contribution

The planner has a qualified outstanding requirement for 10 additional units for SKU A at site N, but lacks available stock for snapshot S1. A stock provider holds that observation. The needed contribution is a statement of usable units for that scope, with its basis. Request that statement. If the provider has only raw on-hand and reserved counts, obtaining the available quantity additionally requires their calculation and check.

This applies the historical [FIPA construction, §§3.19 and 5.3](https://jmvidal.cse.sc.edu/library/XC00037H.pdf): select a communicative act by the intended effect, seek its relevant feasibility conditions and use a request for another act to build the conversation. The formal assumptions delimit this construction; the reply and its use must still be observed.

Establish who can supply the observation, what language and unit both sides understand, and which information the provider may access and disclose to this planner. It may be permitted to share an available count while the individual reservations are restricted. The buyer retains the separate authority to place the order. Agreement to answer leaves the planner awaiting the answer. If the provider refuses for lack of access, take the issue to whoever can provide it. If the calculation fails, correct or rerun it as the cause requires. If the request cannot be interpreted, clarify its wording. Choose the response that supplies what is missing. A conversation alone cannot grant access or settle incompatible assignments.

### Engineering.Reference:27.2 - Agree an interpretation, then obtain its implementation

Use [SYSE.26 and SYSE.27](../syse/_index.md) to construct the interface and examine consequential compatibility; [SIE.9](../sie/_index.md) supplies its semantic interpretation. Specify the receiving quantity before choosing serialization. In this case, available means on-hand units less units reserved for existing commitments, at the named snapshot. Establish which of those commitments already cover the demand the planner is trying to meet. A field called `quantity` is insufficient by itself.

The agreed description states the request identity, product/site/snapshot, unit, successful result meaning, and the distinct unavailable, refused, failed and uninterpretable returns. Include a valid example and a case that must remain unresolved. In the example, the planner proposes a reply giving available pieces. The provider explains that its source contains on-hand and reserved counts at a common snapshot and offers to subtract them. The planner accepts that construction if an absent count produces an unavailable return. Both sides settle the scope, subtraction and failure example before identifying the agreed description. Their implementations must then pass those examples; matching field names alone does not settle the interpretation.

[Agora v1](https://arxiv.org/html/2410.11905v1) offers an implementation choice: identify an agreed protocol document, retrieve and check an unfamiliar document, then interpret the exchange or reuse a suitable routine. Repeated demand can justify negotiating a document and generating an implementation; failures outside that routine return to an available interpretation or a revised agreement. Each side can retain its own implementation.

The example uses the short name `free-stock/1` for the agreed description whose `quantity` is available stock in pieces. A content-addressed implementation uses the agreed document’s digest as its identifier and checks the retrieved document against it. Associate a routine with that description and the receiving input it produces. A matching digest establishes document identity, not the truth of a reported observation.

Obtain a first routine from a programmer or code generator, then exercise it against the agreed examples before entrusting repeated work to it. Where the examples leave an important question open, choose a test that can answer it. Compare the routine’s output with a result established independently. Involve a domain practitioner when the meaning of a stock status needs their judgement or the commission calls for their review. [AutoGen v2, Appendix B.1](https://arxiv.org/abs/2308.08155v2) develops this incremental choice: begin with built-in components and simple interaction, try instructions and configuration, and extend only what the observed failure requires. Human correction supplies development evidence; the automated candidate must subsequently produce the required return under its own intended conditions.

### Engineering.Reference:27.3 - Consume a qualified return

The request below is the comparison basis retained by the planner. A successful reply repeats that basis and carries the value. When obtaining a reply from the provider, verify the provider’s identity and the grounds for the observation through the agreed source relation; a well-formed payload cannot establish them. Proceed to the calculation only when those grounds and the selected snapshot are acceptable for the receiving decision.

```python
request = {
    "id": "R1", "sku": "A", "site": "N", "snapshot": "S1",
    "unit": "piece", "protocol": "free-stock/1",
}
reply = dict(request, status="ok", quantity=7)

def whole_units(value):
    if type(value) is not int or value < 0:
        raise ValueError("a nonnegative whole-unit count is required")
    return value

def consume_stock(reply, request, demand):
    if request["unit"] != "piece":
        raise ValueError("obtain a conversion to the contract's pieces")
    for key in ("id", "sku", "site", "snapshot", "unit", "protocol"):
        if reply.get(key) != request[key]:
            raise ValueError("reply does not match the request: " + key)
    if reply.get("status") != "ok":
        raise ValueError("no usable stock result: " + str(reply.get("status")))
    if request["protocol"] == "free-stock/1":
        available = whole_units(reply.get("quantity"))
    elif request["protocol"] == "gross-stock/2":
        on_hand = whole_units(reply.get("quantity"))
        reserved = whole_units(reply.get("reserved"))
        if reserved > on_hand:
            raise ValueError("this contract requires reserved <= on_hand")
        available = on_hand - reserved
    else:
        raise ValueError("obtain an interpretation for this protocol")
    return {"available": available,
            "proposed_order": max(0, whole_units(demand) - available)}

decision = consume_stock(reply, request, 10)
# {"available": 7, "proposed_order": 3}
```

This function checks and interprets a supplied reply, then uses its value in the replenishment calculation. Obtaining the reply and establishing whether the provider can reliably supply that stock observation are separate operations. If the function rejects the reply, report which field or interpretation is missing. The planner can still use a separately established value or range when it settles the recommendation. The commission may also require the complete reply. Record the accepted stock contribution with the resulting proposal, so that correcting that contribution identifies the calculation that must be reconsidered. Feed the accepted stock value into the calculation even when the recommendation stays the same. Displaying or summarizing the reply leaves the calculation untouched.

### Engineering.Reference:27.4 - Follow a changed meaning through the calculation

The provider now supplies `gross-stock/2`: `quantity=12` means on-hand stock and `reserved=5` identifies the committed part. For the 10 additional units in this order, treating the 12 gross units as free would propose 0 instead of 3. If 10 were instead the entire requirement and five units had already been reserved towards it, five would remain to cover. Seven free units would suffice. The two readings give different orders even with the same verified inventory snapshot. Both payloads contain a number called `quantity`; the semantic change defeats a shape-only check.

If the provider can still supply the former result under its applicable description, that route can remain sufficient. Otherwise obtain and agree the new description. Establish its units, snapshot, reservation rule and relation to the demand being planned. Select or construct the interpretation and establish it on the revised agreement before resuming reuse. A replay of the changed case can check what an implemented adapter actually returns. The old request rejects the new protocol. After the new agreement, the same receiving calculation can be retained:

```python
request2 = dict(request, id="R2", protocol="gross-stock/2")
reply2 = dict(request2, status="ok", quantity=12, reserved=5)
decision2 = consume_stock(reply2, request2, 10)
# {"available": 7, "proposed_order": 3}
```

With twelve on hand and `reserved` missing, admissible reservations can give different proposals. Obtain the missing amount or report the range. If a qualified on-hand count is zero and the stock rule permits reservations only from on-hand stock, available stock is zero. For demand ten, the proposal is ten. A separately commissioned complete reply may still be due. If the provider silently changes meaning while keeping the old identifier, the identifier check cannot discover that fact. Use the observation's grounds and representative reconciliation with the provider to establish continued applicability. A discrepancy returns to the description, producer and affected calculations. Preserve the demand estimate when its grounds are unchanged.

A different request can need a later snapshot or a different unit while the protocol remains stable. Obtain the new observation, a qualified movement record covering the intervening period, or an established unit conversion according to the question. If a request is cancelled, establish whether its calculation or dependent action has already occurred before deciding what remains to stop or revise.

### Engineering.Reference:27.5 - Choose reuse and the next supplier by the whole work

Compare ways of obtaining the same usable result at the time the decision is taken. Before commissioning a routine, suppose preparation and qualification would cost 90 units, maintenance for the intended period would cost 10, and each exchange would cost 2 to process. Interpreting each exchange separately costs 8. At 16 exchanges the routine would cost 132 against 128. At 17 it would cost 134 against 136. Seventeen is the first whole number of exchanges that repays the investment under these assumptions.

If the qualified routine is already available and the 90 has been paid, compare the costs that continuing or discontinuing it would change. Suppose the 10 for maintenance is still avoidable, no retirement charge applies and both routes serve these same requests. For eight more exchanges, continued use costs 26 and separate interpretation costs 64. Use the routine on these terms. Keep the 90 in the history of the original investment. A changed message meaning, maintenance commitment or result quality can change which comparison applies.

When the supplier must be selected from current needs and offers, use [Foundational.Reference:3.10.5.1](../../foundational-thinking-dpf-suite/suite-reference/04-foundational-reference-3---working-combinations.md#foundationalreference31051---route-contributions-by-current-needs-and-offers). Its route identifies a candidate contribution. Apply the interpretation and receiving checks above before consuming that contribution. For fixed, known dependencies a direct request can suffice.

Develop the arrangement through [Reference:19.7](21-engineering-reference-19---make-an-available-contribution-wo.md#engineeringreference197---develop-the-arrangement-across-attempts) and the general trial-to-further-use connection in [Foundational.Reference:3.10](../../foundational-thinking-dpf-suite/suite-reference/04-foundational-reference-3---working-combinations.md#foundationalreference310---develop-a-way-to-act-from-trials). A misunderstood value, an unavailable observation, an unperformed return and a missing authorization call for different changes. Saving a routine may improve the equipped arrangement while leaving a participant's individual mastery unchanged; use [FPF A.2.2:2.1 and E.23.CDI](../../../sections/03-first-principles-framework-readme/_index.md) when the question is whether the participant acquired the capability.
