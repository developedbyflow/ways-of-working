---
name: api-design
description: "How the app and the server talk: the contract between them. Who calls the API and in which style, the map of every endpoint from the PRD's features, the shape of every request and answer (each field with why, personal and health data marked), who may call each one and its errors, lists and pagination, what a repeated request or two writes at once do, the sync protocol for an offline app, webhooks, long operations and files, how the contract changes without breaking old clients, and how it's checked. Writes a folder: a README, one file per topic, one file per module's endpoints, an openapi.yaml checked by a linter, sequence diagrams, and the big choices as ADRs. Use after architecture, alongside or after the data model, before the screens; at work before a new endpoint or a new client, a change that could break old clients, or an integration with another service. Also judges an existing one: /api-design validate <folder>."
argument-hint: "[the product or the change] or validate <folder>"
---

# API design

## When to use it
After Architecture, almost in parallel with the data model and the screens (04–06); once the data model exists, after it, since the tables and the data on the device leave questions for the API. It needs the PRD's features, criteria and build order, the system design's flows, compliance's rights (export, deletion, consents), the architecture's shared rules (login, errors, names, compatibility) and, when it exists, the data model. **Before the first endpoint is written, and above all before the first release:** an endpoint is free to change while nothing calls it; once an app on a phone calls it, every change breaks something.

At work: a feature that needs data from the server; a new client (a mobile app, a partner, another team); an integration with an outside service (webhooks); a change that could break old clients; a PR with a new controller. Also in the first days at a new company: the API's contract (its Swagger page) shows what the product does without reading the code.

## The problem it solves
The architecture gave the shared rules: errors in Problem Details, kebab-case paths, "the API only adds". The data model said what the database keeps. Neither said which endpoints exist, what the app sends and gets back, how a phone that was offline for three days catches up, what happens to a save sent twice because the answer was lost on the way, or how the app learns that an entry was refused and why.

Without an answer, every controller decides in the first PR: the table's class sent out as JSON (a new column appears in the API by itself), a different list shape on every screen, a repeated `POST` that logs the same meal twice, a list that returns 10,000 rows. And after the first release every mistake stays, because the old app on the phone still uses it.

API design decides **the contract between the app and the server**: the resources and endpoints, what goes in and out of each, who may call it, which errors can come back, how long lists arrive, how a repeated request stays harmless, how offline data syncs, and how the contract changes without breaking old apps.

## How to run it
- **The bar:** do what a senior engineer or the CTO at a well-run company would accept, in the simplest form that meets it. Use the real industry method and name it, so the user learns it. Say what you leave out and why.
- **Teach while you go, starting from the problem.** The user may know only the frontend. **Before any tool, file or check, say what problem it prevents, in a situation a frontend developer has lived** (the backend renamed a field and the screen showed `undefined`; Swagger said one thing and the server sent another; every endpoint returned its errors in a different shape). Only then how it works. Never answer a "why" with more "how"; when the user asks "what for?", the answer is one sentence of purpose. Every term gets one line on what it is and what it brings, compared with something a frontend developer knows: the types generated from OpenAPI (`schema.d.ts`) already read a contract; TanStack Query retries a failed read by itself, never a save, so the repeats come from the person pressing Save again after a lost answer and from an offline queue, and the server must survive them; "Load more" with `useInfiniteQuery` is cursor pagination; MSW is a fake server. When the server is in Java, explain Spring the first time, compared with ASP.NET Core: `@RestController` and `@GetMapping` are a controller with `[HttpGet]`; requests and answers are Java `record`s checked with `@Valid` and Jakarta Bean Validation (like DataAnnotations); errors leave through `ProblemDetail` (Spring 6.0 and later); springdoc writes the OpenAPI contract from the controllers, as Swashbuckle does in .NET. **At a technical chunk, plain words and one example with numbers come first,** then what it means for the user; the tables after, or only in the file. A sentence that can be read two ways is settled with options A/B before anything is written.
- **One step per message, and big steps in chunks.** Show a step, wait for the user's OK, then the next. Steps 3, 4 and 7 are big: one module or one sub-topic per chunk; **count the chunks before announcing them** and say so if the count changes; save and commit each chunk once it's confirmed. Why: each decision needs to land before the next one builds on it.
- **Ask only when there's a real choice.** When all the arguments point one way and no realistic alternative fits, write it as decided, with its arguments, and move on to the next real choice. Ask when there are at least two options the user could reasonably pick; once chosen, the choice is final. When the user voices a fear or a doubt next to a choice, resolve it before recording the decision. **Write a choice as its options, lettered A, B,** and the decision with who made it and the date ("chosen by [who] on 2026-11-07 (A)"); the option not chosen stays named, with when it would win ("Not chosen (B): …"), so a later reader sees what was weighed.
- **Before recommending, weigh two things besides the technique:** what most of the industry does, and what serves the user's purpose (what they'll meet at work counts as a real argument). When the options are technically equal, say so first and recommend on those grounds. Change a recommendation only for a new fact, and name the fact. Learned on 2026-10-14: a first recommendation of no version in the path, flipped once the user asked what's best practice, made every other recommendation look unreliable.
- **Every number, shape and rule with its argument:** a known standard (named, its official page checked on the web), a target set earlier (cited), or a guess marked `[ASSUMPTION]` with its reasoning and how and when it's checked (`[ASSUMPTION: measured in slice 5]`); every guess left in the files is also an open question in the README, with the slice that answers it. For a choice, an argument card: why; the main alternative and who uses it; when the alternative is better; what someone may answer, and the reply; the source. When the industry is split (design-first or code-first, an envelope or not, PATCH or PUT), name the camps. In the docs, every table of fields has a "why" column. Why: the user must be able to defend each choice in a review or a technical discussion.
- **Where the documents are:** the `Project documents:` line in `CLAUDE.md` gives the documents folder; without it, use `docs/` in the current folder. Write into `docs/02-design/05-api-design/` and the ADRs into `docs/00-project/adr/`; create them if they don't exist.
- **Read first:** the PRD (`docs/01-discovery/04-prd.md`: features, criteria, journeys, the build order), the system design (`docs/02-design/01-system-design/`: the flows, the targets for answer times, offline, the providers), the compliance folder (rights, consents, what counts as health data), the architecture (`docs/02-design/03-architecture/`: the modules, the shared rules, the conventions for names in the API and JSON, the stack, the frontend's way of talking to the API), the data model (`docs/02-design/04-data-model/`: the tables, the data on the device, the questions it left for the API), and the ADRs. Ask only what's missing.
- **An existing API is a source of facts, not a model.** Read it for which endpoints exist, which the app really calls, what's missing or inconsistent. An endpoint doesn't become right because it's there.
- **The names, errors, login and compatibility rules come from the architecture; the tables from the data model; this step decides the contract.** Don't change a convention or a table here; if one is wrong, stop, say so, and on a yes fix it where it lives, with a journal line. **The same for the PRD and compliance:** any change, even one that only closes a gap, is shown to the user first with its exact text.
- **The table isn't the contract.** Every answer has its own shape, built for what the screen needs: internal columns stay out, computed fields come in, a name can differ. Write the differences from the table down, per endpoint.
- **Two forms of the contract, each with its own reader** (chosen on 2026-10-13). The purpose in one sentence: **the endpoints are written in YAML too, so a program finds the design's mistakes now and, in Build, checks that the code follows the same design.**
  - **markdown, for people:** per module, every endpoint with its fields, rules and **why**; the user reads and approves this one;
  - **`openapi.yaml`, for programs:** the same endpoints in the standard format, in the OpenAPI version the project's generator produces (springdoc: 3.1 by default), so the Build comparison compares like with like. **Checked by a linter** (Redocly CLI, or Spectral), its version pinned, with a `redocly.yaml` next to it: the `recommended` rules, `no-invalid-media-type-examples` and `no-unresolved-refs` as errors, `paths-kebab-case`, every operation named (`operation-operationId`, so the generated client keeps stable names), and the architecture's conventions as the project's own rules (field names in camelCase on `SchemaProperties`, every path under the version prefix, every 4xx and 5xx in Problem Details, a JSON body always an object, never a bare array), plus a plugin rule for what the configurable rules can't say (every array with `maxItems`). **Each rule is proved on a planted mistake:** a file of planted mistakes, one per rule, next to correct operations (a list, a file download), and a script that expects each rule to fire exactly once and nothing on the correct ones. Tried on 2026-10-14: nine rules, nine caught, no false alarm; one rule needed a second try (it looked two levels up and missed a bare array). **A chunk isn't done until the linter passes, and neither is any later change to `openapi.yaml`,** a later step's included: the linter runs before the commit, and the journal line says it passes.
  - **In Build, when the architecture chose code-first** (the contract generated from the code), the code stays the source: per slice, the contract generated from the code is compared with the design's for that slice's endpoints (`oasdiff diff --exclude-elements description,examples,title,summary --fail-on-diff`), and a difference stops CI until the code is fixed or the design changes with a journal line; a copy of the slice's part of the design sits next to the code while the slice is built, when the documents live in another repo. Once the slice ships, the generated contract replaces the design for those endpoints, and the architecture's rule takes over (oasdiff against production). **Tried on 2026-10-14, three things the comparison needs:** both contracts **cut to the slice first** (its addresses and only the schemas they use), since `--match-path` filters the addresses but still compares every schema; **the schema names are the contract's,** since springdoc names a schema after its class and the conventions' `FoodResponse` against the design's `Food` stops the comparison (`@Schema(name = …)`, or one rule dropping the suffix); **every answer field `required`,** since oasdiff reports a removed optional field only as INFO. **The generated contract is committed** in the code repository, written by a test that asks the framework's contract address (springdoc's `/v3/api-docs`, on only in that test and locally, never in production), so a PR shows its contract changes and fails when the file is stale; production's is `main`'s (`origin/main:path`, read by oasdiff directly). **The linter runs on it on every PR too,** with the same rules: once a slice has shipped only `oasdiff breaking` looks at its addresses, and an addition passes it even when it breaks the conventions (a new snake_case field is INFO; a new array's missing `maxItems` isn't seen at all). **When the architecture chose design-first,** `openapi.yaml` stays the source and the server's interfaces are generated from it (openapi-generator).
  - Not markdown alone: nothing checks it now, and nothing compares the code with it later. Not YAML alone: the user would approve the design by reading thousands of lines of YAML, and the reasons would live nowhere. The validation agent compares the markdown and the YAML, endpoint by endpoint.
- **Every endpoint in full detail now, not per slice** (chosen on 2026-10-13): the UI design comes right after and needs to know what each screen gets; the data model is already whole, so most shapes come from it quickly; an endpoint is still free to change until the first release, so a later change costs little. The alternative (the map now, the shapes per slice in Build) wins when the PRD may change a lot after the first slices.
- **The user decides** the map of endpoints (step 3), every real choice in the shapes (step 4), the sync protocol's shape (step 7) and every ADR (step 11). You give the options and a recommendation; they choose. One decision at a time.
- **Check the standards on their official pages,** not from memory: HTTP's methods and status codes (RFC 9110), Problem Details (RFC 9457), the patch formats, the OpenAPI version, the framework's features (Spring Framework 7 has API versioning built in; Spring Boot 4 uses Jackson 3), the tools' rules, the providers' pages (their webhooks' signatures and retries). **Every claim about an outside standard, tool or provider carries the date it was read** ("read 2026-11-07"), and a claim corrected later says so in place ("corrected 2026-11-10: it said …"): a fact about the outside world changes on its own. Learned on 2026-11-07: the IETF's `Idempotency-Key` draft, called "expired" when written, had a new version weeks later. **A library's defaults are read in its documentation or source and set explicitly** where they differ from the design: an AI provider's SDK that makes up to 5 attempts with no time limit by default breaks the design's one retry within 15 s. **Write "tried" only for what a test proved,** and keep every script in `checks/`. **A tool is tried the way the linter was, on planted cases:** oasdiff on copies of the contract with one change each (a stricter limit, a removed field, a deprecation with too short a sunset), each expected to stop or pass, its default levels read in its own source; a tool downloaded for the trial (a Docker image) is named with its size and asked for first.
- **UML sequence diagrams,** written as PlantUML (`.puml` next to its `.svg` in `diagrams/`): the parts as lifelines, the step numbers matching the tables, failures and branches as `alt`, `break`, `loop`, a lost answer as a lost message. `docs/02-design/diagrams.sh` (set up by `/docs-setup`) draws every diagram of the design from text, in a standard notation (decided 2026-10-20), so they read the same at any company; never a hand-made SVG, a home style, or a script that draws SVG itself. One per main flow, **drawn at its step:** a repeated request at step 6, the sync at step 7 (one per direction, the push and the pull), the slowest call to an outside service and the payment at step 8: five for a product that syncs and takes payments; each with a title and a legend. Open each one before committing: no text overlaps. Left to the end, three of the five were missing at the check.
- **A number or a rule decided earlier changes everywhere at once** (decided 2026-10-21, after a whole-design check found ~160 stale mentions left behind by later steps): before committing, `grep` all of `docs/` for the old value and its wording (the number, the name, the phrase) and fix every place in the same commit, or say why one stays (a journal line keeps what was true that day; a past count kept on purpose goes into `docs/02-design/checks/facts-history.txt`). `diagrams.sh` runs `checks/facts.py`, which counts the main facts from their sources (tables, addresses, threats, secrets, screens, ADRs, alerts) and stops on a document that states another number; a new fact that many files repeat gets a line in it. **A change to an address goes into `openapi.yaml`, its endpoint file and the map in the same commit,** the linter passing, with a journal line.
- **A count about the documents comes from a script, never by hand:** the addresses from the map, the operations and the schemas from `openapi.yaml` (`facts.py`), the operations behind a login and the addresses each guard test covers from the contract joined with the map's "Who" (a script 07 Security writes); a number typed by hand is the one that goes stale when a later step adds an address. Run them again at the check.
- **When a later step changes the contract, it's brought up to date here,** with a journal line and the user's yes: UI design changes the error catalog's field reasons, the page size and the requests per screen; Security adds the session addresses, the session cookie and the CSRF header, the upload rules and the counts the tests use; AI design changes the AI requests' answers (a schema of its own when an answer joins two jobs' parts). Each such change follows the rule above: the contract, the endpoint file and the map in one commit, the examples generated again, the linter passing, and the README's one-page summary checked against it.
- **The README's journal is in the user's own voice, one voice from start to end** ("with my yes", "chosen by me (A)"), never "the user" in one line and "I" in the next; the topic files name who chose. A journal line is never rewritten: a later change adds its own line, appended at the bottom, saying what changed, where, and with whose yes. Learned in the walkthrough: third-person slips were found, and fixed, twice (2026-11-07, 2026-11-10).
- **What isn't here:** the tables (04 Data model; the contract doesn't change them), the screens and their states (06 UI design), the session's length, the exact rate limits, CSRF, security headers and Row-Level Security (07 Security), the AI's prompts and limits (08 AI design), the controllers' Java code (Build, per slice).

## The styles
Use this at step 2. Name only what this product needs; explain each one you name.

| Style | What it is | Worth it when |
|---|---|---|
| REST (Roy Fielding, 2000) | resources with addresses, HTTP's methods and status codes with their meaning | almost every web API; caches, proxies and HTTP tools work by themselves |
| RPC over HTTP | functions called remotely: `POST /doSomething` | actions that aren't "a thing"; in a REST API, as sub-paths or Google's `:verb` (AIP-136) |
| A sync protocol (push and pull) | the app sends what changed on it and asks what changed on the server since a number | apps that work offline |
| GraphQL (spec edition September 2025) | the client asks for exactly the fields it needs, on one endpoint | many screens and clients (web, iOS, partners), separate frontend and backend teams; HTTP caching, per-field authorization and cost limits are done by hand |
| gRPC | functions described in Protocol Buffers, binary, over HTTP/2 | between internal services; a browser needs gRPC-Web (with a proxy) or Connect |
| tRPC | TypeScript functions called directly, types flow from server to client | TypeScript at both ends, in a monorepo |
| WebSocket | a connection that stays open, messages both ways | chat, editing together, games |
| Server-Sent Events (WHATWG HTML) | the server pushes a stream of messages on one request, one way | a job's progress, an AI answer word by word |
| Webhooks | another service calls your API when something happens on its side | payments, emails, Git |

How REST an API is (Leonard Richardson's model, Martin Fowler's article, 2010): level 0, one endpoint and everything through POST; 1, resources; 2, HTTP's methods and status codes with their meaning; 3, hypermedia (the answer links to what you can do next). Most good APIs today are at level 2.

## Methods and status codes
Use this at steps 3–4. RFC 9110 (June 2022).

| Method | Does | Safe | Idempotent |
|---|---|---|---|
| GET | reads | yes | yes |
| POST | creates something or performs an action | no | no |
| PUT | puts the whole thing at the given address: creates or replaces it | no | yes |
| PATCH (RFC 5789) | changes a part | no | not unless designed so |
| DELETE | deletes | no | yes |

**Why idempotent matters:** RFC 9110 (9.2.2) says an idempotent request can be repeated automatically when the connection drops before the answer; a POST can't, unless the server has a way to recognise the repeat. On a bad network that's the difference between one meal and two in the log.

The status codes beyond the architecture's: **201** for a creation, with `Location` pointing to the new thing when it has an address of its own; **202** "accepted, working on it"; **204** no body (a deletion); **304** "nothing new" (with an ETag); **412** a condition failed and **428** a condition is required (RFC 6585); **413** the body is too large; **415** a format the endpoint doesn't take.

**In the contract, every answer that can happen:** a creation answers **201**, with `Location` only when the created thing has an address of its own (an invite or a checkout that has no `GET` of its own gets none), and its repeat (the app's id already there) **200 with the stored row**, without `Location`; **400 on every address that checks a header** (the app's version); **413 and 415 on every address with a body**, since the proxy or the framework refuse before the controller. A header an `<img>` or a plain file download can't send (the app's version) is optional on those addresses. The check found 65 addresses without their 400 and 17 creations with only a 201.

## The shape rules
Use this at step 4, chunk 1: decided once for every endpoint.

| Rule | The options | The usual choice and why |
|---|---|---|
| Envelope | `{ "data": …, "error": … }` everywhere, or the thing itself | the thing itself: HTTP already has the status; an envelope only where data must travel alongside (a list with its cursor) |
| Missing field against `null` | "not sent" and "empty" are different, above all in a partial change | one meaning, written; a missing measured value is `null`, never 0 |
| Dates and moments | RFC 3339 text (a profile of ISO 8601), or numbers | text: readable, and OpenAPI names them `date` and `date-time` |
| Numbers | a JSON number, or text | a number while it fits exactly in a `double`; beyond `2^53` or for exact sums, text (RFC 8259, RFC 7493) |
| Fixed lists of values (enums) | text or number | text; **a new value in an answer breaks a client that handles every value**, so the client always has an "other" case |
| A partial change | PUT with the whole object; PATCH with JSON Merge Patch (RFC 7396: `null` removes the field, a list is sent whole); PATCH with JSON Patch (RFC 6902: a list of operations); a separate action | PUT where the client already holds the whole object; Merge Patch for settings, careful with `null`; an action when the change has a rule of its own |
| What never goes out | — | internal fields and other people's; one request record and one answer record per endpoint, never the table's class |
| A field absent from a request | absent means "empty", or "keep what's stored" | **absent keeps the stored value, `null` empties it:** an older app sending a whole object with `PUT` (or a whole row in a sync) doesn't know a field added later, and would erase what a newer app set; without this rule, "a new optional field in a request" isn't safe. In Java the record must tell absent from `null` |
| Examples | in the markdown, in the contract | one per request and success answer in the contract, **generated from the schemas** with realistic values chosen per field name (a day's targets read differently from 100 g of chicken), stored once per schema under `components/examples`, and checked by the linter against their schema; written chunk by chunk, not at the end; the generator writes only the missing ones, and runs again after a schema changes |
| The error codes | — | `module.reason`, lower case with `_`, digits allowed after the first word (`foods.parts_exceed_100g`), matching the contract's pattern for a code; the prefix names who refuses (a module, `common` for what every address shares); **the reason names the cause, not the remedy** (`subscription.read_only`, not `subscription.required`), as Stripe and Google do; the "When" column names every moment a code comes, an outside service's own refusals included; `title` in English for the logs, never `detail`; a 400 for the shape carries `errors`, each with a field and a reason from one written list (`required`, `too_long`, `out_of_range`, `wrong_format`, …), a new reason added to the list and to the app's texts in the same PR |
| Text fields | — | every one with its maximum length, from its column's rule; a text an outside service or the AI fills too |

## Lists
Use this at step 5.

| Kind | Looks like | Good at | Weak at |
|---|---|---|---|
| No paging, with a written limit | the whole list | small, bounded lists | if the limit isn't real, the list grows without end; Google (AIP-158) and Microsoft both say paging added later breaks clients |
| Offset or page number | `?offset=40&limit=20`, `?page=3` | "page 7 of 12", small admin tables | the database reads and discards the skipped rows, so deep pages slow down; a new row shifts everything, so a row shows twice or goes missing (Markus Winand, "No Offset") |
| Cursor (keyset) | "after this row", by a unique order such as `(created_at, id)` | growing lists, endless scrolling; speed doesn't depend on the page | can't jump to page 7 |
| "Changed since N" | a growing number on changes | sync | — |

The rules: a default page that matches the main client's screen ("Show 20 more" is a page of 20), which the client sends itself so a later change of the default never moves it; the server enforces a maximum page size, a larger `limit` brought down, never refused (AIP-158: "coerce down"); the order always has a unique tie-breaker (the id); the cursor is opaque, the client never builds it, holds values rather than a row (the last row may be deleted meanwhile), and carries a short hash of the other parameters, so a cursor sent with other filters is refused with 400; no total count (Zalando #254), the end known by reading one row more than the page; only the filters the screens need; a list pages from its first version. Zalando asks for cursors (rule 160). **A search term that is personal or health data** (what a person ate, a medical word, an email) travels in the body of a `POST` to a sub-path (`POST /recipes/search`), never in the address, where it reaches every access log (ASVS 5.0.0, 14.2.1), until the HTTP `QUERY` method (a read with a body) works on the stack.

## Repeats and concurrent writes
Use this at step 6.

| Kind | How | Worth it when |
|---|---|---|
| By itself | PUT or DELETE at an address holding an id the client made | the client makes the ids |
| Uniqueness in the database | the id in the body; the second time, the database sees the id and saves nothing | creations with ids made by the client |
| An idempotency key | an `Idempotency-Key` header; the server keeps the first answer for a while and gives it again. Stripe keeps keys at least 24 hours and refuses a key reused with other parameters; the IETF's draft (`draft-ietf-httpapi-idempotency-key-header`, version 08 of 22 October 2026, still a draft, not a standard; read 2026-11-10) suggests 400 for a missing required key, 422 for a reused key with another body and 409 while the first request still runs; Google puts a `request_id` in the request (AIP-155) | effects that cost money, send something or call a paid service; a public API with clients you don't write |
| An "in progress" row | the request writes its row "waiting" before the slow outside call; a resend finds it and gets 409, and sends again with growing waits (2, 4, then 8 s, since a resend may carry a large body); a waiting row older than every time limit inside the request, plus a margin, is taken as failed | a write that waits seconds for an outside service (an AI call) |
| The action written as a state | "the day is complete" (`isComplete: true`), not "toggle" | toggle buttons |

**The trap:** a save with a version (optimistic locking), repeated after a lost answer, meets itself: the first save raised the version from 5 to 6, the repeat still says 5 and gets 409, "someone else changed this", though it was the same person. Every write with a version needs a rule for its repeat: on a mismatch the server compares what's stored with what was asked, and equal is 200, not a conflict.

**The lookup comes before every quota:** a repeat never counts against a daily cap, a budget or a rate limit as a new request, and an "in progress" 409 is never counted toward the limit that protects the outside service. **Someone else's id** in a creation changes nothing and is refused without saying whose it is (409), since the client made the id: a bug or a forged request.

Two writes at once: HTTP's own way is an ETag with `If-Match` (RFC 9110 calls it the defence against the "lost update"): 412 when the version moved on, 428 to require the condition (RFC 6585). The other way: the version in the JSON and 409 with who changed it, easier for an app to read.

## Changing the contract
Use this at step 9.

| Versioning | Looks like | Who | Worth it when |
|---|---|---|---|
| No versions, only add | a new field yes; nothing removed or renamed | Google (AIP-180), many | almost always; clients you control |
| In the path, one version for the whole API | `/api/v2/…` for every address once one breaks | the most common: Google requires it (AIP-185), Stripe, Microsoft Graph; Spring Framework 7's own model | rare, large breaking changes |
| In the path, a version per address | `/api/v2/foods/{id}` next to `/api/v1/` for the rest | Kubernetes, per group of its API | parts of a large API changed by different teams |
| In a header, by date | `X-GitHub-Api-Version: 2022-11-28` | GitHub, which keeps the previous version at least 24 months | a public API with many clients |
| In the query | `?api-version=2024-01-01` | Microsoft Azure, required | many services, one rule |
| Per account, by date | each account stays on its version, the server translates | Stripe | thousands of clients that don't update |

| Change | Breaks an old client? |
|---|---|
| a new field in an answer | no, if the client ignores what it doesn't know ("tolerant reader", Martin Fowler, 2011) |
| a new optional field in a request | no, **when a field absent from a request keeps its stored value** (the shape rules); otherwise an older app's `PUT` erases it |
| a new required field in a request | yes: old requests don't have it |
| a field removed, renamed or with another type | yes; oasdiff sees a removal from an answer as an error only when the field is `required`, so every answer field is |
| a new value in a fixed list in an answer | yes, for a client that handles every value; **oasdiff calls it an error by default** (`response-property-enum-value-added`): when the app always has an "other" case, a levels file lowers it to a warning, still shown in the PR. `x-extensible-enum`, Zalando's earlier advice (#112 recommends `examples` since October 2025; oasdiff still reads the extension), doesn't fit code-first: springdoc writes `enum`, and the TypeScript types would lose the values. For the sync's own words (an outcome, a mark's kind) the "other" case is written: the operation stays waiting |
| a stricter validation (a maximum of 100 becomes 50) | yes: what passed yesterday is refused today, offline entries included |
| a lower size limit at the proxy (a body's maximum in bytes) | yes, as a stricter validation; **not in the contract, so no tool sees it:** judged by hand, never lowered within a version |
| a looser validation | no for a request; **yes for an answer** when one schema serves both: a newer app saves 80 servings where an older app's form allows 50 (oasdiff: `response-property-max-increased`). The app first, the server after, and the change accepted with oasdiff's `--err-ignore`, one line per answer it reaches, each with the date and the reason (on MacroMate a recipe's servings raised to 100: 19 lines on 13 addresses, since a creation's 201 and its repeat's 200 are each an answer) |
| a new required header, or one made required | yes; **not seen when the rule lives only in a description** (a CSRF header written in the security scheme's text, not as a parameter): judged by hand |
| a media type a request may use removed | yes: the old app's request gets 415 |
| another status or error code | yes, if the client handles it; a new code for one item of a batch falls into the client's "other" case, but a new code for **the whole batch** of a sync push is a break unless the old app already keeps the batch waiting on it |
| another default order or page size | maybe: Hyrum's law, with enough users every visible behaviour is relied on; oasdiff reports a changed default only as INFO, so `oasdiff breaking` doesn't show it: harmless only while the client always sends the value itself |

**When the rules start** (learned in the walkthrough, 2026-11-07): in Design the contract changes freely, each change with a journal line, since nothing calls it; from an address's first deploy the table applies to it; **an address behind a feature flag that's off (merged, but switched off for everyone) counts as deployed only once the flag is on for any client,** and until then a change to it is a line in oasdiff's accepted list naming the flag; while only the team's own phones call it, a break may pass as an accepted line with the user's yes and a journal line, the entries waiting unsent on those phones sent first; from the first outside users, no exception. The alternative: the table from the first deploy with no exception, stricter, but it makes the team's own phone a reason to keep a second version.

**A newer app against an older server** (after a rollback, the phone keeps the newer app): a feature's API part ships in an earlier release than the app part that calls it, and the app hides the feature when its first call answers 404.

Retiring an endpoint has two standard headers: `Deprecation` (RFC 9745, March 2025: a date as `@` and seconds since 1970) and `Sunset` (RFC 8594, 2019: an HTTP date, a hint that can move later); Spring Framework 7's `StandardApiVersionDeprecationHandler` sends them for a whole version. In the contract, `deprecated: true` and `x-sunset`, which oasdiff reads.

**Spring Framework 7's versioning, checked in its docs and source (7.0.9):** the version is one for the whole API; a method without a version answers every version ("intended to support clients created before a versioned alternative was introduced"); the changed method is `version = "2+"`, since a fixed `"2"` would also hide the method without a version at `v3`; the version read from the path needs `{version}` in the mapping (a common prefix), its parser skips the `v`, the supported versions written in the configuration (`spring.mvc.apiversion.supported`, with `detect-supported=false`, or Spring learns them from the mappings and, while no method carries a version, knows none), and a predicate for the addresses without a version (`/api/health`), or Spring refuses them with 400. **The answer a straggler gets is decided, with where it's produced:** Spring answers an unsupported version with a plain 400 the app can't act on, so the check of the app's version header runs in a servlet filter, before the DispatcherServlet resolves the API's version, and a phone still on the retired version gets the "update required" code it updates on. How springdoc writes a version taken from the path: try it in the first slice.

**What stops CI (oasdiff, levels read in its source):** `oasdiff breaking origin/main:<contract> <contract> --fail-on ERR --severity-levels <file> --err-ignore <file> --deprecation-days-stable 30`: a deprecation must give 30 days (`api-sunset-date-too-small`), a removal before the sunset or without a deprecation is an error; the levels file holds the deliberate exceptions to a check, the accepted file (`--err-ignore`) the deliberate breaks, one dated line each with its reason. When `v2` is made, `v1` against `v2` with the prefixes stripped (`--strip-prefix-base`, `--strip-prefix-revision`) lists what the new version breaks on purpose.

## Security that belongs to the API's shape
Use this at steps 4–5. OWASP API Security Top 10 (2023); the rest is 07 Security's.

| Risk | Looks like | What API design does |
|---|---|---|
| API1, object level authorization | `/api/recipes/{id}` with someone else's id returns it | every endpoint says whose the thing is and what a stranger gets |
| API3, object property level authorization | a request sends `"isApproved": true` and the server saves it (mass assignment), or an answer shows fields it shouldn't | the request record holds only the fields the person may set; the answer only what they may see |
| API4, unrestricted resource consumption | endless lists, huge uploads, too many requests | the maximum page and body size; which endpoints get a rate limit (the numbers in 07) |
| API7, server-side request forgery | the server fetches whatever address it's given | a file the server fetches comes from a fixed list of hosts, a redirect followed only within it |

## Steps

### 1. Read what exists
The PRD's features, criteria and build order; the system design's flows and targets; compliance's rights; the architecture's shared rules, conventions, stack and the frontend's way of talking to the API; the data model's tables, the data on the device and **the questions it left for the API** (search its files for "API design"); the ADRs. List what's missing and ask only that.

**If an API exists,** read it for facts: the endpoints, which the app calls, what's inconsistent. Not as a model.

### 2. Who calls the API, and in which style
The clients (the app, the admin, the browser on its own for a login's navigation or a file, the services that send webhooks, the monitoring and the deploy's smoke tests, anyone downloading a public file, a future partner), **how each proves who it is** (a session, a signature, a token, or nothing, with why), **how old an app that still calls can be** (days offline, how it updates), worked through one example (a phone offline for five days sends its first sync in the old version's shape), and the style for each kind of data (REST, sync, webhooks), with the argument card; whether the app and the API share an origin, so CORS is needed or not; and what is **not** a client (the services the API calls, which never call it). Usually decided already by the system design and the architecture: then write it as decided, with the reasons.

### 3. The map of endpoints, before the shapes
First the rules of the whole map: the version prefix and its exceptions (the framework's own login addresses, a health check that must never move), kebab-case plural paths, an action that isn't create, read, change or delete as a sub-path with `POST`, who may delete, the levels of "who" (anyone, logged in, confirmed again, admin, the browser), and **personal or health data never in an address** (a token from an email, a barcode, a search: in the body). Then, from the PRD's features and criteria and the flows, per module (one chunk per module, counted first, in the order of the slices): the ideas behind it as argument cards, and the resources (nouns) and the actions (verbs that aren't create, read, change, delete), each with its number, method, path, who calls it, what it does, the PRD feature it serves, whether it's limited (429) and whether it's a one-way door.
- **every PRD criterion reaches an endpoint, or a written reason** (computed on the device, shown from data already there);
- **every endpoint serves a feature:** no endpoint "we may need" (Joshua Bloch: when in doubt, leave it out; you can always add, never remove);
- how many **round trips** each main screen waits for, on the system design's slow network: requests sent together over HTTP/2 cost about one, so the count is of the requests that wait for each other; a screen that waits for more than one gets one endpoint built for it, or a reason;
- **mark the one-way doors:** what the app calls offline or what the phone stores, since an old app calls it for days after a release;
- the whole map's total stated once, counted by a script.

**The user decides** the map.

### 4. The shapes, module by module
**Chunk 1, the rules every endpoint follows,** decided once: the envelope or not, the list shape, `null` against a missing field, numbers, fixed lists of values (the client tolerates a new value), partial changes (PUT, PATCH or an action), the names (a moment ends in `At`, a yes/no reads as a question, `isComplete`), the headers in both directions (the app's version, the request id, `Retry-After`, `Location`), **the catalog of error codes** (`module.reason`, each with its status, its `params` and when it comes), **the maximum body sizes, each from the largest valid request, built at every limit and measured in bytes** (every text at its maximum, in every language), the limit about twice it so a valid request never gets 413; a KB written as 1,024 bytes and given to the proxy in its own unit (Caddy reads `KB` as 1,000, so it's given `KiB`). Start `openapi.yaml` with them (the shared error answers, the list shape, the headers, the security scheme) and `redocly.yaml` with the conventions as rules, each proved on its planted mistake.

Then one chunk per module (a module with an admin side gets two, `[module].md` and `[module]-admin.md`), every endpoint in full:
- the rules behind the module's shapes, and its shared answers as tables;
- the request and the answer: field, type, required, rule, **why**, personal or health data, one example; **a table for every shape, requests and summaries included, never a prose list** (the check found nine shapes written as sentences);
- the status codes and the error codes it can return; who may call it (the architecture's access rules), and what a stranger gets;
- **the request holds only the fields the person may set; the answer only what they may see;**
- **the differences from the table, written** (a computed field, a hidden one, another name);
- **every PRD criterion tried on the shape:** "can this screen show everything from this one answer?";
- the codes it adds to the catalog, each with its status, `params` and when;
- added to `openapi.yaml` with its examples (generated from the schemas, as in the shape rules), every answer that can happen (the status codes above), and the linter passes before the chunk is done.

**The user decides** each real choice.

### 5. Lists
Every list with its size today and at 10× (from the data model's questions), the hidden ones too (the members inside a team's answer): no paging only with a written limit, and what happens at it (the next add refused with 422 and the limit as a parameter, counted under a lock so two adds can't pass it together; or the oldest dropped, for what the person doesn't manage, like sessions); a cursor for growing lists, with the cursor's rules written once (above); offset only where "page 7" is needed and the list is small; the maximum page size; the order with a unique tie-breaker (the newest first for people, the oldest first for a work queue); only the filters and sorts the screens need; where a search happens and how its term travels. **Try it on generated data** in a real database: a cursor's pages lose and repeat no row when rows are added and deleted between pages, and the same pages read with an offset, counting the rows read twice and never read, so the difference is shown, not argued; keep the script in `checks/`. List the Build tests: every page read while rows change, `limit=1000` answering the maximum, a cursor with other parameters answering 400, a list ending on a full page answering no next cursor, never an empty page; every limit at the limit plus one, twice at the same moment. Each limit's code goes into the catalog, with its text in every language, in the same PR.

### 6. Repeats and concurrent writes
First where repeats come from, each with how often and how late it can arrive: the person after a lost answer, the client library's own retries (read its default: TanStack Query retries no mutation by default), the device's offline queue, the providers' webhooks, your own jobs after a crash, a mass resend you trigger yourself (after a backup restore). For every write, what happens when it arrives twice: by itself (an id made by the app, PUT, the database's uniqueness), with an idempotency key (where the effect costs money, sends something or calls a paid service), with an "in progress" row (a write that waits for an outside service), or written as a state rather than a toggle; what the app gets the second time, and **the answers it takes as done** (404 after its own delete, 401 after its own logout); a secret shown only once (an invite's link) can't be answered again, so its repeat gets its own code; **a save with a version, repeated, doesn't meet itself;** the lookup comes before every quota; someone else's id refused without saying whose; "only one at a time" rules (one export being prepared, one open checkout) held by a partial unique index (a uniqueness rule on only the rows in that state). Concurrency: the version the screen saw and 409 with who changed it (or `If-Match` and 412), or "the last change wins" where that's the rule (one person's own data); one operation per item where people act at once on purpose (the ticks of a shared list); **a rule across rows locks its parent first, then counts,** so two requests at a limit never pass it together; and the races you accept, written with what bounds them. **Reproduce each case on a real database** (two sessions, the same request twice), keep the scripts in `checks/`, and list the tests that prove it in Build. **Every write goes in the table, the small ones too:** a report (give it the app's id), leaving a group or accepting an invite sent twice (the second sees the first's result: the app takes it as done), a file uploaded twice (the orphan swept); the check found ten missing. Write each creation's 201 (with `Location` when the created thing has an address of its own) and its repeat's 200 into the contract now. Draw the repeat's sequence diagram.

### 7. Sync
Only for a product that works offline; built on the data model's identity of a row the device makes offline and its order of changes (a counter per person raised in the writing transaction, not a sequence or a timestamp, which can become visible out of order); in chunks:
- **push:** the batch's shape and its maximum size (the operations and the bytes, its upload time on the slow network); the answer per operation (confirmed; lost to a newer change; refused, with its error code); how the device says a row is new; what an old app version sends; **each row checked on its own** in the service, not with `@Valid` on the batch, which would refuse 99 good rows for one bad one; **what each answer for the whole batch makes the device do:** a 401, a 429, an "update required", a refused CSRF token keep the batch waiting whole (a fresh token fetched and the batch sent again once), any other 4xx sends one operation at a time, so it never loops; a word it doesn't know keeps the operation waiting;
- **pull:** "changed since N", in pages that never split the rows of one number; the first load of the window kept on the device; a reload when the device is below what was purged;
- **after a backup restore:** the server's numbers go back while the devices keep theirs; a restore id in every sync request, another than the database's answered with its own code, nothing saved or read, and the device sends its window again and pulls from 0; what can't be recovered, written in the breach register;
- **the copies** the device keeps (reference data, settings): how they arrive, their size on the slow network, a compact shape where the size demands it; **the data model decides what the device stores,** so an `ETag` goes only on what it stores, and the rest is asked whole;
- **when the sync runs and how many requests it makes:** at the opening, when the network returns, after every change, in the background where the browser allows it (Background Sync, not on Safari); one sender at a time (a Web Lock, the browser's lock shared by the tabs and the service worker); a failed attempt tried again with a growing delay; the opening's requests counted and their round trips.

One sequence diagram per direction. **The user decides** the shape. **Then re-read the data model's integrity, lifecycle and device files:** the protocol changes their rules (how a day's row is saved, what a long-deleted row gets, who writes the log); the check found four contradictions there.

### 8. Outside services, long operations and files
First the list of every edge, from the container diagram and the flows: who calls you, whom you call, what takes longer than a request, every file that enters, leaves or is fetched by the server.
- **webhooks received:** the strongest proof the provider offers (an HMAC signature, a hash of the timestamp and the body with a secret both sides hold, else a token, else IP ranges), checked on the raw body, compared in constant time so the time taken tells an attacker nothing, **before anything is saved or read**; a fast 2xx, processed after; the repeat recognised by the event id; no reliance on order (the job reads the current state); a callback after an account is gone saved, never refused forever;
- **every call to an outside service: its time limit, its retries and what the person sees past it,** in one table: who waits sets the limit (a person: seconds; a job: longer; a download: connect, idle and total); retries only where a repeat is safe, with growing pauses, never after a timeout on a call with side effects; no redirect followed; one shared client; **the client library's own retries read in its docs and set to match** (an AI SDK's default of several attempts with no time limit, set to the design's one retry within the limit);
- **operations longer than a request:** 202 with the thing's state in the body, a job, and how the outcome is learned: a status address with `Location` and `Retry-After`, or, when nobody polls, a list the screen reads anyway and an email, the 202 then carrying neither header;
- **operations of a few seconds** (an AI call): the request waits, with a time limit that covers every call inside it, its retry included; what the app sees on failure, each cause named; the progress shown by the app; what a resend does while the first still runs (step 6);
- **files uploaded:** through the API (`multipart/form-data`) or straight to storage with a signed address valid a few minutes, argued from the files' size and weekly volume; the maximum size at the proxy; **the type read from the file's first bytes, never its name or its part's `Content-Type`;** the pixel or unpacked size read from the header and capped before decoding (a 50 KB image can decode to 1.6 GB); re-encoded into a clean copy without metadata, the only one stored or sent on; a limit on decodes at once; one code per refusal (413 too large, 415 another request format, 422 a file inside that can't be used), checked before anything is counted; the cleanup of what nothing references;
- **files downloaded and fetched:** who may read each; `Content-Disposition` with a name the server made, never one built from a person's input; a deliberate `Cache-Control`; how long it lives; a file the server fetches only from a fixed list of hosts, a redirect only within it, its fingerprint kept, its unpacked size capped (OWASP API7);
- **webhooks sent,** if any: Standard Webhooks (`webhook-id`, `webhook-timestamp`, `webhook-signature`, retries with growing pauses);
- the sequence diagrams of the slowest outside call and of the payment.

### 9. Changing the contract
**When the rules start** (above), then the architecture's compatibility rule made into a table, in both directions (the old client sending, the old client reading): which changes are allowed and which break (a new value in a fixed list in an answer and a stricter validation included), why, for these clients, oasdiff's check and its level, or "not seen" for what the contract can't show (the proxy's size limits, a header written only in a description, defaults, order, the addresses outside the contract), and what you do; what the client does with what it doesn't know; how a breaking change ships without stranding anyone (expand, migrate, contract: add the new, move every client to it, then remove the old; a looser limit client first; a feature's server part a release before its client part, for a newer app meeting an older server); how a version is retired (`Deprecation` and `Sunset`, the old calls counted per app version, the minimum version raised, the specific answer a straggler gets and where it's produced, the code deleted); which oasdiff checks stop CI, **tried on planted changes** (above). With the version in the path, settle with the user whether a break raises the whole API or only one address, after reading the framework's model. End with when the policy is read again (a store app, a partner, a public API).

### 10. Checking the contract
First the mistakes between the contract and the code, as the reader meets them (Swagger says one thing and the server sends another; a new endpoint ships without its "someone else's item" test; a strange input gives a 500; a change breaks the app already on phones; the conventions drift), each given the earliest moment that catches it and a tool, in one table: `| When | What | Catches | Tool |`, each tool with its pinned version.
- in Design: the linter on `openapi.yaml`, with the project's rules, each proved on its planted mistake;
- in Build, on every PR: the linter on the generated contract; the comparison between the contract generated from the code and the design's, per slice, and against production's (above); the types the app generates from the contract, regenerated and type-checked;
- **the tests per endpoint, most written once as guard tests that run over every address it covers:** no endpoint without an access rule; 401 without a login; 404 for someone else's item; 403 for a user on an admin address, for a read-only account, and for a write without the CSRF token; 400 for a broken body; every error in Problem Details. **Their lists come from a script** that joins the contract with the map's access rule (the security step writes it), so a new address gets its cases by itself, and **each test's count is the script's, never typed by hand;** the rest by hand per address: each 422 rule, the repeat, the pages, 429 where limited, 413 per size limit against the proxy's configuration;
- **the addresses outside the contract** (the framework's own login and passkey addresses, a health check) and what covers them instead: the end-to-end tests, the deploy's smoke test;
- whether a tool that sends generated requests from the contract (Schemathesis) runs in CI, with its argument card. **When it runs follows the CI budget the architecture counted** (free minutes a month, the 10-minute PR), with the arithmetic written: on MacroMate, twice a week inside the whole browser matrix's nightly run (~9 runs a month, ~5 minutes each: 139 operations × 100 requests × ~20 ms), since on every PR it would pass the 2,000 free minutes. Schemathesis 4.32.7 (its checks first read in 4.31.0, and the same in 4.32.7 on 2026-11-10) checks a 500, an answer outside the contract, invalid data accepted, and with two people set up as peers **one person reading another's item** (OWASP API1); it learns the links between addresses from `Location`; a batch that answers 200 with refusals is configured as such. **It runs with real sessions:** two ordinary people in two separate spaces and an admin, made by the run's setup as the end-to-end tests make them, their cookies and the CSRF header given as fixed headers in a Web Fuzzing Commons document (a standard file of the test users and how each one authenticates; its peers work only with that kind of authentication, not with a login hook of your own), the admin's second factor confirmed beforehand in a browser; the requests that would end the run's own session (log out, delete the account) left out, their endpoint tests covering them. The alternatives: EvoMaster (white-box, writes JUnit tests, supports Java up to 21), RESTler (Microsoft Research).
- **every tool's version pinned,** the planted cases run again on every upgrade (oasdiff's 19 gave the same results on 1.33.0 and 1.35.0), and when a check moves written down (a paid plan, more people changing the API, a new client).

### 11. The big decisions become ADRs
Only one-way doors (for example the style, the error format, the sync protocol's shape, how repeats are handled, the pagination style, the versioning). First propose the list, with **what doesn't get an ADR and why** (grouped: rules in the code, what other documents own, what can change freely before the first release). When a decision was already taken in the steps, write the ADR and give it to the user to check, a few at a time. Otherwise one at a time: options, your recommendation, **the user chooses**. **After each ADR, re-read the earlier files it changes,** the architecture's, the data model's and the earlier ADRs included, link each decision to its ADR, and look for the old version of a decision that changed during the steps.

### 12. Check it
- every PRD criterion reaches an endpoint, or has a reason;
- every endpoint has a feature, an owner module, an access rule, its error codes and an example;
- every list has a written limit or pagination; every write has its behaviour on a repeat;
- no table class goes out as JSON; every difference from the table is written;
- the markdown and `openapi.yaml` agree, endpoint by endpoint, and the linter passes;
- every error code is in the catalog, with a text in each of the product's languages planned;
- nothing contradicts the architecture, the data model, compliance or the system design; every question the data model left is answered;
- every count the documents state matches its script (`facts.py`), and every claim about an outside standard or tool carries the date it was read.

Run the check with a **separate agent** that has only the documents (`/api-design validate <folder>`), then verify its findings in the files before showing them: it can be wrong. Look especially for **contradictions left by a changed decision**, above all in the files the step didn't touch (the architecture's conventions, testing and frontend files, the data model's integrity, lifecycle and device files, an ADR). Tell the user upfront how long it usually takes (15–20 minutes; 18 on MacroMate) and that there's nothing for them to do meanwhile. Show the verified findings by severity with a recommendation; a rule that changes in another step's document is shown with its exact new text before it's written.

Write as you go: each step's file once the user confirms it, with a journal line in the README; **the README's summary, "not doing" and glossary grow with the steps**, not at the end. **Before calling it done, read the README against every file,** not only the one that changed last: the counts against the scripts, each summary bullet against its file and its ADR today, every term the page uses against the glossary (the walkthrough found 19 terms without a line), and "Next" against today's next step. At the end, set this step's row in `docs/02-design/README.md` to done, with the date, and link the folder.

```
docs/02-design/05-api-design/
  README.md            the entry: status, summary, where to start, files, what it builds on, what we skip, open questions, ADRs, glossary, journal
  01-clients.md        02-map.md           03-shape-rules.md
  04-lists.md          05-repeats.md       06-sync.md
  07-outside.md        08-changes.md       09-checks.md
  endpoints/           one file per module: [module].md (a module with an admin side gets two: [module].md, [module]-admin.md)
  openapi.yaml         every endpoint, every answer that can happen, an example per request and success answer
  redocly.yaml         the linter's rules: Redocly's recommended set plus the conventions as checks
  checks/              the scripts behind the claims, each named in the file whose claim it proves:
                       lint.sh; lint-planted.sh with planted-mistakes.yaml (each rule caught exactly once);
                       redocly-rules.js (a plugin rule the configurable rules can't say); make-examples.py;
                       a measurement of the largest shapes; cursor-pages.sh; repeats.sh; pull-pages.sh;
                       oasdiff-plant.py and oasdiff-planted.sh with oasdiff-levels.txt and oasdiff-accepted-example.md;
                       oasdiff-slice.py (a contract cut to one slice's addresses and schemas, for Build)
  diagrams/            the UML sequence diagrams, each [name].puml next to its .svg: repeat, sync-push, sync-pull,
                       the slowest outside call, payment
docs/02-design/diagrams.sh        draws every diagram of the design from text
docs/02-design/checks/facts.py    stops on a document that states another count than its source
docs/00-project/adr/
  NNNN-[title].md …
```

The README:

````markdown
# API design – [Product]
| | |
|---|---|
| **Status** | draft / confirmed by [who], [date]: [which check]; brought in line on [dates] |
| **Author** | |
| **Updated** | |
| **Next** | [the next step, written for today, not copied from this template]; in Build, [how each slice's part of the contract reaches the code and is compared with it] |
## In one page
What the contract covers and its two forms (markdown for people, `openapi.yaml` for programs, checked by [the linter]); then one bullet per question a senior asks first, each leading with its decision, carrying its number and ending with its link: who calls it; the shapes and errors; the style; the endpoints (the total, the operations in the contract and outside it, per kind of caller, the version prefix and its exceptions, round trips per main screen); lists; repeats; the sync; the outside services; the session and CSRF; changing it; checking it (with the guard tests' counts). Never the contract pasted in.

**Where to start:** [the clients], then [the map], then [the shape rules], then the endpoint file of the module you care about; the other files in order after that.
## The files
| File | What it answers |
(the topic files, each endpoint file, the contract and the linter's rules, the diagrams with their sources, every script with the claim it proves)

**How the files stay in agreement:** which file is the source of which fact (the markdown the reasons, the YAML the shapes); which check fails when two differ (the linter and its planted mistakes, the oasdiff trial, the count script, the join of the contract with the access map); what changes in the same commit.
## What it builds on
| Document | What it gives the API |
(and what this step changed there, where, with whose yes)
## Not doing, and why
| Not doing | Why | It comes back when |
## Open questions
| Question | Answered by | When |
(each with the assumption used meanwhile; a closed one stays, struck through, with its answer and where it's written)
## Decisions (ADRs)
| ADR | Decision |

Decided in later steps, and binding the API:
| ADR | Decision |

Decided before, and shaping the API: [ADR] ([what it gives]), …
## Glossary
- **Term:** what it is, compared with something the reader already knows
## Journal
- [date]: step [n], [topic]: [what was decided, by whom]. [What changed in other documents, with whose yes].
- [date]: changed in [the later step], with [who]'s yes: [what changed in the contract, and where]; the lint passes.
````

Each topic file starts with `# NN – [Topic]` and a link back to the README, then:

| File | Holds |
|---|---|
| `01-clients.md` | `\| Client \| Calls \| Proves who it is \| Oldest version still calling \| Style \|`; one origin or CORS; what isn't a client; how old a calling app can be, worked through one example; the style per kind of data, with its argument card; the styles not chosen |
| `02-map.md` | the rules of the whole map; per module the ideas behind it as argument cards, `\| # \| Method \| Path \| Who \| What it does \| Feature \| Limited \| One-way door \|` and `\| PRD \| Endpoint \|` (every criterion reaches one); the whole map's count; the requests per main screen `\| Screen \| Requests before it shows \| In the background \| Round trips \| Why it's enough \|` |
| `03-shape-rules.md` | (a) the shapes `\| Rule \| Example \| Why \| The other camp \|`; (b) the headers `\| Header \| Direction \| When \| Why \|` and the maximum sizes `\| Body \| Maximum \| Why \|`; (c) the error catalog `\| Code \| Status \| Params \| When \|` and the field reasons; the linter's rules `\| Rule \| Checks \| Tried on \|` |
| `endpoints/[module].md` | the links to its map chunk, the shape rules, its tables and its tag in the contract; the rules behind its shapes; the shared answers; per endpoint: what it does, who may, the request and answer `\| Field \| Type \| Required \| Rule \| Why \| Personal / health \|`, the differences from the table, the status and error codes, the repeat, one example; the codes it adds to the catalog |
| `04-lists.md` | the three kinds; the cursor's rules; `\| List \| Rows now / at 10× \| Kind \| Largest page \| Order \|`; a search and where its term travels; the trial on a real database; how it's checked; the codes for the limits |
| `05-repeats.md` | where repeats come from; the few rules; `\| Write \| Sent twice \| Two at once \| Proved by \|`; two writes at once; the tests in Build; the codes |
| `06-sync.md` | the push, the pull, the copies, each with its step table and diagram; after a backup restore; the opening and when the sync runs |
| `07-outside.md` | the webhooks received, one column per provider; the calls to outside services `\| Call \| Time limit \| Retries \| A retry is safe? \|`; long operations; operations of a few seconds; the files, and what the server does with an upload; the webhooks sent |
| `08-changes.md` | when the rules start `\| When \| The rule \| Why \|`; `\| Change \| Breaks the old app? \| Why, here \| oasdiff's check and its level \| What we do \|`; a looser limit; a newer app against an older server; the versioning, with its argument card; retiring a version; the check in CI; when this is read again |
| `09-checks.md` | `\| When \| What \| Catches \| Tool \|`; the linter now and on every PR; the code against the design and against production; the tests per endpoint `\| Test \| Written \| Which addresses \| From \|`; the generated requests, with their sessions and their argument card |

And one file per decision in `docs/00-project/adr/NNNN-[title].md`, in the ADR template of `/system-design` (status, date, updated, context, options, decision, consequences, revisit when), with its row in the index `docs/00-project/adr/README.md` in the same commit.

## Validate mode
`/api-design validate <folder>`: judge an existing API design or contract, change nothing.
1. Read the folder, `openapi.yaml`, its ADRs and the README's journal, the PRD, the system design, compliance, the architecture and the data model; the running API's contract if it exists.
2. Check the template and "Done when" item by item, citing the lines; run the linter.
3. Then ask: does every PRD criterion reach an endpoint? Does every endpoint have a feature, an owner, an access rule, its errors and an example? Does any answer copy a table's class, or any request accept a field the person may not set? Does every list have a limit or paging, every write a behaviour on a repeat, every versioned save a rule for its own repeat? Do the markdown and the YAML agree? Is any change listed as allowed actually breaking (a new enum value in an answer, a stricter validation)? Is every term explained? Does a creation without an address of its own send no `Location`? Do the counts the documents state match their scripts, and does "Next" name today's next step? Does every claim about an outside standard or tool carry the date it was read, and is it still true (a draft called expired)? Is the journal in one voice, appended, never rewritten? **Then the decisions that changed during the steps and in the later steps** (the journal's "changed", "corrected", "from 06 UI design", "from 07 Security"): is the old version still written anywhere, above all in files the step didn't touch?
4. Report: findings by severity, each with the line, what's wrong and what to change; then what's done well; then what you couldn't evaluate. The user picks what to apply.

## The bad version and why not
- The table's class sent out as JSON: a new column appears in the API by itself, and an internal field (the role, the approval) can be written by anyone who sends the right JSON.
- Verbs in every path (`/getFoods`, `/createRecipe`): neither REST nor clean RPC; everyone invents another verb.
- `200 OK` with `{"error": …}` in the body: the app, the proxies and the monitoring think it worked.
- Every controller with its own error shape: the app handles every screen differently.
- A list with no limit: it works on your data and falls over at the first person with 5,000 entries.
- Offset on a growing list: slower and slower, with rows repeated or lost.
- A `POST` that creates on every repeat: on a bad network, two meals in the log; a toggle sent twice cancels itself.
- A field renamed "because it reads better" after the release: the app on the phone breaks, and its offline entries are refused.
- `/v2` for every change: five versions to keep alive.
- The `userId` taken from the request's body: anyone writes into someone else's log.
- What a person searched or ate in the address (`GET /recipes?q=…`): it lands in every access log and proxy.
- An upload trusted by its name or its `Content-Type`: an HTML page named `photo.jpg` and sent as `image/jpeg` passes.
- The contract written by hand in a document with nothing comparing it to the server: in two weeks it says something else.
- The Java exception's message sent in the answer: it shows an attacker the classes and the database.

## What breaks if you skip it
Every controller decides its endpoints in the first PR, each one differently. On a bad network, repeated saves make duplicates. The screens don't know what one request gives them: five requests per screen, slow on mobile, or one huge answer. Planning can't estimate. Above all, after the first release every mistake in the contract stays: the app kept on the phone, offline for days, still calls the old endpoint, so a fix costs a new endpoint and weeks with two versions alive.

## The principle behind it
**An API is a promise you can't take back.** The code behind it can be rewritten any day; the contract only grows, because someone relies on every visible detail (Hyrum's law), here an old app on an offline phone. Joshua Bloch ("How to Design a Good API and Why it Matters", OOPSLA 2006): public APIs are forever, you can always add but never remove, so when in doubt leave it out; and a good API is easy to use right and hard to use wrong. So design from the outside in: from what the screen and the flow need, not from what the table holds. And on Postel's principle ("be conservative in what you send, liberal in what you accept"), the IETF's current view (RFC 9413, 2023) is that unlimited tolerance hides bugs: ignore the fields you don't know, but validate strictly what you use.

## How to apply it at work
- At a new company, read the OpenAPI contract (its Swagger UI) before the code, and ask which clients the API has and how old the oldest is.
- For a change, a short design doc with only the steps it touches. **A new endpoint:** its row in the map, with who may call it and its feature; its shape in the module's endpoint file and in the contract, the linter passing; its new codes in the catalog; its list, if it answers one; what it does when sent twice; its tests, most given by the guard tests already running over every endpoint. **A new client:** who it is, how it proves who it is and how old a version can still call, then the change policy, since a store app can't be made to update.
- In code review, for a new endpoint ask: who may call it, and where is the test where someone else gets 404? What happens when it arrives twice? Does the list have a limit? Does it break an old client (oasdiff)? Does a table's class go out? Are the errors in the shared format?
- For an integration with another service: ask for its contract, check its webhooks' signatures, handle repeats and order.
- As a senior or CTO: the company's API guidelines (like Zalando's, Google's, Microsoft's), turned into rules checked automatically (a linter ruleset in CI); a deprecation policy with dates and headers; a catalog of the APIs; for a public API, the API is a product: documentation, examples, SDKs, a changelog, limits per client.

## Done when
- [ ] the clients, how each proves who it is, the oldest version still calling, one origin or CORS, and the style per kind of data
- [ ] the map: every endpoint per module with method, path, who, feature, limited and one-way door; every PRD criterion reaches one or has a reason; every main screen shows after at most one round trip, or has an endpoint built for it, or a reason; the total counted by a script; chosen by the user
- [ ] the shape rules and the error catalog, decided once; every maximum size from the largest valid request, measured
- [ ] every endpoint: request and answer with type, required, rule, why, personal or health data, an example; status and error codes; who may; the differences from the table; chosen by the user where there was a choice
- [ ] `openapi.yaml` holds every endpoint, every answer that can happen (a creation's 201, with `Location` only where it has an address, and its repeat's 200) and an example for every request and success answer, and passes the linter with the project's rules, each rule proved on its planted mistake exactly once; it agrees with the markdown
- [ ] every list: a written limit or paging, the maximum page, a unique order; tried on generated data
- [ ] every write: its behaviour on a repeat and under concurrency, the lookup before every quota; reproduced on a real database
- [ ] the sync protocol, if the product works offline, with its diagrams and what happens after a backup restore; chosen by the user
- [ ] webhooks, every outside call with its time limit and retries, long operations and files with their upload rules
- [ ] when the rules start; the allowed and breaking changes, what the contract can't show included; how a version is retired; what CI stops
- [ ] how the contract is checked in Build, and the tests per endpoint, the guard tests' counts from a script
- [ ] every one-way door an ADR, chosen by the user; the earlier files re-read after each one
- [ ] every question the data model left for the API answered
- [ ] a glossary for every term the files use, grown with the steps
- [ ] the README: status, summary, where to start, the files and how they stay in agreement, what it builds on, what we skip and why, open questions, the ADRs in three groups, the journal in one voice; read against every file, its counts matching the scripts, "Next" naming today's next step
- [ ] the row in `docs/02-design/README.md` set to done
- [ ] the five sequence diagrams (a repeat, the sync's push and pull, the slowest outside call, the payment), UML, drawn by `diagrams.sh`, their numbers matching a step table in the Markdown, each opened, no text overlapping
- [ ] oasdiff's rules tried on planted changes

## Sources
1. IETF, [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html), 2022; [RFC 6585](https://www.rfc-editor.org/rfc/rfc6585.html) (428).
2. IETF, [RFC 9457: Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457.html), 2023.
3. IETF, [RFC 5789 (PATCH)](https://www.rfc-editor.org/rfc/rfc5789.html), [RFC 7396 (JSON Merge Patch)](https://www.rfc-editor.org/rfc/rfc7396.html), [RFC 6902 (JSON Patch)](https://www.rfc-editor.org/rfc/rfc6902.html).
4. [OpenAPI Specification](https://spec.openapis.org/oas/latest.html); springdoc, [properties](https://springdoc.org/properties.html) (OpenAPI 3.1 by default).
5. Redocly CLI, [lint](https://redocly.com/docs/cli/commands/lint), [recommended rules](https://redocly.com/docs/cli/rules/recommended), [configurable rules](https://redocly.com/docs/cli/rules/configurable-rules); [oasdiff](https://github.com/oasdiff/oasdiff).
6. Spring Framework 7, [API versioning](https://docs.spring.io/spring-framework/reference/web/webmvc-versioning.html), [API version in request mapping](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-controller/ann-requestmapping.html#mvc-ann-requestmapping-version), [the MVC config](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-config/api-version.html); Spring Boot 4.1, `spring.mvc.apiversion.*` (`WebMvcProperties`).
7. Stripe, [Idempotent requests](https://docs.stripe.com/api/idempotent_requests); IETF, [draft-ietf-httpapi-idempotency-key-header](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/), version 08, 22 October 2026, an active draft until 25 April 2027 (read 2026-11-10).
8. Google, [API Improvement Proposals](https://google.aip.dev/): 121, 136, 151, 155, 158, 180.
9. Zalando, [RESTful API Guidelines](https://opensource.zalando.com/restful-api-guidelines/) (#110, #112 recommending `examples` over `x-extensible-enum` since October 2025, #160, #254; read 2026-11-10); Microsoft, [Azure REST API Guidelines](https://github.com/microsoft/api-guidelines/blob/vNext/azure/Guidelines.md); GitHub, [API versions](https://docs.github.com/en/rest/about-the-rest-api/api-versions).
10. Martin Fowler, [Richardson Maturity Model](https://martinfowler.com/articles/richardsonMaturityModel.html), 2010; [Tolerant Reader](https://martinfowler.com/bliki/TolerantReader.html), 2011.
11. Markus Winand, [No Offset](https://use-the-index-luke.com/no-offset).
12. IETF, [RFC 9745 (Deprecation)](https://www.rfc-editor.org/rfc/rfc9745.html), [RFC 8594 (Sunset)](https://www.rfc-editor.org/rfc/rfc8594.html).
13. OWASP, [API Security Top 10, 2023](https://api-security.owasp.org/editions/2023/en/0x11-t10).
14. [Hyrum's Law](https://www.hyrumslaw.com/); IETF, [RFC 9413: Maintaining Robust Protocols](https://www.rfc-editor.org/rfc/rfc9413.html), 2023; Joshua Bloch, [Bumper-Sticker API Design](https://www.infoq.com/articles/API-Design-Joshua-Bloch).
15. [Standard Webhooks](https://www.standardwebhooks.com/).
16. oasdiff 1.35.0 (28 October 2026; the levels first read in 1.33.0, the same in 1.35.0): [breaking changes](https://github.com/oasdiff/oasdiff/blob/v1.35.0/docs/BREAKING-CHANGES.md) (levels, `--severity-levels`, `--err-ignore`), [deprecation](https://github.com/oasdiff/oasdiff/blob/v1.35.0/docs/DEPRECATION.md), [git revisions](https://github.com/oasdiff/oasdiff/blob/v1.35.0/docs/GIT-REVISION.md), [diff](https://github.com/oasdiff/oasdiff/blob/v1.35.0/docs/DIFF.md); the default levels in [`checker/rules.go`](https://github.com/oasdiff/oasdiff/blob/v1.35.0/checker/rules.go) (read 2026-11-10).
17. Schemathesis 4.32.7 (27 October 2026; its checks first read in 4.31.0, the same in 4.32.7, read 2026-11-10): [checks](https://github.com/schemathesis/schemathesis/blob/v4.32.7/docs/reference/checks.md), [stateful testing](https://github.com/schemathesis/schemathesis/blob/v4.32.7/docs/guides/stateful-testing.md) (links learned from `Location`), [authentication](https://github.com/schemathesis/schemathesis/blob/v4.32.7/docs/guides/auth.md) (Web Fuzzing Commons), [object-level authorization](https://github.com/schemathesis/schemathesis/blob/v4.32.7/docs/guides/object-level-authorization.md) (peers); [EvoMaster](https://github.com/WebFuzzing/EvoMaster).
18. [Kubernetes, API overview](https://kubernetes.io/docs/reference/using-api/) (versions per API group).
19. OWASP, [File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) (the type from the content, not the name).

## Next
UI design (`/ui-design`): the screens, built on what each endpoint gives. Then Security (`/security`) checks it all: the session, the limits, CSRF, Row-Level Security; AI design (`/ai-design`) follows for a product with AI, then Planning. Each of them that changes the contract writes the change here too: `openapi.yaml`, the endpoint file and the map in one commit, the linter passing, with its journal line. In Build, each slice's part of the contract is copied next to the code and compared with it until the slice ships (step 10).
