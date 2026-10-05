# Security audit

- **Bar:**
  - the OWASP Top 10 categories as the checklist;
  - for a deeper pass, OWASP ASVS level 1.
- **Tools:**
  - `npm audit` and `dotnet list package --vulnerable`;
  - Dependabot or Renovate alerts;
  - a secret scan over the whole git history (gitleaks);
  - the response headers in DevTools;
  - an OWASP ZAP baseline scan, only against your own app.

Defense only: you check that the protections are in place.

## Backend
- [ ] Sign-in comes from the framework (ASP.NET Core Identity) or a provider, not hand-made. The framework hashes the passwords.
- [ ] Every endpoint checks authorization, and every object checks its owner. Access is denied by default.
- [ ] Input is validated on the server, whatever the frontend already checked.
- [ ] SQL only through parameters or EF Core, never built from strings.
- [ ] Secrets live in environment variables or a secret manager, and none appear anywhere in the git history.
- [ ] Errors return Problem Details, without stack traces.
- [ ] Rate limits on sign-in, sign-up, password reset and expensive endpoints.
- [ ] CORS allows only your own origins. Cookies are `Secure`, `HttpOnly` and `SameSite`.
- [ ] Logs hold no passwords, tokens or personal data.
- [ ] HTTPS only, with HSTS.
- [ ] Uploads have size and type limits, and are stored outside the web root.

## Frontend
- [ ] The session lives in an `HttpOnly` cookie, not in `localStorage`.
- [ ] User content never reaches `dangerouslySetInnerHTML` unless it's sanitized (DOMPurify).
- [ ] A Content Security Policy header is set.
- [ ] Scripts from a CDN carry an integrity hash (SRI).
- [ ] `frame-ancestors` blocks other sites from framing yours (clickjacking).
- [ ] No secrets in the bundle. Public environment variables are public.
- [ ] Every third-party script is listed, with why it's there, and loads only after consent where that's required.
- [ ] `postMessage` handlers check the origin.

## Dependencies
- [ ] The lockfile is committed.
- [ ] No known critical vulnerabilities.
- [ ] Licenses are on the allowed list.
- [ ] Unmaintained packages are flagged.

## Concepts
- Security on the backend → [Backend 05 Security](https://claude.ai/artifact/M4ZwELWPjW8CDG5J3eaaA8)
- Security in the browser → [F13 Security in the browser](https://claude.ai/artifact/C4xcdjwcyvELDEWqgusVUD)
- Security across a system → [S11 Security, Multi-tenancy and Cost](https://claude.ai/artifact/QfiYqZe1T5h1Y2NMkKMV9S)

## Changelog
- 2026-10-05: v1
