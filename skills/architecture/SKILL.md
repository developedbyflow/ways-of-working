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
- **Every number and every convention with its argument:** a known standard (named, its official page checked on the web), a target set earlier (cited), or a guess marked `[ASSUMPTION]` that says how and when it's checked (`[ASSUMPTION: measured in slice 1]`); the guesses a later moment must settle are gathered in the README's open questions, with that moment. Write "tried" only for what was actually run, with the date ("tried on 2026-10-31 with Hibernate's class"). For a convention or a tool, an argument card: why; the main alternative and who uses it; when the alternative is better; what someone may answer, and the reply; the source. When the industry is split, name the camps.
- **Where the documents are:** the `Project documents:` line in `CLAUDE.md` gives the documents folder; without it, use `docs/` in the current folder. Write into `docs/02-design/03-architecture/` and the ADRs into `docs/00-project/adr/`; create them if they don't exist.
- **Read first:** the PRD (`docs/01-discovery/04-prd.md`: features, journeys, glossary, non-functional requirements, the build order), the system design (`docs/02-design/01-system-design/`: containers, flows, failures, the doors left open at scale, providers, the questions marked "03 Architecture"), the compliance folder (`docs/02-design/02-compliance/`: the new requirements), the ADRs, and the After-MVP High ideas in `docs/00-project/ideas.md`. Ask only what's missing.
- **Existing code is a source of facts, not a model.** Read it for what it does, what data it holds, which frameworks it uses and where it hurts. A style doesn't become a rule because it's there, least of all in code written in a hurry or by AI without rules. Keep only what passes this step's criteria.
- **The targets come from earlier; this step picks the mechanism.** The functional and non-functional requirements live in the PRD, and the system design put numbers on them. Don't set new targets or rank the qualities again: for each requirement, decide how the code meets it and how that's checked automatically. Add only the qualities the user never sees (ease of change, compatibility between versions, documentation). If a need of the user shows up that the PRD doesn't have, stop, propose it, and on a yes add it to the PRD with a journal line.
- **The user decides** keep, change or rewrite for existing code (step 1), the modules (step 2), the inside of a module (step 3), the stack (step 7), the testing strategy (step 9) and every ADR (step 12). You give the options and a recommendation; they choose. One decision at a time. **Write a choice as its options, lettered A, B, C** (a table when they differ on several points, the chosen column marked "(chosen)"), and the decision with who made it and the date: "chosen by me on 2026-10-31, option A". A decision changed later keeps both dates and says what it replaced ("changed on 2026-10-31: …; first …").
- **The simplest structure that holds the boundaries.** Modules by feature, in one service; layers and interfaces only where they bring something (a rule tested without the database, a provider you may swap), not everywhere. Every extra layer is one more file for every new feature, forever.
- **Check versions on the official pages,** not from memory: the current version and its release date, when its support ends, its licence; and whether a tool is still maintained (its repository archived? its last release? "maintenance mode" in its README?), whether it works with the versions of the rest of the stack, and whether its terms fit how you work (a test library whose README asks AI agents not to use it collides with an agent that runs the tests).
- **Check every claim at its source, with the date it was read:** a version, a plan's limits, a price, a browser's behaviour, a platform's guideline, a quote. The date goes next to the claim or in the file's numbered sources ("read 2026-11-07"); a claim corrected later says so in place ("corrected 2026-11-08: it said …"). Memory isn't a source, and a secondhand summary stands in only where no official page exists: rereading the pages corrected a size called a platform's minimum that its page calls the default, a storage rule said to apply "without a visit" that applies without a tap, a runtime's next long-term version, and a tool called unmaintained that had released that week.
- **A library's defaults are read in its documentation or its source, never assumed,** and set explicitly where they differ from the design; the stack's row says both, the default and what you set. An AI provider's SDK may retry by itself, up to 5 attempts, with no time limit at all; a server-data library retries every failed read 3 times; a framework's password-hash defaults may sit under the minimum of OWASP (the non-profit whose lists are the reference for web security): each one silently breaks a number decided earlier.
- **A number about the documents is counted by a script, or taken from the step that counts it, with the link,** never by hand: the endpoints behind a login, the addresses that take an id, the names a mapping rule breaks (a simulation of the rule over `schema.sql`), the CI minutes as a table whose rows add up to its total. Run it again at the check.
- **Diagrams in standard notations, drawn from text** (decided 2026-10-20), like the system design's: the modules as a **C4 component view in the same Structurizr model**, `docs/02-design/c4/workspace.dsl`, so the containers and the outside systems keep exactly the system design's names; one action inside a module as a **UML sequence diagram**, a `.puml` next to its `.svg` in `diagrams/`. `docs/02-design/diagrams.sh` draws them all (add the view to `c4/views.txt`). One relationship per direction, each label starting with its row number in the table under the drawing; a title per view, the shared legend; `diagrams.sh` checks the arrows against `01-modules.md`'s table (add it as the view's third field in `c4/views.txt`). A relationship every module has (its own tables) is drawn from each module that has it, not from one that stands for all, and the table's row names them all. Never a hand-made SVG or a home style. Open each one before committing: no text overlaps. When a later decision renames something (a platform, a technology), change it once in the model and redraw.
- **A number or a rule decided earlier changes everywhere at once** (decided 2026-10-21, after a whole-design check found ~160 stale mentions left behind by later steps): before committing, `grep` all of `docs/` for the old value and its wording (the number, the name, the phrase) and fix every place in the same commit, this README's one-page summary and glossary and the other steps' READMEs included, or say why one stays (a journal line keeps what was true that day; a past count kept on purpose goes into `docs/02-design/checks/facts-history.txt`). `diagrams.sh` runs `checks/facts.py`, which counts the main facts from their sources (tables, addresses, threats, secrets, screens, ADRs, alerts) and stops on a document that states another number; a new fact that many files repeat gets a line in it.
- **What isn't here:** the exact tables (04 Data model), the endpoints (05 API design), the screens (06 UI design), threats and security tests (07 Security), AI evals (08 AI design). Deployment, environments, CI/CD and monitoring were decided in the system design and are built in Build; this step only adds its own checks to the pipeline. The test plan for each feature is written per slice, in Planning and Build; here it's the strategy.
- **What this step puts off or rules out goes to `docs/00-project/ideas.md`:** a "Not doing" row that's a feature for later becomes an idea there with the next ID, and the row cites it (MacroMate's "compare foods side by side", put off in 06 UI design, is F-48); an idea this step rules out moves to "Dropped" with the date and the decision that forbids it (an ADR, the DPIA); either way the file's Next free ID, Updated and History follow.

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
| Module alone | one module started without the others, on the real database: it doesn't secretly need another module, and it publishes its events | 1–3 per module |
| Integration | the API with a real database (in a container), the providers replaced by fakes | every important endpoint and rule |
| Migrations | every migration runs on an empty database when the tests start, and the mapping checks that the classes match the tables | none written by hand: every run |
| Contract | the contract generated from the code is the committed one, passes the linter, matches the design and doesn't break the one in production; the app's types generated from it are current | a few checks in CI |
| Component | one UI component, used the way a person uses it (Testing Library) | the components with logic |
| End-to-end | a simulated person: browser, API, database, like production; slow and brittle, so few | the 2–3 flows from the system design |
| Accessibility | automatic checks on every screen (axe), plus a manual pass with a screen reader | every screen |
| Architecture | the boundaries: who may use whom (fitness functions) | a few rules, in CI |
| Guard tests | one parametrized test that runs over **every** endpoint or table: no endpoint without an access rule, 404 on someone else's data, on every address that answers with a list two people's rows in the database and only the caller's in the answer, one error format, every table with personal data covered by export and deletion, nothing personal in the logs, the query count per request | a handful that cover everything, new code included |
| Performance | response time and size under load | when a number in the PRD or the system design asks for it |
| Property-based and mutation | the first generates thousands of random inputs and checks a rule that must always hold; the second breaks the code on purpose and checks that the tests notice | on the critical rules |
| Smoke, after deploy | a few quick checks that production answers after each release | one per deploy |
| AI evals | the AI's answers on a fixed set of examples | → 08 AI design |

## Steps

### 1. Read what exists
The PRD's functional requirements (MVP features, journeys, glossary), its non-functional requirements and the build order; the system design's containers, flows, failures, the doors left open at scale, the providers and the questions left for 03; compliance's new requirements; the ADRs; the High ideas. List what's missing and ask only that.

**Then decide the server's language and framework, as an ADR, before step 2.** Steps 2–6 are written in its terms (packages, transactions, annotations), so it can't wait for step 7, which only adds the versions and the other tools. It's a one-way door: argue it as step 7 says (what the user or the team knows, maturity, how hard it is to leave). In MacroMate it was decided "ahead of step 7" on the same day, and the files written before step 7 had to point forward to it. **A file may point to a later file only for the detail;** the rule itself is written where it's decided.

**If code exists**, read it for facts (what it does, what data it holds, which frameworks it uses) and for what hurts, **not as a model**. The git history shows where it hurts: files that change often and always together are either one module or tied the wrong way. For each part: keep, change or rewrite, why, and what it costs. Keep only what passes this step's criteria, not what happens to exist. The user decides.

### 2. The modules (C4, level 3)
Split the API by the PRD's features and words (the log, recipes, a shared kitchen), not by technique ("Services", "Helpers"). For each module:
- what it does, in one sentence;
- **the data it owns:** its tables; nobody else writes to them, and others read them only through its interface;
- what it exposes and whom it calls; no cycles (A calls B and B calls A);
- how modules talk: a direct call through the interface (the default), or an event ("account deleted") when one action touches many modules.

A C4 level 3 diagram of the API: a `component` view of the model, each module a component tagged `Module`, the libraries without business data tagged `Library`. The arrow from the app goes to the part that receives every request first (a filter or a gateway inside the API), not to the container's border, which C4 can't draw. **Readable, or split:** past about 12 arrows, one drawing crosses too much to read (MacroMate's 35 rows were unreadable, and so were 26 with their texts); draw instead a map with only the arrows' numbers (their texts in the table under it) and one view per module, the module with who calls it, whom it calls and its outside systems, the arrows between its neighbours left out; a row every module shares (each one, its own tables) is a sentence, not an arrow per module. The test of a good boundary: a High idea from `ideas.md` fits in one module. **The user decides.**

### 3. Inside a module
- **The style:** by feature, each action with its endpoint, validation, logic and data access close together; or by type inside each module (`controller/`, `service/`, `repository/`) when that's how the user's framework and job usually work, since the module boundaries keep each module small. For each style considered, count the files a new feature touches (by type ~4; clean architecture ~8).
- **Where the business rules live:** pure functions, no database, no network, tested in milliseconds.
- **What goes behind an interface:** only what you want to swap or replace in tests: the providers, the storage, the clock.
- **The dependency rule:** the business rules depend on nothing outside; the database, the framework and the providers depend on them.
- **Who may see what:** say what guards the boundary between modules. In Java, a class without `public` is visible only in its own package, and each sub-folder is a package of its own, so with folders by type (`controller/`, `service/`) the classes the layers share must be `public` and the language can't keep other modules out; a tool must (Spring Modulith's `ApplicationModules.verify()` treats only the module's top package as its API, or ArchUnit). Only with all of a module's classes in one package can package-private guard it. MacroMate first wrote both "folders by type" and "package-private except the door", which can't both hold.

One action traced from the request to the database and back, as a numbered table like the system design's flows, with a UML sequence diagram: the shared rules, the controller, the service, the rules, the repository as lifelines, a call to another module through its door, each check that can refuse as a `break` with its status code. **The user decides.**

### 4. The requirements, in the code
For every requirement that becomes code, pick the module, the mechanism and **the automatic check**:
- from the PRD, the non-functional ones: performance, accessibility, languages, browsers and devices, offline (use the qualities table);
- from the system design: sync, the AI interface per kind of request, scheduled jobs, webhooks, timeouts and retries;
- from compliance: consent records, the retention clean-up job, export and deletion, the label on what the AI made.

The target doesn't change here. A missing requirement or a new need of the user (for example weights in pounds for users in the US) is proposed, and on a yes it goes into the PRD with a journal line.

One section per kind of requirement (speed, accessibility, languages, offline, devices, the outside services, jobs and payments, availability and backups, personal data), one table each. **Every number says why it's that number:** a standard with its source (a response time people feel as instant), the earlier step's choice with its argument, or `[ASSUMPTION]`; the user will ask where the numbers come from. **Where nothing automatic can check it, say so, and what checks it instead:** "measured, not tested" (uptime, the real monthly cost, in a report), a pass by hand from a written checklist (a screen reader, a real phone), or "none possible", with why. Under a table, note what automation misses (a test tool that runs a feature on one browser engine only) and what covers it. List every job the requirements need in one table: what it does, how often, why, which module. Security's requirements only point to 07 Security, which gives each threat its check.

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
- how it talks to the API: types generated from the contract and **one client for every request**, which sends the shared headers and handles the shared answers; a table of each answer (not logged in, not allowed, changed meanwhile, too many tries, unavailable…) and what the app does, with a test per row;
- **a time limit on every request,** set once in the client: a weak signal often shows bars and carries nothing, and the browser still says it's online, so without a limit the screens hang instead of going offline;
- **what the data libraries retry by themselves,** read in their documentation and set to what the design wants (a read retried 3 times by default is 3 requests the person didn't ask for);
- the shared components (details → 06 UI design) and the languages;
- **the size budget:** how much JavaScript on the first load, checked in CI;
- **how a new version reaches the device:** for a PWA, the service worker update, without losing what wasn't sent;
- the folders: by feature, like the API.

### 7. Languages, frameworks and tools
For each need (the language, the API framework, database access and migrations, login, validation, jobs, the app framework, routing, state, offline storage, UI components, languages, tests) and for the tools (build, lint, formatting, CI, automatic dependency updates): the choice, why, **the version with its release date** and when its support ends, the licence, **when to revisit**. The top of the file says the day the versions were read on the official pages (and the day they were read again, when a later check redoes it); from then on the update bot (Renovate or Dependabot) moves them. When the framework fixes the versions of the libraries it manages (Spring Boot's BOM, its "bill of materials": a list of versions tested together), those rows say "managed by" and move with it; the others carry their own version and their own revisit. Where a library's default differs from the design, the row says the default and what you set (above).

Include the categories easily forgotten: **code quality platforms** (SonarQube, Codacy, Qodana) and **AI code review** (CodeRabbit, Copilot, Claude Code's `/code-review` in a new session); for each, check the free plan against the repository's visibility (several are free only for public code) and say whether it's a **gate** (stops the code) or a **signal** (reports, a person decides); a gate whose rules can't be changed (for example a fixed coverage threshold) becomes a signal. The git hooks tool. For the app, **the size of each library actually used**, added up against the size budget of step 6, with the way back if it's passed.

Choose by: the user or the team knows it (when the project is also learning for a job, what that job uses counts); mature, with long-term support; the community, the docs and how well AI agents know it; the licence; how hard it is to leave. **Boring technology** (Dan McKinley, "Choose Boring Technology"): you have only a few innovation tokens; spend them where the product is different. What runs today is one option, with its cost of change, not the starting point. Every row gets a real **revisit condition**, not "updates proposed automatically" (that's how updates arrive, not when to reconsider); **one default rule, written once at the top,** covers the small libraries and the test tools: 12 months without a release, a licence change, or the end of its major's support, and the choice is weighed again, not just updated. The rows already past it are named, each with the moment it's weighed (a slice); a stable 1.0 with no release isn't a stopped project. **A new major, and every new minor of a version below 1.0** (whose minors may break as majors do), **is read by hand before it's taken,** never an automatic update: the row says which version the design stays on and when the new one is weighed. **The user decides.**

### 8. Conventions and code standards
Names (tables, columns, JSON fields, files, routes, translation keys, environment variables), the error and date formats, where tests live, commit messages and branches, and what's forbidden (for example a module writing to another module's tables). Grouped by where they apply (the database, the server's language, the API and JSON, the app, commits and branches); short, each with an example, so an AI agent can follow them, and each with its argument card under its table. **Where the industry is split, a table of the camps** (for JSON fields: Microsoft camelCase, Zalando snake_case) with this product's choice as the last column. In Build the rules and examples go into the code repo's `CLAUDE.md` and its path-scoped rule files, with a link back for the arguments. Small style (spaces, quotes) isn't discussed: the formatter decides it. Whatever can be checked automatically (lint, formatting, architecture tests) becomes a check in CI, and the file lists everything that runs on every PR.

**Code standards per language,** complete, by area, not a handful of rules: for the app (types, components, hooks and effects, data, forms, styles, accessibility, languages, errors, performance, security, offline, tests) and for the server (types and null, dependency injection, transactions, data access, validation, errors, logs, time, tests). Each rule with why and what checks it (a tool, a test, or review). **Check every example against the framework's real behaviour,** by running it: a name mapping that puts `_` only before a capital followed by a lower-case letter turns `proteinG` into `proteing`, so a field whose name holds a digit or a one-letter word needs its column written out; count with a script how many names on the schema it breaks. Names a generated contract repeats (a request or an answer record) are the contract's own, or the comparison with the design breaks. **The list of what's forbidden says how each item is caught:** automatic, half automatic (a check flags it, a person confirms), or review, and why a rule stays review (no check catches it without false alarms, and a rule that rings for nothing gets ignored); a rule "caught by a test" must name a check that can really see it (a boundary test sees Java types, not the text of SQL).

### 9. The testing strategy
For each level in the table above, the server's and the app's in two tables: what it catches in this product, with which tool, how many (a rule, "on every endpoint, X", not a total).
- the 2–3 flows from the system design become the end-to-end tests; when 06 UI design adds its flows, each becomes an end-to-end test written in its slice before the screen's code, and its CI minutes are counted here (more than the free allowance is an open question, never a silent overrun);
- **each of the system design's top 3 qualities gets a test** (for example "data is never lost" → sync tests with duplicate requests, out of order, offline);
- **where the component tests run** (a simulated browser such as jsdom, or a real one such as Vitest Browser Mode): a decision when the app uses offline storage, focus or layout;
- **each outside provider, in a table:** its fake in the tests, in end-to-end, and when the real one is checked; "only mock types that you own" (a fake of your interface, HTTP fakes only for the adapter); check the fake tools are still maintained;
- "data is never lost" also needs **the backup restore test** (every copy restored into a throwaway database and its rows counted before it leaves, daily, on the server; plus **the restore drill** by hand, timed, before the beta and every 6 months), tests that a restore doesn't bring deleted people back or lose what clients had confirmed, and **the rollback test** (the previous version on the migrated database; a release that changes the device's database can't go back, so it's fixed forward and CI refuses a lower version); check each tool's limits (Playwright runs service workers on Chromium only);
- **what runs when,** a table by moment: before a commit, before a push, the PR's fast first stage and its parallel second stage, before the merge (an AI review in a new session), after the merge (the gate, the rollback test, the deploy, smoke tests), on a schedule (the whole browser matrix, every engine at every screen width; mutation tests), each slice by hand, once before launch; what runs on every PR stays under about 10 minutes (Fowler's ten-minute build); with a private repository, **count the CI minutes** against the free allowance (step 10);
- **flaky tests:** how many retries, when one is quarantined, which levels are never retried;
- coverage (the share of code the tests reach) is a signal, not a target; mutation tests on the critical rules, after checking the tool runs on this version of the test framework;
- what's tested but designed in another step (AI evals, security), and what isn't tested, and why, and when it comes back.

It's the strategy, not the plan: the tests for each feature are written per slice, in Planning and Build. **The user decides.** AI evals are in 08, security tests in 07.

### 10. The repo and the local start
- one repo for the API and the app (a monorepo) or several;
- **public or private**, decided once, with the real costs (branch protection, secret scanning and CI minutes differ by visibility and plan) and the user's fears answered (leaked secrets are the real risk of a public repository);
- **on a private free plan, what replaces what it lacks:** the pipeline as the gate for `main` (the deploy starts at once only for code a PR already tested, otherwise the tests run again first), a local hook and a rule for AI agents against a direct push to `main`, a secret scanner (gitleaks) in place of the platform's; and **the CI minutes counted** in a table (what runs, times a month, minutes per run, total), in job-minutes, not waiting time (4 jobs in parallel for 6 minutes use 24), each "times a month" worked out honestly (twice a week is ~9 runs, "2–3 times" is ~11, not 10), every row `[ASSUMPTION: measured in slice 1]`; the ways to stay under (a new push cancels the run still going, the slow matrix less often, a card with a spending limit for an urgent fix);
- the build's shape (one project or several sub-projects), and the meanings of "module" that collide at work;
- the folder tree; each PRD feature → its module and folder, so each slice in Planning knows where it writes; a feature that lands in three modules is noted as several features;
- one command that starts everything locally, with **invented** test data (seeded through the modules' doors, never real personal data, one invented person per state a screen shows) and the providers faked by default; one file of local services shared with the end-to-end tests; a real provider only with a separate test key with a spending cap, exported in the terminal for one session, never in a file an AI agent could read;
- **what runs before a commit and before a push,** a table: the formatters, lint and the secret scanner on the changed files before a commit; the small tests before a push, so a failing test spends no CI minutes; for a product with AI, a changed prompt's evals before its push, and since a push can't carry files written while it runs, the hook writes the results and stops the push until they're committed;
- **for AI agents, rules and a sandbox,** since an instruction alone isn't enough: a hook that runs before each of the agent's commands (Claude Code's `PreToolUse`) blocks a push to `main` and skipping the hooks (`--no-verify`, on a commit or a push); its permissions deny reaching production (`ssh`, `scp`, `sftp`, `rsync`, reading `~/.ssh`) and editing the CI workflows (on a free private plan any branch's workflow can read the deploy's secrets); and the agent's **sandbox** is on (the operating system itself refuses each command the agent runs that reads or writes outside what's allowed), because permissions are a guard, not a wall; the agent updated from its stable channel; no production secret on the laptop beyond the owner's SSH key;
- the code repo's `CLAUDE.md` under 200 lines, the rules per language in path-scoped files; the documents folder added to the agent's allowed folders, so it reads the PRD and the ADRs too.

### 11. Documentation and technical debt
- where decisions and explanations live, one place per kind, in a table (what, where, why there): the why in the documents; the one-way doors as ADRs with their "Revisit when"; how to work in `CLAUDE.md`, its path rules and the README's local start; what a module does in one paragraph next to its code (Java's `package-info.java`); the API's contract generated from the code and committed, never served in production; comments only for "why";
- the module map **generated from the code** where the framework can (Spring Modulith's Documenter), compared with the drawings at each slice's end, and **the generated one wins:** the drawings are corrected, with a journal line;
- how a shortcut taken on purpose is recorded (what, why, cost, when it gets fixed): Fowler's debt quadrant, only prudent deliberate debt logged, in the same list as the planned work; `TODO(ID)` in the code, a bare `TODO` fails CI; the entries whose time has come paid at the end of each slice;
- **the upgrade rhythm,** one table (what, how often it changes, the rule, the next date) gathered from step 7's "Revisit when", the ADRs' and, with AI, the models' reviews:
  - the patches and minors in one automatic PR a week, merged by itself when the tests pass, **after the waits** set with 07 Security (the update bot proposes a version only days after its release, the package manager installs nothing younger than a day), so the waits, the tests and the vulnerability scanner stand in for a review; held for a person's merge once half the month's availability budget is spent; never merged by itself: a version below 1.0, a library whose tables you copy into your migrations (its release notes read for a table change), the framework's own minor (a planned move);
  - security fixes in their own PR at once, with a deadline by severity (48 hours for one already exploited, on CISA's KEV list; 7 days critical; 30 days high);
  - the framework's minors within ~6 months, before their free fixes end; the language, the runtime and the database by their support dates, a database's major tried first on a copy; a major by hand, one per PR, after its migration guide;
  - with AI, the pinned models reviewed on fixed months, every job's evals run on the candidate before it's taken (08 AI design);
  - one hour every 3 months that reads every "Revisit when" and applies step 7's default rule, since endoflife.date (the site that lists support dates) tracks only the big projects;
- who reads the documentation: a new person, or an AI agent that must understand the code without its author; the test: a new AI session, given only the repositories, starts the app, says where a feature goes and adds a field end to end; what it has to ask is what `CLAUDE.md` is missing.

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

Write as you go: each step's file once the user confirms it, with a journal line in the README. **The journal speaks in one voice, the owner's,** in the first person, the same in every line ("confirmed by me", "with my yes (option A)", "chosen by me"), never a mix with "with [name]'s yes"; each line has its date, where it came from (a step and its chunk, the outside check, or a later step: "from 05 API design's lists"), and what it changed in which files. A later step that changes this folder writes its line here too, and a line keeps what was true that day: a later change is a line of its own. At the end, set this step's row in `docs/02-design/README.md` (the map of the Design steps) to done, with the date, and link the folder.

```
docs/02-design/03-architecture/
  README.md                   the entry: status, summary, files, what we skip, open questions, ADRs, glossary, journal
  01-modules.md               02-inside-a-module.md     03-requirements-in-code.md
  04-cross-cutting.md         05-frontend.md            06-stack.md
  07-conventions.md           08-testing.md             09-repo.md
  10-maintenance.md
  diagrams/                   c4-modules (the map) and modules/<module> (SVG, from the C4 model); one action inside a module (.puml + SVG)
docs/02-design/c4/workspace.dsl   the C4 model, shared with /system-design: the components view is added here
docs/00-project/adr/
  NNNN-[title].md …
```

The README:

````markdown
# Architecture – [Product]
| | |
|---|---|
| **Status** | draft / confirmed by me, [date]: [the steps], checked by an outside reader; brought in line after [a later check, a walkthrough], [dates], with my yes |
| **Author** | |
| **Updated** | |
| **Next** | the next step (04 Data model, 05 API design, 06 UI design; Planning once Design is done); what Build owes and when (the trials in Open questions; at each slice's end, the module map generated from the code against the drawings) |
## In one page
One bullet per file, and one for the existing code: the decision first, in bold, then the numbers that matter and the file's link.
## The files
| File | What it answers |
## Not doing, and why
| Not doing | Why | It comes back when |
## Open questions
| Question | Answered by | When |
## Decisions (ADRs)
| ADR | Decision |
Started in this step, written later: [ADR] ([what]). Used here, decided elsewhere: [ADR] ([what]).
## Glossary
- **Term:** what it is, compared with something the reader already knows
## Journal
- [date]: [where it came from], [whose decision, in the owner's voice: "confirmed by me", "with my yes (option A)"]: [what it changed, in which files]
````

- **The status, the Next and the journal in the owner's voice** ("me"), like the rest of the README.
- **An open question has a moment,** never "later": a slice, or an event (the database created, a job built, before the first flow test). The `[ASSUMPTION]`s a later moment settles are among them; one row may group several ("the timings marked `[ASSUMPTION]`: measured in slice 1"). An answered one stays, crossed out, with the step and the date that answered it.
- **The ADRs:** the table holds those written here; the line under it, those started here and written in a later step, and those this step uses but decided before it or after it.
- **The glossary** holds every term the files use, corrected when a file changes one; a term kept only to contrast is marked "(for contrast: not used in the files)".

Each topic file starts with `# NN – [Topic]` and a link back to the README. **The titles of the server's and the app's files say which side they're about:** `# 01 – Backend: the modules`, `# 02 – Backend: inside a module`, `# 04 – Backend: the rules every module follows`, `# 05 – Frontend: the app`, and the README's table of files uses the same titles. Why: the server has three files and the app one, so without the word a reader thinks the backend is missing (asked on 2026-10-13). Then:

| File | Holds |
|---|---|
| `01-modules.md` | the map (a view of the C4 model) with `\| # \| From → to \| What \|` under it; `\| Module \| What it does \| Owns \| Exposes to the others \| Calls \|`; one drawing per module; how modules talk, the events as `\| Event \| Announced by \| Listened to by \| What they do \|`; what sits outside the API; the High-idea test, `\| Idea \| Module \|` |
| `02-inside-a-module.md` | one module's folder tree; `\| Folder \| Holds \| Depends on \|`; who may see what; the styles considered, with the files a new feature touches in each; the dependency rule, what's behind an interface; one action traced, `\| # \| Where \| What happens \|`, with its sequence diagram |
| `03-requirements-in-code.md` | one section per kind of requirement, each `\| Requirement \| Why this number \| Where \| Mechanism \| Automatic check \|`; the jobs, `\| Job \| How often \| Why \| Module \|`; availability and backups "measured, not tested"; personal data per module; what automation misses; security as a pointer to 07 |
| `04-cross-cutting.md` | per concern, `\| Concern \| The rule \| Where it lives \| Example \|`; concurrency per kind of data, `\| What \| The rule \| Why \| Example \|` |
| `05-frontend.md` | rendering; the routes, `\| Area \| Routes \| Offline \|`; `\| State \| Examples \| Lives in \| Source of truth \| Library \|`; the one client and `\| Answer \| What the app does \|`; the time limit on every request; the size budget; new versions; the folders; the rules both sides run |
| `06-stack.md` | what was decided ahead of step 7; the default revisit rule and the day the versions were read; per area `\| Need \| Choice \| Why \| Version, support until \| Licence \| Revisit when \|` (the version with its release date), the app's rows with a `Size` column summed against the budget, the test tools as `\| Need \| Choice \| What it does \| Version \| Licence \|` under the default rule; keep, change or rewrite, `\| Part \| Decision \| Why \|` |
| `07-conventions.md` | per topic `\| Rule \| Example \|`, each rule's argument card under its table, the camps where the industry is split; `\| Forbidden \| Why (where) \| How it's caught \|`; what runs on every PR; where tests live; the coding standards per language and area, `\| Rule \| Why \| Checked by \|` |
| `08-testing.md` | the shapes and `\| Part \| Shape \| Why \|`; the server's and the app's levels, each `\| Level \| What it catches here \| Tool \| How many \|`; `\| Service \| In the server's tests \| In end-to-end (CI) \| The real one, when \|`; the top 3 qualities as tests (`\| What could lose data \| The test \| Level \|` for the first); `\| Flow \| The test \| Where \|`; `\| When \| What runs \| Time \|`, flaky tests, the CI minutes; coverage and mutations; `\| What \| How \| Where \|` for what another step designs; `\| Not tested \| Why \| It comes back when \|` |
| `09-repo.md` | one repository or several; public or private as options, with `\| What runs \| Times a month \| Minutes per run \| Total \|` for a private plan; the tree; the build's shape; `\| PRD feature \| Module (server) \| App \|`; the local start, `\| What \| How \| Why \|`; `\| When \| What runs \| Time \|` before a commit, before a push and for AI agents; the hooks tool; the file for AI agents, the agent's permissions and sandbox |
| `10-maintenance.md` | `\| What \| Where \| Why there \|`; the debt quadrant and where the log lives; `\| What \| How often it changes \| The rule \| Next \|`; who reads it and the new-session test |

A topic file that cites anything ends with `## Sources`, numbered and cited in the text as `[n]`, each with the date it was read when it can change (a plan, a price, a version).

And one file per decision in `docs/00-project/adr/NNNN-[title].md`, in the ADR template of `/system-design` (status, date, updated, context, options, decision, consequences, revisit when), with its row in the index `docs/00-project/adr/README.md` in the same commit.

## Validate mode
`/architecture validate <folder>`: judge an existing architecture, change nothing.
1. Read the folder, its ADRs and the README's journal, the PRD, the system design, the compliance folder, `docs/00-project/ideas.md`, and the code if it exists.
2. Check the template and "Done when" item by item, citing the lines.
3. Then ask: does every MVP feature have a module, and every table one owner? Are there cycles? Does every provider sit behind one interface? Does every non-functional requirement in the PRD, and every requirement from the system design and compliance, have a mechanism and an automatic check? Do export and deletion cover every module with personal data? Does each of the top 3 qualities have a test? Does every stack choice have a reason, a version with its date, a licence and a revisit condition, and is every library default the design depends on read and set? Does every number say why it's that number, every claim cite its source with the date it was read, every count come from a script or the step that counts it, every guess say how and when it's checked, with those a later moment settles among the open questions? Does every convention have an example and its argument, and does every forbidden item name a check that can really see it? Was a style kept only because it existed? Does a High idea fit in one module? Is every term explained? Is the journal in one voice, the owner's? Does any older file contradict a decision changed later in the journal, or keep a concept from an abandoned platform? Does the components view come from the same C4 model as the system design's drawings, with the same names?
4. Report: findings by severity, each with the line, what's wrong and what to change; then what's done well; then what you couldn't evaluate. The user picks what to apply.

## The bad version and why not
- Clean architecture with 4 projects and 6 layers for 30 endpoints: every new feature touches 8 files, and half of them only pass the data along.
- Everything in one file, or in `Utils/` and `Helpers/`: nobody knows where anything goes, so it goes everywhere.
- Organized only by type (`Controllers/`, `Services/`, `Repositories/`): one feature is spread across four folders.
- The modules drawn by hand in a separate file: the providers get other names than in the system design, and nobody else's tools can read the drawing.
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
- [ ] every non-functional requirement in the PRD and every requirement from the system design and compliance has a module, a mechanism and an automatic check (or says what checks it instead, and why), and every number says why it's that number
- [ ] export and deletion are a rule of every module with personal data, with a test that catches a new table
- [ ] one rule for each shared concern, concurrency and compatibility between versions included
- [ ] the frontend: the three kinds of state, the contract client with its answer to each shared error, a time limit on every request, the size budget, how new versions arrive
- [ ] the languages, frameworks and tools, each with a reason, a version with its release date checked on the official page, a licence and when to revisit; the default revisit rule written once; the defaults that matter read and set; chosen by the user
- [ ] the conventions, each with an example and its argument, the camps where the industry is split; what's forbidden with how each is caught; the automatic ones in CI
- [ ] the testing strategy: the shape per part, every level, the guard tests, each provider's fake, the flows as end-to-end tests, a test for each of the top 3 qualities (backup restore and rollback included), what runs on each PR and later within the CI budget, flaky tests, what isn't tested; chosen by the user
- [ ] the repo, public or private decided once, the CI minutes counted for a private plan, each PRD feature mapped to a folder, one command to start locally with invented data, the hooks for people and AI agents, the agent's permissions and sandbox
- [ ] documentation and technical debt: where decisions live, the generated module map that wins, the debt log, the upgrade rhythm with its waits and the updates never merged by themselves
- [ ] every one-way door an ADR, chosen by the user; the earlier files re-read after each one
- [ ] a glossary for every term
- [ ] the README: status and Next in the owner's voice, one bullet per file, what we skip and why, open questions each with its moment, the ADRs written, started and used here, the journal in one voice
- [ ] the row in `docs/02-design/README.md` set to done
- [ ] every diagram in a standard notation, drawn by `diagrams.sh` (the components from the C4 model, the action as a sequence diagram), opened, no text overlapping

## Next
Data model (`/data-model`), API design (`/api-design`) and UI design (`/ui-design`), almost in parallel: they take the modules, the shared rules and the conventions from here. Then Security (`/security`) checks it all, AI design (`/ai-design`) follows for a product with AI, then Planning. Each of them that changes this folder writes the change here too, with its journal line.
