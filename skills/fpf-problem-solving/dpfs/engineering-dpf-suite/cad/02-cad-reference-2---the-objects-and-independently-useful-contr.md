## CAD.Reference:2 - The objects and independently useful contributions

The plant, sensors, actuators and controller computers are systems. A dynamical model is a mathematical description of selected behavior. A feedback law prescribes how to choose an input; an implementation performs that calculation and applies an actual input. A design Method constructs or assesses an arrangement; one run of that Method is design work. The framework describes Methods and their relations. A model or feedback-law revision can change the required computation without requiring a different physical plant; changing a processor can change timing without changing the law.

In CAD.5, a *channel* is a realizable observation alternative with a measurement meaning, uncertainty, sample times, arrival conditions and resource demands. An *information state* retains what is needed to update the compatible possibilities and choose the next action. It can be a history, a sufficient recursive state or a conservative set representation; it is not necessarily another sensor or a physical control layer. The estimate \(\hat x\), the true model state \(x\), estimation error \(\eta=x-\hat x\), nominal state \(z\) and tracking error \(e=x-Pz\) have different meanings.

In CAD.1–CAD.4, *planner*, *tracker* and *layer* identify contributions in a selected control organization. They do not automatically identify processor boundaries, physical parts or system-role assignments. Different functions can share a processor; one function can be distributed. Their order is not a ranking of people.

| Recurring design question | What its Method constructs | Why the result can be needed independently |
| --- | --- | --- |
| Information sufficient for action | CAD.5: channel/timing alternatives, sufficient memory and update, estimation uncertainty and admissible action or impossibility | A single controller may need better observations without a different decomposition. |
| Useful separation of decisions | CAD.1: alternative decompositions, reasons for each split and exposed losses | A timing or horizon problem can change the split while sensing remains adequate. |
| Meaning and behavior of an exchange | CAD.2: reconstruction, command, hold/interpolation/reset rules and error dynamics | A communication or reference representation can change without replacing either controller. |
| Feasible command and continuation | CAD.3: compatible error and command sets, state/input margins and continuation conditions | A larger demand can exceed a previously useful domain while the architecture remains unchanged. |
| Realizable whole choice | CAD.4: feasible configurations, comparison under common demands, execution and revision conditions | A processor, solver or scheduling change can alter the preferred realization. |

These are connected problem families with independent uses. CAD.4 constructs the comparison of whole layered candidates; CAD.5:4.8 compares information arrangements. This Reference explains the quantities shared by those Methods and the conditions under which their results can be combined.
