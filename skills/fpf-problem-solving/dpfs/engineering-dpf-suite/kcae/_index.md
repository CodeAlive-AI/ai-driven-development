# Knowledge-Corpus Access Engineering Principles Framework

**DocID:** `KCAE` within **FPF Library**.

Methods for designing, using and changing access to documentary knowledge.

# Table of Contents

**Reader entry and explanation**

| Publication unit | What it helps you do |
| --- | --- |
| [Knowledge-Corpus Access Engineering Readme](_index.md#knowledge-corpus-access-engineering-readme) | Enter through a present access problem. |
| [Knowledge-Corpus Access Engineering Principles Framework Architectural Reference](_index.md#knowledge-corpus-access-engineering-principles-framework-architectural-reference) | Understand the field, the relations among its methods and one complete construction. |
| [KCAE.Reference:1](01-kcae-reference-1---the-working-problem-and-the-governed-obje.md) | The working problem and the governed object |
| [KCAE.Reference:2](02-kcae-reference-2---why-changing-questions-defeat-fixed-repre.md) | Why changing questions defeat fixed representations |
| [KCAE.Reference:3](03-kcae-reference-3---the-objects-an-engineer-must-keep-distinc.md) | The objects an engineer must keep distinct |
| [KCAE.Reference:4](04-kcae-reference-4---how-the-methods-work-together.md) | How the methods work together |
| [KCAE.Reference:5](05-kcae-reference-5---alternatives-and-the-cost-of-the-whole-ar.md) | Alternatives and the cost of the whole arrangement |
| [KCAE.Reference:6](06-kcae-reference-6---scope-preparation-and-evidence.md) | Scope, preparation and evidence |
| [KCAE.Reference:7](07-kcae-reference-7---relation-to-fpf-and-other-frameworks.md) | Relation to FPF and other frameworks |
| [KCAE.Reference:8](08-kcae-reference-8---using-and-changing-this-account.md) | Using and changing this account |
| [KCAE.Reference:10](10-kcae-reference-10---fpf-and-dpf-supplier-returns.md) | FPF and DPF supplier returns |
| [KCAE.Reference:11](11-kcae-reference-11---working-vocabulary-and-result-boundaries.md) | Working vocabulary and result boundaries |
| [KCAE.Reference:12](12-kcae-reference-12---conditions-that-change-the-framework-and.md) | Conditions that change the framework and its uses |

**Patterns**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| --- | --- | --- | --- | --- |
| 1 | [KCAE.USE - Choose an Access Arrangement for the Work](14-kcae-use---choose-an-access-arrangement-for-the-work.md) | Stable | workload, authority, source boundary, build or reuse; “What must this access system make possible?” | Uses F.1 and C.11.DUA; supplies all design choices. |
| 2 | [KCAE.SOURCE - Prepare Addressable Sources without Losing Their Context](15-kcae-source---prepare-addressable-sources-without-losing-the.md) | Stable | extraction, OCR, table, section, edition, translation; “What does this searchable text leave out?” | Receives the source and use boundary from KCAE.USE; uses A.6.3.RT and NOT.5 where their transformation questions apply. |
| 3 | [KCAE.INDEX - Build Complementary Ways to Find Unknown Material](16-kcae-index---build-complementary-ways-to-find-unknown-materi.md) | Stable | hybrid retrieval, embeddings, BM25, graph, fusion, persistent search; “How do I find a useful passage when I cannot name it?” | Uses KCAE.SOURCE addresses; evaluated by KCAE.EVAL; maintained by KCAE.CHANGE. |
| 4 | [KCAE.SEARCH - Continue a Search as the Question Develops](17-kcae-search---continue-a-search-as-the-question-develops.md) | Stable | query planning, corpus synthesis, direct scan, blind spot, stopping, coverage; “What should the next search obtain?” | Uses the routes actually available, including KCAE.INDEX; returns candidates to KCAE.ASSESS. |
| 5 | [KCAE.ASSESS - Determine What a Candidate Can Support](18-kcae-assess---determine-what-a-candidate-can-support.md) | Stable | criterion, unknown, contradiction, reranking, typed decision; “Is this useful evidence or merely similar text?” | Receives source context; supplies KCAE.COMPOSE and KCAE.DELIVER. |
| 6 | [KCAE.COMPOSE - Connect Contributions to a Feasible Whole Result](19-kcae-compose---connect-contributions-to-a-feasible-whole-res.md) | Stable | missing result, method set, shared resource, alternatives; “What else is needed, and can these contributions work together?” | Uses C.39, KCAE.ASSESS and relevant subject methods; returns missing inputs to KCAE.SEARCH. |
| 7 | [KCAE.DELIVER - Put Sufficient Source Material within the Reader's Reach](20-kcae-deliver---put-sufficient-source-material-within-the-rea.md) | Stable | context budget, packet, full reading, pagination, history; “What must the recipient actually receive?” | Uses C.2.8; receives KCAE.SOURCE, KCAE.ASSESS and, where needed, KCAE.COMPOSE results. |
| 8 | [KCAE.CHANGE - Keep Source Reading and Derived Views Coherent through Change](21-kcae-change---keep-source-reading-and-derived-views-coherent.md) | Stable | incremental index, snapshot, deletion, generation, recovery; “What remains usable after this update?” | Preserves KCAE.SOURCE and KCAE.INDEX contracts; reopens dependent judgements. |
| 9 | [KCAE.ENCOUNTER - Arrange a Useful Encounter with Knowledge during Work](22-kcae-encounter---arrange-a-useful-encounter-with-knowledge-d.md) | Stable | event, observer, quiet mode, notification, permission; “Why would the user begin this inquiry now?” | Applies A.15.11 and B.5.PI through an actual event source; uses KCAE.SEARCH and KCAE.ASSESS. |
| 10 | [KCAE.MEMORY - Reuse Connections while Keeping Open Questions Revisable](23-kcae-memory---reuse-connections-while-keeping-open-questions.md) | Stable | unresolved cue, episode, conditional memory, recognition question; “What should survive without fixing the next interpretation?” | Uses KCAE.ASSESS, KCAE.COMPOSE and KCAE.CHANGE; can supply KCAE.ENCOUNTER. |
| 11 | [KCAE.EVAL - Compare Access Arrangements by Useful Results and Full Cost](24-kcae-eval---compare-access-arrangements-by-useful-results-an.md) | Stable | held-out episode, ablation, no useful answer, update trial; “Which change earns adoption?” | Consumes the use from KCAE.USE and the complete arrangement; uses C.11.DUA. |

**Applications and source return**

| Publication unit | What it helps you do |
| --- | --- |
| [KCAE.Application](_index.md#applications) | Work through a large bilingual support corpus, a historical inquiry and a method library. |
| [KCAE.Profiles](_index.md#engineering-profiles) | Select replaceable retrieval, assessor and execution technologies. |
| [Source contributions and comparison boundaries](09-kcae-reference-9---source-contributions-and-comparison-bound.md) | Recover external contributions, evidence limits, vocabulary and refresh conditions. |

# Knowledge-Corpus Access Engineering Readme

## Practical entries

These are selected examples of entry. Bring the actual question. Use the index, a direct pattern or search across the publication when neither example fits. You can ask an assisting agent: “Explain this and comment in ordinary language, without framework jargon.”

### changed-reading - A search opens the wrong edition

- **Situation:** A result names a useful clause, but the opened text is newer, missing or at another location.
- **Question:** Can this result still support the work?
- **First useful result or blocker:** A coherent source reading, or a precise unavailable-edition result that prevents the unsupported use.
- **Start with:** KCAE.CHANGE:4.3, then KCAE.SOURCE when the address itself is ambiguous.
- **Stop or return:** Stop when the necessary reading is coherent; reopen its assessment if the governing content or receiving situation changed.

### Practical-Use Cards

These examples retain longer connections across methods. They do not prescribe a workflow for every query.

#### unknown-contribution - Build access for questions that do not name their sources

- **Situation:** A large changing corpus contains useful knowledge, but readers describe work in another vocabulary and cannot identify the right passage.
- **Question:** How can the system obtain a useful contribution at a sustainable cost?
- **First useful result or blocker:** A testable access design with source returns, complementary finding routes, adequate reading and honest limits.
- **Mantra:** Start from the work; preserve sources; widen finding; check the contribution; deliver enough; revisit what changed.
- **Start with:** KCAE.USE, KCAE.SOURCE and KCAE.INDEX; follow the connected construction in KCAE.Reference:4.
- **Stop or return:** Keep a sufficient existing arrangement. Reopen a route, judgement or delivery when its premise fails.

## Who this framework serves

This framework serves information and software engineers who construct or maintain access to technical publications, support libraries, research collections, organizational documentation or comparable documentary corpora. It also serves analysts who must explain an access failure or compare an arrangement supplied by others. Readers are expected to understand ordinary software interfaces, identifiers, data structures, testing and basic descriptive statistics. A named domain specialist or source owner supplies authority rules and interpretations that require that profession; the engineer obtains and carries those results rather than silently inventing them.

You can use a direct pattern without learning the whole framework. Someone who already has a sufficient source can read and apply it immediately. Engineering the access arrangement becomes useful when repeated or difficult use requires better finding, interpretation support, delivery, maintenance or encounter. The aim is to make those operations constructible and revisable, including when an adequate result is a missing fact or an unavailable source.

---

## Files of this publication

Generated by the skill's splitter: one file per section, in reading order.


### Knowledge-Corpus Access Engineering Principles Framework Architectural Reference

- [KCAE.Reference:1 - The working problem and the governed object](01-kcae-reference-1---the-working-problem-and-the-governed-obje.md) (8 lines)
- [KCAE.Reference:2 - Why changing questions defeat fixed representations](02-kcae-reference-2---why-changing-questions-defeat-fixed-repre.md) (10 lines)
- [KCAE.Reference:3 - The objects an engineer must keep distinct](03-kcae-reference-3---the-objects-an-engineer-must-keep-distinc.md) (12 lines)
- [KCAE.Reference:4 - How the methods work together](04-kcae-reference-4---how-the-methods-work-together.md) (18 lines)
- [KCAE.Reference:5 - Alternatives and the cost of the whole arrangement](05-kcae-reference-5---alternatives-and-the-cost-of-the-whole-ar.md) (10 lines)
- [KCAE.Reference:6 - Scope, preparation and evidence](06-kcae-reference-6---scope-preparation-and-evidence.md) (10 lines)
- [KCAE.Reference:7 - Relation to FPF and other frameworks](07-kcae-reference-7---relation-to-fpf-and-other-frameworks.md) (8 lines)
- [KCAE.Reference:8 - Using and changing this account](08-kcae-reference-8---using-and-changing-this-account.md) (6 lines)
- [KCAE.Reference:9 - Source contributions and comparison boundaries](09-kcae-reference-9---source-contributions-and-comparison-bound.md) (17 lines)
- [KCAE.Reference:10 - FPF and DPF supplier returns](10-kcae-reference-10---fpf-and-dpf-supplier-returns.md) (19 lines)
- [KCAE.Reference:11 - Working vocabulary and result boundaries](11-kcae-reference-11---working-vocabulary-and-result-boundaries.md) (16 lines)
- [KCAE.Reference:12 - Conditions that change the framework and its uses](12-kcae-reference-12---conditions-that-change-the-framework-and.md) (8 lines)
- [KCAE.Reference:End](13-kcae-reference-end.md) (2 lines)

### Patterns

- [KCAE.USE - Choose an Access Arrangement for the Work](14-kcae-use---choose-an-access-arrangement-for-the-work.md) (85 lines)
- [KCAE.SOURCE - Prepare Addressable Sources without Losing Their Context](15-kcae-source---prepare-addressable-sources-without-losing-the.md) (85 lines)
- [KCAE.INDEX - Build Complementary Ways to Find Unknown Material](16-kcae-index---build-complementary-ways-to-find-unknown-materi.md) (109 lines)
- [KCAE.SEARCH - Continue a Search as the Question Develops](17-kcae-search---continue-a-search-as-the-question-develops.md) (146 lines)
- [KCAE.ASSESS - Determine What a Candidate Can Support](18-kcae-assess---determine-what-a-candidate-can-support.md) (99 lines)
- [KCAE.COMPOSE - Connect Contributions to a Feasible Whole Result](19-kcae-compose---connect-contributions-to-a-feasible-whole-res.md) (110 lines)
- [KCAE.DELIVER - Put Sufficient Source Material within the Reader's Reach](20-kcae-deliver---put-sufficient-source-material-within-the-rea.md) (105 lines)
- [KCAE.CHANGE - Keep Source Reading and Derived Views Coherent through Change](21-kcae-change---keep-source-reading-and-derived-views-coherent.md) (109 lines)
- [KCAE.ENCOUNTER - Arrange a Useful Encounter with Knowledge during Work](22-kcae-encounter---arrange-a-useful-encounter-with-knowledge-d.md) (121 lines)
- [KCAE.MEMORY - Reuse Connections while Keeping Open Questions Revisable](23-kcae-memory---reuse-connections-while-keeping-open-questions.md) (97 lines)
- [KCAE.EVAL - Compare Access Arrangements by Useful Results and Full Cost](24-kcae-eval---compare-access-arrangements-by-useful-results-an.md) (118 lines)

### Applications

- [KCAE.Application:1 - Constructing access for CedarBench support](25-kcae-application-1---constructing-access-for-cedarbench-supp.md) (78 lines)
- [KCAE.Application:2 - A historical inquiry with no external processing](26-kcae-application-2---a-historical-inquiry-with-no-external-p.md) (10 lines)
- [KCAE.Application:3 - Finding and using contributions from a method library](27-kcae-application-3---finding-and-using-contributions-from-a.md) (30 lines)
- [KCAE.Application:End](28-kcae-application-end.md) (2 lines)

### Engineering profiles

- [KCAE.Profiles:1 - Retrieval and query construction](29-kcae-profiles-1---retrieval-and-query-construction.md) (36 lines)
- [KCAE.Profiles:2 - Typed assessors and generative readers](30-kcae-profiles-2---typed-assessors-and-generative-readers.md) (22 lines)
- [KCAE.Profiles:3 - Packages, tools, dynamic loading and storage](31-kcae-profiles-3---packages-tools-dynamic-loading-and-storage.md) (22 lines)
- [KCAE.Profiles:End](32-kcae-profiles-end.md) (1 lines)
