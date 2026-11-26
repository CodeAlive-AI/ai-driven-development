## KCAE.DELIVER - Put Sufficient Source Material within the Reader's Reach

> **Type:** Method pattern
> **Status:** Stable

### KCAE.DELIVER:1 - Problem frame

**Use this when** a found contribution must cross to another person, model call, tool or later occasion, and its source conditions may not survive that crossing. A brief search excerpt is enough to choose what to open; it may be insufficient to use the method safely or explain its result.

Give the reader the material, context and access needed for the intended contribution. When the reader already has and understands a sufficient source, use it directly without building a packet. Do not require exhaustive source delivery when a bounded result with recoverable grounds meets the receiving use.

### KCAE.DELIVER:2 - Problem

Source retention, a correct citation and a successful tool call do not establish that the recipient received enough. Truncation can remove a condition, a summary can remove a countercase, and a model can spend its remaining window on candidate listings before reaching the selected method.

### KCAE.DELIVER:3 - Forces

More source context can improve recoverability while increasing cost and distraction. Different readers have different preparation and tools. A compact result can be ideal for one recipient and misleading for another. Some runtimes support isolated readers or controlled history reconstruction; others only return another message into the same accumulating context.

### KCAE.DELIVER:4 - Solution

#### KCAE.DELIVER:4.1 - Specify the receiving contribution and reader

Identify what the recipient will do: choose a source, understand an explanation, perform a method, check a conclusion or maintain the access service. State the preparation already available and the operations the runtime supports. For a human, available time, domain competence and access permissions matter. For a model, include current instructions, model capability, tool access, residual window and output limits. Total historical tokens consumed and free space in the active context are different resources.

Work back from the contribution entrusted to each participant. If a service searches and inspects records on someone’s behalf, establish which records it may inspect and what it may disclose. An authorized finding can settle the recipient’s question even when the underlying record is closed to them. For a recipient’s own judgement, give them the original question, sufficient permitted evidence and the freedom to report whatever that evidence warrants. They may confirm the finding, correct it or leave a question open. A named passage with its qualifications can suffice to judge its meaning. Reviewing the coverage of a search also requires grounds for detecting material the search could have missed. For an unaided search, let the recipient select material from the permitted corpus before disclosing another reader’s choices. A request to verify a specified passage can name it at the outset.

A search packet can contain a candidate's identity, edition, brief reason for relevance and source address. An application packet usually needs the method's recognition conditions, required inputs, consequential exceptions, operating instructions, stop conditions and any joining operation not already known to the reader. Derive the necessary material and the space it requires from the intended use and inspected source.

#### KCAE.DELIVER:4.2 - Recover the required reading closure

Start with the selected passage and follow dependencies needed to interpret or apply it: definitions, qualifications, tables, footnotes, named prerequisites and relevant adjacent exceptions. Expand across documents when a release note or external criterion changes the meaning. Stop expansion when the intended reader can obtain the receiving result without guessing an essential relation; unrelated background need not travel.

Keep original passages distinguishable from the engineer's explanation. A generated contextual prefix is discovery support, not a quote from the author. A translated passage is a translation with a stated role, not automatically the governing edition. If a missing source dependency prevents adequate delivery, return that specific limitation.

For consequential use, choose a question that depends on the vulnerable distinction. A support reader can explain why protocol v1 requires manual reconciliation while v2 can permit a resend. If the service engineer must learn to design the access arrangement, supply the users' requests, permissions and source conditions before showing the worked design. Have the engineer choose how the relevant evidence will reach the intended reader and trace what that reader can conclude. Suppose the configuration record is available only on site. A permitted finding from a qualified local reader may settle a scheduling question. If the designated analyst has to examine the record personally, the design must provide authorized access for that analyst or identify the outstanding examination. An earlier comparable design can show which choices the engineer made independently. Attributing a gain to this teaching also requires evidence of earlier ability and what changed with teaching. KCAE.EVAL provides a bounded reader-use comparison when the design depends on that capability.

#### KCAE.DELIVER:4.3 - Read complete bounded units through a pinned sequence

When source reading is paginated, the reader needs an edition or snapshot identifier, a bounded unit, a continuation token or explicit next position, and a completion indication. Pin the edition for the sequence. Record which portions were returned, and detect a gap, duplicate or changed generation before combining them. A source hash can confirm the obtained bytes; it cannot prove that a truncated tool message conveyed those bytes to the reader.

Use the interface’s output limits. Request a smaller portion when a response is truncated, verify the continuation boundary, and continue until the needed unit is complete. Do not take “command succeeded” as an end-of-document signal. A tool may store a complete file while showing only its beginning. Its reader interface must distinguish the saved result from the shown portion.

A method can span more than one call, provided the recipient can retain or revisit the dependencies it needs. Very long sources may require an external notebook of source-addressed intermediate results and selective rereading. The notebook can omit distinctions in the original. Preserve the exact return path and reread the relevant original when its omitted distinction becomes live.

#### KCAE.DELIVER:4.4 - Choose a delivery arrangement the runtime can perform

**Direct complete reading** is suitable for a manageable dossier and a capable recipient. **Retrieval followed by selective reading** spends context on material selected for the current use. **An isolated reader** can inspect a larger or private portion and return a bounded result, provided the platform creates an independent context and the result retains enough grounds for its consumer. **Controlled history reconstruction** can retain current instructions and selected state while removing obsolete search output, but only when the runtime exposes that operation.

An instruction such as “forget the preceding search” does not establish deletion or reclaim a context window. A skill or tool that returns a concise message does not establish an isolated reader. Verify these runtime properties through documentation and a relevant observable test. Where isolation is unavailable, keep search material outside the main dialogue as far as the interface allows, use smaller returns and plan the necessary reading before filling the window. Where a fresh context is used, explicitly supply its governing instructions, source permissions, question and necessary prior results; independence is not inherited knowledge.

Separate conversation contexts can still share a filesystem, credentials, tools or network access. Before assigning a private dossier to another reader, check which resources the contexts share and what access each permits. Context separation alone is neither a permission grant nor a security sandbox. Supply only the authorized material and capabilities needed for the bounded contribution.

A cached long-context source can be a credible alternative when the platform supports it and the workload amortizes cost. Cache storage does not guarantee reliable attention to every needed item. Compare its delivery performance on the workload and the provider’s current charging rules with selective reading. A cache holding an old edition remains an old edition.

#### KCAE.DELIVER:4.5 - Budget discovery, application and explanation together

Reserve room and time for the selected source, necessary connections, answer and uncertainty before spending the entire allowance on candidate discovery. Include the cost of parallel calls and external readers in total work, even if they save main-context space. A cheaper main dialogue can conceal a much more expensive service.

Use a runtime observation of remaining capacity where available. When it is unavailable, label the estimate and leave a margin for interface overhead and output. Cumulative billed tokens across calls do not reveal the active window's remaining space; cached, repeated and external-reader input can be counted differently.

For example, if the active window has room for 12,000 further tokens, and source closure plus explanation is estimated at 7,000, a 9,000-token candidate dump is infeasible even if the model has consumed only a small fraction of its account quota. Either shrink discovery output, use a genuine external reader, obtain more capacity or return a narrower justified result. These invented numbers illustrate reservation, not a recommended product limit.

Check data boundaries on every transfer. Public retrieval can use a sanitized question; local case facts can remain with a local assessor. A remote provider's retention and logging behavior is part of the chosen interface, not implied by calling the input “context.” Redact with attention to meaning: if removing the decisive condition makes assessment impossible, obtain an approved local route or a permission decision rather than guessing.

#### KCAE.DELIVER:4.6 - Confirm receipt and expose what remains to be done

Return the contribution at the level the recipient needs: conclusion, grounds, conditions and next operation. For execution, distinguish a recommended action from an action already performed. For later use, include sufficient edition and dependency information to detect staleness. For human adoption, a readable explanation or small first useful exercise can reduce the burden; dumping every engineering detail may make correct material practically unusable.

Confirm receipt at the point named in the commission. A service’s acknowledgement can establish delivery to that service. Evidence that a named analyst inspected the governing edition must connect that analyst’s work to the relevant passage. Display on a shared screen, a service account opening the file, and a person using its finding support different claims. Where receipt or use remains unobserved, give the conclusion that the available evidence supports. If the recipient cannot recover a needed distinction, repair the representation, preparation or access implicated by that failure.

### KCAE.DELIVER:5 - Archetypal Grounding

A search excerpt says that CedarBench supports automatic resend. The needed manual unit also contains a protocol condition and links to a compatibility-table footnote. The assistant opens the pinned manual section and table, obtains the missing protocol from the authorized local configuration service, and gives the analyst a conditional result. For v1 it explains the manual reconciliation route and the absent automated prerequisite. The excerpt alone would have supported a wrong instruction.

Suppose the analyst only needs to schedule reconciliation. The authorized finding about v1 can settle that decision. Now keep the configuration and the answer fixed, and commission the analyst to check the advice independently. Supply the governing section with its table note and an authorized basis for establishing the installed protocol. The analyst can then test whether the service applied the rule correctly. If a personal inspection of the configuration record is required and the analyst cannot open it, the service’s finding remains available for scheduling and the personal check is outstanding. A service engineer building the integration additionally needs the receipt-ID mapping and the access-generation contract.

### KCAE.DELIVER:6 - Bias-Annotation

Authors and powerful models may fill missing connections from their own knowledge and mistake that for sufficient delivery. Test whether the intended reader can recover those connections using the material and aids supplied for that use. Conversely, excessive precaution can overload a simple use. Ask which omitted distinction can change the result before adding another source bundle.

### KCAE.DELIVER:7 - Conformance Checklist

Is the receiving use explicit? Does the material contain the consequential conditions and joins? Are source text and interpretation distinguishable? Has the necessary reading completed without a generation change or hidden truncation? Does the runtime support the assumed isolation or history control? Are total cost, residual window and permissions treated separately? Is receipt or comprehension claimed only where observed?

### KCAE.DELIVER:8 - Common Anti-Patterns and How to Avoid Them

A citation without obtainable text does not supply the method. A summary of a summary can inherit the very omission that defeated retrieval; return to the source. A success flag is not a reading-completion marker. A request to forget is not a runtime operation. A fixed small packet cannot satisfy every reader and use; derive its content from the receiving contribution.

### KCAE.DELIVER:9 - Consequences

The arrangement can save main-context capacity while moving some reading work elsewhere. Source closure and privacy checks add effort, but make the basis of the result inspectable. Some tasks return a delivery limitation or a request for a prepared reader.

### KCAE.DELIVER:10 - Architectural Rationale

C.2.8 makes recoverable structure relative to a reader and support. This construction turns that distinction into source expansion, bounded reading, runtime choice and receipt checks. Discovery and application packets differ because they support different operations.

### KCAE.DELIVER:11 - SoTA-Echoing

Anthropic's context-engineering account motivates selective runtime access; Gemini's long-context documentation makes caching a serious alternative while retaining multi-item retrieval limitations. These capabilities are developed in KCAE.Profiles:3. The method adopts both as conditional means and requires runtime support for history or isolation claims. Requalify delivery when a model, tool-output cap, caching interface or reader population changes.

For Cochrane intervention reviews, a shared set of search results can supply the full reports from which at least two people independently judge final eligibility. A qualified specialist can review the search strategy before it runs. Checking the strategy, finding a report and deciding whether the study qualifies are distinct contributions. The evidence needed depends on which of them was entrusted to the reviewer. [Cochrane Handbook, chapter 4, §§4.2.2, 4.4.8 and 4.6.4](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04)

### KCAE.DELIVER:12 - Relations

KCAE.SOURCE supplies exact reading units and addresses; KCAE.ASSESS and KCAE.COMPOSE determine what the contribution requires; KCAE.CHANGE preserves edition coherence; KCAE.EVAL tests actual receiving use. C.2.8 supplies reader-relative recoverability and C.11.DUA supplies the burden question. Neither is replaced by a token count.

### KCAE.DELIVER:End
