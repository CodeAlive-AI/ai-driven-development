# Security Rules

Actionable rules for applying STRIDE at code level. One section per threat category.

## Spoofing

### 1. Require authentication for anything that matters

If the system makes a decision based on identity, that identity must be authenticated. If it does not matter who the caller is (e.g. a public reservation form that only records a name), document that choice explicitly.

### 2. Use established identity providers

Do not hand-roll password checks, session tokens, or cryptographic primitives. Plug into an existing provider (OAuth 2.0 / OpenID Connect, JWT with a trusted issuer, a platform identity service).

- Validate tokens on every request, including signature, issuer, audience, and expiry.
- Treat role/scope claims as the authorisation source, not raw user IDs.

### 3. Keep the decision to require auth at the endpoint

Do not defer "should this be protected?" to infra. Mark the endpoint and write an integration test that a call without a valid token gets `401` or `403`.

**Example** (C#, xUnit):
```csharp
[Fact]
public async Task ScheduleRequiresAuth()
{
    using var api = new SelfHostedApi();
    var client = api.CreateClient(); // no token
    var actual = await client.GetSchedule("Nono", 2021, 12, 6);
    Assert.Equal(HttpStatusCode.Unauthorized, actual.StatusCode);
}
```

## Tampering

### 1. Always use parameterised queries

Never concatenate user input into SQL. Use named or positional parameters so the driver escapes values.

**Example** (C# / ADO.NET):
```csharp
// Bad - string concatenation, SQL injection vulnerable
var sql = $"DELETE [dbo].[Reservations] WHERE [PublicId] = '{id}'";

// Good - named parameter
const string deleteSql = @"
    DELETE [dbo].[Reservations]
    WHERE [PublicId] = @id";
using var cmd = new SqlCommand(deleteSql, conn);
cmd.Parameters.AddWithValue("@id", id);
```

### 2. Require HTTPS; do not make TLS optional

A plaintext HTTP endpoint exposes every request and response to MITM tampering. Redirect HTTP to HTTPS at the edge, and refuse HTTP in production config.

### 3. Never trust client-side state

Any value the client sends (IDs, prices, flags, role claims outside signed tokens) is tamperable. Re-validate on the server. Do not read authorisation decisions from a request body.

### 4. Use opaque, high-entropy resource identifiers

Where resource URLs double as capability tokens, make the ID unguessable - a GUID is a 128-bit number, effectively equivalent to a cryptographic key. Sequential integer IDs are trivially enumerable.

## Repudiation

### 1. Log every state-changing action with an attributable identity

Create, update, delete, money movements, and permission changes must be logged with: who, what, when, and what changed. If the caller is anonymous, log that too and raise it as a threat.

### 2. Make audit logs tamper-evident

Audit logs should be append-only where possible. Ship them to a separate store so a compromised service cannot rewrite its own history.

### 3. Do not let a user deny a recorded action without evidence

If repudiation is a real risk (payments, contracts), consider stronger mechanisms: digital signatures on submitted data, pre-authorisation via credit card, cryptographic receipts.

### 4. Balance friction against value

Requiring every restaurant guest to authenticate would scare customers away. Pick the smallest mitigation that covers the threat at an acceptable UX cost, and let stakeholders sign off.

## Information Disclosure

### 1. Minimise what you expose

An endpoint should return the smallest projection a caller needs. Do not dump full rows "because they might be useful".

### 2. Require authentication for any endpoint that returns PII or sensitive data

```csharp
// Schedule endpoint exposes names and emails -> require JWT with MaitreD role
var token = new JwtTokenGenerator(new[] { restaurantId }, "MaitreD")
    .GenerateJwtToken();
```

Write an integration test that proves a caller without the right role gets `403 Forbidden`.

### 3. Do not log secrets

Never write passwords, tokens, API keys, full card numbers, session cookies, or raw JWTs to logs. Scrub them before they reach the log pipeline.

### 4. Be explicit about PII

Mark fields containing PII (email, name, phone, address). Apply it in code (so reviewers see it), in storage (encryption or column-level protection if needed), and in retention policies.

### 5. Treat sensitive URLs as secrets

If possessing a URL is equivalent to holding a capability (e.g. a reservation edit link), send it only over HTTPS and do not leak it in referer headers, error messages, or analytics.

## Denial of Service

### 1. Rate-limit public endpoints

Cap requests per IP / per token / per account. Do this at a gateway where possible, but have a code-level fallback for anything critical.

### 2. Set timeouts on every outbound call

No call to a database, HTTP service, or queue should be allowed to hang forever. Set a bounded timeout and handle the failure.

### 3. Cap payload sizes and collection lengths

Reject requests larger than a sensible limit. Validate that arrays/lists in a body are below a maximum count before iterating.

### 4. Prefer managed languages for new services

Buffer overflows that crash a process are largely a property of unmanaged code. In managed runtimes, keep the platform patched; a DoS via overflow there is a platform bug, not yours.

### 5. For write-heavy spike workloads, consider CQRS

If the system must survive thousands of writes per second (ticketing, flash sales), enqueue writes to a durable queue and read from materialised views. This is a significant architectural commitment - only take it when the ROI is clear.

## Elevation of Privilege

### 1. Principle of least privilege

Every service, database user, and OS account gets only the permissions it actually needs. The app's database user should be able to `SELECT`/`INSERT`/`UPDATE`/`DELETE` on its tables - not `CREATE USER`, not `xp_cmdshell`, not `sysadmin`.

### 2. Do not run as root / administrator

Production containers and services should run as a non-root user. The database should never run as OS administrator. A privilege-escalation bug in a process running as root hands over the host.

### 3. Separate authentication from authorisation

Authentication answers "who are you?". Authorisation answers "can you do this?". Keep them as distinct steps: validate the token first, then check role/scope claims against the requested action.

### 4. Close SQL injection paths (again)

SQL injection is not just a tampering issue - it is also the most common elevation vector. A single unparameterised query can end in OS command execution. See Tampering rule 1.

### 5. Disable dangerous stored procedures

Never enable `xp_cmdshell` on SQL Server (it is disabled by default since 2005 - keep it that way). Audit similar capabilities on other databases.

## Quick Reference

| STRIDE | Core rule | Layer |
|--------|-----------|-------|
| S | Require auth; use an identity provider | Code |
| T | Parameterised SQL; mandatory HTTPS; opaque IDs | Code + Infra |
| R | Attributable audit logs for state changes | Code |
| I | Minimise data; auth PII endpoints; no secrets in logs | Code |
| D | Rate-limit; timeouts; payload caps | Code + Infra |
| E | Least privilege; non-root; separate authn/authz | Infra + Code |
