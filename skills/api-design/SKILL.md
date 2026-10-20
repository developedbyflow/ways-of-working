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
- **Teach while you go, starting from the problem.** The user may know only the frontend. **Before any tool, file or check, say what problem it prevents, in a situation a frontend developer has lived** (the backend renamed a field and the screen showed `undefined`; Swagger said one thing and the server sent another; every endpoint returned its errors in a different shape). Only then how it works. Never answer a "why" with more "how"; when the user asks "what for?", the answer is one sentence of purpose. Every term gets one line on what it is and what it brings, compared with something a frontend developer knows: the types generated from OpenAPI (`schema.d.ts`) already read a contract; TanStack Query retrying a failed request is why the server must survive repeats; "Load more" with `useInfiniteQuery` is cursor pagination; MSW is a fake server. When the server is in Java, explain Spring the first time, compared with ASP.NET Core: `@RestController` and `@GetMapping` are a controller with `[HttpGet]`; requests and answers are Java `record`s checked with `@Valid` and Jakarta Bean Validation (like DataAnnotations); errors leave through `ProblemDetail` (Spring 6.0 and later); springdoc writes the OpenAPI contract from the controllers, as Swashbuckle does in .NET. **At a technical chunk, plain words and one example with numbers come first,** then what it means for the user; the tables after, or only in the file. A sentence that can be read two ways is settled with options A/B before anything is written.
- **One step per message, and big steps in chunks.** Show a step, wait for the user's OK, then the next. Steps 3, 4 and 7 are big: one module or one sub-topic per chunk; **count the chunks before announcing them** and say so if the count changes; save and commit each chunk once it's confirmed. Why: each decision needs to land before the next one builds on it.
- **Ask only when there's a real choice.** When all the arguments point one way and no realistic alternative fits, write it as decided, with its arguments, and move on to the next real choice. Ask when there are at least two options the user could reasonably pick; once chosen, the choice is final. When the user voices a fear or a doubt next to a choice, resolve it before recording the decision.
- **Before recommending, weigh two things besides the technique:** what most of the industry does, and what serves the user's purpose (what they'll meet at work counts as a real argument). When the options are technically equal, say so first and recommend on those grounds. Change a recommendation only for a new fact, and name the fact. Learned on 2026-10-14: a first recommendation of no version in the path, flipped once the user asked what's best practice, made every other recommendation look unreliable.
- **Every number, shape and rule with its argument:** a known standard (named, its official page checked on the web), a target set earlier (cited), or a guess marked `[ASSUMPTION]` with its reasoning. For a choice, an argument card: why; the main alternative and who uses it; when the alternative is better; what someone may answer, and the reply; the source. When the industry is split (design-first or code-first, an envelope or not, PATCH or PUT), name the camps. In the docs, every table of fields has a "why" column. Why: the user must be able to defend each choice in a review or a technical discussion.
- **Where the documents are:** the `Project documents:` line in `CLAUDE.md` gives the documents folder; without it, use `docs/` in the current folder. Write into `docs/02-design/05-api-design/` and the ADRs into `docs/00-project/adr/`; create them if they don't exist.
- **Read first:** the PRD (`docs/01-discovery/04-prd.md`: features, criteria, journeys, the build order), the system design (`docs/02-design/01-system-design/`: the flows, the targets for answer times, offline, the providers), the compliance folder (rights, consents, what counts as health data), the architecture (`docs/02-design/03-architecture/`: the modules, the shared rules, the conventions for names in the API and JSON, the stack, the frontend's way of talking to the API), the data model (`docs/02-design/04-data-model/`: the tables, the data on the device, the questions it left for the API), and the ADRs. Ask only what's missing.
- **An existing API is a source of facts, not a model.** Read it for which endpoints exist, which the app really calls, what's missing or inconsistent. An endpoint doesn't become right because it's there.
- **The names, errors, login and compatibility rules come from the architecture; the tables from the data model; this step decides the contract.** Don't change a convention or a table here; if one is wrong, stop, say so, and on a yes fix it where it lives, with a journal line. **The same for the PRD and compliance:** any change, even one that only closes a gap, is shown to the user first with its exact text.
- **The table isn't the contract.** Every answer has its own shape, built for what the screen needs: internal columns stay out, computed fields come in, a name can differ. Write the differences from the table down, per endpoint.
- **Two forms of the contract, each with its own reader** (chosen on 2026-10-13). The purpose in one sentence: **the endpoints are written in YAML too, so a program finds the design's mistakes now and, in Build, checks that the code follows the same design.**
  - **markdown, for people:** per module, every endpoint with its fields, rules and **why**; the user reads and approves this one;
  - **`openapi.yaml`, for programs:** the same endpoints in the standard format, in the OpenAPI version the project's generator produces (springdoc: 3.1 by default), so the Build comparison compares like with like. **Checked by a linter** (Redocly CLI, or Spectral) with a `redocly.yaml` next to it: the `recommended` rules, `no-invalid-media-type-examples` and `no-unresolved-refs` as errors, `paths-kebab-case`, and the architecture's conventions as the project's own rules (field names in camelCase on `SchemaProperties`, every 4xx in Problem Details, every list with a limit). **A chunk isn't done until the linter passes.** Tried on 2026-10-13: four planted mistakes (a camelCase path, a misspelled `$ref`, an example breaking a `minimum`, a snake_case field), all four caught.
  - **In Build, when the architecture chose code-first** (the contract generated from the code), the code stays the source: per slice, the contract generated from the code is compared with the design's for that slice's endpoints (`oasdiff diff --exclude-elements description,examples,title,summary --fail-on-diff`), and a difference stops CI until the code is fixed or the design changes with a journal line; a copy of the slice's part of the design sits next to the code while the slice is built, when the documents live in another repo. Once the slice ships, the generated contract replaces the design for those endpoints, and the architecture's rule takes over (oasdiff against production). **Tried on 2026-10-14, three things the comparison needs:** both contracts **cut to the slice first** (its addresses and only the schemas they use), since `--match-path` filters the addresses but still compares every schema; **the schema names are the contract's,** since springdoc names a schema after its class and the conventions' `FoodResponse` against the design's `Food` stops the comparison (`@Schema(name = …)`, or one rule dropping the suffix); **every answer field `required`,** since oasdiff reports a removed optional field only as INFO. **The generated contract is committed** in the code repository, so a PR shows its contract changes, and production's is `main`'s (`origin/main:path`, read by oasdiff directly). **When the architecture chose design-first,** `openapi.yaml` stays the source and the server's interfaces are generated from it (openapi-generator).
  - Not markdown alone: nothing checks it now, and nothing compares the code with it later. Not YAML alone: the user would approve the design by reading thousands of lines of YAML, and the reasons would live nowhere. The validation agent compares the markdown and the YAML, endpoint by endpoint.
- **Every endpoint in full detail now, not per slice** (chosen on 2026-10-13): the UI design comes right after and needs to know what each screen gets; the data model is already whole, so most shapes come from it quickly; an endpoint is still free to change until the first release, so a later change costs little. The alternative (the map now, the shapes per slice in Build) wins when the PRD may change a lot after the first slices.
- **The user decides** the map of endpoints (step 3), every real choice in the shapes (step 4), the sync protocol's shape (step 7) and every ADR (step 11). You give the options and a recommendation; they choose. One decision at a time.
- **Check the standards on their official pages,** not from memory: HTTP's methods and status codes (RFC 9110), Problem Details (RFC 9457), the patch formats, the OpenAPI version, the framework's features (Spring Framework 7 has API versioning built in; Spring Boot 4 uses Jackson 3), the tools' rules. **Write "tried" only for what a test proved,** and keep every script in `checks/`. **A tool is tried the way the linter was, on planted cases:** oasdiff on copies of the contract with one change each (a stricter limit, a removed field, a deprecation with too short a sunset), each expected to stop or pass, its default levels read in its own source; a tool downloaded for the trial (a Docker image) is named with its size and asked for first.
- **UML sequence diagrams,** written as PlantUML (`.puml` next to its `.svg` in `diagrams/`): the parts as lifelines, the step numbers matching the tables, failures and branches as `alt`, `break`, `loop`, a lost answer as a lost message. `docs/02-design/diagrams.sh` (set up by `/docs-setup`) draws every diagram of the design from text, in a standard notation (decided 2026-10-20), so they read the same at any company; never a hand-made SVG, a home style, or a script that draws SVG itself. One per main flow, **drawn at its step:** a repeated request at step 6, the sync at step 7, the slowest call to an outside service and the payment at step 8; each with a title and a legend. Open each one before committing: no text overlaps. Left to the end, two of the four were missing at the check.
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

The status codes beyond the architecture's: **201** for a creation, with `Location` pointing to the new thing; **202** "accepted, working on it"; **204** no body (a deletion); **304** "nothing new" (with an ETag); **412** a condition failed and **428** a condition is required (RFC 6585); **413** the body is too large; **415** a format the endpoint doesn't take.

**In the contract, every answer that can happen:** a creation answers **201 with `Location`**, and its repeat (the app's id already there) **200 with the stored row**; **400 on every address that checks a header** (the app's version); **413 and 415 on every address with a body**, since the proxy or the framework refuse before the controller. A header an `<img>` or a plain file download can't send (the app's version) is optional on those addresses. The check found 65 addresses without their 400 and 17 creations with only a 201.

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
| Examples | in the markdown, in the contract | one per request and success answer in the contract, **generated from the schemas** with realistic values chosen per field name (a day's targets read differently from 100 g of chicken), stored once per schema under `components/examples`, and checked by the linter against their schema; written chunk by chunk, not at the end |
| The error codes | — | each code matches the contract's pattern for a code (digits allowed if a code has them: `foods.parts_exceed_100g`) |

## Lists
Use this at step 5.

| Kind | Looks like | Good at | Weak at |
|---|---|---|---|
| No paging, with a written limit | the whole list | small, bounded lists | if the limit isn't real, the list grows without end; Google (AIP-158) and Microsoft both say paging added later breaks clients |
| Offset or page number | `?offset=40&limit=20`, `?page=3` | "page 7 of 12", small admin tables | the database reads and discards the skipped rows, so deep pages slow down; a new row shifts everything, so a row shows twice or goes missing (Markus Winand, "No Offset") |
| Cursor (keyset) | "after this row", by a unique order such as `(created_at, id)` | growing lists, endless scrolling; speed doesn't depend on the page | can't jump to page 7 |
| "Changed since N" | a growing number on changes | sync | — |

The rules: the server enforces a maximum page size; the order always has a unique tie-breaker (the id); the cursor is opaque, the client never builds it; a list pages from its first version. Zalando asks for cursors (rule 160).

## Repeats and concurrent writes
Use this at step 6.

| Kind | How | Worth it when |
|---|---|---|
| By itself | PUT or DELETE at an address holding an id the client made | the client makes the ids |
| Uniqueness in the database | the id in the body; the second time, the database sees the id and saves nothing | creations with ids made by the client |
| An idempotency key | an `Idempotency-Key` header; the server keeps the first answer for a while and gives it again. Stripe keeps keys at least 24 hours and refuses a key reused with other parameters; an IETF draft (last version October 2025, expired without becoming a standard) suggests 422 for a reused key with another body and 409 while the first request still runs; Google puts a `request_id` in the request (AIP-155) | effects that cost money, send something or call a paid service |
| The action written as a state | "the day is complete" (`complete: true`), not "toggle" | toggle buttons |

**The trap:** a save with a version (optimistic locking), repeated after a lost answer, meets itself: the first save raised the version from 5 to 6, the repeat still says 5 and gets 409, "someone else changed this", though it was the same person. Every write with a version needs a rule for its repeat.

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
| a new value in a fixed list in an answer | yes, for a client that handles every value; **oasdiff calls it an error by default** (`response-property-enum-value-added`): when the app always has an "other" case, a levels file lowers it to a warning, still shown in the PR. Zalando's `x-extensible-enum` (#112) doesn't fit code-first: springdoc writes `enum`, and the TypeScript types would lose the values. For the sync's own words (an outcome, a mark's kind) the "other" case is written: the operation stays waiting |
| a stricter validation (a maximum of 100 becomes 50) | yes: what passed yesterday is refused today, offline entries included |
| a looser validation | no for a request; **yes for an answer** when one schema serves both: a newer app saves 80 servings where an older app's form allows 50 (oasdiff: `response-property-max-increased`). The app first, the server after, and the change accepted with oasdiff's `--err-ignore`, one line per address it reaches (12 for a recipe's servings) |
| another status or error code | yes, if the client handles it |
| another default order or page size | maybe: Hyrum's law, with enough users every visible behaviour is relied on |

Retiring an endpoint has two standard headers: `Deprecation` (RFC 9745, March 2025: a date as `@` and seconds since 1970) and `Sunset` (RFC 8594, 2019: an HTTP date, a hint that can move later); Spring Framework 7's `StandardApiVersionDeprecationHandler` sends them for a whole version. In the contract, `deprecated: true` and `x-sunset`, which oasdiff reads.

**Spring Framework 7's versioning, checked in its docs and source (7.0.9):** the version is one for the whole API; a method without a version answers every version ("intended to support clients created before a versioned alternative was introduced"); the changed method is `version = "2+"`, since a fixed `"2"` would also hide the method without a version at `v3`; the version read from the path needs `{version}` in the mapping (a common prefix), its parser skips the `v`, the supported versions written in the configuration (`spring.mvc.apiversion.supported`), and a predicate for the addresses without a version (`/api/health`), or Spring refuses them with 400. How springdoc writes a version taken from the path: try it in the first slice.

**What stops CI (oasdiff, levels read in its source):** `oasdiff breaking origin/main:<contract> <contract> --fail-on ERR --severity-levels <file> --err-ignore <file> --deprecation-days-stable 30`: a deprecation must give 30 days (`api-sunset-date-too-small`), a removal before the sunset or without a deprecation is an error. When `v2` is made, `v1` against `v2` with the prefixes stripped (`--strip-prefix-base`, `--strip-prefix-revision`) lists what the new version breaks on purpose.

## Security that belongs to the API's shape
Use this at steps 4–5. OWASP API Security Top 10 (2023); the rest is 07 Security's.

| Risk | Looks like | What API design does |
|---|---|---|
| API1, object level authorization | `/api/recipes/{id}` with someone else's id returns it | every endpoint says whose the thing is and what a stranger gets |
| API3, object property level authorization | a request sends `"isApproved": true` and the server saves it (mass assignment), or an answer shows fields it shouldn't | the request record holds only the fields the person may set; the answer only what they may see |
| API4, unrestricted resource consumption | endless lists, huge uploads, too many requests | the maximum page and body size; which endpoints get a rate limit (the numbers in 07) |

## Steps

### 1. Read what exists
The PRD's features, criteria and build order; the system design's flows and targets; compliance's rights; the architecture's shared rules, conventions, stack and the frontend's way of talking to the API; the data model's tables, the data on the device and **the questions it left for the API** (search its files for "API design"); the ADRs. List what's missing and ask only that.

**If an API exists,** read it for facts: the endpoints, which the app calls, what's inconsistent. Not as a model.

### 2. Who calls the API, and in which style
The clients (the app, the services that send webhooks, the admin, a future partner), **how old an app that still calls can be** (days offline, how it updates), and the style for each kind of data (REST, sync, webhooks), with the argument card. Usually decided already by the system design and the architecture: then write it as decided, with the reasons.

### 3. The map of endpoints, before the shapes
From the PRD's features and criteria and the flows, per module (one chunk per module, counted first): the resources (nouns) and the actions (verbs that aren't create, read, change, delete), each with its method, path, who calls it, and the PRD feature it serves.
- **every PRD criterion reaches an endpoint, or a written reason** (computed on the device, shown from data already there);
- **every endpoint serves a feature:** no endpoint "we may need" (Joshua Bloch: when in doubt, leave it out; you can always add, never remove);
- how many requests each main screen makes, on the system design's slow network: a screen that needs five requests gets one endpoint built for it, or a reason;
- **mark the one-way doors:** what the app calls offline or what the phone stores, since an old app calls it for days after a release.

**The user decides** the map.

### 4. The shapes, module by module
**Chunk 1, the rules every endpoint follows,** decided once: the envelope or not, the list shape, `null` against a missing field, numbers, fixed lists of values (the client tolerates a new value), partial changes (PUT, PATCH or an action), the headers (the app's version, the request id), **the catalog of error codes** (`module.reason`, each with its status and its `params`), the maximum body size. Start `openapi.yaml` with them (the shared error answer, the list shape) and `redocly.yaml` with the conventions as rules.

Then one chunk per module, every endpoint in full:
- the request and the answer: field, type, required, rule, **why**, personal or health data, one example; **a table for every shape, requests and summaries included, never a prose list** (the check found nine shapes written as sentences);
- the status codes and the error codes it can return; who may call it (the architecture's access rules), and what a stranger gets;
- **the request holds only the fields the person may set; the answer only what they may see;**
- **the differences from the table, written** (a computed field, a hidden one, another name);
- **every PRD criterion tried on the shape:** "can this screen show everything from this one answer?";
- added to `openapi.yaml` with its examples (generated from the schemas, as in the shape rules), every answer that can happen (the status codes above), and the linter passes before the chunk is done.

**The user decides** each real choice.

### 5. Lists
Every list with its size today and at 10× (from the data model's questions): no paging only with a written limit; a cursor for growing lists; offset only where "page 7" is needed and the list is small; the maximum page size; the order with a unique tie-breaker; only the filters and sorts the screens need. **Try it on generated data** in a real database: a cursor's pages lose and repeat no row when rows are added between pages; keep the script in `checks/`.

### 6. Repeats and concurrent writes
For every write, what happens when it arrives twice: by itself (an id made by the app, PUT, the database's uniqueness), with an idempotency key (where the effect costs money, sends something or calls a paid service), or written as a state rather than a toggle; what the app gets the second time; **a save with a version, repeated, doesn't meet itself.** Concurrency: the version the screen saw and 409 with who changed it (or `If-Match` and 412), or "the last change wins" where that's the rule. **Reproduce each case on a real database** (two sessions, the same request twice), keep the scripts in `checks/`, and list the tests that prove it in Build. **Every write goes in the table, the small ones too:** a report (give it the app's id), leaving a group or accepting an invite sent twice (the second sees the first's result: the app takes it as done), a file uploaded twice (the orphan swept); the check found ten missing. Write each creation's 201 with `Location` and its repeat's 200 into the contract now. Draw the repeat's sequence diagram.

### 7. Sync
Only for a product that works offline; in chunks:
- **push:** the batch's shape and its maximum size; the answer per operation (confirmed; lost to a newer change; refused, with its error code); how the device says a row is new; what an old app version sends; **each row checked on its own** in the service, not with `@Valid` on the batch, which would refuse 99 good rows for one bad one; what the device does with a 4xx for the whole batch (sends one operation at a time, so it never loops); a word it doesn't know keeps the operation waiting;
- **pull:** "changed since N", in pages that never split the rows of one number; the first load of the window kept on the device; a reload when the device is below what was purged;
- **the copies** the device keeps (reference data, settings): how they arrive, their size on the slow network, a compact shape where the size demands it; **the data model decides what the device stores,** so an `ETag` goes only on what it stores, and the rest is asked whole.

One sequence diagram per direction. **The user decides** the shape. **Then re-read the data model's integrity, lifecycle and device files:** the protocol changes their rules (how a day's row is saved, what a long-deleted row gets, who writes the log); the check found four contradictions there.

### 8. Outside services, long operations and files
- **webhooks received:** the signature checked, a fast 2xx, processed after, the repeat recognised by the event id, no reliance on order; a callback after an account is gone saved, never refused forever;
- **operations longer than a request:** 202 and a status address, or an email with a link;
- **operations of a few seconds** (an AI call): the request waits, with a time limit; what the app sees on failure;
- **files:** through the API (`multipart/form-data`) or straight to storage with a signed address valid a few minutes; the maximum size; download links that expire;
- **webhooks sent,** if any: Standard Webhooks (`webhook-id`, `webhook-timestamp`, `webhook-signature`, retries with growing pauses);
- the sequence diagrams of the slowest outside call and of the payment.

### 9. Changing the contract
The architecture's compatibility rule, made into a list: which changes are allowed and which break (a new value in a fixed list in an answer and a stricter validation included); what the client does with what it doesn't know; how a breaking change is made (a new address, `Deprecation` and `Sunset`, how you measure that nothing calls the old one); when the app is told to update; which oasdiff checks stop CI, **tried on planted changes** (above). With the version in the path, settle with the user whether a break raises the whole API or only one address, after reading the framework's model.

### 10. Checking the contract
- in Design: the linter on `openapi.yaml`, with the project's rules;
- in Build, per slice: the comparison between the contract generated from the code and the design's (above); the tests every endpoint gets (401 without login, 404 for someone else's thing, 403 for a read-only account, 400 and 422, the repeat, 429 where limited); whether a tool that sends generated requests from the contract (Schemathesis) runs in CI, with its argument card. **When it runs follows the CI budget the architecture counted** (free minutes a month, the 10-minute PR): on MacroMate, 2–3 nights a week with the end-to-end matrix. Schemathesis 4.31 checks a 500, an answer outside the contract, invalid data accepted, and with two people set up as peers **one person reading another's item** (OWASP API1); it learns the links between addresses from `Location`; a batch that answers 200 with refusals is configured as such. The alternatives: EvoMaster (white-box, writes JUnit tests, supports Java up to 21), RESTler (Microsoft Research). The guard tests that go over every address: 401, 404 for someone else's, 403 for a read-only account, 400 for a broken body, every error in Problem Details.

### 11. The big decisions become ADRs
Only one-way doors (for example the sync protocol's shape, how repeats are handled, the pagination style, the versioning). First propose the list, with **what doesn't get an ADR and why** (grouped: rules in the code, what other documents own, what can change freely before the first release). When a decision was already taken in the steps, write the ADR and give it to the user to check, a few at a time. Otherwise one at a time: options, your recommendation, **the user chooses**. **After each ADR, re-read the earlier files it changes,** the architecture's, the data model's and the earlier ADRs included, link each decision to its ADR, and look for the old version of a decision that changed during the steps.

### 12. Check it
- every PRD criterion reaches an endpoint, or has a reason;
- every endpoint has a feature, an owner module, an access rule, its error codes and an example;
- every list has a written limit or pagination; every write has its behaviour on a repeat;
- no table class goes out as JSON; every difference from the table is written;
- the markdown and `openapi.yaml` agree, endpoint by endpoint, and the linter passes;
- every error code is in the catalog, with a text in each of the product's languages planned;
- nothing contradicts the architecture, the data model, compliance or the system design; every question the data model left is answered.

Run the check with a **separate agent** that has only the documents (`/api-design validate <folder>`), then verify its findings in the files before showing them: it can be wrong. Look especially for **contradictions left by a changed decision**, above all in the files the step didn't touch (the architecture's conventions, testing and frontend files, the data model's integrity, lifecycle and device files, an ADR). Tell the user upfront how long it usually takes (15–20 minutes; 18 on MacroMate) and that there's nothing for them to do meanwhile. Show the verified findings by severity with a recommendation; a rule that changes in another step's document is shown with its exact new text before it's written.

Write as you go: each step's file once the user confirms it, with a journal line in the README; **the README's summary, "not doing" and glossary grow with the steps**, not at the end. At the end, set this step's row in `docs/02-design/README.md` to done, with the date, and link the folder.

```
docs/02-design/05-api-design/
  README.md            the entry: status, summary, files, what we skip, open questions, ADRs, glossary, journal
  01-clients.md        02-map.md           03-shape-rules.md
  04-lists.md          05-repeats.md       06-sync.md
  07-outside.md        08-changes.md       09-checks.md
  endpoints/           one file per module: [module].md
  openapi.yaml         every endpoint, checked by the linter
  redocly.yaml         the linter's rules: the conventions as checks
  checks/              the scripts: the lists, the repeats, the sync's pages, oasdiff's planted changes, the examples' generator
  diagrams/            the sequence diagrams (.puml + SVG)
docs/00-project/adr/
  NNNN-[title].md …
```

The README:

````markdown
# API design – [Product]
| | |
|---|---|
| **Status** | draft / confirmed by [who], [date] |
| **Author** | |
| **Updated** | |
| **Next** | 06 UI design, 07 Security |
## In one page
The clients and the style, how many endpoints per module, the main choices (repeats, pagination, sync, versioning): 5–6 lines.
## The files
| File | What it answers |
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
| `01-clients.md` | `\| Client \| Calls \| Oldest version still calling \| Style \|` |
| `02-map.md` | per module `\| Method \| Path \| Who \| Feature \| One-way door \|`; the requests per main screen |
| `03-shape-rules.md` | the rules of chunk 1; the error catalog `\| Code \| Status \| Params \| When \|` |
| `endpoints/[module].md` | per endpoint: what it does, who may, the request and answer `\| Field \| Type \| Required \| Rule \| Why \| Personal / health \|`, the differences from the table, the status and error codes, the repeat, one example |
| `04-lists.md` | `\| List \| Rows now / at 10× \| Paging \| Max page \| Order \|` |
| `05-repeats.md` | `\| Write \| Sent twice \| Concurrent \| Proved by \|` |
| `06-sync.md` | push, pull, the copies, with their diagrams |
| `07-outside.md` | webhooks, long operations, files |
| `08-changes.md` | allowed and breaking changes, retiring an endpoint, what CI stops |
| `09-checks.md` | the linter's rules, the Build comparison, the tests per endpoint |

And one file per decision in `docs/00-project/adr/NNNN-[title].md`, with the same sections as every ADR: status, date, context, options (for and against), decision, consequences, revisit when.

## Validate mode
`/api-design validate <folder>`: judge an existing API design or contract, change nothing.
1. Read the folder, `openapi.yaml`, its ADRs and the README's journal, the PRD, the system design, compliance, the architecture and the data model; the running API's contract if it exists.
2. Check the template and "Done when" item by item, citing the lines; run the linter.
3. Then ask: does every PRD criterion reach an endpoint? Does every endpoint have a feature, an owner, an access rule, its errors and an example? Does any answer copy a table's class, or any request accept a field the person may not set? Does every list have a limit or paging, every write a behaviour on a repeat, every versioned save a rule for its own repeat? Do the markdown and the YAML agree? Is any change listed as allowed actually breaking (a new enum value in an answer, a stricter validation)? Is every term explained? **Then the decisions that changed during the steps** (the journal's "changed", "corrected"): is the old version still written anywhere, above all in files the step didn't touch?
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
- The contract written by hand in a document with nothing comparing it to the server: in two weeks it says something else.
- The Java exception's message sent in the answer: it shows an attacker the classes and the database.

## What breaks if you skip it
Every controller decides its endpoints in the first PR, each one differently. On a bad network, repeated saves make duplicates. The screens don't know what one request gives them: five requests per screen, slow on mobile, or one huge answer. Planning can't estimate. Above all, after the first release every mistake in the contract stays: the app kept on the phone, offline for days, still calls the old endpoint, so a fix costs a new endpoint and weeks with two versions alive.

## The principle behind it
**An API is a promise you can't take back.** The code behind it can be rewritten any day; the contract only grows, because someone relies on every visible detail (Hyrum's law), here an old app on an offline phone. Joshua Bloch ("How to Design a Good API and Why it Matters", OOPSLA 2006): public APIs are forever, you can always add but never remove, so when in doubt leave it out; and a good API is easy to use right and hard to use wrong. So design from the outside in: from what the screen and the flow need, not from what the table holds. And on Postel's principle ("be conservative in what you send, liberal in what you accept"), the IETF's current view (RFC 9413, 2023) is that unlimited tolerance hides bugs: ignore the fields you don't know, but validate strictly what you use.

## How to apply it at work
- At a new company, read the OpenAPI contract (its Swagger UI) before the code, and ask which clients the API has and how old the oldest is.
- In code review, for a new endpoint ask: who may call it, and where is the test where someone else gets 404? What happens when it arrives twice? Does the list have a limit? Does it break an old client (oasdiff)? Does a table's class go out? Are the errors in the shared format?
- For an integration with another service: ask for its contract, check its webhooks' signatures, handle repeats and order.
- As a senior or CTO: the company's API guidelines (like Zalando's, Google's, Microsoft's), turned into rules checked automatically (a linter ruleset in CI); a deprecation policy with dates and headers; a catalog of the APIs; for a public API, the API is a product: documentation, examples, SDKs, a changelog, limits per client.

## Done when
- [ ] the clients, the oldest version still calling, and the style per kind of data
- [ ] the map: every endpoint per module with method, path, who and feature; every PRD criterion reaches one or has a reason; the one-way doors marked; chosen by the user
- [ ] the shape rules and the error catalog, decided once
- [ ] every endpoint: request and answer with type, required, rule, why, personal or health data, an example; status and error codes; who may; the differences from the table; chosen by the user where there was a choice
- [ ] `openapi.yaml` holds every endpoint, every answer that can happen and an example for every request and success answer, and passes the linter with the project's rules; it agrees with the markdown
- [ ] every list: a written limit or paging, the maximum page, a unique order; tried on generated data
- [ ] every write: its behaviour on a repeat and under concurrency; reproduced on a real database
- [ ] the sync protocol, if the product works offline, with its diagrams; chosen by the user
- [ ] webhooks, long operations and files
- [ ] the allowed and breaking changes, how an endpoint is retired, what CI stops
- [ ] how the contract is checked in Build, and the tests per endpoint
- [ ] every one-way door an ADR, chosen by the user; the earlier files re-read after each one
- [ ] every question the data model left for the API answered
- [ ] a glossary for every term the files use, grown with the steps
- [ ] the README: status, summary, what we skip and why, open questions, the ADR table
- [ ] the row in `docs/02-design/README.md` set to done
- [ ] the four sequence diagrams (a repeat, the sync, the slowest outside call, the payment), UML, drawn by `diagrams.sh`, their numbers matching a step table in the Markdown, each opened, no text overlapping
- [ ] oasdiff's rules tried on planted changes

## Sources
1. IETF, [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html), 2022; [RFC 6585](https://www.rfc-editor.org/rfc/rfc6585.html) (428).
2. IETF, [RFC 9457: Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457.html), 2023.
3. IETF, [RFC 5789 (PATCH)](https://www.rfc-editor.org/rfc/rfc5789.html), [RFC 7396 (JSON Merge Patch)](https://www.rfc-editor.org/rfc/rfc7396.html), [RFC 6902 (JSON Patch)](https://www.rfc-editor.org/rfc/rfc6902.html).
4. [OpenAPI Specification](https://spec.openapis.org/oas/latest.html); springdoc, [properties](https://springdoc.org/properties.html) (OpenAPI 3.1 by default).
5. Redocly CLI, [lint](https://redocly.com/docs/cli/commands/lint), [recommended rules](https://redocly.com/docs/cli/rules/recommended), [configurable rules](https://redocly.com/docs/cli/rules/configurable-rules); [oasdiff](https://github.com/oasdiff/oasdiff).
6. Spring Framework 7, [API versioning](https://docs.spring.io/spring-framework/reference/web/webmvc-versioning.html), [API version in request mapping](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-controller/ann-requestmapping.html#mvc-ann-requestmapping-version), [the MVC config](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-config/api-version.html); Spring Boot 4.1, `spring.mvc.apiversion.*` (`WebMvcProperties`).
7. Stripe, [Idempotent requests](https://docs.stripe.com/api/idempotent_requests); IETF, [draft-ietf-httpapi-idempotency-key-header](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/) (expired).
8. Google, [API Improvement Proposals](https://google.aip.dev/): 121, 136, 151, 155, 158, 180.
9. Zalando, [RESTful API Guidelines](https://opensource.zalando.com/restful-api-guidelines/); Microsoft, [Azure REST API Guidelines](https://github.com/microsoft/api-guidelines/blob/vNext/azure/Guidelines.md); GitHub, [API versions](https://docs.github.com/en/rest/about-the-rest-api/api-versions).
10. Martin Fowler, [Richardson Maturity Model](https://martinfowler.com/articles/richardsonMaturityModel.html), 2010; [Tolerant Reader](https://martinfowler.com/bliki/TolerantReader.html), 2011.
11. Markus Winand, [No Offset](https://use-the-index-luke.com/no-offset).
12. IETF, [RFC 9745 (Deprecation)](https://www.rfc-editor.org/rfc/rfc9745.html), [RFC 8594 (Sunset)](https://www.rfc-editor.org/rfc/rfc8594.html).
13. OWASP, [API Security Top 10, 2023](https://api-security.owasp.org/editions/2023/en/0x11-t10).
14. [Hyrum's Law](https://www.hyrumslaw.com/); IETF, [RFC 9413: Maintaining Robust Protocols](https://www.rfc-editor.org/rfc/rfc9413.html), 2023; Joshua Bloch, [Bumper-Sticker API Design](https://www.infoq.com/articles/API-Design-Joshua-Bloch).
15. [Standard Webhooks](https://www.standardwebhooks.com/).
16. oasdiff 1.33.0: [breaking changes](https://github.com/oasdiff/oasdiff/blob/v1.33.0/docs/BREAKING-CHANGES.md) (levels, `--severity-levels`, `--err-ignore`), [deprecation](https://github.com/oasdiff/oasdiff/blob/v1.33.0/docs/DEPRECATION.md), [git revisions](https://github.com/oasdiff/oasdiff/blob/v1.33.0/docs/GIT-REVISION.md), [diff](https://github.com/oasdiff/oasdiff/blob/v1.33.0/docs/DIFF.md); the default levels in `checker/rules.go`.
17. Schemathesis 4.31.0, [checks](https://github.com/schemathesis/schemathesis/blob/v4.31.0/docs/reference/checks.md), [stateful testing](https://github.com/schemathesis/schemathesis/blob/v4.31.0/docs/guides/stateful-testing.md); [EvoMaster](https://github.com/WebFuzzing/EvoMaster).
18. [Kubernetes, API overview](https://kubernetes.io/docs/reference/using-api/) (versions per API group).

## Next
UI design (`/ui-design`): the screens, built on what each endpoint gives. Then Security (`/security`) checks it all: the session, the limits, CSRF, Row-Level Security.
