---
name: architecture
description: "How the code is organized. The modules (C4 level 3) and the data each one owns, what a module looks like inside, where every requirement from the PRD, the system design and compliance lives in the code and how it's checked automatically, the rules every module follows (login and permissions, errors, logs, dates, concurrency, old app versions), the frontend's structure, the languages, frameworks and tools, the conventions people and AI agents follow, the testing strategy, the repo, documentation and technical debt, and the big choices as ADRs. Writes a folder: a README and one file per topic, with diagrams. Use after compliance, before the data model, the API and the screens; at work before a new module, a rewrite, or when every change breaks something else. Also judges an existing one: /architecture validate <folder>."
argument-hint: "[the product or the change] or validate <folder>"
---

# Architecture

## When to use it
After Compliance, before the data model, the API and the screens (04–06). It needs the PRD's requirements, the containers and flows from the system design and the new requirements from compliance. What it decides (the modules, the shared rules, the conventions) is the frame that 04–06 fill with tables, endpoints and screens. And before the first new code, before any AI agent writes code: the conventions here are what it reads to write the same way every time.

At work: a new service, a new module in an existing codebase, a rewrite, or when "every change breaks something else". Also in the first weeks at a new company, to understand the code.

## The problem it solves
The system design said which parts the system is made of: the app on the phone, the API, the database. It didn't say what's inside the API: where the code for the food log lives, who may write to the subscription tables, where a new feature goes, how you check that sync never loses data.

Without an answer, the code becomes whatever the first PRs made it: a big ball of mud, where everything is tied to everything, every change breaks something else, and switching the AI provider touches twenty files. With AI agents writing code it happens faster: each session picks its own style when nothing is written down.

Architecture decides **how the code is organized**: the modules and their boundaries, what a module looks like inside, how the code meets the requirements from the earlier steps, the languages and tools, the shared rules and how it's tested. A new feature then has an obvious place, and a change stays where it belongs.

## How to run it
- **The bar:** do what a senior engineer or the CTO at a well-run company would accept, in the simplest form that meets it. Use the real industry method and name it, so the user learns it. Say what you leave out and why.
- **Teach while you go:** the user may be doing this for the first time. Every term gets one line on what it is and what it brings, compared with something a frontend developer already knows: folders by type (`components/`, `hooks/`) or by feature (`features/journal/`) is already an architecture choice; a component that calls a hook that calls the API client is already layers; server data in TanStack Query and screen state in `useState` are already kinds of state, each with its place. Show the full picture of the topic, then mark what this product needs.
- **One step per message, and big steps in chunks.** Show a step, wait for the user's OK, then the next. Steps 4–11 are big: cut each into chunks (one sub-topic per message), **count the chunks before announcing them** and say so if the count changes; save and commit each chunk once it's confirmed.
- **Ask only when there's a real choice.** When all the arguments point one way and no realistic alternative fits, write the chunk as decided, with its arguments, and move on to the next real choice; asking "confirm?" on a foregone conclusion wastes the user's attention. Ask when there are at least two options they could reasonably pick, and once they've chosen, the choice is final: no "private now, public later".
- **Every number and every convention with its argument:** a known standard (named, its official page checked on the web), a target set earlier (cited), or a guess marked `[ASSUMPTION]`. For a convention or a tool, an argument card: why; the main alternative and who uses it; when the alternative is better; what someone may answer, and the reply; the source. When the industry is split, name the camps.
- **Where the documents are:** the `Project documents:` line in `CLAUDE.md` gives the documents folder; without it, use `docs/` in the current folder. Write into `docs/02-design/03-architecture/` and the ADRs into `docs/00-project/adr/`; create them if they don't exist.
- **Read first:** the PRD (`docs/01-discovery/04-prd.md`: features, journeys, glossary, non-functional requirements, the build order), the system design (`docs/02-design/01-system-design/`: containers, flows, failures, the doors left open at scale, providers, the questions marked "03 Architecture"), the compliance folder (`docs/02-design/02-compliance/`: the new requirements), the ADRs, and the After-MVP High ideas in `docs/00-project/ideas.md`. Ask only what's missing.
- **Existing code is a source of facts, not a model.** Read it for what it does, what data it holds, which frameworks it uses and where it hurts. A style doesn't become a rule because it's there, least of all in code written in a hurry or by AI without rules. Keep only what passes this step's criteria.
- **The targets come from earlier; this step picks the mechanism.** The functional and non-functional requirements live in the PRD, and the system design put numbers on them. Don't set new targets or rank the qualities again: for each requirement, decide how the code meets it and how that's checked automatically. Add only the qualities the user never sees (ease of change, compatibility between versions, documentation). If a need of the user shows up that the PRD doesn't have, stop, propose it, and on a yes add it to the PRD with a journal line.
- **The user decides** keep, change or rewrite for existing code (step 1), the modules (step 2), the inside of a module (step 3), the stack (step 7), the testing strategy (step 9) and every ADR (step 12). You give the options and a recommendation; they choose. One decision at a time.
- **The simplest structure that holds the boundaries.** Modules by feature, in one service; layers and interfaces only where they bring something (a rule tested without the database, a provider you may swap), not everywhere. Every extra layer is one more file for every new feature, forever.
- **Check versions on the official pages,** not from memory: the current version, when its support ends, its licence; and whether a tool is still maintained (its repository archived? its last release?), and whether it works with the versions of the rest of the stack.
- **Diagrams as SVG files** in `diagrams/`, in the C4 notation, like the system design's: each box with its name, type and technology; the container's border dashed; a title and a legend; numbered arrows explained in a table under the diagram. Open each one before committing: no text overlaps. When a later decision renames something drawn (a platform, a technology), fix the old diagrams too and check the new text still fits its box.
- **What isn't here:** the exact tables (04 Data model), the endpoints (05 API design), the screens (06 UI design), threats and security tests (07 Security), AI evals (08 AI design). Deployment, environments, CI/CD and monitoring were decided in the system design and are built in Build; this step only adds its own checks to the pipeline. The test plan for each feature is written per slice, in Planning and Build; here it's the strategy.

## Which level a decision belongs to
The same topic shows up at every level; what matters is what you decide about it. Three questions:

| Question | System design | Architecture | Implementation |
|---|---|---|---|
| Where's the line? | between parts that run separately and talk over a network | inside one part, across several modules | inside one module or file |
| What does a mistake cost? | months: data to move, money, providers | a week, and it breaks other parts | an hour |
| Who must know? | also whoever pays, runs the servers or answers legally | everyone who writes code, people and AI agents | whoever writes the function |

For example, an AI photo feature: the system design picks the provider, the region, the time limit, what the user sees when it's down, the cost; the architecture puts it in one AI module with one interface ("estimate the plate"), so the rest of the code doesn't know the provider and tests replace it with a fake; the implementation is the prompt, the class names, how the answer is read.

In C4 terms: the system design drew levels 1 and 2 (the country and the city); this step zooms into one container, the API, and draws **level 3, the components**: its modules. Level 4 (the classes) stays in the code.

At work you'll hear **high-level design** (HLD: the parts and how they talk; here the system design plus the modules) and **low-level design** (LLD: inside one part; here the rest of this step, the data model and the API design). This step sits on the border, which is why it feels mixed. `docs/02-design/README.md` holds the map.

## The styles
Use this at steps 2–3. Name only what this product needs; explain each one you name.

| Style | What it is | Worth it when |
|---|---|---|
| By type (layered, n-tier) | folders by technical role: `Controllers/`, `Services/`, `Repositories/` | small apps with simple create, read, update, delete on tables |
| By feature (vertical slices) | each feature or action in one folder with all it needs: endpoint, validation, logic, data access | almost always, as the starting point |
| Modular monolith | one deployed service whose modules have guarded boundaries: each owns its tables, they talk only through interfaces | the default for one team or a few (Shopify runs this way) |
| Hexagonal (ports and adapters) | the logic in the centre; everything outside (database, AI, email, payments) behind interfaces | providers you want to swap; logic you test without them |
| Clean / Onion architecture | hexagonal plus strict layers (domain, application, infrastructure, presentation), often as separate projects | big domains, big teams, code that lives 10+ years |
| DDD (domain-driven design) | the code speaks the domain's words; the model is split into bounded contexts (areas where a word has one meaning, like "portion" for a food and for a recipe); aggregates (objects that change only together, through one door) | complex domains with many rules (banking, logistics, insurance); "DDD-lite" (the PRD's glossary names things, the contexts become modules) fits most products |
| Domain events | a module announces "something happened" ("account deleted"); others react without knowing each other | one action triggers work in many modules |
| CQRS (command query responsibility segregation) | writes and reads on separate paths, with different models | reads and writes look very different or scale very differently |
| Event sourcing | store the sequence of events, not the state; the state is rebuilt from them | full audit, financial domains |
| Microservices | each module a separate service, with its own deploy and database | many teams that must release independently; parts with very different scale |
| Micro-frontends | the browser app split by team, each part deployed separately | many teams on one product |

## The qualities
Use this at step 4. The target comes from the PRD or the system design; the architecture picks the mechanism that's cheap now and expensive after the first code, and the automatic check.

| Quality | Target from | What the architecture decides |
|---|---|---|
| Performance | PRD, system design | budgets with numbers checked in CI (bundle size, response time), pagination everywhere, screens loaded on demand, how many database calls a page makes, measuring with real users |
| Accessibility | PRD, compliance | accessible components from the start (keyboard, screen reader), semantic HTML, where focus goes when the screen changes, an automatic check in CI |
| Internationalization | PRD | no text written in the code; numbers, dates and units formatted by language; what's translated in the interface and what in the data; time zones |
| Browsers and devices | PRD | the supported list, what an older one shows, which ones the end-to-end tests run on |
| Compatibility between versions | the architecture (users don't see it) | an old version of the app talks to the new API: how long old requests are accepted, how the contract changes without breaking old clients, how a new version reaches the device |
| Concurrency | PRD, the architecture | two people or two devices change the same thing: who wins and how the other finds out |
| Easy to change and to test | the architecture | the modules, the dependency rule, architecture tests |
| Documentation and technical debt | the architecture | where decisions live, how a shortcut is recorded so it gets fixed, how often the frameworks are upgraded |

Security has its own step (07); logs are in the shared rules (step 5).

## The testing levels
Use this at step 9. The known shapes, so the user can name them at work:

| Shape | From | What it says |
|---|---|---|
| Pyramid | Mike Cohn (2009); Ham Vocke on martinfowler.com (2018) | many small tests, few end-to-end; "push your tests as far down as you can"; Google's rough guide: 80% small, 15% integration, 5% end-to-end |
| Trophy | Kent C. Dodds (2018) | static checks at the base, most tests at integration, where pieces meet |
| Honeycomb | Spotify (2018) | for microservices: most tests at the service's boundary |
| Anti-patterns | *Software Engineering at Google* | the ice-cream cone (mostly end-to-end) and the hourglass (nothing in the middle) |

Pick the shape **per part, by where the risk is** (often the pyramid for pure rules and the trophy for endpoints and screens), and no percentages: each bug at the lowest level that can catch it.

| Level | What it checks | How many |
|---|---|---|
| Unit | one function or rule, no database, no network; milliseconds | many, on the business rules |
| Integration | the API with a real database (in a container), the providers replaced by fakes | every important endpoint and rule |
| Contract | the app and the API agree: the types generated from the API are current | one check in CI |
| Component | one UI component, used the way a person uses it (Testing Library) | the components with logic |
| End-to-end | a simulated person: browser, API, database, like production; slow and brittle, so few | the 2–3 flows from the system design |
| Accessibility | automatic checks on every screen (axe), plus a manual pass with a screen reader | every screen |
| Architecture | the boundaries: who may use whom (fitness functions) | a few rules, in CI |
| Guard tests | one parametrized test that runs over **every** endpoint or table: no endpoint without an access rule, 404 on someone else's data, one error format, every table with personal data covered by export and deletion, the query count per request | a handful that cover everything, new code included |
| Performance | response time and size under load | when a number in the PRD or the system design asks for it |
| Property-based and mutation | the first generates thousands of random inputs and checks a rule that must always hold; the second breaks the code on purpose and checks that the tests notice | on the critical rules |
| Smoke, after deploy | a few quick checks that production answers after each release | one per deploy |
| AI evals | the AI's answers on a fixed set of examples | → 08 AI design |

## Steps

### 1. Read what exists
The PRD's functional requirements (MVP features, journeys, glossary), its non-functional requirements and the build order; the system design's containers, flows, failures, the doors left open at scale, the providers and the questions left for 03; compliance's new requirements; the ADRs; the High ideas. List what's missing and ask only that.

**If code exists**, read it for facts (what it does, what data it holds, which frameworks it uses) and for what hurts, **not as a model**. The git history shows where it hurts: files that change often and always together are either one module or tied the wrong way. For each part: keep, change or rewrite, why, and what it costs. Keep only what passes this step's criteria, not what happens to exist. The user decides.

### 2. The modules (C4, level 3)
Split the API by the PRD's features and words (the log, recipes, a shared kitchen), not by technique ("Services", "Helpers"). For each module:
- what it does, in one sentence;
- **the data it owns:** its tables; nobody else writes to them, and others read them only through its interface;
- what it exposes and whom it calls; no cycles (A calls B and B calls A);
- how modules talk: a direct call through the interface (the default), or an event ("account deleted") when one action touches many modules.

A C4 level 3 diagram of the API. The test of a good boundary: a High idea from `ideas.md` fits in one module. **The user decides.**

### 3. Inside a module
- **The style:** by feature, each action with its endpoint, validation, logic and data access close together.
- **Where the business rules live:** pure functions, no database, no network, tested in milliseconds.
- **What goes behind an interface:** only what you want to swap or replace in tests: the providers, the storage, the clock.
- **The dependency rule:** the business rules depend on nothing outside; the database, the framework and the providers depend on them.

One action traced from the request to the database and back, as a numbered table like the system design's flows, with a diagram. **The user decides.**

### 4. The requirements, in the code
For every requirement that becomes code, pick the module, the mechanism and **the automatic check**:
- from the PRD, the non-functional ones: performance, accessibility, languages, browsers and devices, offline (use the qualities table);
- from the system design: sync, the AI interface per kind of request, scheduled jobs, webhooks, timeouts and retries;
- from compliance: consent records, the retention clean-up job, export and deletion, the label on what the AI made.

The target doesn't change here. A missing requirement or a new need of the user (for example weights in pounds for users in the US) is proposed, and on a yes it goes into the PRD with a journal line.

**Personal data, as a rule of every module:** every module that holds personal data can export it and delete it for one person, and a test fails when a new table with personal data isn't covered. Otherwise the export falls behind at the first new table. Define how the test recognises such a table (a column naming rule), and give the deletion test **the list of rows the law requires to keep** (proof of consent, the deleted account's id for re-deletion after a restore, shared items), or it fails by design or deletes what must stay.

Also give a row and a check to availability and backups (measured, not tested: uptime; the restore drill, timed), and to every outside provider's callbacks (webhooks such as payments and email bounces).

### 5. The rules every module follows
One rule, written once, for:
- login and permissions: not only "logged in" but "allowed to see this" (in a shared space, only its members);
- validation: where, and with what;
- errors: one format for the whole API (for example Problem Details, the standard for HTTP API errors); the unexpected ones caught in one place;
- logs: structured, with one id per request that ties its lines together;
- language and **dates:** the moment in UTC, plus the person's local day, because "today" depends on their time zone;
- ids (made on the client when it works offline, for example UUID v7, which sorts by time), configuration and secrets;
- scheduled jobs (a jobs table, one run even on two servers), idempotency, rate limiting, the consent check;
- **concurrency:** two people or two devices change the same thing: who wins, and how the other finds out;
- **compatibility between versions:** an old version of the app talks to the new API; how long old requests are accepted, and how the contract changes without breaking old clients.

### 6. The frontend
- how it's rendered (decided in the system design) and the routes;
- **the three kinds of state:** data from the server, offline data on the device, screen state; the source of truth for each;
- how it talks to the API: a client generated from the contract;
- the shared components (details → 06 UI design) and the languages;
- **the size budget:** how much JavaScript on the first load, checked in CI;
- **how a new version reaches the device:** for a PWA, the service worker update, without losing what wasn't sent;
- the folders: by feature, like the API.

### 7. Languages, frameworks and tools
For each need (the language, the API framework, database access and migrations, login, validation, jobs, the app framework, routing, state, offline storage, UI components, languages, tests) and for the tools (build, lint, formatting, CI, automatic dependency updates): the choice, why, the version and when its support ends, the licence, **when to revisit**.

Include the categories easily forgotten: **code quality platforms** (SonarQube, Codacy, Qodana) and **AI code review** (CodeRabbit, Copilot, Claude Code's `/code-review` in a new session); for each, check the free plan against the repository's visibility (several are free only for public code) and say whether it's a **gate** (stops the code) or a **signal** (reports, a person decides); a gate whose rules can't be changed (for example a fixed coverage threshold) becomes a signal. The git hooks tool. For the app, **the size of each library actually used**, added up against the size budget of step 6, with the way back if it's passed.

Choose by: the user or the team knows it (when the project is also learning for a job, what that job uses counts); mature, with long-term support; the community, the docs and how well AI agents know it; the licence; how hard it is to leave. **Boring technology** (Dan McKinley, "Choose Boring Technology"): you have only a few innovation tokens; spend them where the product is different. What runs today is one option, with its cost of change, not the starting point. Every row gets a real **revisit condition**, not "updates proposed automatically" (that's how updates arrive, not when to reconsider); a default rule for the small libraries is fine (12 months without a release, a licence change, the end of support). **The user decides.**

### 8. Conventions and code standards
Names (tables, columns, JSON fields, files, routes), the error and date formats, where tests live, commit messages, and what's forbidden (for example a module writing to another module's tables). Short, each with an example, so an AI agent can follow them; in Build they go into the code repo's `CLAUDE.md`. Small style (spaces, quotes) isn't discussed: the formatter decides it. Whatever can be checked automatically (lint, formatting, architecture tests) becomes a check in CI.

**Code standards per language,** complete, by area, not a handful of rules: for the app (types, components, hooks and effects, data, forms, styles, accessibility, languages, errors, performance, security, offline, tests) and for the server (types and null, dependency injection, transactions, data access, validation, errors, logs, time, tests). Each rule with why and what checks it (a tool, a test, or review). Check every example against the framework's real behaviour (a name mapping that adds no `_` before a digit breaks at start). The list of what's forbidden says how each item is caught, and a rule "caught by a test" must name a check that can really see it (a boundary test sees Java types, not the text of SQL).

### 9. The testing strategy
For each level in the table above: what's tested there, with which tool, how many.
- the 2–3 flows from the system design become the end-to-end tests;
- **each of the system design's top 3 qualities gets a test** (for example "data is never lost" → sync tests with duplicate requests, out of order, offline);
- **where the component tests run** (a simulated browser such as jsdom, or a real one such as Vitest Browser Mode): a decision when the app uses offline storage, focus or layout;
- **each outside provider, in a table:** its fake in the tests, in end-to-end, and when the real one is checked; "only mock types that you own" (a fake of your interface, HTTP fakes only for the adapter); check the fake tools are still maintained;
- "data is never lost" also needs **the backup restore test** (a backup actually restored, monthly) and **the rollback test** (the previous version on the migrated database); check each tool's limits (Playwright runs service workers on Chromium only);
- what runs on every PR (fast, under about 10 minutes, Fowler's ten-minute build) and what runs later; with a private repository, **count the CI minutes** against the free allowance;
- **flaky tests:** how many retries, when one is quarantined, which levels are never retried;
- coverage (the share of code the tests reach) is a signal, not a target; mutation tests on the critical rules, after checking the tool runs on this version of the test framework;
- what isn't tested, and why.

It's the strategy, not the plan: the tests for each feature are written per slice, in Planning and Build. **The user decides.** AI evals are in 08, security tests in 07.

### 10. The repo and the local start
- one repo for the API and the app (a monorepo) or several;
- **public or private**, decided once, with the real costs (branch protection, secret scanning and CI minutes differ by visibility and plan) and the user's fears answered (leaked secrets are the real risk of a public repository);
- the build's shape (one project or several sub-projects), and the meanings of "module" that collide at work;
- the folder tree; each PRD feature → its module and folder, so each slice in Planning knows where it writes; a feature that lands in three modules is noted as several features;
- one command that starts everything locally, with **invented** test data (seeded through the modules' doors, never real personal data) and the providers faked by default; one file of local services shared with the end-to-end tests;
- what runs before a commit and before a push; for AI agents, a hook that blocks a push to `main` and skipping the hooks (an instruction alone isn't enough);
- the code repo's `CLAUDE.md` under 200 lines, the rules per language in path-scoped files.

### 11. Documentation and technical debt
- where decisions and explanations live: the ADRs, the READMEs, comments only for "why";
- the module map **generated from the code** where the framework can (Spring Modulith's Documenter), compared with the drawing at each slice end;
- how a shortcut taken on purpose is recorded (what, why, cost, when it gets fixed): Fowler's debt quadrant, only prudent deliberate debt logged, in the same list as the planned work; `TODO(ID)` in the code, a bare `TODO` fails CI;
- **an upgrade calendar** gathered from step 7's revisit column, with the next dates;
- who reads the documentation: a new person, or an AI agent that must understand the code without its author; the test: a new AI session, given only the repositories, starts the app and adds a field end to end.

### 12. The big decisions become ADRs
Only one-way doors: the style, the language and framework of the API and of the app, maybe how the tests reach the database. First propose the list, with **what doesn't get an ADR and why** (two-way doors live in the topic files). When the decisions were already taken in the steps, write the ADRs and give them to the user to check together. Otherwise one at a time: you give the options and your recommendation, **the user chooses**. Note what each decision pulls along. **After each ADR, re-read the earlier files it changes,** the system design and its diagrams included.

### 13. Check it
- every MVP feature has a module; every table has one owner module; no cycles;
- every provider sits behind one interface;
- every non-functional requirement in the PRD and every requirement from the system design and compliance has a mechanism and a check;
- each of the top 3 qualities has a test; the flows are the end-to-end tests;
- every convention has an example;
- someone outside knows where they'd put a High idea.

Run the check with a **separate agent** that has only the documents (`/architecture validate <folder>`), then verify its findings before showing them: it can be wrong. Look especially for **contradictions left by a changed decision** (the journal says one thing, an older file another), **words left from an abandoned platform** (a framework's own concepts that the new one doesn't have), paths and examples that disagree, and terms missing from the glossary.

Write as you go: each step's file once the user confirms it, with a journal line in the README. At the end, set this step's row in `docs/02-design/README.md` (the map of the Design steps) to done, with the date, and link the folder.

```
docs/02-design/03-architecture/
  README.md                   the entry: status, summary, files, what we skip, open questions, ADRs, glossary, journal
  01-modules.md               02-inside-a-module.md     03-requirements-in-code.md
  04-cross-cutting.md         05-frontend.md            06-stack.md
  07-conventions.md           08-testing.md             09-repo.md
  10-maintenance.md
  diagrams/                   c4-components (the API, level 3), one action inside a module (SVG)
docs/00-project/adr/
  NNNN-[title].md …
```

The README:

````markdown
# Architecture – [Product]
| | |
|---|---|
| **Status** | draft / confirmed by [who], [date] |
| **Author** | |
| **Updated** | |
| **Next** | 04 Data model, 05 API design, 06 UI design |
## In one page
The style, the modules, how the requirements are met, the stack, how it's tested: 5–6 lines.
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

Each topic file starts with `# NN – [Topic]` and a link back to the README. **The titles of the server's and the app's files say which side they're about:** `# 01 – Backend: the modules`, `# 02 – Backend: inside a module`, `# 04 – Backend: the rules every module follows`, `# 05 – Frontend: the app`, and the README's table of files uses the same titles. Why: the server has three files and the app one, so without the word a reader thinks the backend is missing (asked on 2026-10-13). Then:

| File | Holds |
|---|---|
| `01-modules.md` | the diagram; `\| Module \| What it does \| Owns \| Exposes \| Calls \|`; how modules talk; the High-idea test |
| `02-inside-a-module.md` | the style, the layers, the dependency rule, what's behind an interface; one action traced, `\| # \| Where \| What happens \|`, with its diagram |
| `03-requirements-in-code.md` | `\| Requirement \| From \| Where it lives \| How it's checked \|`; personal data per module |
| `04-cross-cutting.md` | `\| Concern \| The rule \| Where it lives \| Example \|` |
| `05-frontend.md` | the routes; `\| State \| Lives in \| Source of truth \| Library \|`; the contract client, the size budget, new versions, the folders |
| `06-stack.md` | `\| Need \| Choice \| Why \| Version, support until \| Licence \| Revisit when \|`; the tools; keep, change or rewrite for existing code |
| `07-conventions.md` | `\| Topic \| Rule \| Example \|`; what's forbidden; which rules are checked automatically |
| `08-testing.md` | `\| Level \| What it checks \| Tool \| How many \| Runs on \|`; the top 3 qualities → their tests; the flows → end-to-end; what isn't tested |
| `09-repo.md` | the tree; `\| PRD feature \| Module \| Folder \|`; the local start; what runs before a commit |
| `10-maintenance.md` | where decisions live, the debt log, the upgrade rhythm, who reads the documentation |

And one file per decision in `docs/00-project/adr/NNNN-[title].md`, with the same sections as every ADR: status, date, context, options (for and against), decision, consequences, revisit when.

## Validate mode
`/architecture validate <folder>`: judge an existing architecture, change nothing.
1. Read the folder, its ADRs and the README's journal, the PRD, the system design, the compliance folder, `docs/00-project/ideas.md`, and the code if it exists.
2. Check the template and "Done when" item by item, citing the lines.
3. Then ask: does every MVP feature have a module, and every table one owner? Are there cycles? Does every provider sit behind one interface? Does every non-functional requirement in the PRD, and every requirement from the system design and compliance, have a mechanism and an automatic check? Do export and deletion cover every module with personal data? Does each of the top 3 qualities have a test? Does every stack choice have a reason, a version, a licence and a revisit date? Does every convention have an example? Was a style kept only because it existed? Does a High idea fit in one module? Is every term explained? Does any older file contradict a decision changed later in the journal, or keep a concept from an abandoned platform?
4. Report: findings by severity, each with the line, what's wrong and what to change; then what's done well; then what you couldn't evaluate. The user picks what to apply.

## The bad version and why not
- Clean architecture with 4 projects and 6 layers for 30 endpoints: every new feature touches 8 files, and half of them only pass the data along.
- Everything in one file, or in `Utils/` and `Helpers/`: nobody knows where anything goes, so it goes everywhere.
- Organized only by type (`Controllers/`, `Services/`, `Repositories/`): one feature is spread across four folders.
- The AI provider called directly from ten places: switching it touches the whole code.
- Modules only on the diagram: anyone reads and writes anyone's tables, so the boundaries don't exist.
- Microservices for one person, because "that's what big companies do".
- A framework picked from the latest tutorial or because it's fashionable.
- Languages and accessibility left to the end: every text and every component has to be touched again.
- Only end-to-end tests (slow and brittle), or 90% coverage on simple code and no tests on sync.
- Unwritten conventions: every person and every AI session does it differently.
- The existing code's style copied because it's there: mistakes made in a hurry become the rule.

## What breaks if you skip it
The code becomes whatever the first PRs made it: a ball of mud where every change breaks something else. Switching the AI provider touches the whole code instead of one module. Export and deletion miss the tables added later, so a GDPR request gets an incomplete answer. Languages and accessibility get added on top of finished code, the most expensive moment. Tests come "at the end", meaning never, and AI agents write in three styles in the same week.

## The principle behind it
Split the code by what may change: each module hides one decision (the AI provider, the shape of the tables, the sync rule), so it can change without touching the rest (David Parnas, 1972). What changes together stays together, and the business rules don't depend on details (the database, the framework, the providers); the details depend on them.

## How to apply it at work
- For a new feature, ask: which module does it go in? If the answer is "three", the boundaries are wrong or the feature is really three features.
- In a codebase new to you, draw the main service's level 3 in the first weeks, helped by the git history: it's the fastest way to understand it and to show you did.
- At large companies much comes decided by the platform teams (an accessible design system, a library for languages, shared lint rules): read the company's standards first, and decide only where you deviate, with a reason.
- In code review, check the boundaries and the conventions, not only that it works; move what can be checked automatically into CI.
- As a senior or CTO: **Conway's law** (a system ends up copying the structure of the teams that build it), so module boundaries and team boundaries are decided together; one shared set of frameworks and conventions for every team (a paved road, or golden path); a tech radar: the public list of technologies, in rings (adopt, trial, assess, hold).

## Done when
- [ ] existing code read for facts, each part kept, changed or rewritten with a reason, chosen by the user
- [ ] the modules, each with the data it owns, what it exposes and whom it calls; no cycles; a C4 level 3 diagram; chosen by the user
- [ ] the inside of a module: the style, the dependency rule, what's behind an interface; one action traced with a diagram; chosen by the user
- [ ] every non-functional requirement in the PRD and every requirement from the system design and compliance has a module, a mechanism and an automatic check
- [ ] export and deletion are a rule of every module with personal data, with a test that catches a new table
- [ ] one rule for each shared concern, concurrency and compatibility between versions included
- [ ] the frontend: the three kinds of state, the contract client, the size budget, how new versions arrive
- [ ] the languages, frameworks and tools, each with a reason, a version checked on the official page, a licence and when to revisit; chosen by the user
- [ ] the conventions, each with an example, the automatic ones in CI
- [ ] the testing strategy: the shape per part, every level, the guard tests, each provider's fake, the flows as end-to-end tests, a test for each of the top 3 qualities (backup restore and rollback included), what runs on each PR and later within the CI budget, flaky tests, what isn't tested; chosen by the user
- [ ] the repo, public or private decided once, each PRD feature mapped to a folder, one command to start locally with invented data, the hooks for people and AI agents
- [ ] documentation and technical debt: where decisions live, the debt log, the upgrade rhythm
- [ ] every one-way door an ADR, chosen by the user; the earlier files re-read after each one
- [ ] a glossary for every term
- [ ] the README: status, summary, what we skip and why, open questions, the ADR table
- [ ] the row in `docs/02-design/README.md` set to done
- [ ] every diagram opened in a browser, no text overlapping

## Next
Data model (`/data-model`), API design (`/api-design`) and UI design (`/ui-design`), almost in parallel: they take the modules, the shared rules and the conventions from here. Then Security (`/security`) checks it all.
