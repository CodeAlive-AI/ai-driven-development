# Resolving Ambiguities via Git History Mining

Read this when the `## Unresolved` section has entries and the user wants them
resolved **without** answering every question by hand — or when a naming decision
hinges on "which of these two names came first / replaced which".

This is an **optional last step** of thesaurus generation (Step 6 in
[generating-thesaurus.md](generating-thesaurus.md)) and can also be run on its own
against an existing thesaurus.

## What history can and cannot decide

Git history is **evidence of what happened**, never authority on what *should* be.
It answers questions of fact that no static scan of the current tree can:

| Question | History answers it | Signal |
|----------|-------------------|--------|
| Which of two synonyms is newer? | yes | first commit that introduced each identifier |
| Did `A` replace `B`, or do they coexist by design? | usually | one commit removes `A` and adds `B` in the same files |
| Is a term dying or growing? | yes | additions vs deletions per year |
| Was this rename deliberate? | often | the commit message / PR that did it |
| Why do two modules spell the same concept differently? | sometimes | the two names were born in different commits by different authors, never reconciled |
| What does the domain expert call it? | **no** | ask the user |
| Which name *should* be canonical? | **no** | ask the user; history only ranks the candidates |

**Rule:** history mining produces *ranked hypotheses with citations*, not decisions.
Every resolution it proposes is presented to the user with the commits behind it.
An `## Unresolved` entry is promoted to the Index only after the user agrees — the
one exception is a rename so unambiguous (single commit, message says "rename X to Y",
no later reappearance of X in new code) that it can be proposed as a `## Legacy` line
and confirmed in a single yes/no.

## When to offer it

Offer once, right after presenting `## Unresolved` to the user (Step 5), phrased as
an option and never as a blocking question:

```
5 unresolved naming issues remain. Before you answer them one by one, I can mine
the git history — when each name was born, which one replaced which, and which is
growing vs dying. It builds a temporary index outside the repo (~1-3 min for this
repo's size, deleted afterwards) and comes back with evidence-backed proposals for
each item. Want me to try that first?
```

Skip the offer entirely when any of these hold:

- The repository has < ~50 commits, or its history starts with a single "initial import"
  squash — there is nothing to mine.
- There is no `.git` (a vendored copy, an export, a fresh `mkdir`).
- The `## Unresolved` items are white spots (`[WHITE-SPOT]` tag) rather than conflicts —
  a concept nobody has named yet cannot appear in history.
- The user already answered the questions.

## Tooling

Two layers. Use the index for anything term-shaped; drop to raw git for the last mile.

### 1. The throwaway index — `scripts/git_term_index.py`

Dependency-free Python 3.9+ (stdlib `sqlite3`), needs only `git`. Writes **one SQLite
file outside the working tree** (`$TMPDIR/ubiquitous-language-git-index/<repo>-<hash>.sqlite3`)
— never into the repo, never committed. Safe to delete at any moment.

```bash
S=path/to/skills/ubiquitous-language/scripts/git_term_index.py

# messages + paths + renames — seconds
python3 $S build --repo-dir .

# + every identifier in the FULL diff history — the mode that answers naming questions
python3 $S build --repo-dir . --content

python3 $S query Account Customer      # per-term evidence report
python3 $S pair User Customer Account  # competing names, head to head
python3 $S contexts Account            # where the name lives — the polysemy check
python3 $S search 'rename account'     # BM25-ranked commit-message search
python3 $S status                      # what is indexed, how big
python3 $S clean                       # delete the index
```

Schema:

| Table | Content | Answers |
|-------|---------|---------|
| `commits` + `commits_fts` (FTS5) | sha, date, author, subject, body | "what did people *say* about this name?" — ranked by BM25, not by recency |
| `files` | commit, status, path, oldpath | "where did the name live?" |
| `renames` | detected renames (`-M`) | "was the file itself renamed?" |
| `tokens` (`tok`, `norm`) | every spelling, plus a casing-independent normal form | `OrderLineItem`, `order_line_item` and `ORDER_LINE_ITEM` are one concept — so a PascalCase thesaurus Identifier finds a snake_case codebase |
| `token_sub` | camelCase/snake_case subwords | `--family` widens `Order` to `OrderLineItem`, `order_id` |
| `paths` | files touched | — |
| `tc` | identifier × commit × **file**, with add/delete counts | birth, death, volume, co-occurrence, *and* which files a name lives in |

**Why identifier × file and not identifier × commit.** One commit touches many files, so
commit-level co-occurrence cannot localise a name: measured on git.git, the directory
distribution of one identifier was 74% "wherever the code is". Per-file rows buy the two
things the protocol actually needs — the **polysemy split** (does any file contain both
names? which directories does each occupy?) and **same-file exchanges**, which are much
stronger rename evidence than "both names appear somewhere in one commit".

**The whole history is indexed, not a recent window.** That matters: a windowed index
reports "first seen in the window" and an agent reads it as a birth date. Measured on
git.git, a 3000-commit window covered 10 months of a 21-year history and dated
`oid_array` to 2025 instead of 2017.

**Defaults worth knowing:**

- **HEAD only.** Side branches carry status files, release notes and vendored trees whose
  vocabulary is not the project's. `--all-refs` opts in. (On git.git, `--all` dated
  `oid_array` to a "What's cooking" status email three days before the real rename commit.)
- **Vendored and generated paths excluded** — `vendor/`, `third_party/`, `node_modules/`,
  `testdata/`, `*.pb.go`, `zz_generated*`, lockfiles, minified assets. They dominate token
  counts and hold no domain vocabulary. `--no-default-excludes` turns this off.
- **Merges excluded** (`--no-merges`), so a squash-merge is counted once, not twice.
- **Concept, not family.** `pair Account BillingAccount` compares two concepts; it does not
  let the `Account` set swallow `BillingAccount` (which would cancel the deletions against
  the additions and hide the very exchange being measured). `--family` opts into the wider
  match, and identifiers shared by both sides are dropped from each.
- **Scope is part of the index identity.** An index built with `--pathspec src/` is not
  reused for a whole-repo question, and every report prints the scope it was built with.

**Cost.** Measured on an M-series laptop:

| Repo | Indexed commits | `build` | `build --content` | Index size | `query` / `pair` / `search` |
|------|-----------------|---------|-------------------|-----------|------------------------------|
| small skill repo | 238 | 1 s | 4 s | 11 MB | instant |
| git/git (21 years) | 60 751 | 5 s | **111 s** | 232 MB | 0.1 s |
| kubernetes (12 years, 140 k on HEAD) | 82 704 | 11 s | **249 s** | 1 040 MB | 0.1–1.3 s |

Per-file granularity costs +18% on disk on git.git and no extra time; on kubernetes, whose
commits touch far more files, it is the dominant cost (15.7 M identifier×commit×file rows,
1 GB). If a repo of that size is too heavy, `--pathspec` is the lever — it cuts the corpus
and sharpens the signal at once.

The diff pass streams at roughly 12 MB/s of diff text and `git` itself is most of that —
tokenising is nearly free, so the cost scales with how much diff the repo has, not with how
many terms you ask about. That is the whole argument for the index: `git log -S` costs 4 s
per term on git.git and 84–98 s per term on kubernetes, *every time*.

Levers when a repo is too big or too noisy: `--pathspec pkg/ src/` (the strongest — it cuts
the corpus *and* sharpens the signal by dropping docs and scripts), `--since '5 years ago'`,
and `--content-max-commits N` (a hard cap; it makes the index truncated and every report
then says so). Tell the user the scope you chose. Always `clean` when done.

### 2. Raw git for the last mile

The index narrows to a handful of commits; these confirm them. **Always confirm a rename
candidate by reading the diff** — the index tells you a commit removed one name and added
another, not that they mean the same thing.

```bash
git show <sha> -- path/to/file                        # read the actual change — do this
git log -S'OrderLineItem' --oneline --name-status     # pickaxe, straight from git
git log -G'Order(Line)?Item' --oneline                # regex over diff content
git log --follow --oneline -- src/billing/Account.ts  # a file's life across renames
git log --grep='rename' -i --oneline                  # deliberate rename commits
git shortlog -sn -- src/billing/                      # who owns this vocabulary
```

Note on `git log -S` vs the index: pickaxe needs no index and is exact, but it walks the
whole history *per term* — measured at 4 s per term on git.git and 84–98 s per term on
kubernetes. The SQLite index pays that cost once and then answers in ~0.1 s, which is why
it wins as soon as you have more than a couple of names to settle. `--pickaxe-regex` (for
whole-identifier matching) is another ~40× slower again; don't reach for it.

The agent may also use the [investigating-repository-history](../../investigating-repository-history/)
skill when an item needs PR discussion and review comments, not just commits — that
is where the human reasoning behind a rename usually lives.

## Protocol

Run per `## Unresolved` entry, batched — collect all findings, report once.

### Step 1: Scope and build

1. Confirm the repo has usable history: `git rev-list --count HEAD`, and
   `git log --reverse --oneline -1` (how far back does it actually go?).
2. Choose the scope. Default to the full history — that is the point of the index. Reach
   for `--pathspec` when the repo is large or when the unresolved entries name specific
   modules; it is both the cheapest and the sharpest lever.
3. `build --content`. Report what you indexed, over what window, and how long it took.

### Step 2: Gather evidence per entry

For each entry, extract the candidate names from its `**Found in**` / `**Options**`
lines and run `query` on each, then `pair` on the competing set. Collect:

- **Birth order** — which identifier is older; the older one is usually the incumbent,
  the newer one is either a replacement or an unreconciled fork of vocabulary. Read the
  birth commit's subject: a rename usually announces itself there.
- **Dormancy** — the last commit that touched the name. A name nothing has changed in
  years is retired vocabulary, whatever the current tree still contains. `pair` flags this
  and states a displacement hypothesis.
- **Trajectory** — adds vs dels, and mentions per year. Heavy deletions with no recent
  additions means dying: `## Legacy` or an `avoid:` list, not the Index.
- **Swap commits** — `pair` counts the commits that **remove one name while adding the
  other** and lists them first. These are the rename candidates; open them with `git show`.
- **Path split** — `pair` ends with `files: A in N, B in M, both in K`. `both in 0` means no
  file has ever contained both names: two concepts sharing a vocabulary, a candidate bounded
  context — not a rename. `contexts <name>` does the same for a single word and is the
  polysemy check: one word split across two directories is the `Account` billing-vs-auth case.
  **Only claim a path split when one of those commands printed it** — never infer it.
- **Stated intent** — commit messages, PR/issue numbers, and `BREAKING`/`rename`/`migrate`
  wording. Use `search` (BM25) to find the commits that *explain* rather than merely mention.
  A message that says why beats any inference from counts.
- **Ownership** — different authors owning the two spellings, never touching each other's
  files, is drift, not design.

**Worked example 1 — a rename.** `pair sha1_array oid_array` on git.git (60 751 commits, 0.1 s):

```
### `sha1_array`
- born: 2009-05-09 6212b1aae — bisect: use "sha1_array" to store skipped revisions
- last grown:   2017-03-31 910650d2f — Rename sha1_array to oid_array
- signal: dormant ~9.4 years — nothing has *added* it since 2017

- verdict: **RENAME — strong.** `sha1_array` → `oid_array` — net exchange in 1 commit,
  announced in 1 subject.
- subjects that announce it (both names present):
  - 2017-03-31 910650d2f Rename sha1_array to oid_array
```

What carried it: the *last grown* date (not last touched — a stale comment naming the old
identifier was deleted in 2020, long after anyone stopped writing it), plus one commit that
both net-exchanges the names and announces the rename with both names present.

**Worked example 2 — the same machinery at scale.** `pair Minion Node` on kubernetes
(82 704 commits indexed, 1.3 s):

```
### `Minion`
- born: 2014-06-06 2c4b3a562 — First commit
  - caveat: present in the repository's oldest indexed commit — import artefact or a
    common English word, not a naming event
  - signal: dormant ~3.8 years — nothing has *added* it since 2022-11-10

- shared commits: 526 · net exchanges `Minion`→`Node`: 39 (reverse: 2)
  · same-file exchanges: 35 · subjects naming a rename: 6
- verdict: **RENAME — strong.**
- strongest exchanges (same-file ones first):
  - 2014-12-07 19379b5a3 (net -144 `Minion` / +144 `Node`, 35 files swapped in place)
    Internal rename api.Minion -> api.Node
  - 2016-05-05 9d5bac633 (net -146 / +141, 24 files swapped in place) Change minion to node
- files: `Minion` in 525, `Node` in 5574, **both in 363**
  - heavily shared (69% of the smaller set) — they live in the same code, so a rename
    or synonym drift is plausible
```

Neither birth date carried this verdict — both words appear in the repo's first commit and
are flagged as such. What carried it: dormancy, 35 commits that swap the names *inside the
same files*, and six subjects naming both sides. For contrast, the five unrelated k8s pairs
tested alongside it (`Kubelet`/`Scheduler`, `Pod`/`Deployment`, …) reach at most 6 same-file
exchanges in 1 193 shared commits and zero naming subjects — all correctly COEXISTENCE.

**Worked example 3 — polysemy, the case the protocol exists for.** `contexts Account` on a
repo where `billing/` and `auth/` both define an `Account`:

```
## `Account`
- directories (2 total):
  - billing        67%  (8 additions)
  - auth           33%  (4 additions)
- **possible polysemy**: the name is split across `billing` (67%) and `auth` (33%).
  Read one file from each before assuming they mean the same thing.
```

and `pair account_balance account_email`:

```
- verdict: **COEXISTENCE.** No exchange, both still growing.
- files: `account_balance` in 4, `account_email` in 4, **both in 0**
  - **disjoint** — no file has ever contained both. Two concepts that share a
    vocabulary, not two names for one thing. Candidate bounded-context split.
  - `account_balance` by directory: billing 100%
  - `account_email` by directory: auth 100%
```

COEXISTENCE plus a disjoint path split is a real finding — it is the evidence for two
bounded contexts. COEXISTENCE with *shared* files is not: that is synonym drift, and history
cannot settle it. Do not report one as the other.

### What `pair` decides, and how far to trust it

`pair` emits one labelled verdict per pair. The label already encodes the confidence —
**do not upgrade it in your report.**

| Verdict | Emitted when | What to do |
|---------|--------------|------------|
| **RENAME — strong** | Net exchange *and* at least one subject naming **both** sides with rename wording | Propose the Legacy line, citing the announcing commit |
| **RENAME — probable** | Commits swap the names **inside the same files** (with or without the old name having stopped growing earlier), but no subject says so | Read the top commits with `git show` before proposing |
| **RENAME — possible** | Net exchange and the old name stopped growing ≥2 years earlier, but never within one file | Weak. Verify before it goes near the thesaurus |
| **DRIFT / PARTIAL MIGRATION — weak** | Net exchange, never inside one file, both names still being added | Not a settled rename; ask whether the migration should finish |
| **NOT A RENAME** | No meaningful exchange; one name merely stopped growing earlier | An abandoned concept, not a replaced name |
| **COEXISTENCE** | No exchange, both still growing | Two live concepts or synonym drift — settle it with the path split below, not by guessing |

Direction is inferred from the evidence, not from argument order: `pair Cart Basket` and
`pair Basket Cart` both conclude `Basket` → `Cart`. When there is no exchange evidence at
all, the pair is oriented by dormancy so the label cannot flip with argument order either.

**How the thresholds were set** — by falsification, not taste. Each was added after a
measured false positive or false negative on a real repository:

- **Net direction.** The first version flagged "A deleted at all, B added at all". On a real
  repo that labelled **105 of 174** commits touching two unrelated integrations (`jira`,
  `telegram`) as rename candidates — including commits where *both* names were net-removed
  and commits where `jira` actually grew. A swap now needs A to net-shrink by ≥3 and B to
  net-grow by ≥3 in the same commit. That single change took 105 → 2.
- **Noise floor.** Two exchanges out of 145 shared commits (`bisect`/`rebase` in git.git) is
  churn. Exchanges must be ≥2 commits and ≥5% of shared commits to carry a verdict; below
  that they print as "below the noise floor", explicitly not as evidence. Same-file exchanges
  are stronger and clear half that bar — but not no bar: making any same-file swap sufficient
  put `bisect`/`rebase` straight back to RENAME on 2 swaps in 111 shared commits.
- **Both names in the subject.** Accepting one name let "Rename Telegram meeting wrapper"
  certify `club` → `meeting`. Every true announcement names both sides — "Rename sha1_array
  to oid_array", "Change minion to node", "Internal rename api.Minion -> api.Node".
- **Last *grown*, not last touched.** A retired name keeps being deleted for years after
  nobody adds it. git.git's `get_sha1` was last *touched* in 2026 by a commit deleting a
  stale comment; it was last *grown* in 2017.
- **Casing-independent identity.** `query OrderLineItem` returned "never appears" on a
  snake_case repository — a false negative on this skill's own canonical input, since
  thesaurus Identifiers are PascalCase by format. Identifiers now carry a normal form
  computed *before* lowercasing, so all spellings of one concept share it.
- **Concepts, not families, when comparing.** The `Account` set contained `BillingAccount`,
  so B's additions cancelled A's deletions and masked the very exchange being measured.
  Identifiers shared by both sides are dropped from each; `--family` opts into wider matching.
- **Locale and changelog files excluded.** `.po` files made "l10n: zh_CN …" the top rename
  candidate for two unrelated git.git terms; changelog churn did the same on kubernetes.

Measured after those fixes across three repositories: **18 negative controls → zero false
rename verdicts** (the worst reaches 6 same-file exchanges in 1 193 shared commits and no
naming subject), while `sha1_array`→`oid_array`, `get_sha1`→`get_oid`, `Minion`→`Node` and
two synthetic ground-truth repos all still land as RENAME — strong.

**What it cannot do.** `pair` compares *identifiers*. A rename that only moved files
(`sha1_file.c` → `object-file.c`) shows up in `query`'s **file renames** section, not here —
run both. And history never says which name *should* be canonical: it ranks candidates, the
user decides.

### Step 3: Classify each entry

| Evidence pattern | Proposal | Thesaurus effect |
|------------------|----------|------------------|
| One commit removes `A`, adds `B`, message says rename | **Rename**, high confidence | Index line keeps `B`; `` `A` → `B` `` Legacy line |
| `A` dying (dels ≫ adds, no recent adds), `B` growing | **Deprecate `A`**, medium | `B` in the Index; `A` in its `avoid:` or a Legacy line with `in:` paths |
| COEXISTENCE **and** `both in 0` files (disjoint directories) | **Two concepts**, medium | Two Index lines; propose `ctx:` only if the user confirms the invariant test |
| COEXISTENCE with files shared between the names | **Synonym drift**, low | History cannot separate these; take it to the user |
| Both alive, same paths, interchangeable in diffs | **Synonym drift**, medium | One Index line; the loser joins `avoid:` |
| `A` born once, never touched again, only in tests/migrations | **Obsolete**, high | Not in the Index at all; note for cleanup |
| Nothing conclusive | **Unresolved**, stays | Keep the entry; append a `**History**` line with what was found |

Confidence is part of every proposal. Say `low` when the only evidence is counts.

### Step 4: Report and let the user decide

One batch report, ordered by impact (files affected), each item citing its commits:

```
History mining — 5 unresolved items, 3 resolvable:

1. `User` vs `Customer` — RENAME, high confidence
   `Customer` born 2023-11-04 (a41f2c9 "rename User→Customer in domain layer");
   `User` has 0 additions since, 41 deletions. 3 files still use it: api/v1/*.
   → Propose: Index `Customer`; Legacy line `User` → `Customer` in: `api/v1/`.

2. `Account` billing/ vs auth/ — TWO CONCEPTS, medium confidence
   Born in unrelated commits (2021-03 by @alice in billing/, 2022-08 by @bob in
   auth/), never co-edited, no shared fields. Reads as parallel vocabularies.
   → Propose: BillingAccount + UserAccount, or contexts Billing / Identity.
     Needs the invariant test — an invariant true inside one and not the other?

3. `Status` vs `State` — INCONCLUSIVE
   Both grow steadily, same modules, no rename commit. History cannot settle this.
   → Still needs your call. Recorded what was found under the entry.

Apply 1 and 2 as proposed?
```

Apply only what the user approves. Then delete the index (`clean`) and say so.

### Step 5: Record the provenance

The thesaurus is "reconstructed, not authored" — a resolution mined from history is
still a reconstruction, and readers must be able to check it. When a history-mined
decision lands in the thesaurus, cite it:

- On a `## Legacy` line, the note field carries the commit:
  `` - `User` → `Customer` in: `api/v1/` — renamed in a41f2c9 (2023-11-04) ``
- On an entry, an optional line:
  `- **History**: split from `Account` in 8e21f0b (2022-08); billing/ and auth/ never co-edited`
- On an entry that stays in `## Unresolved`, the same `**History**` line records what was
  ruled out, so the next run does not repeat the work.

These are prose lines inside entries and the free-text tail of Legacy lines — they add
no new tokens and do **not** change the thesaurus format (still `2.0`).

## Failure modes to state out loud

- **Squashed / imported history.** If most files trace back to one "initial commit", birth
  dates are meaningless. Check with `git log --diff-filter=A --oneline -- <path> | tail -1`
  before trusting any "born" date, and say so in the report. A term whose birth commit is
  the repo's first commit is almost always an import artefact, not a naming event.
- **A common English word is not an identifier.** `Node`, `Item`, `State`, `Order` occur in
  comments, docs and unrelated code. Their "birth" is usually noise; their *dormancy* and
  *swap commits* are still meaningful. Prefer the compound form (`OrderLineItem`,
  `oid_array`) when one exists, and scope with `--pathspec` to the domain layer.
- **Bulk reformatting and mass renames** (a linter run, a directory move) inflate token
  counts across the board. A commit touching hundreds of files is not vocabulary evidence —
  discount it.
- **Vendored, generated and minified files** dominate token counts. They are excluded by
  default; if you pass `--no-default-excludes`, expect the signal to degrade.
- **Side branches** carry release notes, status files and imported trees. The index walks
  HEAD by default for that reason — `--all-refs` is opt-in and noisier.
- **Shallow clones** (`git rev-parse --is-shallow-repository` → `true`) have no early
  history. The build prints a warning and every report repeats it; treat every date as a
  lower bound rather than a birth.
- **A truncated diff index lies about birth.** If `--content-max-commits` was used, every
  report says so — pass that caveat on to the user instead of quoting the date as a birth.
- **The index is a snapshot** keyed to the HEAD sha *and the build scope*; rebuild with
  `--refresh` after new commits land. Changing `--pathspec`/`--since`/`--all-refs` rebuilds
  automatically rather than silently reusing a narrower index.
- **One index per repository path.** Two agents mining the same checkout at once will delete
  each other's index; pass `--index-file` to give a second session its own.
- **Never resolve silently.** History moves an item from "unknown" to "probable". The user
  moves it to "decided".
