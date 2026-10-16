---
name: security
description: "What can be attacked and how it's protected, proven before the code. What's worth protecting and from whom, with a bar from OWASP ASVS; the map of the system with its trust boundaries and every way in; the threats on every flow (STRIDE), each with the protection that exists, the gap, the check and the decision; authentication and sessions with their numbers (password length, leaked passwords, hashing, session lengths, step-up, second factor, limits on attempts); authorization and the database's users; the browser (CSRF, CSP and the other headers, caching); data, files and the inventory of secrets; the supply chain and CI; the server and the providers' accounts; what's logged and alerted, and the technical side of an incident; how each protection is checked, automatically and by hand. Writes a folder: a README with the accepted risks, one file per topic, the map as SVG, the scripts that try the decisions, and the big choices as ADRs. Use after the data model, the API and the screens, before Planning; at work before a feature that touches login, money, personal data or uploads, a new provider or integration, a customer's security questionnaire, a pentest report or a critical vulnerability. Also: /security slice <n> checks one slice's new ways in before its code; /security validate <folder> judges an existing one."
argument-hint: "[the product or the change], slice <n>, or validate <folder>"
---

# Security

## When to use it
After the data model, the API design and the UI design (04–06), before Planning: security checks what they decided, so the tables, the endpoints and the flows must exist. It needs the PRD's security requirements and non-goals, the system design's containers, providers, data map, deployment and monitoring, compliance's DPIA, breach plan, processors and retention, the architecture's shared rules (login, permissions, errors, logs), stack, testing, repository and maintenance, the data model's tables with personal and health data marked, the API's map (who may call each endpoint, which ones are limited) and error catalog, and the UI's flows with their failure paths. Plus everything 01–06 left "for Security". **Before the first line of code:** a protection decided now is a rule every slice follows; one found after launch is a fix across the code, maybe after the data has already left.

Then once per slice in Build (`/security slice <n>`): a short pass over what the slice brings in, and its protections proven; and again before the first tester and before launch, as a checklist, like compliance.

At work: a feature that touches login, money, personal data or uploaded files; a new provider or integration (a webhook, a sign-in with Google); a big customer's security questionnaire, or a request for ISO 27001 or SOC 2; a pentest report; a critical vulnerability in a library used everywhere (Log4Shell, December 2021); after an incident; a code review of a new endpoint. Also in the first days at a new company: the threat model (if one exists), how login works, where the secrets live and who can reach production tell you quickly how mature the product is.

## The problem it solves
Steps 01–06 decided many protections, each in its place: a session in an `HttpOnly` cookie, passwords hashed with Argon2id, 404 for someone else's item, every endpoint closed unless it says who may use it, 429 on too many attempts, secrets only on the server, a secret scan before a commit. No document looked at the whole system as an attacker would: what's worth stealing (a person's weight and log, the admin's account, the keys), where you get in (every endpoint, a payment provider's webhook, the links in emails, an uploaded photo, CI, the hosting account), what happens when a single protection fails, and how you find out someone is trying. And the numbers stayed open: how long a session lasts, how many login attempts, 8 or 15 characters, how long a reset link works.

Without an answer, each protection is decided by the first PR that needs it, and the holes sit between PRs: a new endpoint without the "is it yours?" check (first in the OWASP API Security Top 10); a compromised npm package running on the laptop and in CI; the admin's account with a password leaked from another site, changing shared data for everyone; a GitHub account without a second factor, which opens everything. And a user finds out first.

Security decides **what is protected, from whom, how, and how each protection is proven**: the assets and the realistic attackers, the map with its trust boundaries, the threats on every flow, each one's protection with its numbers, the shared protections (headers, keys, the database's users, dependencies, CI, the providers' accounts), what's logged and what raises an alert, and the tests that prove each protection, automatically and by hand.

## How to run it
- **The bar:** do what a senior security engineer or the CTO of a well-run company would accept, in the simplest form that meets it. Use the real industry method and name it (STRIDE, OWASP ASVS, NIST SP 800-63B), so the user learns it. Say what you leave out and why.
- **Teach while you go, starting from the problem.** The user may be a frontend developer with no backend experience. **Before any tool, file or check, say what problem it prevents, in a situation a frontend developer has lived** (a token put in `localStorage` "just for now"; an `.env` pushed by mistake; a Dependabot PR ignored for months; a CORS error that turned out to be a protection). Only then how it works; a "why" gets one sentence of purpose, never more "how". Every term gets one line on what it is, compared with something a frontend developer knows: React escaping text in JSX is already an XSS defence; an `HttpOnly` cookie is already a session no script can read; `pnpm audit` is already a dependency scan; a CSP error in the console is already a security header at work. **At a technical chunk, plain words and one example with numbers come first** (a password of 8 mixed characters has about 95⁸ ≈ 6.6 × 10¹⁵ combinations, one of 15 random lowercase letters about 26¹⁵ ≈ 1.7 × 10²¹), then what it means for the user; the tables after, or only in the file.
- **One step per message, and big steps in chunks.** Show a step, wait for the user's OK, then the next. Steps 4 and 5 are big: one area or one sub-topic per chunk; **count the chunks before announcing them**; save and commit each chunk once it's confirmed, **added to its file, never by rewriting the file** (`>>`, not `>`).
- **Ask only when there's a real choice.** When all the arguments point one way and no realistic alternative fits, write it as decided, with its arguments, and move on. Ask when there are at least two options the user could reasonably pick; once chosen, the choice is final. When the user voices a fear or a doubt next to a choice, resolve it before recording the decision.
- **Before recommending, weigh two things besides the technique:** what most of the industry does, and what serves the user's purpose (what they'll meet at work counts as a real argument). When the options are technically equal, say so first. Change a recommendation only for a new fact, and name the fact.
- **Every number with its argument:** a known standard (named, its official page checked on the web), a target set earlier (cited), or a guess marked `[ASSUMPTION]` with its reasoning. For a choice, an argument card: why; the main alternative and who uses it; when the alternative is better; what someone may answer, and the reply; the source. When the industry is split (SameSite alone or a CSRF token; Row-Level Security or filters in the code), name the camps. Why: the user must be able to defend each choice in a security review or a customer's questionnaire.
- **Where the documents are:** the `Project documents:` line in `CLAUDE.md` gives the documents folder; without it, use `docs/` in the current folder. Write into `docs/02-design/07-security/` and the ADRs into `docs/00-project/adr/`; create them if they don't exist.
- **Read first:** the PRD (`docs/01-discovery/04-prd.md`: the security requirements, the roles, the non-goals), the system design (`docs/02-design/01-system-design/`: containers, data, providers, deployment, monitoring, failures), compliance (`docs/02-design/02-compliance/`: the record, the processors, retention, the DPIA, the breach plan), the architecture (`docs/02-design/03-architecture/`: the shared rules, the stack, testing, the repository, maintenance), the data model (`docs/02-design/04-data-model/`: the tables with personal and health data marked, the one-time links, the sessions, the lifecycle), the API design (`docs/02-design/05-api-design/`: the map with who may call each endpoint and which are limited, the error catalog, `openapi.yaml`), the UI design (`docs/02-design/06-ui-design/`: the flows and their failure paths), and the ADRs. **Search every earlier folder for "Security" and "07"** and gather everything left for this step in one list, each item with where it came from. Ask only what's missing.
- **An existing app is a source of facts, not a model.** Read it for the headers it sends, how it keeps sessions, which accounts reach production. A gap in an internal app isn't treated as a live incident unless the user says so.
- **The protections decided in 01–06 aren't decided again.** Here they're gathered, seen together and proven. If one is wrong or missing, stop, say so, and on a yes fix it where it lives, with a journal line. **The same for the PRD and compliance:** any change, even a number that only closes a gap, is shown to the user first with its exact text.
- **Defence only.** Checks run on the user's own local copies and their own staging, never on someone else's systems; a scanner that attacks (ZAP's active scan) only with the user's yes, on the user's address. **No secret in the documents:** write where a key lives, what it opens and who can read it, never its value.
- **The whole threat model in Design** (chosen on 2026-10-16). The purpose in one sentence: **a threat found before the code changes a contract nobody has built yet, so it costs minutes.** Every flow of the MVP goes through step 4 now, because the API design already wrote every endpoint; in each slice, `/security slice <n>` only passes over what's new or changed and proves the slice's protections. Why: unlike screens, endpoints don't change after the tests with people; OWASP's Threat Modeling Cheat Sheet: "ideally performed early in the SDLC, such as during the design phase", then "maintained, updated and refined alongside the system". The alternative (the riskiest flows now, the rest per slice, as the UI design does for screens) wins when the API is written sprint by sprint with no map ahead, which is most agile teams.
- **The bar is OWASP ASVS, its level chosen per product** (decided): the only standard with verifiable requirements on levels; customers' questionnaires and pentests at work map to it. The OWASP Top 10 is an awareness list, used at step 4 so no category is forgotten.
- **The model lives in markdown, in the repository, with the map drawn by a script** (decided): read in a PR like every earlier step, and checked by a script (every endpoint in `openapi.yaml` appears in the model). At work, OWASP Threat Dragon, Microsoft's Threat Modeling Tool or IriusRisk where the team already uses them.
- **Try the decisions now, as the data model ran its schema on a real database:** Row-Level Security on a real PostgreSQL with the app's user (if chosen), the password hash's time on the server's size, the CSP on the UI design's pages (served with the header, zero violations in the console), a query to the leaked-password service with a test hash. **Write "tried" only for what a test proved,** and keep every script in `checks/`. **A check is tried on planted mistakes** (a fake key for the secret scanner, a library version with a known vulnerability, a missing header, an endpoint without an access rule), one per rule, and on a correct case where nothing must be found; a tool downloaded for the check is named with its size and asked for first.
- **The AI as a provider is here; the AI's prompts are not.** This step covers the AI's key, its budget, what leaves for it and its answer treated like any outside data; prompt injection and the answers' quality are in 08 AI design, where the prompts are written.
- **The user decides** the bar (step 2), every accepted risk and every protection that costs (step 4), the numbers with a real choice (step 5), Row-Level Security (step 6), the outside test before launch (step 12) and every ADR (step 13). You give the options and a recommendation; they choose. One decision at a time.
- **A number about the documents is counted by a script before it's written** (the endpoints, the ways in, the threats, the secrets), and the script is run again at the check.
- **Check the standards on their official pages,** not from memory: OWASP (ASVS, the Top 10 lists, the Cheat Sheets), NIST SP 800-63B, the framework's security docs, the browsers' support, the tools' versions and licences. Security moves fast: a tool can itself be compromised (Trivy, March 2026), a default can change (pnpm 11 waits a day before a new version).
- **Diagrams as SVG files** in `diagrams/`, drawn by a script kept next to them: the map with its trust boundaries, drawn at step 3, with a title and a legend. Open it before committing.
- **What isn't here:** the legal texts and telling the authority and the people about a breach (02 Compliance; here the technical side of the plan); the AI's prompts and answers' quality (08 AI design); the protections' code (Build, per slice); uptime monitoring and backups (01 System design; here only what concerns an attack); the pentest itself (before launch, if chosen).

## Threat modeling
Use this at steps 3 and 4. **The four questions** (Adam Shostack; the Threat Modeling Manifesto, 2020): what are we working on? (the map) what can go wrong? (the threats) what are we going to do about it? (the protections, or the risk accepted) did we do a good enough job? (the checks). An hour at a whiteboard with the team is already a model.

**STRIDE** (Loren Kohnfelder and Praerit Garg, Microsoft, 1999), so no category is forgotten at "what can go wrong?":

| Letter | The threat | Violates | Example | The usual protection |
|---|---|---|---|---|
| **S**poofing | I pretend to be someone else | authenticity | a bot logs in with a password leaked from another site | leaked-password check, limits on login, a second factor |
| **T**ampering | I change data I may not change | integrity | a forged payment webhook marks an account paid | the webhook's signature checked |
| **R**epudiation | I deny doing something, and nothing proves otherwise | non-repudiation | nobody knows who approved a wrong value in shared data | an audit log of the admin's actions |
| **I**nformation disclosure | I see what I may not see | confidentiality | one user reads another's weight; a leaked backup | "is it yours?" on every request; encryption |
| **D**enial of service | I stop the app or make it too expensive | availability | a script asks for 300 password resets and uses up the day's emails on a free plan; someone spends the month's AI budget | limits per endpoint, per account, per IP |
| **E**levation of privilege | I get rights I don't have | authorization | a user sends `"isAdmin": true` in a body and becomes admin | DTOs without that field; the role read only from the database |

**How it's applied:** on every flow of the map (phone → API, API → database, payment provider → API), ask the six letters in turn. What 01–06 already decided goes in as the protection, with its link; what's missing becomes a new protection or an accepted risk, written with its reason.

| Method | Worth it when |
|---|---|
| STRIDE | almost always: the most used, easy to learn |
| LINDDUN (KU Leuven): linking, identifying, detecting, non-compliance and other privacy threats | products with a lot of personal data; a DPIA often covers it |
| PASTA: seven stages from business goals to attack simulation | large companies with a security team and formal risk analysis |
| Attack trees (Bruce Schneier, 1999): the attacker's goal at the top, every path to it below | one goal that matters a lot ("become admin") |
| Tools: OWASP Threat Dragon, Microsoft Threat Modeling Tool, IriusRisk | the team already uses one |

**A risk has four answers:** reduce it (a protection), accept it (written, with why and who accepted it), transfer it (to a provider: the payment provider holds the card data), avoid it (drop the feature).

## The standards
Use this at steps 2 and 12. They're often confused, above all the Top 10 with ASVS.

| Standard | What it is | What it's for |
|---|---|---|
| OWASP Top 10 (2025) | the ten most frequent risk categories in web apps; OWASP calls it "a standard awareness document" | awareness, training, a list so nothing is forgotten |
| OWASP API Security Top 10 (2023, still the latest) | the same for APIs; first, someone else's object asked for by its id (BOLA) | the review of every endpoint |
| OWASP ASVS (5.0.0, May 2025) | 345 verifiable requirements in 17 chapters, on three levels | the security "done when", requirements in a contract, a pentest's checklist |
| NIST SP 800-63B, revision 4 (July 2025) | the US government's authentication rules, followed by the industry | the numbers for passwords, sessions and second factors |
| OWASP Cheat Sheets | short recipes per topic | implementing a protection correctly |
| CWE Top 25 (2025: XSS, SQL injection and CSRF first) | the most dangerous weaknesses in code, from real vulnerability data | code analysis tools report in CWE |
| NIST SSDF, OWASP SAMM | how mature a team's security process is | a CTO decides where to invest |
| ISO/IEC 27001, SOC 2 | a company certified by an auditor | B2B customers ask before they sign |
| OWASP Top 10 for LLM Applications (2026) | the risks of apps with language models, prompt injection first | 08 AI design |

**What changed in the Top 10 in 2025:** broken access control stays first; using components with known vulnerabilities, on the list since 2013, widens into software supply chain failures and rises to third; mishandling of exceptional conditions enters at tenth; logging becomes "logging and alerting".

**ASVS levels** (counted in version 5.0.0's tables): **L1**, 70 requirements, the minimum, the first layer; **L2**, 183 more (253 in all), the level ASVS says "most applications should be striving to achieve"; **L3**, 92 more, for applications that must show the highest level (its example: online banking). Version 4 tied L2 to sensitive data; 5.0 leaves the choice to each product's risk (a startup with little sensitive data may start at L1). Cite a requirement with its version (`v5.0.0-7.5.1`): the numbers change between versions.

## Authentication in numbers
Use this at step 5. In short: a password must be long, not complicated; the leaked-password list matters more than any rule; the server slows attempts down, it doesn't lock the account.

| What | The standard says |
|---|---|
| Minimum length | **15** when the password is the only factor, **8** only with a second factor (NIST 800-63B-4, 3.1.1.2, "SHALL"; OWASP the same) |
| Maximum length | at least 64 (NIST, "SHOULD"), so a passphrase fits |
| Composition rules | forbidden ("SHALL NOT"): they produce "Password1!" |
| Periodic change | forbidden; required only on evidence of compromise |
| Leaked and common passwords | checked, the whole password ("SHALL"), and the person told why it was refused |
| Failed attempts | at most **100** consecutive on one account (NIST, 3.2.2); growing waits, "30 seconds up to an hour" |
| Password managers and paste | autofill allowed ("SHALL"), paste allowed ("SHOULD") |
| Hints and security questions | forbidden |
| The hash | **Argon2id**, at least 19 MiB of memory, 2 passes, 1 thread (OWASP Password Storage); bcrypt only for legacy systems, and it cuts the password at 72 bytes. **Spring Security's Argon2 defaults are 16 MiB with 2 passes, under OWASP's minimum: set the parameters explicitly** |
| A reset link | single use, expiring "after an appropriate period" (OWASP, no number); NIST: a recovery code sent by email lasts at most 24 hours |

- **Where it usually breaks:** around the hash, not in it. **Credential stuffing:** bots don't guess, they replay passwords leaked elsewhere, so the leaked-password check and the login limit matter more than the algorithm. **Enumeration:** login, sign-up and "forgot password" answer the same whether the address has an account (OWASP's wording: "If that email address is in our database, we will send you an email"). **The reset:** the token is random, stored only as a hash, works once and briefly, and the other sessions end after the change.
- **Leaked passwords, two ways.** A: Have I Been Pwned's range API gets only the first 5 characters of the password's SHA-1 and returns every hash starting with them; the match happens on the server, so the password never leaves (k-anonymity); free, no key, no rate limit, behind Cloudflare; with `Add-Padding` every answer has 800–1,000 rows. B: a local list, downloaded and kept up to date. Spring Security has A built in since 6.3 (`HaveIBeenPwnedRestApiPasswordChecker`), with two details found in its source (October 2026): it **fails open** (if the service doesn't answer, the password passes) and sends no padding; it checks at login on its own, but sign-up and password change must call it.
- **Two clocks on a session:** inactivity and total. **NIST ties them to the assurance level:** at AAL1 (a password alone) the total "should" be at most 30 days and inactivity isn't required; at AAL2 (a second factor) at most 24 hours in total and 1 hour inactive; at AAL3, 12 hours and 15 minutes. **OWASP:** 2–5 minutes inactive for high-value apps, 15–30 for low-risk ones, an absolute timeout always, a new session id after login. **Spring Boot's default is 30 minutes inactive** (`server.servlet.session.timeout`), too short for an app opened a few times a day; Spring Session's remember-me keeps a session 30 days by default.
- **Step-up ("confirm it's you")** before changing the email or the password and before deleting the account: someone holding an unlocked phone can't lock the owner out. NIST gives no number; GitHub's sudo mode lasts **2 hours**, each sensitive action restarting the clock; ASVS 5.0 asks full reauthentication before changing the email (7.5.1); Spring Security 7 has it built in (a recent factor: its docs' examples, 30 minutes for an admin area, 1 hour for settings).
- **A second factor and passkeys.** A TOTP code stops a bot holding only the password, not a fake site that also asks for the code; a passkey stops the fake site too, because it's bound to the site's address. FIDO Alliance estimates 7 billion passkeys in use (October 2026); WebAuthn Level 3 is a W3C Recommendation since 25 August 2026; Spring Security supports passkeys since 6.4. NIST calls synced passkeys "syncable authenticators" and accepts them up to AAL2. The real question is **for whom**: an admin who changes shared data for everyone is a different risk from a user.
- **Limits: slow down, don't lock.** An account locked after 5 wrong passwords can be locked by anyone who knows the email. Count on several keys at once (per IP, per account, per target email), answer 429 with `Retry-After`. OWASP counts per account, not only per IP, because bots rotate IPs. **Spring has no built-in limits** (the request has been open since 2016): a library (Bucket4j, with a PostgreSQL back-end) or the proxy.
- **Sign-in with Google:** link to an existing account only by the identity provider's `sub`, and only when the email is trusted; an unconfirmed account loses its password at the link. Otherwise someone who signed up first with your address and a password they know gets in after you: "pre-account hijacking" (Sudhodanan and Paverd, USENIX Security 2022: at least 35 of 75 popular services were vulnerable). **Google says its email claim is authoritative only for `@gmail.com` addresses and Workspace ones (with `hd`)**; for others, even with `email_verified`, it recommends a further check, because the address may have changed hands.

## Authorization and the database
Use this at step 6. First in the OWASP API Security Top 10 is someone else's object asked for by its id (BOLA): the server checks "logged in?" and not "is it yours?". The layers:
1. every query filters by the owner (the person, the team, the tenant), never a row loaded by its id alone;
2. someone else's item answers 404, not 403, so ids can't be probed;
3. every endpoint is closed unless it states who may call it, and a test fails on one without a rule; **a script compares `openapi.yaml` with the rules**;
4. optionally, the database itself:

| | Filters in the code | Plus Row-Level Security in PostgreSQL |
|---|---|---|
| What it does | the owner's id in every query, checked by an architecture rule and a per-endpoint test | the database adds the condition to every query, from a user id set at the start of each transaction |
| What it catches besides | — | a hand-written query (reports, raw SQL) that forgot the filter |
| What it costs | nothing more | a policy per table; the id set per transaction (`set_config('app.user_id', …, true)`) so it doesn't stay on a pooled connection; the policy's columns indexed; **the table's owner bypasses it** unless `FORCE ROW LEVEL SECURITY`; superusers and `BYPASSRLS` roles always do. A policy that reads only the row's own columns is the fastest case |
| Who uses it | the usual way with an ORM (Spring Data, Rails, Django) | Supabase (it asks for it on every table in an exposed schema), multi-tenant products with strict requirements |

**The database's users:** the app never connects as the tables' owner. One user runs the migrations (creates and changes tables), the app's user reads and writes rows, nothing more: an SQL injection can't drop a table, and the owner's bypass of Row-Level Security doesn't apply to the app. On a managed database, check what the given account may do (on OVHcloud, `avnadmin` isn't a superuser but can create roles, and OVHcloud advises against using it for the app). Since PostgreSQL 15, nobody can create tables in `public` without an explicit grant, in databases created since.

**Mass assignment:** bind only the fields a request may set, through DTOs that leave out the sensitive ones (the role, the owner, the price) (OWASP Mass Assignment Cheat Sheet).

## The browser
Use this at step 7. React already stops most XSS; the headers are the safety net for the day someone writes `dangerouslySetInnerHTML`. **A reverse proxy usually sets no security header on its own** (Caddy doesn't): they're written in its configuration.

| Header | What it does | Value (OWASP) |
|---|---|---|
| `Content-Security-Policy` | where the page may load scripts, styles, images and connections from; stops an XSS even when the attacker's text reached the page | for an SPA without server rendering, the scripts' hashes (web.dev's "strict CSP"), plus `object-src 'none'`, `base-uri 'none'`, `frame-ancestors 'none'`, `form-action 'self'`; never `'unsafe-inline'` |
| `Strict-Transport-Security` | the browser refuses HTTP on the domain from now on | `max-age=63072000; includeSubDomains` (2 years); `preload` only knowingly: leaving the browsers' list takes months |
| `X-Content-Type-Options` | the browser doesn't guess a file's type (a "photo" that is HTML) | `nosniff` |
| `Referrer-Policy` | how much of the address leaves for another site | `strict-origin-when-cross-origin` (the Cheat Sheet) or `no-referrer` (the Secure Headers Project); `no-referrer` on a page with a token in its address |
| `Permissions-Policy` | which browser features the page may use | off for what's unused; **keep what the product needs** (`camera=(self)` for an app that scans) |
| `Cross-Origin-Opener-Policy`, `Cross-Origin-Resource-Policy` | isolate the window and the resources from other sites | `same-origin`; resources `same-origin` or `same-site` (the two OWASP sources differ); tried with the payment window and the identity provider |
| `X-Frame-Options` | no one frames the app to trick a click (clickjacking) | `DENY`, and `frame-ancestors 'none'` in the CSP |
| `Clear-Site-Data` | at sign-out, the browser clears its cache, cookies and storage | `"cache", "cookies", "storage"` |

- **Not set any more:** `X-XSS-Protection` (off or absent; the CSP replaces it), `Expect-CT`, `Feature-Policy` (now `Permissions-Policy`); remove `X-Powered-By`.
- **Trusted Types**, in every major browser since February 2026 (Chrome 83, Firefox 148, Safari 26): with `require-trusted-types-for 'script'` in the CSP, `innerHTML` with a plain string stops working, only through a policy you write; the net under `dangerouslySetInnerHTML`.
- **CSRF with a session cookie.** The cookie goes with every request to the domain, even one started by another site. `SameSite=Lax` stops most cases, but OWASP and Spring treat it as defence in depth, not the whole defence; **only Chrome and Edge default to `Lax`**, Firefox and Safari don't, so set it explicitly. Spring Security 7 (November 2025) has `csrf.spa()`: the token in a cookie the app reads and sends back in a header another site can't set. The newer way, `Sec-Fetch-Site` set by the browser (Go's `CrossOriginProtection` since August 2025; OWASP accepts it with an `Origin` check when it's missing), isn't in Spring yet.
- **Cookies:** `Secure`, `HttpOnly`, `SameSite` explicit, no `Domain`, and the `__Host-` prefix, which forces those (OWASP recommends it for session ids).
- **`Cache-Control: no-store`** on answers with sensitive data: the browser keeps none on disk after sign-out. OWASP asks it on every API answer a browser reads; MDN warns against it everywhere, since the page loses the back/forward cache. For sensitive data OWASP wins. It doesn't break `ETag`: an app that keeps its own copies (IndexedDB) sends `If-None-Match` itself and gets 304.
- **CORS:** same origin behind the proxy, so none; a list of exact origins otherwise, never `*` with credentials.

## Data, files and secrets
Use this at step 8.
- **The inventory of secrets**, one row each: what it opens, where it lives, who can read it, how it's rotated, what to do if it leaks. "Secrets only on the server" is the start, not the inventory. A key that must never be lost (a key that links proofs kept for years) is kept outside the server too, and never rotated without keeping the old one.
- **Where secrets live, simple to complex:** a file on the server readable only by the app's user; encrypted files in the repository (SOPS, a CNCF project, with age); a secret manager (HashiCorp Vault, OpenBao, its open-source fork, or the cloud's own: OVHcloud Secret Manager since April 2026, Scaleway Secret Manager), with logged access and rotation. The last two earn their place with several people or servers; with one server and one person, a strict file plus an encrypted copy elsewhere is usually enough.
- **Encryption in layers,** each against a different attacker: in transit (HTTPS to the proxy, TLS to the database); at rest by the provider (against a disk stolen from the data centre, not against someone coming in through the app); per column or in the app (against a stolen backup too, but search and sort get harder). The question is "against whom", not "encrypt or not".
- **Uploaded files** (OWASP File Upload Cheat Sheet): an allowlist of types, checked by content, with the file's signature as one check but never the only one; a size limit; an image decoded and re-encoded on the server, which also drops its metadata (a phone photo can carry the GPS position of a kitchen, so a home address); a new name; private storage served through links that expire.
- **Logs never hold** passwords, tokens, cookies, session ids (a hash at most), keys, connection strings, request bodies with sensitive data, or what the person asked not to keep (OWASP Logging Cheat Sheet); the route as a template, not the raw path with ids.
- **Outside services' answers are outside data:** validated like a user's input, and a URL is never fetched from what a user sent without an allowlist (SSRF: OWASP's cheat sheet).

## The supply chain
Use this at step 9. A `pnpm install` runs code written by hundreds of people on the laptop and in CI, where the keys are.

| When | What | How | What would have stopped it |
|---|---|---|---|
| March 2024 | XZ Utils (CVE-2024-3094) | years of trust earned by a "contributor", then a backdoor in the published archives | nothing simple: an engineer noticed SSH logins about half a second slower, before most distributions' stable releases |
| March 2025 | `tj-actions/changed-files` (CVE-2025-30066) | the action's tags moved to a commit that printed CI secrets to the log | actions pinned to a commit (SHA), not a tag |
| September 2025 | `chalk` and `debug` on npm | a maintainer phished; new versions that stole crypto from browsers | a wait before any new version |
| September and November 2025 | Shai-Hulud, an npm worm | stole the installing machine's tokens and published itself into the victim's packages; 500+ packages removed | install scripts off; short-lived publishing tokens |
| March 2026 | Trivy (CVE-2026-33634), **a vulnerability scanner** | a bad release, and 76 of 77 tags of its GitHub Action moved to bad code | security tools are dependencies too: pinned by SHA |
| May 2026 | TanStack: 84 bad versions in 42 packages, `@tanstack/react-router` among them | a `pull_request_target` workflow, a poisoned CI cache, then the publishing token taken from the runner's memory; live 3–4.5 hours | a one-day wait: never installed |

**What protects, cheap to expensive:** the lockfile committed and CI installing only from it; **a wait before any new version** (pnpm 11 waits a day by default, `minimumReleaseAge`, for indirect dependencies too); **install scripts off** (pnpm since 10, npm since 12; only packages listed in `allowBuilds` run code at install); frequent updates, read (Renovate or Dependabot, a security fix as its own PR at once; Dependabot alerts are free on every plan); a dependency scanner in CI failing on a critical vulnerability; **CI kept tight:** actions pinned by SHA, `GITHUB_TOKEN` read-only by default and raised per job, no `pull_request_target` (where Trivy's and TanStack's compromises started), GitHub's workflow lockfiles (public preview); **an SBOM** (`pnpm sbom`, the CycloneDX Maven plugin), so on the next incident you know in minutes whether you're affected; **what an AI coding agent may run** and which secrets it never sees. At work, further: OpenSSF Scorecard (20 automatic checks of an open-source project, before choosing a library) and SLSA 1.2 (builds anyone can verify).

## The server and the accounts
Use this at step 10. On one server the protections are few and known: SSH with keys only, no password and no root login; a firewall letting through only 80, 443 and SSH; the system's security updates installed automatically; container ports bound locally, so the database and the API are reached only through the proxy; a managed database reachable only from the server's IP; the provider's DDoS protection (OVHcloud includes it on its VPSs, except Local Zone ones); TLS 1.2 and 1.3 (Mozilla's "intermediate" profile; Caddy's default), HTTP redirected to HTTPS, certificates renewed automatically as their lifetimes shrink (Let's Encrypt: 64 days from February 2027, 45 from February 2028), with an alert for one about to expire.

**The providers' accounts matter as much as the server:** the code host, the hosting provider, the cloud with the AI key, the payment provider, the email provider, the log service, the domain registrar and the owner's own mailbox (it resets every other password), each with a second factor (a passkey or a hardware key, not SMS) and recovery codes kept offline. Verizon DBIR 2026 (22,000+ confirmed breaches): exploited vulnerabilities were the first way in for the first time (31%), stolen credentials appear in 36%, a third party in 48%.

## Detection and response
Use this at step 11.
- **Security events logged:** failed logins, and successful ones from a new device; limits hit; password and email changes; roles given and taken; every admin action; unusual numbers of 403 and 404. **Alerts on patterns, not on every event** (hundreds of failed logins a minute; a new admin): an alert for everything gets read by nobody.
- **The technical side of the breach plan:** which key is rotated and how, how everyone is signed out (deleting the session rows), what's kept as evidence; the legal side stays in compliance.
- **How fast a vulnerability is fixed,** from three public signals: CVSS 4.0 (November 2023) for technical severity, 0–10; EPSS (FIRST, version 5, June 2026) for the probability of exploitation in the next 30 days, recalculated daily; CISA's KEV catalog for those already exploited (1,746 on 16 October 2026). One in KEV is fixed first, whatever its score. Verizon DBIR 2026: only 26% of KEV vulnerabilities were fully fixed, after a median of 43 days.
- **How a report reaches you:** `/.well-known/security.txt` (RFC 9116, April 2022) with `Contact` and `Expires` (under a year); then a vulnerability disclosure policy (what good-faith researchers may test, no payment), a bug bounty (rewards; European platforms: YesWeHack, Intigriti), a pentest (a paid specialist, a few days, a report).

## The tools
Use this at steps 9 and 12. None catches everything; our own tests prove what no tool sees.

| Kind | Catches | Tools |
|---|---|---|
| Secrets | a key in a commit | gitleaks; GitHub's secret scanning and push protection, free on public repositories |
| Dependencies (SCA) | a library with a known vulnerability | Dependabot alerts; OSV-Scanner (Google); OWASP Dependency-Check for Maven (an NVD key strongly advised); Trivy and Grype, for container images too |
| Our code (SAST) | a dangerous pattern: SQL glued from pieces, an XSS | SonarQube (SonarSource, Geneva); CodeQL (free on public repositories); Semgrep CE (its maintained rules under a restrictive licence since December 2024) and Opengrep, the open fork; SpotBugs with Find Security Bugs for Java |
| The running app (DAST) | missing headers, cookies without attributes, errors that say too much | ZAP (now "ZAP by Checkmarx", still free): the baseline scan only looks, it doesn't attack |
| The API with unexpected data | a 500 on a value nobody thought of | Schemathesis, from `openapi.yaml` |
| The headers | missing or wrong | Mozilla HTTP Observatory |
| Our tests | the protection really holds | "user A asks for user B's data" → 404 on every endpoint with an id; 429 after the limit; a request without the CSRF token refused; a listed password refused |
| By hand | logic no tool sees | the ASVS list of the chosen level |
| A pentest | what an experienced person finds by chaining small weaknesses | a European firm publishes €1,600 a person-day, 3–5 days for a small web app (Syslifters, the only public price found) |

## The law
Use this at steps 2 and 11. **GDPR article 32** asks measures "appropriate to the risk", given the state of the art and the cost, and names four: pseudonymisation and encryption; confidentiality, integrity, availability and resilience; restoring data in time after an incident; **regular testing of the measures**. Breaking it: up to €10 million or 2% of turnover (article 83(4)). **The Cyber Resilience Act** (Regulation (EU) 2024/2847) asks security of products with digital elements sold in the EU: reporting exploited vulnerabilities from 11 September 2026, the rest from 11 December 2027; **a web app used only in a browser, a PWA included, isn't such a product** (the Commission's guidance, 27 July 2026), while a native or store-wrapped app would bring its backend in as remote data processing. **NIS2** (Directive (EU) 2022/2555; in Romania, OUG 155/2024) applies, as a rule, to medium and large companies (50+ people, or turnover and balance sheet both over €10 million). ENISA published a Secure by Design and Default Playbook for SMEs (July 2026).

## Steps

### 1. Read what exists
As in "Read first": every document, and **one list of everything 01–06 left for Security**, each with where it came from. If an app exists, read it for facts (the headers it sends, how sessions are kept, who can reach production). List what's missing and ask only that.

### 2. What is protected, and from whom
- **the assets,** each with what it means to be seen, changed or lost: health or personal data, accounts, shared data, the subscription's state, the keys, a paid outside budget (the AI), the app being up;
- **the realistic attackers:** bots replaying leaked passwords, a curious or malicious user, a member of a shared space, a compromised package, whoever steals the laptop or the code host's account, the owner making a mistake, an AI agent with too many rights; and **who is out of scope** (an attacker with a state's resources), with why;
- **the bar:** the ASVS level the product aims for, with the argument card (the data, the users, the customers' expectations, the work it means). **The user decides.**

### 3. The map and its trust boundaries
- **the data flow diagram** with its boundaries (drawn by a script, as SVG): the users' devices, the proxy, the API, the database, files, every provider, the code host and CI, the owner's laptop and accounts;
- **every way in,** counted by a script from `openapi.yaml`, plus those that aren't endpoints: webhooks, links in emails, uploaded files, SSH, CI, the providers' consoles, the domain, the owner's mailbox; one row each: who can use it, what data passes, what guards it.

### 4. The threats, in chunks
One area per chunk, counted first (on MacroMate: accounts and login; personal data and shared spaces; shared data and the admin; payments; the AI and files; sync and the phone; the server and the supply chain). On every flow of the area, the six letters of STRIDE, with the OWASP Top 10 and API Top 10 at hand so no category is forgotten. One row per threat: an id (`T-01`), the scenario in plain words, how likely and how bad (low, medium, high), **the protection that exists** (linked to 01–06), the gap and the new protection, **how it's checked**, and the decision (reduce, accept, transfer, avoid). **An accepted risk is written with its reason and who accepted it. The user decides** each accepted risk and each protection that costs.

### 5. Authentication and sessions, with their numbers
In chunks, from "Authentication in numbers": the password's minimum and maximum length; the leaked-password check (an outside service or a local list, and what happens when it doesn't answer); the hash's parameters, **measured on the server's size** (OWASP: under a second); linking an identity provider; the session's two clocks and remember-me; the step-up's minutes; how long each emailed link lasts; the answers that don't reveal which addresses have an account; a second factor, and for whom; **the table of limits:** per limited endpoint, how many attempts, in what window, counted by what (IP, account, target email), what the person sees. Each number with its card; **the user decides** each real choice.

### 6. Authorization and the database
The access rule of every endpoint, from the API's map, **checked by a script against `openapi.yaml`** (no endpoint without a rule); the test "user A asks for user B's data" on every endpoint with an id; the admin's actions and how the role is given; mass assignment; **the database's users** (migrations, the app, read-only for reports if needed), each with its grants; Row-Level Security yes or no, **the user decides**, and if yes, **tried on a real PostgreSQL** with the app's user and a pooled connection.

### 7. The browser
The cookies (name, attributes); the CSRF defence; **the exact CSP**, tried on the UI design's pages (served with the header, zero violations in the console); the other headers with their values; which answers get `no-store`; CORS; what the service worker caches; outside scripts (a payment provider's) and where they may run.

### 8. Data, files and secrets
Encryption in transit and at rest (what the provider does, what we do); **the inventory of secrets**; the keys that must never be lost and where their copy lives; uploaded files; what never reaches the logs; the backups (encrypted, who can restore them).

### 9. Dependencies, CI and AI agents
How security fixes arrive (their own PR at once, outside the weekly one) and how long a new version waits; which scanners run at which CI stage, within the CI minutes' budget; actions pinned and the token's permissions; the container images (where from, how updated); an SBOM or not; what an AI coding agent may run and which secrets it never sees. Each scanner tried on its planted mistake.

### 10. The server and the accounts
The server (SSH keys only, no root, the firewall, automatic security updates, ports bound locally); the database reachable only from the server; TLS; DDoS; **a second factor on every account that reaches production**, recovery codes offline; who else has access.

### 11. Detection and response
The security events logged and the alerts with their thresholds (in the system design's monitoring); the admin's audit log; **the technical side of the breach plan**; `security.txt` and how a report reaches the owner; **the time to fix** by severity (KEV first).

### 12. How it's checked
**One table: every protection → its check** (an automatic test with its CI stage, or a manual check with its moment); the scanners, each tried on planted mistakes; **the manual list before the first tester** (the ASVS requirements of the chosen level that apply, each with how it's met); **the outside test before launch** (a pentest or not, with its cost, against the alternatives: a ZAP active scan on staging, a disclosure policy, a bug bounty later); **the user decides**; what each slice's pass checks.

### 13. The big decisions become ADRs
Only one-way doors (for example the ASVS level, Row-Level Security, a key that is never rotated, the session model if not yet recorded). First propose the list, with **what doesn't get an ADR and why** (most numbers change easily). **The user chooses**, one at a time. After each ADR, re-read the earlier files it changes.

### 14. Check it
- every asset has its threats; every way in on the map appears in the model;
- every endpoint in `openapi.yaml` has an access rule (the script run again); every count in the README matches the files;
- every threat has a protection or an accepted risk with its reason and who accepted it; every protection has its check;
- every number has its source or is marked `[ASSUMPTION]`;
- every question the earlier steps left for Security is answered;
- no secret's value in any document;
- nothing contradicts the PRD, compliance, the architecture, the data model, the API or the UI design.

Run the check with a **separate agent** that has only the documents (`/security validate <folder>`), then verify its findings in the files before showing them: it can be wrong. Look especially for **contradictions left by a changed decision**, above all in files the step didn't touch. Tell the user upfront how long it usually takes (15–20 minutes) and that there's nothing for them to do meanwhile. Show the verified findings by severity with a recommendation; a rule that changes in another step's document is shown with its exact new text before it's written.

Write as you go: each step's file once the user confirms it, with a journal line in the README; **the README's summary, accepted risks and glossary grow with the steps**, not at the end. At the end, set this step's row in `docs/02-design/README.md` to done, with the date, and link the folder.

## A slice's pass
`/security slice <n>`, in Build, **before the slice's first line of code**, next to `/ui-design slice <n>`.
1. **Read** the slice's features, its endpoints, tables, files and providers, the threats of its flows, and **what changed since Design** (the earlier slices, the journal).
2. **What's new or changed** (an endpoint, a table, a file type, a provider, a role) goes through STRIDE; new rows in the model, the user deciding any new accepted risk.
3. **The slice's protections enter its "done when"**, each with its test; the slice's ASVS requirements listed.
4. **At the end of the slice:** the tests green, the scanners clean, the new endpoints in the access-rule script, the map and the README's journal updated; checked by a separate agent against the list in step 14, for this slice only.

```
docs/02-design/07-security/
  README.md                    the entry: status, summary, files, accepted risks, what we skip, open questions, ADRs, glossary, journal
  01-assets-and-attackers.md   02-map.md                    03-threats.md
  04-authentication.md         05-authorization.md          06-browser.md
  07-data-and-secrets.md       08-supply-chain.md           09-infrastructure.md
  10-detection-and-response.md 11-checks.md
  diagrams/                    the map (SVG) and the script that draws it
  checks/                      the scripts that try the decisions, and their planted mistakes
docs/00-project/adr/
  NNNN-[title].md …
```

The README:

````markdown
# Security – [Product]
| | |
|---|---|
| **Status** | draft / confirmed by [who], [date]; slices passed: [n] |
| **Author** | |
| **Updated** | |
| **Bar** | OWASP ASVS [version], level [n] |
| **Next** | 08 AI design; each slice's pass with /security slice <n> |
## In one page
What's protected and from whom, the ways in, the threats per area, the main protections and numbers: 5–6 lines.
## The files
| File | What it answers |
## Accepted risks
| Threat | Why accepted | Accepted by, when | Revisit when |
## Not doing, and why
| Not doing | Why | It comes back when |
## Open questions
| Question | Answered by | When |
## Decisions (ADRs)
| ADR | Decision |
## Glossary
- **Term:** what it is, compared with something the reader already knows
## Journal
- [date]: [what was decided, by whom, what it changed]
````

Each topic file starts with `# NN – [Topic]` and a link back to the README, then:

| File | Holds |
|---|---|
| `01-assets-and-attackers.md` | `\| Asset \| Seen \| Changed \| Lost \|`; `\| Attacker \| Wants \| Can \| In scope \|`; the bar with its argument card |
| `02-map.md` | the diagram; `\| Way in \| Who can use it \| Data that passes \| Guarded by \|` |
| `03-threats.md` | per area `\| ID \| Flow \| STRIDE \| Scenario \| Likely \| Impact \| Protection that exists \| Gap and new protection \| Check \| Decision \|` |
| `04-authentication.md` | the numbers, each with its card; `\| Endpoint \| Limit \| Window \| Counted by \| Answer \|` |
| `05-authorization.md` | the rules per endpoint (or the script that checks them), the admin, the database's users and grants, Row-Level Security |
| `06-browser.md` | the cookies, CSRF, the exact headers with why, caching, CORS, outside scripts |
| `07-data-and-secrets.md` | encryption per layer; `\| Secret \| Opens \| Lives in \| Who reads it \| Rotation \| If it leaks \|`; uploads; logs; backups |
| `08-supply-chain.md` | updates and waits, scanners per CI stage, CI's permissions, images, SBOM, AI agents |
| `09-infrastructure.md` | the server, TLS, DDoS, `\| Account \| Second factor \| Recovery \| Who has access \|` |
| `10-detection-and-response.md` | `\| Event \| Logged \| Alert when \|`; the incident runbook's technical side; the time to fix per severity; `security.txt` |
| `11-checks.md` | `\| Protection \| Check \| Where \| When \| Tried on \|`; `\| ASVS requirement \| Applies \| How it's met \| Checked by \|` |

And one file per decision in `docs/00-project/adr/NNNN-[title].md`, with the same sections as every ADR: status, date, context, options (for and against), decision, consequences, revisit when.

## Validate mode
`/security validate <folder>`: judge an existing threat model or security design, change nothing.
1. Read the folder, its ADRs and the README's journal, the PRD, compliance, the architecture, the data model, the API design (with `openapi.yaml`) and the UI design; the running app's headers and configuration if they exist.
2. Check the template and "Done when" item by item, citing the lines; run the access-rule script and the counts.
3. Then ask: is any way in missing from the map? Any endpoint without a rule, or with an id and no "is it yours?" test? Any threat without a check? Any accepted risk without a reason or an owner? Any number without a source? Any secret's value written? Any protection decided earlier and silently changed here? **Then the decisions that changed during the steps:** is the old version still written anywhere, above all in files the step didn't touch?
4. Report: findings by severity, each with the line, what's wrong and what to change; then what's done well; then what you couldn't evaluate. The user picks what to apply.

## The bad version and why not
- Security "at the end", with a pentest as the only measure: it finds what it can in a few days; the rest stays, and the fixes touch code already built.
- The OWASP Top 10 ticked as a list of requirements: ten broad categories, not verifiable requirements; that's ASVS.
- Login or crypto written by hand: the framework has the version thousands of teams have tried.
- "Is it yours?" checked only in the app (a hidden button): the API can be called directly, with `curl`.
- A JWT in `localStorage`: any XSS steals it, and "sign me out everywhere" needs a list of blocked tokens.
- An account locked after 5 wrong passwords: anyone who knows the email can lock it; slow down instead.
- Composition rules and a password changed every 90 days: NIST forbids both; they produce "Password1!", then "Password2!".
- "This email already has an account": a list of addresses for phishing; on a health app, having an account is already information about a person.
- Secrets in the repository "because it's private": GitGuardian found plaintext secrets in 35% of its customers' private repositories.
- The app connected as the tables' owner: one SQL injection can drop them.
- Updates postponed "until things settle": in 2025, four years after Log4Shell, about 13% of ~300 million Log4j downloads still had it, and 95% of vulnerable components downloaded already had a fixed version (Sonatype, December 2025).
- Every new version taken in its first hour: TanStack's bad versions were live 3–4.5 hours (May 2026); whoever installed them then ran them.
- CI actions on a tag (`@v4`) with a token that can write everywhere: a tag can be moved to bad code.
- A request body logged "for debugging": passwords and health data at a log provider for weeks.
- A stack trace in an answer: a map of the code for the attacker.
- A CSP with `'unsafe-inline'` "to make it work": it no longer stops XSS.
- No second factor on the code host and the hosting provider: the shortest way to everything, without a single vulnerability in the code.
- An alert for everything: nobody reads them, not even the real one.

## What breaks if you skip it
Each protection is decided by the PR that needs it, and the numbers stay the framework's defaults: Spring Boot ends a session after 30 minutes unused, so people are signed out after every meal, and someone "fixes" it with a session of a year. The first tester puts their data into a system whose protections nobody tried together. The first leak is found by a user; with health data, the authority gets a description of it and of the measures within 72 hours (GDPR article 33), and GDPR asks measures "appropriate to the risk", tested regularly (article 32), not the ones thought of in a hurry.

## The principle behind it
**A protection is an assumption until it's tried, and never the only thing between an attacker and someone's data.** It comes from Saltzer and Schroeder (1975), the principles modern security rests on: **complete mediation** (check every access, every time: "is it yours?" on every request), **fail-safe defaults** (closed unless allowed), **least privilege** (each user and program gets only what it needs), **economy of mechanism** (the simplest protection, since a complicated one hides holes). And Microsoft's Zero Trust adds **assume breach**: design for the day a layer falls, not only so it doesn't.

## How to apply it at work
- At a new company: ask for the threat model; if there's none, run the four questions for an hour on the main flow; look at who can reach production, where the secrets live and when the dependencies were last updated.
- In code review, for a new endpoint: who may call it and where is that checked? What comes in unchecked? What reaches the log? Does "doesn't exist" answer like "isn't yours"? For a new library: who maintains it, since when, what does it run at install?
- With a customer's security questionnaire, ISO 27001 or SOC 2: the model, the inventory of secrets, the incident plan and the ASVS list answer most questions.
- When a critical vulnerability is published: the SBOM says in minutes whether you're affected; KEV and EPSS say how urgent it is.
- As a senior or a CTO: a security champion in every team, ASVS in the definition of done, scanners in CI as a gate for "critical", a pentest every year and at every big change, a public disclosure policy, a second factor for everyone, access reviewed at every departure, a tabletop incident exercise a year, maturity measured with OWASP SAMM.

## Done when
Design:
- [ ] everything 01–06 left for Security gathered in one list, each item answered
- [ ] the assets, the attackers in and out of scope; the ASVS level, chosen by the user
- [ ] the map with its trust boundaries, drawn; every way in listed, the endpoints counted by a script
- [ ] every flow of the MVP through STRIDE: every threat with its protection, gap, check and decision; every accepted risk with its reason and owner, decided by the user
- [ ] authentication and sessions with their numbers, each with its card; the table of limits
- [ ] every endpoint with an access rule, checked by a script; the "is it yours?" test per endpoint with an id; the database's users and grants; Row-Level Security decided by the user, and tried if chosen
- [ ] the cookies, the CSRF defence, the exact headers; the CSP tried on the UI design's pages
- [ ] encryption per layer, the inventory of secrets, uploads, logs, backups
- [ ] updates, waits, scanners per CI stage, CI's permissions, images, SBOM, AI agents; each scanner tried on its planted mistake
- [ ] the server, TLS, DDoS, a second factor on every account that reaches production
- [ ] the security events and alerts, the incident runbook's technical side, the time to fix, `security.txt`
- [ ] every protection with its check; the manual ASVS list for the first tester; the outside test before launch decided by the user
- [ ] every one-way door an ADR, chosen by the user; the earlier files re-read after each one
- [ ] no secret's value in any document
- [ ] a glossary for every term the files use, grown with the steps
- [ ] the README: status, bar, summary, accepted risks, what we skip and why, open questions, the ADR table
- [ ] the row in `docs/02-design/README.md` set to done

Each slice:
- [ ] what's new in the slice through STRIDE, before its first code; new accepted risks decided by the user
- [ ] its protections in its "done when", each with its test; its ASVS requirements listed
- [ ] the tests green and the scanners clean at the end; the access-rule script covering its endpoints
- [ ] checked by a separate agent; the README's journal updated

## Sources
1. Threat modeling: [Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/), 2020; Adam Shostack, [The Four Question Framework](https://shostack.org/files/papers/The_Four_Question_Framework.pdf) and [20 Years of STRIDE](https://shostack.org/blog/20-years-of-stride-looking-back-looking-forward/); Microsoft, [STRIDE and the properties](https://learn.microsoft.com/en-us/azure/security/develop/secure-design); OWASP, [Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html); [LINDDUN](https://linddun.org/); Bruce Schneier, [Attack Trees](https://www.schneier.com/academic/archives/1999/12/attack_trees.html), 1999; [OWASP Threat Dragon](https://github.com/OWASP/threat-dragon/releases); [Microsoft Threat Modeling Tool](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-releases).
2. OWASP: [Top 10:2025](https://top10.owasp.org/2025/); [API Security Top 10, 2023](https://api-security.owasp.org/editions/2023/en/0x11-t10); [ASVS 5.0.0](https://github.com/OWASP/ASVS/releases/tag/v5.0.0_release) and [its levels](https://github.com/OWASP/ASVS/blob/v5.0.0_release/5.0/en/0x03-What-is-the-ASVS.md); [Top 10 for LLM Applications 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/); [SAMM](https://owaspsamm.org/model/).
3. MITRE and CISA, [CWE Top 25, 2025](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25.html); NIST, [SSDF, SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final); NIST, [CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final).
4. NIST, [SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html), July 2025: passwords (3.1.1.2), rate limiting (3.2.2), sessions per level (2.1.3, 2.2.3, 2.3.3, 5.2), syncable authenticators (appendix B).
5. OWASP Cheat Sheets: [Authentication](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html), [Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html), [Forgot Password](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html), [Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html), [CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html), [Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html), [IDOR](https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html), [Mass Assignment](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html), [File Upload](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html), [SSRF](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html), [Logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html), [Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html), [HTTP Headers](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html), [REST Security](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html), [Vulnerability Disclosure](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerability_Disclosure_Cheat_Sheet.html); [OWASP Secure Headers Project](https://raw.githubusercontent.com/OWASP/www-project-secure-headers/master/ci/headers_add.json).
6. Spring: [Spring Security 7.0](https://spring.io/blog/2025/11/17/spring-security-releases/); [CSRF for an SPA](https://docs.spring.io/spring-security/reference/servlet/exploits/csrf.html#csrf-integration-javascript-spa); [password storage](https://docs.spring.io/spring-security/reference/features/authentication/password-storage.html); [passkeys](https://docs.spring.io/spring-security/reference/servlet/authentication/passkeys.html); [MFA and a recent factor](https://docs.spring.io/spring-security/reference/servlet/authentication/mfa.html); [Fetch Metadata request](https://github.com/spring-projects/spring-security/issues/18361); [rate limiting request](https://github.com/spring-projects/spring-security/issues/3802); Spring Boot, [application properties](https://docs.spring.io/spring-boot/appendix/application-properties/index.html); Spring Session, [JDBC](https://docs.spring.io/spring-session/reference/configuration/jdbc.html) and [remember-me](https://docs.spring.io/spring-session/reference/spring-security.html); [Bucket4j](https://bucket4j.com/8.21.0/toc.html).
7. Have I Been Pwned, [Pwned Passwords API](https://haveibeenpwned.com/API/v3#PwnedPasswords); W3C, [WebAuthn Level 3](https://www.w3.org/TR/webauthn-3/); FIDO Alliance, [7 billion passkeys](https://fidoalliance.org/7-billion-passkeys-and-counting-the-next-chapter-of-passwordless-authentication/), October 2026.
8. Cookies and CSRF: IETF, [RFC 6265bis](https://datatracker.ietf.org/doc/draft-ietf-httpbis-rfc6265bis/), still a draft; Chromium, [SameSite Lax by default](https://www.chromium.org/updates/same-site/); Go, [`CrossOriginProtection`](https://pkg.go.dev/net/http#CrossOriginProtection).
9. Google, [OpenID Connect](https://developers.google.com/identity/openid-connect/openid-connect) and [when Google is authoritative for an email](https://developers.google.com/identity/gsi/web/guides/verify-google-id-token); A. Sudhodanan and A. Paverd, [Pre-hijacked accounts](https://www.usenix.org/conference/usenixsecurity22/presentation/sudhodanan), USENIX Security 2022; GitHub, [sudo mode](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/sudo-mode).
10. The browser: web.dev, [Strict CSP](https://web.dev/articles/strict-csp); MDN, [CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP), [Trusted Types](https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API), [caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching); [HSTS preload](https://hstspreload.org/); IETF, [RFC 9111](https://www.rfc-editor.org/rfc/rfc9111.html); Mozilla, [HTTP Observatory](https://developer.mozilla.org/en-US/observatory).
11. The server: Caddy, [Automatic HTTPS](https://caddyserver.com/docs/automatic-https), [tls](https://caddyserver.com/docs/caddyfile/directives/tls), [header](https://caddyserver.com/docs/caddyfile/directives/header); Mozilla, [Server Side TLS](https://ssl-config.mozilla.org/guidelines/latest.json); Let's Encrypt, [from 90 to 45 days](https://letsencrypt.org/2025/12/02/from-90-to-45) and [64-day certificates](https://letsencrypt.org/2026/10/07/64-day-certs); OVHcloud, [VPS anti-DDoS](https://docs.ovhcloud.com/en/guides/bare-metal-cloud/virtual-private-servers/vps-faq).
12. The database: PostgreSQL, [Row Security Policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html), [`set_config`](https://www.postgresql.org/docs/current/functions-admin.html), [version 15](https://www.postgresql.org/docs/release/15.0/); OVHcloud, [users and roles in managed PostgreSQL](https://docs.ovhcloud.com/en/guides/public-cloud/databases/postgresql-users-roles-grants); Supabase, [Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security).
13. Secrets: GitHub, [security features](https://docs.github.com/en/code-security/getting-started/github-security-features); CNCF, [SOPS](https://www.cncf.io/projects/sops/); OVHcloud, [Secret Manager](https://blog.ovhcloud.com/en/posts/discover-the-external-secret-operator-eso-ovhcloud-provider-to-manage-your-kubernetes-secrets/); [Scaleway Secret Manager](https://www.scaleway.com/en/secret-manager/); Google Cloud, [budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets) and [spend caps](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps).
14. The supply chain: Openwall, [XZ](https://www.openwall.com/lists/oss-security/2024/03/29/4); CISA, [tj-actions](https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-tj-actionschanged-files-cve-2025-30066-and-reviewdogaction) and [Shai-Hulud](https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem); GitHub advisories: [`debug`](https://github.com/debug-js/debug/security/advisories/GHSA-4x49-vf9v-38px), [Trivy](https://github.com/advisories/GHSA-69fq-xp46-6x23), [TanStack](https://github.com/advisories/GHSA-g7cv-rxg3-hmpx); TanStack, [postmortem](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem); GitHub, [npm's plan](https://github.blog/security/supply-chain-security/our-plan-for-a-more-secure-npm-supply-chain/) and [npm 12](https://github.blog/changelog/2026-07-08-npm-install-time-security-and-gat-bypass2fa-deprecation/); pnpm, [supply chain security](https://pnpm.io/supply-chain-security); GitHub, [secure use of Actions](https://docs.github.com/en/actions/reference/security/secure-use) and [workflow lockfiles](https://docs.github.com/en/actions/concepts/security/workflow-dependency-lockfiles); OpenSSF, [Scorecard checks](https://raw.githubusercontent.com/ossf/scorecard/main/docs/checks.md); [SLSA](https://slsa.dev/spec/); [CycloneDX](https://cyclonedx.org/specification/overview/); Sonatype, [The Persistence of Open Source Vulnerabilities](https://www.sonatype.com/blog/unnecessary-risk-the-persistence-of-open-source-vulnerabilities), December 2025; GitGuardian, [State of Secrets Sprawl 2025](https://blog.gitguardian.com/the-state-of-secrets-sprawl-2025/).
15. Tools and reports: Semgrep, [the rules' licence](https://semgrep.dev/blog/2024/important-updates-to-semgrep-oss); [Opengrep](https://www.opengrep.dev/); ZAP, [joining Checkmarx](https://www.zaproxy.org/blog/2024-09-24-zap-has-joined-forces-with-checkmarx/); Syslifters, [web application pentest pricing](https://www.syslifters.com/en/pentests/web-applications); [YesWeHack](https://www.yeswehack.com/); [Intigriti](https://www.intigriti.com/); FIRST, [CVSS 4.0](https://www.first.org/cvss/v4.0/specification-document) and [EPSS](https://www.first.org/epss/); CISA, [KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) and [a disclosure policy template](https://www.cisa.gov/vulnerability-disclosure-policy-template); IETF, [RFC 9116](https://www.rfc-editor.org/rfc/rfc9116.html); Verizon, [DBIR 2026](https://www.verizon.com/business/resources/T343/reports/2026-dbir-data-breach-investigations-report.pdf).
16. The law: [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj), articles 32, 33 and 83(4); European Commission, [Cyber Resilience Act](https://digital-strategy.ec.europa.eu/en/policies/cra-summary) and [guidance C(2026) 5252](https://ec.europa.eu/newsroom/dae/redirection/document/131456); [NIS2](https://digital-strategy.ec.europa.eu/en/policies/nis2-directive); [the SME definition](https://single-market-economy.ec.europa.eu/smes/sme-fundamentals/sme-definition_en); ENISA, [Secure by Design and Default Playbook](https://www.enisa.europa.eu/publications/enisa-secure-by-design-and-default-playbook), 2026.
17. J. H. Saltzer and M. D. Schroeder, [The Protection of Information in Computer Systems](https://www.cs.virginia.edu/~evans/cs551/saltzer/), 1975; Microsoft, [Zero Trust](https://learn.microsoft.com/en-us/security/zero-trust/zero-trust-overview).

## Next
AI design (`/ai-design`), for products with AI: evals, prompts, limits, cost. In Build, before each slice's code: `/security slice <n>` next to `/ui-design slice <n>`; before the first tester and before launch, `/security validate` on the folder.
