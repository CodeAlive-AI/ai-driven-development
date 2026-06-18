# Threat Model Workflow (STRIDE)

Walk a new endpoint or service through the six STRIDE threats and decide mitigations.

## Table of Contents

- [When to Use](#when-to-use)
- [Prerequisites](#prerequisites)
- [Step 1: Describe the Component](#step-1-describe-the-component)
- [Step 2: Spoofing — Who's Calling?](#step-2-spoofing--whos-calling)
- [Step 3: Tampering — Can Data Be Modified?](#step-3-tampering--can-data-be-modified)
- [Step 4: Repudiation — Can Actions Be Denied?](#step-4-repudiation--can-actions-be-denied)
- [Step 5: Information Disclosure — What Leaks?](#step-5-information-disclosure--what-leaks)
- [Step 6: Denial of Service — Can It Be Overwhelmed?](#step-6-denial-of-service--can-it-be-overwhelmed)
- [Step 7: Elevation of Privilege — Can Someone Gain Access They Shouldn't?](#step-7-elevation-of-privilege--can-someone-gain-access-they-shouldnt)
- [Step 8: Record Decisions](#step-8-record-decisions)
- [Quick Checklist](#quick-checklist)
- [Common Mistakes](#common-mistakes)
- [Exit Criteria](#exit-criteria)

## When to Use

- Adding a new HTTP endpoint, RPC, or any externally reachable service
- Reviewing a PR that exposes new attack surface
- Before shipping anything that handles untrusted input or holds sensitive data
- Periodically on a running service (e.g. yearly audit)

## Prerequisites

- A description of the component under review (endpoint, service, integration)
- Awareness of what data the component handles and who can reach it

**Primary references**: `references/security/knowledge.md`, `references/security/rules.md`, `references/security/checklist.md`

---

## Workflow Steps

### Step 1: Describe the Component

**Goal**: One paragraph: what is this, who reaches it, what does it touch?

- [ ] Name the component and its boundary (URL / topic / queue)
- [ ] List callers: who reaches it (public users? internal services? admins?)
- [ ] List data: what does it read / write / return? Any PII or secrets?
- [ ] List integrations: what does it call downstream?

**Ask**: "If this component is compromised, what gets lost?"

---

### Step 2: Spoofing — Who's Calling?

**Goal**: Can the component verify identity?

- [ ] Is authentication required? (If not, justify why.)
- [ ] Is it using an established identity provider (OAuth, OIDC, cloud IAM), not a home-grown check?
- [ ] Are credentials sent over TLS only?
- [ ] For service-to-service: mTLS or signed tokens?

**Mitigation examples**: OAuth2 / OIDC, mutual TLS, API keys rotated via secret manager, SPNEGO.

**Reference**: `references/security/rules.md` (Spoofing section)

---

### Step 3: Tampering — Can Data Be Modified?

**Goal**: Ensure no attacker can silently change data in transit or at rest.

- [ ] TLS for all external communication?
- [ ] Client-side state (cookies, JWTs) — signed / HMAC'd?
- [ ] Database writes — access control checked server-side (never trust the client)?
- [ ] Binary artefacts (uploads, downloads) — checksummed / signed?
- [ ] SQL queries — parameterised (no string concatenation)?

**Mitigation examples**: Signed JWTs, parameterised queries, prepared statements, content-hash checks.

**Reference**: `references/security/rules.md` (Tampering section)

---

### Step 4: Repudiation — Can Actions Be Denied?

**Goal**: Log enough to prove who did what.

- [ ] Security-relevant events logged (auth success/failure, privilege changes, admin actions)?
- [ ] Logs are append-only / tamper-evident / shipped off-host quickly?
- [ ] Timestamps are server-side and from a trusted clock?
- [ ] User identity in every audit line (not just session ID)?

**Mitigation examples**: Structured audit log stream, centralised log store with WORM semantics.

**Reference**: `references/security/rules.md` (Repudiation section), `references/separation-of-concerns/patterns.md` (Decorator for audit logging)

---

### Step 5: Information Disclosure — What Leaks?

**Goal**: Minimise exposure of sensitive data.

- [ ] What fields does the endpoint return — any over-fetching of PII?
- [ ] Error responses: do they leak internals (stack traces, SQL)?
- [ ] Logs: any secrets / tokens / PII written to them?
- [ ] Responses to unauthenticated requests — any info about the system (e.g. "user X exists")?
- [ ] Data at rest encrypted? Data in transit encrypted?

**Mitigation examples**: Response DTOs with explicit fields (not domain objects), generic error pages, log scrubbing, at-rest encryption.

**Reference**: `references/security/rules.md` (Information Disclosure section)

---

### Step 6: Denial of Service — Can It Be Overwhelmed?

**Goal**: Survive or gracefully degrade under load / abuse.

- [ ] Request rate limits (per-IP / per-key)?
- [ ] Payload size limits (body size, collection sizes, nesting depth)?
- [ ] Query timeouts end-to-end?
- [ ] Downstream circuit breakers / retry budgets?
- [ ] Any expensive operations exposed without auth (regex, crypto, image processing)?

**Mitigation examples**: WAF, rate limiter, timeouts, circuit breakers, request body size caps, query cost limits.

**Reference**: `references/security/rules.md` (Denial of Service section)

---

### Step 7: Elevation of Privilege — Can Someone Gain Access They Shouldn't?

**Goal**: Principle of least privilege throughout.

- [ ] The process runs as the minimum privileged user (not root)?
- [ ] Every authorisation check happens server-side (never trust "I'm an admin" from the client)?
- [ ] Auth checks happen on every action, not just login?
- [ ] Role / permission boundaries enforced at the data layer, not only in the UI?
- [ ] Secrets scoped to just what this service needs?

**Mitigation examples**: Per-request authZ middleware, row-level security in DB, scoped service accounts.

**Reference**: `references/security/rules.md` (Elevation of Privilege section)

---

### Step 8: Record Decisions

**Goal**: Make the threat model reviewable and revisitable.

- [ ] For each of the six threats, record: mitigated / accepted / deferred, and why
- [ ] Link to the code locations that implement each mitigation
- [ ] Name owners for any deferred items
- [ ] Schedule a re-review for next major change

**Reference**: `references/security/checklist.md`

---

## Quick Checklist

```
[ ] Step 1: Component described (boundary, callers, data, integrations)
[ ] Step 2: Spoofing — authn in place
[ ] Step 3: Tampering — integrity, TLS, parameterised queries
[ ] Step 4: Repudiation — audit logs
[ ] Step 5: Information Disclosure — minimise, encrypt, scrub
[ ] Step 6: Denial of Service — rate limits, timeouts, caps
[ ] Step 7: Elevation of Privilege — least privilege, server-side authZ
[ ] Step 8: Decisions recorded with owners
```

---

## Common Mistakes

| Mistake | Why It's Bad | Do Instead |
|---------|--------------|------------|
| "We have a WAF, we're safe" | A WAF doesn't replace authZ or input validation | Defence in depth; fix at each layer |
| Rolling custom crypto / auth | Almost always broken | Use vetted libraries, standard protocols |
| Writing "TODO: fix later" and shipping | Almost always ships without the fix | Deferred decisions get an owner + date |
| Threat-modelling in isolation | Misses context | Include infra + product people who know callers |
| Treating STRIDE as a form to fill | Missed real risks | Use it as a lens; dig into concrete scenarios |

---

## Exit Criteria

Threat model is done when:
- [ ] All six STRIDE categories have a recorded decision (mitigated / accepted / deferred)
- [ ] Every "mitigated" has a code pointer
- [ ] Every "deferred" or "accepted" has an owner and a date
- [ ] The document is stored where PRs that touch this area can re-reference it
