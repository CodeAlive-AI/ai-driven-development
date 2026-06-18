# STRIDE Threat-Model Checklist

Use this when adding a new endpoint, feature, or service. Walk every STRIDE letter. For each threat, answer three questions: did we consider it, what is the mitigation, and does the mitigation live in code or in infra?

## Before You Start

- [ ] I can describe the feature in one sentence (what it does, who calls it, what data it touches).
- [ ] I have identified the sensitive data in scope: PII, credentials, money, capability URLs.
- [ ] I know whether the caller is authenticated and, if so, what identity provider issues the token.
- [ ] I have a stakeholder I can ask if a mitigation is business-acceptable.

## S - Spoofing

- [ ] Did we consider whether a caller could claim a false identity?
- [ ] Is authentication required? If not, is that an explicit, documented decision?
- [ ] Are we using an established identity provider (OAuth / OIDC / JWT) rather than a hand-rolled password check?
- [ ] Is token validation complete (signature, issuer, audience, expiry)?
- [ ] Is there an integration test that unauthenticated calls get `401`?
- [ ] **Mitigation:** ______________________________________
- [ ] **Lives in:** [ ] code  [ ] infra  [ ] both

## T - Tampering

- [ ] Did we consider whether data in transit could be modified?
- [ ] Is HTTPS mandatory for this endpoint (no plaintext fallback)?
- [ ] Did we consider whether data at rest could be modified by an unauthorised party?
- [ ] Are all SQL queries parameterised (no string concatenation of user input)?
- [ ] Do we re-validate every client-supplied value on the server (no blind trust in request bodies)?
- [ ] If resource URLs are capability tokens, are the IDs unguessable (GUIDs / 128-bit)?
- [ ] **Mitigation:** ______________________________________
- [ ] **Lives in:** [ ] code  [ ] infra  [ ] both

## R - Repudiation

- [ ] Did we consider whether a user could later deny performing an action here?
- [ ] Does every state-changing operation write an audit log entry (who, what, when, before/after)?
- [ ] Is the caller's identity actually attributable in the log (not just "anonymous")?
- [ ] Are audit logs append-only and shipped to a store the service cannot rewrite?
- [ ] If the action carries real-world consequences (payment, contract), do we need a stronger signal (signed submission, pre-authorisation)?
- [ ] Have we balanced friction against UX with a stakeholder?
- [ ] **Mitigation:** ______________________________________
- [ ] **Lives in:** [ ] code  [ ] infra  [ ] both

## I - Information Disclosure

- [ ] Did we inventory what the response contains? Is any of it PII, credentials, financial, or capability data?
- [ ] Is the response the minimum projection the caller needs (no extra fields "just in case")?
- [ ] Is authentication + authorisation required for PII or sensitive endpoints? Integration test covering `403` for wrong-role callers?
- [ ] Is HTTPS mandatory to prevent MITM reads?
- [ ] Have we confirmed that secrets (passwords, tokens, API keys, raw JWTs) never get logged?
- [ ] Have we marked PII fields explicitly and applied retention/encryption rules?
- [ ] Are sensitive URLs kept out of logs, referer headers, and error messages?
- [ ] **Mitigation:** ______________________________________
- [ ] **Lives in:** [ ] code  [ ] infra  [ ] both

## D - Denial of Service

- [ ] Did we consider what happens under 10x, 100x, or malicious traffic?
- [ ] Is there a rate limit on this endpoint (per IP, per token, or per account)?
- [ ] Does every outbound call (DB, HTTP, queue) have a bounded timeout?
- [ ] Is there a maximum payload size? A maximum array length for bulk operations?
- [ ] For spike workloads, have we considered a queue + materialised view architecture?
- [ ] Is the platform/runtime patched (so we are not carrying unfixed platform-level DoS bugs)?
- [ ] For fully distributed DoS: have we raised this with IT / the infra team?
- [ ] **Mitigation:** ______________________________________
- [ ] **Lives in:** [ ] code  [ ] infra  [ ] both

## E - Elevation of Privilege

- [ ] Did we consider whether a regular user could acquire permissions they were not granted?
- [ ] Does this service run with the minimum privileges it needs (non-root / non-admin DB user)?
- [ ] Are authentication and authorisation separate, explicit steps?
- [ ] Have we closed SQL injection paths (see Tampering)?
- [ ] Are dangerous database features (e.g. `xp_cmdshell`) disabled?
- [ ] If a request carries a role/scope claim, is it read only from a signed, validated token - never from a body field or header the client controls?
- [ ] **Mitigation:** ______________________________________
- [ ] **Lives in:** [ ] code  [ ] infra  [ ] both

## Red Flags

Stop and address before shipping if you see:

- A SQL query built by string concatenation or interpolation of request data.
- An endpoint returning PII with no auth check, or with auth deferred entirely to infra.
- Secrets, tokens, or full request bodies written to application logs.
- A service container running as root, or a database user with admin/sysadmin rights.
- A state-changing action that writes no audit log.
- Unlimited payloads, unbounded outbound calls, or no rate limit on a public write endpoint.
- A role or permission read from the request body instead of a signed token claim.
- Sequential integer IDs used as capability tokens.
- HTTP allowed alongside HTTPS with no forced redirect.

## Outcome

For each STRIDE letter you should be able to answer one of:

1. **Mitigated in code** - describe how, link tests.
2. **Mitigated in infra** - describe how, name the owner.
3. **Knowingly deferred** - describe the residual risk and who signed off.

A threat identified and explicitly accepted is a valid outcome. A threat that was never considered is not.

## Quick Reference

| Letter | One-line check | Typical layer |
|--------|----------------|---------------|
| S | Auth required? Real identity provider? | Code |
| T | Parameterised SQL + HTTPS + server-side re-validation? | Code + Infra |
| R | Attributable audit log on state changes? | Code |
| I | Minimal response + auth on PII + no secrets in logs? | Code |
| D | Rate limits + timeouts + payload caps? | Code + Infra |
| E | Least privilege + authn/authz separate + no SQL injection? | Infra + Code |
