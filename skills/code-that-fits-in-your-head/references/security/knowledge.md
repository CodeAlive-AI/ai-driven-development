# Security Knowledge

Core concepts for threat-modelling software with STRIDE. Security is part of design, not an ops afterthought that gets bolted on.

## Overview

Software security is like insurance: you don't want to pay for it, but if you don't, you'll be sorry. There is no such thing as a completely secure system; security engineering is about finding an appropriate balance of risks, mitigations, and cost. Programmers own a specific slice of that balance (code-level defences) and share the rest with IT professionals and business stakeholders.

## STRIDE

**Definition**: A threat-modelling acronym developed at Microsoft, used as a checklist to enumerate threats against a system. Each letter names one category of threat. You walk through each letter and ask "is this system vulnerable to this?" then decide on a mitigation (or an explicit decision to accept the risk).

STRIDE is a thought exercise or workshop, informal or systematic. It brings programmers, IT professionals, and business owners together because mitigations live in different layers: some in code, some in network configuration, and some are business decisions.

## The Six Threat Categories

### Spoofing

**Definition**: Attackers pose as someone they are not to gain unauthorised access.

**Example**: A reservation API that accepts any name means a caller can make a booking under "Keanu Reeves". Whether that matters depends on whether the system makes decisions based on identity.

**Typical mitigation**: Authentication. Use an established identity provider (OAuth, OpenID Connect, JWT) rather than a home-grown password check.

### Tampering

**Definition**: Attackers modify data in transit or at rest without authorisation.

**Example**: A man-in-the-middle intercepts an HTTP response containing a resource URL and uses it to `DELETE` someone else's record. Or an attacker injects SQL through an unsanitised query to rewrite rows.

**Typical mitigation**: Integrity checks (HTTPS/TLS, hashes, digital signatures), parameterised SQL queries, never trusting client-side state.

### Repudiation

**Definition**: Attackers (or regular users) deny performing an action, with no evidence to refute them.

**Example**: A user makes a restaurant reservation and then never shows up, later claiming they never booked. Doctors, hairdressers, and ticketing systems all suffer this.

**Typical mitigation**: Audit logs attributable to an authenticated identity; digital signatures; pre-authorisation charges. Mitigations must be balanced against user friction.

### Information Disclosure

**Definition**: Attackers read data they should not have access to.

**Example**: A schedule endpoint returns names and email addresses of all guests for a day. Without authentication, anyone could harvest that PII. Resource URLs that double as capability tokens are also sensitive - possession is authorisation.

**Typical mitigation**: Encryption in transit (HTTPS), access control on sensitive endpoints, treating resource URLs as secrets, parameterised SQL, explicit PII handling.

### Denial of Service

**Definition**: Attackers make the system unavailable for legitimate users.

**Example**: A distributed flood of requests overwhelms capacity when concert tickets go on sale. Historically, buffer overflows in C/C++ code were a common DoS vector; managed languages largely remove that class.

**Typical mitigation**: Rate limiting, request timeouts, payload size caps, keeping the runtime patched, architectural choices like CQRS with durable queues for write spikes. Full mitigation of distributed attacks is typically an IT/infra problem.

### Elevation of Privilege

**Definition**: Attackers gain more permissions than they were granted - for example, a regular user becoming an administrator.

**Example**: SQL injection that lets an attacker run arbitrary SQL can often spawn operating system processes (e.g. `xp_cmdshell` on SQL Server). A database running as root then hands the attacker the host.

**Typical mitigation**: Principle of least privilege - services run with the minimum permissions needed. Never run the database as administrator. Separate authentication (who you are) from authorisation (what you can do).

## Where Mitigations Live

| Threat | Primary layer | Developer owns? |
|--------|---------------|-----------------|
| Spoofing | Auth middleware / identity provider | Partial (wire up, don't hand-roll) |
| Tampering (SQL injection) | Code | Yes |
| Tampering (MITM) | Infra (HTTPS) | No, but insist on it |
| Repudiation | Code (audit logs) + business process | Yes |
| Information Disclosure | Code (access control) + infra (TLS) | Shared |
| Denial of Service | Infra (rate limit, capacity) + architecture | Shared |
| Elevation of Privilege | Infra (least-privilege accounts) + code (SQL injection) | Shared |

## Key Ideas

- **Security is a design concern, not a ﬁnal polish.** Thread it through stories, reviews, and pair programming from the start.
- **It is a balance.** A system so secure it cannot be used fails its purpose. Accept some risk explicitly.
- **Know which threats are yours.** Programmers can reliably own SQL injection, audit logging, access control, and input validation. Network-layer DoS usually is not yours.
- **A threat identified and knowingly deferred is a valid outcome** - as long as the rest of the organisation understands the risk.

## Terminology

| Term | Definition |
|------|------------|
| STRIDE | Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege |
| Threat model | Structured enumeration of how a system could be attacked |
| PII | Personally Identifiable Information (names, emails, addresses) |
| Least privilege | A component gets only the permissions it strictly needs |
| Authn / Authz | Authentication (who are you) vs Authorisation (what can you do) |
