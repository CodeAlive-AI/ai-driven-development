# STRIDE Threat-Model Checklist

Use this when adding a new endpoint, feature, or service. Walk every STRIDE letter. For each threat, answer: did we consider it, what is the mitigation, and does it live in code or infra? Process steps live in `workflows/threat-model.md`.

## S - Spoofing

- [ ] Is authentication required? If not, is that an explicit, documented decision?
- [ ] Established identity provider (OAuth / OIDC / JWT), not a hand-rolled password check?
- [ ] Token validation complete (signature, issuer, audience, expiry)?
- [ ] Integration test: unauthenticated calls get `401`?
- [ ] **Mitigation:** ______________________________________
- [ ] **Lives in:** [ ] code  [ ] infra  [ ] both

## T - Tampering

- [ ] HTTPS mandatory (no plaintext fallback)?
- [ ] All SQL queries parameterised (no string concatenation of user input)?
- [ ] Server re-validates every client-supplied value (no blind trust in request bodies)?
- [ ] If resource URLs are capability tokens, are IDs unguessable (GUIDs / 128-bit)?
- [ ] **Mitigation:** ______________________________________
- [ ] **Lives in:** [ ] code  [ ] infra  [ ] both

## R - Repudiation

- [ ] Every state-changing operation writes an audit log (who, what, when, before/after)?
- [ ] Caller's identity attributable in the log (not just "anonymous")?
- [ ] Audit logs append-only / shipped to a store the service cannot rewrite?
- [ ] Real-world consequences (payment, contract) → stronger signal needed (signed submission, pre-auth)?
- [ ] **Mitigation:** ______________________________________
- [ ] **Lives in:** [ ] code  [ ] infra  [ ] both

## I - Information Disclosure

- [ ] Response is the minimum projection the caller needs (no extra PII "just in case")?
- [ ] Authn + authz required for PII/sensitive endpoints (`403` test for wrong-role)?
- [ ] Secrets (passwords, tokens, API keys, raw JWTs) never logged?
- [ ] Sensitive URLs kept out of logs, referer headers, and error messages?
- [ ] **Mitigation:** ______________________________________
- [ ] **Lives in:** [ ] code  [ ] infra  [ ] both

## D - Denial of Service

- [ ] Rate limit on this endpoint (per IP, per token, or per account)?
- [ ] Every outbound call (DB, HTTP, queue) has a bounded timeout?
- [ ] Maximum payload size / maximum array length for bulk operations?
- [ ] Fully distributed DoS raised with IT / infra when applicable?
- [ ] **Mitigation:** ______________________________________
- [ ] **Lives in:** [ ] code  [ ] infra  [ ] both

## E - Elevation of Privilege

- [ ] Service runs with minimum privileges (non-root / non-admin DB user)?
- [ ] Authentication and authorisation are separate, explicit steps?
- [ ] Role/scope claims read only from a signed, validated token — never from body/header the client controls?
- [ ] Dangerous database features (e.g. `xp_cmdshell`) disabled; SQL injection paths closed?
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
