# Threat model: promises that must survive a hostile caller

How to find, at design time, the outcomes a caller could force on purpose, and to put each
guarantee where that caller cannot get around it.

## Contents

- [When this is worth doing](#when-this-is-worth-doing)
- [Draw what the change exposes](#draw-what-the-change-exposes)
- [Six questions](#six-questions)
- [From a threat to a property card](#from-a-threat-to-a-property-card)
- [Where the mechanism lives](#where-the-mechanism-lives)
- [Record](#record)
- [What this is not](#what-this-is-not)

## When this is worth doing

The failure model in `failure-and-recovery.md` assumes honest parties and bad luck: a lost
response, a crash, a second writer. A threat model adds a party that picks the worst sequence on
purpose. Do it while the contract and the data model can still change. A threat found in review
is a redesign.

Triggers:

- a new entry point reachable from outside the trust boundary: an endpoint, a webhook, a queue
  others can publish to, a file or document the system parses;
- a change in who may read or do what: roles, ownership, sharing, tenancy;
- newly stored data that harms someone if read or altered: personal data, credentials, money;
- an agent or automation that reads content it does not control and holds tools or credentials.

No trigger, no threat model. It is sized like the rest of the method: for one endpoint this is
ten minutes and a few lines.

## Draw what the change exposes

One paragraph before any category:

- **the boundary:** what becomes reachable, and by which route;
- **the callers:** anonymous, authenticated, another tenant, an internal service, an
  administrator;
- **the assets:** what it reads, writes, returns and triggers downstream;
- **the trust boundary:** the line past which data is no longer checked by this system.

Ask: if this component did the worst thing a caller could make it do, what would be lost?

## Six questions

STRIDE is a lens for finding forbidden outcomes, not a form to fill. For each letter, ask whether
this change makes the outcome possible. Dismiss a category in one line when it does not apply.

| Threat | Question | Typical mechanism |
|---|---|---|
| **Spoofing** | Can a caller act as someone else? | Authentication by an established provider, never a home-made credential check |
| **Tampering** | Can data be changed in transit, at rest, or through input that reaches a query or a command? | TLS; parameterised queries; checks on the server; no trust in state the client holds |
| **Repudiation** | Can someone deny an action, with nothing to show otherwise? | An attributable, append-only record of every state-changing action |
| **Information disclosure** | Can a caller read what is not theirs: another tenant's rows, internals in an error, a secret in a log, whether an account exists? | Explicit response fields; authorisation on every read; scrubbed errors and logs |
| **Denial of service** | Can one caller exhaust what the others need? | Limits on rate, size and depth; timeouts; a retry budget; costly work only behind authentication |
| **Elevation of privilege** | Can a caller do more than they were granted? | Authorisation on the server for every action; least privilege for the process and its credentials |

When an agent or automation is in scope, add three lists: the untrusted text it reads
(repository, issue, web page, tool output); the tools, files, network and credentials it holds;
its actions that cannot be undone, and who approves them. Text it reads is data, never
instructions.

## From a threat to a property card

A threat that applies is a promise with an adversary in its counterexample. Write it as the
property card of `SKILL.md`:

- **Property:** the outcome that must not happen ("a user never reads another tenant's
  invoice");
- **Counterexample:** the shortest sequence a hostile caller would try (a guessed identifier, a
  replayed request, a second request racing the permission change, an oversized body), and the
  exact point where the mechanism stops it;
- **Mechanism:** where the check lives, who owns it, and why no other route gets around it;
- **Limits:** the nearest attack the mechanism does not stop, and who accepted that.

Two rules of the method apply here with more force:

- **A guarantee lives where its violation is controlled.** That is the server and the data, not
  the client and not the user interface. A hidden button protects nothing.
- **A check on one route is no guarantee while a second route reaches the same asset.** List
  every entry point to the asset: the API, the background job, the export, the admin tool, the
  restore.

## Where the mechanism lives

Some mitigations are code (authorisation, parsing at the boundary, parameterised queries, audit
records). Some are infrastructure (TLS, network limits, least-privilege accounts). Some are a
business decision (how much friction a sign-up may carry). Name the owner of each.

A threat knowingly accepted or deferred is a valid outcome when the one who bears the risk
accepted it, by name and with a date. The designer does not accept it for them.

## Record

For each threat that applied, one line next to the design record: mitigated (where), accepted
(by whom), or deferred (owner and date). Reopen it when a new entry point or a new kind of
caller is added.

## What this is not

Not a security audit of existing code, a penetration test or a compliance review: those need a
dedicated security skill or reviewer. And not a reason to add a mechanism that none of the six
questions asked for.
