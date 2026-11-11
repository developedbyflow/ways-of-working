---
name: system-design
description: "How the system runs. Requirements with numbers and the top 3 qualities, a back-of-the-envelope calculation, the context and container diagrams (C4), how much works offline, 2–3 flows traced end to end, where the data lives, what happens when each part fails, what breaks first at 10×, monitoring, deployment and CI/CD as decisions, the providers, the monthly cost, and the big choices as ADRs. Writes a folder: a README (status, summary, what we skip, open questions) and one file per topic, with diagrams. Use after the PRD, as the first Design step, or at work before a new service or data flow. Also judges an existing design: /system-design validate <folder>."
argument-hint: "[the product or the change] or validate <folder>"
---

# System design

## When to use it
The first Design step, after the PRD (and the prototype, if there was one). At work: a new system, or a big change to how the parts fit together (a new service, a new data flow, a new need for scale or availability).

## The problem it solves
The PRD says what the product does. System design says how it runs: which parts it's made of, how data moves between them, what happens when one fails, what it costs, how code reaches production and how you find out something is wrong. The big decisions are made here, with numbers, before the first PR makes them by accident.

## How to run it
- **The bar:** do what a senior engineer or the CTO at a well-run company would accept, in the simplest form that meets it. Use the real industry method and name it, so the user learns it. Senior also means knowing what to leave out: say what you skip and why.
- **Teach while you go:** the user may be doing this for the first time. Every term gets one line on what it is and what it brings, compared with something they already know (a frontend developer knows `fetch` and JSON; system design is everything on the other side of that `fetch`). Show the full picture of the topic, then mark what this product needs.
- **Where the documents are:** the `Project documents:` line in `CLAUDE.md` gives the documents folder; without it, use `docs/` in the current folder. Every `docs/…` path below means that folder. Write into `docs/02-design/01-system-design/` (one folder per Design step, numbered in the order of the road) and the ADRs into `docs/00-project/adr/` (decisions come from every phase); create them if they don't exist.
- **Spot risky assumptions for the user:** when a decision rests on something nobody has checked ("the AI answers in 5 s", "the free tier is enough") and being wrong would cost a lot, stop and propose a risk test: what to check, how long it takes, the pass mark, and when. The user only says yes or no; run it with `/risk-tests`. A test that hasn't run by its date stays in the README's status and open questions ("planned for [date], not run yet on [date]"), and every number waiting for it says so.
- **Every number with its source, so the user can defend it:** a price, a plan's limit, a provider's region, how long it keeps data or how long its own repairs take is read on the provider's own page, linked, with the day it was read ("checked 2026-10-21"); its words quoted when they're vague (a lost database node replaced in "multiple hours"); a figure from memory or a comparison site is marked so until it's read at the source. A factor nobody has measured is `(guess)`, with what it comes from; a fact about a provider or the system not tried yet is `[ASSUMPTION: what, when it's tried, what happens if it's wrong]`; a target the design sets itself says so ("my design target, not a PRD line"). A count (alerts, jobs, heartbeats, ADRs) comes from its source table or a script, never from memory.
- **Read first:** the running system if there is one (step 1), `docs/01-discovery/04-prd.md` (journeys, glossary, non-functional requirements, open decisions), the money check in `03-product-brief.md`, the risk tests (`docs/01-discovery/risk-tests/`), and `docs/00-project/ideas.md` (the After-MVP High ideas). Ask only what is missing.
- **The user decides** at three points: the numbers (step 2), the shape of the system (step 5) and every ADR (step 14), and every smaller choice met on the way. You give the options and a recommendation; they choose. One decision at a time. A choice is offered as A and B, each with what it costs, and the file records it where it applies, with the option not taken: "(decided [date], option A; B, [what it was], would [what it would cost])".
- **In the user's voice:** the documents are theirs, so the status, the journal and the files say "confirmed by me", "with my yes", "decided by me (option A)", in one voice from the first line to the last, never "[name]'s yes" in some lines and "my yes" in others.
- **No new requirements here.** If the design needs a requirement the PRD doesn't have (for example how much works offline), stop, propose it, and on a yes add it to the PRD with a journal line.
- **Start with the fewest parts.** Every extra box is one more thing that fails, needs watching and costs money. A part is added only when a number asks for it.
- **Diagrams in standard notations, drawn from text** (decided 2026-10-20), so they read the same at any company and can't drift apart: **C4** levels 1–2 and where the data lives (a C4 deployment view) from **one Structurizr model**, `docs/02-design/c4/workspace.dsl` (Structurizr DSL: the elements and relationships written once, each drawing a view of them); the flows as **UML sequence diagrams**; the road to production as a **UML activity diagram**, each a `.puml` next to its `.svg` in `diagrams/`. `docs/02-design/diagrams.sh` (set up by `/docs-setup`) draws them all with the Structurizr CLI and PlantUML, both free. In C4: drawn in Structurizr's own look (the type under every name: [Person], [Software System], [Container: tech], as C4's notation asks); each element's description says what it does for this system, on one line (C4 asks for its responsibilities: "Checkout, VAT, receipts.", not "Ciqual, USDA."), commas between things of one kind, a semicolon before one extra fact ("Nutrition tracker; logging works offline."); one relationship per direction (a webhook back is a second arrow); each label short, saying what flows and starting with its row number in the table under the drawing (arc42's diagram + table), the details in the table; the technology as the relationship's technology; the outside systems in one `group`; a title per view; the shared legend. **`diagrams.sh` checks every numbered arrow against its table** (`c4/check-tables.py`: the same numbers, the same two ends) and fails on a difference; add each view's Markdown file as the third field of `c4/views.txt`. Never a hand-made SVG or a home style; not Mermaid in chat (the arrows get lost). Open each one before committing: no text overlaps.
- **A number or a rule decided earlier changes everywhere at once** (decided 2026-10-21, after a whole-design check found ~160 stale mentions left behind by later steps): before committing, `grep` all of `docs/` for the old value and its wording (the number, the name, the phrase) and fix every place in the same commit, or say why one stays (a journal line keeps what was true that day; a past count kept on purpose goes into `docs/02-design/checks/facts-history.txt`). `diagrams.sh` runs `checks/facts.py`, which counts the main facts from their sources (tables, addresses, threats, secrets, screens, ADRs, alerts) and stops on a document that states another number; a new fact that many files repeat gets a line in it. This step's are the alerts to the phone, counted from the rows of `09-monitoring.md`'s `| Alert | When | What I do |` table (so keep that header), and the number of ADRs.
- **A change after confirmation is dated where it's made:** "(added 2026-11-09)", "(changed in 05 API design, 2026-11-07; first …)", "(corrected 2026-11-10: it said …)", so a reader sees what moved, when, and what it was before. The README's "In one page" says only what's true now; the history is in the journal.
- **Security has its own step** (07 Security, `/security`): it needs the API and the data model, which come later. Here, only the mechanisms the other steps need (for example a webhook's signature, a daily AI cap); the README points to 07.

## The building blocks
Use this list at steps 4–5 and 9. Name only the parts this system needs; explain each one you name.

**Almost every system:**
- **Client:** what people see (web app, PWA, mobile app).
- **API (the server):** receives requests, checks who you are, applies the rules, answers.
- **Database:** where data lives for good.
- **File storage:** a separate place for large files; the database keeps only their address.
- **External services:** bought, not built, paid per use (AI, payments, email, SMS).
- **Worker and queue:** work put aside and done in the background so nobody waits. Optional.
- **Monitoring:** how you learn something is broken before a customer tells you.

**Usually present, in the background:** domain and DNS, CDN, service worker (offline, for PWAs), scheduled jobs (cron), login (build or buy), rate limiting, a place for secrets, product analytics.

**Added only when a number asks for it:**

| Part | What it is | Add it when |
|---|---|---|
| Cache (Redis) | fast memory for answers asked for often | the database gets slow under load |
| Load balancer | splits requests across servers | one server isn't enough, or one server failing must not take the app down |
| Read replicas | copies of the database used only for reads | reads are too many for one database |
| Sharding | the database split across servers | data or writes don't fit on one server; very late, it's complex |
| Connection pooler (PgBouncer) | shares the few connections a database allows | many processes or serverless functions connect |
| Search engine (Meilisearch, Elasticsearch) | fast, typo-tolerant search | database search isn't good enough |
| Message broker (RabbitMQ, Kafka) | a large, reliable queue between many services | many services send each other messages |
| Real-time (WebSockets) | the server pushes data without being asked | people must see each other's changes at once |
| Push notifications | messages on the phone with the app closed | the product must bring people back |
| API gateway | one door in front of many services | there are microservices |
| BFF (backend for frontend) | a small server shaped for one kind of client | web and mobile need very different data |
| Containers (Docker) | the app packed with everything it needs, runs the same everywhere | the hosting asks for it or there are several services |
| Kubernetes | starts, moves and restarts many containers | many services and a team to run it |
| Reverse proxy (Nginx, Caddy) | HTTPS, compression, routing in front of the app | self-hosting on a VPS; a PaaS includes it |
| Workflow engine (Temporal) | long multi-step processes that finish even if something fails midway | processes that run for days (onboarding, orders, approvals) |
| Vector database (pgvector, Pinecone) | search by meaning; the base of AI that answers from your data (RAG) | the AI must answer from your documents or data |
| Data warehouse | a separate database for large reports | reports slow down the app |
| Distributed tracing | follows one request through every service, with the time in each | a request crosses several services |
| WAF and DDoS protection | filters known attacks and floods of fake traffic | you're attacked or a large customer asks; often comes with the CDN |
| Feature flags | switch a feature on or off without a deploy | rolling out gradually |

## Steps

### 1. Read what exists
Journeys, glossary, non-functional requirements and open decisions from the PRD; the money check from the brief; the risk tests. List what's missing and ask only that.

**If the system already runs**, read how it runs first: the deploy files, Docker Compose, the backup. It's the starting point, not a rule. For each part show what it is today, keep or change, why, and what moving costs (data to migrate, scripts to rewrite, what could break). Change only for a reason: a requirement it doesn't meet or a number it can't carry. The user decides.

### 2. Requirements, with numbers
- **The 3–7 main jobs** of the system, headed "the functional requirements, from the PRD journeys and features", each with its source code (UJ-…, F-…). A job states the need, the technology at the end ("log a plate from a photo …: with AI"), so it stays true if the solution changes.
- **The qualities, with numbers,** in a table whose column says "Quality (non-functional requirement)": users (at the target and at 10×, from the real costs once step 13 has them, not only the brief's guess), requests per second at peak, data growth per year, response time for the main actions, availability, RPO (how much data you may lose in a failure) and RTO (how long until you're back), what must never be lost. A row the PRD doesn't give (the API's own answer time on the server) says in its source that the design set it.
- **The top 3 qualities, in order** (for example "data is never lost > logging works offline > low cost"). When two conflict, the higher one wins.
- **The constraints, separately:** legal (the law, contracts) and organizational (how many people build and run it, their hours, the budget), each with its source; they aren't ranked, a choice that breaks one is out.
- **The user decides:** confirm the numbers before going on.

### 3. Back-of-the-envelope calculation
Storage per year, peak requests, AI calls per day and their cost, photo traffic. Write the calculation, not only the result: "300 users × 20 entries a day = 6,000 writes a day, about 0.07 per second; one small server is plenty." Without it, a cache or a queue is a guess.
- **Mark every factor you guessed** `(guess)`, with what it's derived from ("from UJ-1: ~4 meals × 3–4 foods"). The peak hour's share of the day has no published standard: say so; interview books use peak = 2 × average (Alex Xu), stricter is fine if argued.
- **Every table that grows,** not only the biggest one, and the large files apart from the database.
- **The AI, one row per job** (`| Use | Model | Per user a day | Cost per request | Why |`), at the price of the region you'll use (an EU endpoint can cost more than the global one) and the price after any discount ends, the output counting the model's thinking too; then a typical user, and a heavy one at the daily cap, against the monthly AI budget; what's paid once, not per user (for example the AI that helps an admin fill in a new item), on a line of its own.
- **The conclusion must match step 9:** "one small server carries N×" only up to the limit the scale file gives; past it, a bigger server, then a second one at its trigger.
- **Write back what later steps measure** (the data model's real row sizes, the API's requests counted screen by screen, the AI test's tokens), with a journal line; the old guess stays visible ("first guessed ~3 GB").

### 4. Context (C4, level 1)
C4 draws the system at zoom levels, like a map: level 1 shows the system as one box and the world around it, level 2 opens the box. Here: who uses the system and which outside systems it talks to (payments, email, AI, data sources). A diagram, with the relationship table under it.
- **Name each outside system by its provider once chosen** ("Paddle (payments)"); providers come at step 12, so the context is read again then.
- **Every row has a "How":** for a system, its protocol (HTTPS, a webhook, OpenID Connect); for a person, how they reach the system ("the app (PWA), in a browser"), never an empty cell.
- **The outside systems in one group** (`group "Outside systems"` in the model), so the drawing keeps them together; the context drawn left to right (people on the left, the system in the middle, the group on the right); people as rounded boxes with [Person] under the name (C4 asks for the type, not a shape).
- **Every provider of step 12 appears** in the drawing or in a "left out of the drawing" list with the reason (monitoring, backups, plan B), the tools that build or serve the app but hold no one's data too (the domain, the code hosting, the code checks); what's only imported, not called while the app runs, is marked so (a dashed arrow).

### 5. Containers (C4, level 2)
The parts deployed separately and how they talk (HTTP, a queue, a database connection). A diagram, with the relationship table under it.
- **Default: one API and one database** (a monolith), until a number asks for more.
- **Every part that runs on its own is a container:** the scheduled backup job or a worker too, not only the app, the API and the database. An arrow starts at the part that does the work (a database doesn't send its own backups; the backup job reads it and sends the copy), and imported data goes to the container that runs the import. Mark the containers that keep health or other sensitive data, even for a short time (a file storage holding data exports for a few days), with a tag that has its own border in the legend. Under the table, what's left out of the drawing (monitoring, secrets, plan B providers, one-shot deploy containers), each with the container that talks to it. The outside systems keep their group here too: `diagrams.sh` adds it (`c4/add-groups.py`), since the Structurizr export leaves groups out of container and component views.
- **Every scheduled job, listed once,** with where it runs: a timer inside the API, or a container of its own when it needs its own rights or must run while the API is broken (the backup job). The same list gives each job its failure row (step 8) and its heartbeat (step 10). If the system runs today, the file ends with what changes from it.
- **How the app reaches people:** static files (PWA, SPA) or a server that renders pages (SSR). It changes the hosting.
- **How much works offline**, a one-way door:
  1. it opens and shows what you saw last;
  2. you can also create data; it's sent when the connection returns;
  3. everything works offline, shared data too, so you must decide who wins when two people change the same thing.

  Each level costs much more than the one before. If the PRD doesn't say, go back to it.
- **The user decides:** confirm the shape (how many parts, how the app is delivered, how much works offline).

### 6. The main flows, end to end
The 2–3 most important and most risky actions (for example: log a food; scan a plate with AI; pay). Each as a numbered table: step, where, what happens. For each:
- what happens right away and what goes to the background;
- what must be correct at once (payment, the account) and what can be correct a little later (sync, statistics);
- the offline path, if the flow works offline;
- **the "server says no" path:** what happens to an entry the server refuses (an expired login, an ended trial, a bad value). Signing out or an expired login never deletes what wasn't sent without asking;
- offline edits and deletes, not only new entries.

Draw each flow as a **UML sequence diagram**: the parts on top, time going down, the numbered steps matching the table; a step inside one part is an arrow back to it; failures as `alt` or `break`. The parts are the containers of step 5, with the same names, and every request passes the ones it really passes (the web server too); each flow draws its failure paths (no answer, refused, the login expired), not only the happy path. **A flow is re-read after the steps that detail it** (the data model, the API design, security, AI design): they decide its fields, limits and failure codes, and the flow is brought in line with a journal line; the flow keeps the path and what fails, the call's details stay in the API design. Once the UI design has written the app's words, a flow quotes what the person sees with the words file's text and its key (for example "Log in to send 3 entries.", `state.login_to_send`).

These flows become the end-to-end tests; the rest of the testing strategy is decided in `/architecture`.

### 7. The data
Where each kind of data lives, which copy is the source of truth (the server, or the phone until sync), what is sensitive (health data, payments), how it's backed up and where the backup copy lives (3-2-1: 3 copies, on 2 kinds of storage, 1 offsite; at another company if you also fear the provider, stricter than the rule asks). A diagram of where the data and its copies live: a C4 deployment view of the model (where each part runs, the copies as infrastructure nodes, health data marked). Logs with a user's id or IP address are still personal data under GDPR: never write "no personal data"; write what they hold, for how long and where. Details of tables and fields → `/data-model`.
- **Under the drawing, its arrows** (`| # | From → to | What |`), with the containers' numbers and a letter for each copy a provider makes by itself (A), checked by `check-tables.py` like the other views.
- **Every kind of personal data is a row,** what lives only at a provider too (the logs, the email addresses, the support mail, the AI's requests, the analytics), with how long it's kept. Once `/compliance` has written its record of processing, the two list the same data.
- **Encryption** in transit and at rest, store by store (the database, the file storage, each backup copy), and on the device, if the app keeps data there.
- **How a deletion reaches the backups:** they age out within N days by each storage's own expiry rule, and a restore inside that window redoes the deletions (step 8).
- **A backup is trusted only once tested:** each daily copy restored into a throwaway database and its rows counted before it leaves, and a full restore drill, timed under half the RTO, before the first tester and then on a fixed rhythm (for example every 6 months).

### 8. What happens when something fails
A table with every dependency (the database, the AI, payments, email, the server itself) × slow, down, returns garbage: timeout, retry, fallback, what the user sees.
- **Three rules everywhere, said once above the table:** every call to another part has a timeout; retries with growing pauses (backoff) only for what's safe to repeat; every container starts again by itself if it stops. Once the API design lists the outside calls with their limits, this file points to that one table instead of repeating the numbers.
- **The parts you don't see count too:** the monitoring itself, the backup job, the image registry, the domain and DNS, the HTTPS certificate; the secrets store (what starts during its outage can't read its secrets, so no deploy then); the log shipper (the small program that sends the logs to the monitoring tool; the alerts read from the logs stop with it); the scheduled jobs; the migrations; the server's disk; CI's free minutes (spent: no deploy, not even a fix); the support mailbox; the tools that build and import. For an offline app, the device's storage: the one failure that can lose what wasn't sent.
- **A lost server:** how it's rebuilt and in how long (a restore script, a DNS record with a short time to live, for example 5 minutes, so the new address is reached fast).
- **After a restore, the database is back in the past.** Name what that undoes and redo it before the app opens, in an after-restore job the restore script runs first: the account deletions made since the copy (keep the deleted ids as long as the oldest copy, and refuse a copy older than that); for an offline app, the devices' place in the sync (a new restore id makes each device send its recent data again and reload, so an entry the restore lost comes back from the device that wrote it). A restore the provider does by itself (a lost database node, one of the managed database's machines, rebuilt from its backup) is noticed too and runs the same job: for example PostgreSQL starts a new timeline at every restore, never at a restart, and the API reads it.
- **Single points of failure:** list them, and accept each one knowingly or remove it; the person who runs the system is one too.
- **Idempotency:** the same request received twice (a payment webhook, a retry after a timeout) doesn't do the work twice. Name where you need it and how (an idempotency key, a unique constraint), and where a repeat is harmless and accepted (an email sent twice).

### 9. Scale
What breaks first, from the providers' plans up to 100×, and **the number at which you change something**. "At" is where you expect it; the trigger is **what you watch**, in an alert or the weekly report (step 10), never the number of users ("CPU over 70% at the daily peak for a week: a bigger server"). Don't build for 100× now; know what you'd do then. Bigger server first (vertical), more servers later (horizontal). Name the part from the building blocks you'd add at each threshold; mark `(guess)` what nothing has measured yet.
- **The rows go by kind.** The providers' plans and caps first, since they break before the server: a spend cap, a free email plan, an outside API's rate limit, the logs' volume, CI's free minutes (which grow with the work, not the users). Then you and the servers: the hours a week the queues and support take, against the hours you have. Then the database's own rows: its size against the plan, a lost node, a restore that takes too long. Then what grows with something else: the data on the device, the alerts' thresholds, a legal duty that starts with size (a data protection officer, once health data is processed "on a large scale"). Each row says what you'd do at 100×.
- **Checked, and holds at 100×:** the parts you checked that don't break, each with its number, so nobody worries about them again.
- **Doors kept open** (cheap now, expensive later): nothing lives only on one server (the sessions, the limits' counters and any state that decides what the API does are read from the database, never kept in one server's memory, so two servers agree; not even the login keys, or a rebuilt server signs everyone out; what is on the disk, the restore script makes again); scheduled jobs (hourly, daily) run from one table, each run claimed by one server with a lock, so two servers never run one twice; ids that don't come from one server's counter (made by the app); the big tables indexed the way they're read.

### 10. Monitoring
- structured logs, one line per event with its fields named (the route's template, `/foods/{id}`, never the raw path, which carries ids), and a "never logged" list (emails, names, passwords, tokens, bodies with sensitive data); the user's id and IP that remain are personal data: where they're kept and for how long;
- the four golden signals: latency, traffic, errors, saturation, with where each saturation number is read (for example a Java server keeps the memory it reserved, so the server's memory says nothing: read what the API still uses after Java's garbage collection has freed the rest);
- errors from the app and the server in one place;
- an outside check that the site answers (uptime), on a health address that answers "up" only when the API reaches the database;
- how alerts reach the user (calls and SMS, or a chat app while only they use the system), and what happens when the monitoring tool itself is down;
- alerts that reach the user, few, each with what to do (`| Alert | When | What I do |`), on failures that last, tied to the availability target (the SLO, for example "works 99.5% of the time"): alert when you're burning through it, not on every error (for example at half the month's availability budget, the downtime the SLO allows, after which only fixes deploy until the month ends). An alert counts only what it's named for, with a minimum count: "AI failing" counts the provider's errors, never people stopped by your own limits, and needs at least 5 of them, so one failure at night isn't 100%;
- a heartbeat for every scheduled job of step 5 (a signal the job sends at every run; a missing one is an alert), after its period plus a margin (a daily job after 26 hours); count the monitors and heartbeats against the tool's plan;
- **a weekly report, no alert:** every trigger of step 9 that isn't an alert is a line of it, read against its trigger; a trigger nobody reads isn't watched;
- a budget alert for each paid service, **set at the provider too** (for example a cloud billing alert), not only in the app: a stolen key skips the app's own counter. Where the provider offers a hard cap that stops the spending, set it above the alert (for example at twice the alert's amount); a plan B provider gets its own limit as it's switched on, before its first call;
- **reminders, not alerts,** in a calendar, for what expires (the domain, access certificates, key rotations) and for reading every ADR's "Revisit when" on a fixed rhythm.

### 11. Deployment and CI/CD, as decisions
The implementation comes in Build, with `project-setup`. If a pipeline runs today, start from it: `| Today | Keep or change | Why |`, one row per piece.
- **Where it runs:** PaaS (a platform runs the code for you, for example Render or Fly), a VPS (a rented server you run yourself) or serverless (functions that start only when called). The trade-off: your operating time vs cost vs control. Name the operating system and what runs on it with their versions, and when the system's support ends, read on its page.
- **The region**, from the personal-data requirements.
- **Environments:** local, staging (a copy of production to check before release; yes or no, and why), production. Staging earns its cost when something can't be tested in CI (a webhook that needs a public address, an attack scan); then on a server of its own, so a scan never touches production, with invented data only.
- **The pipeline:** lint, tests, one build, deploy from `main`; each check where it's worth its minutes; only code whose tests passed is deployed. Preview deploys per PR if the hosting offers them. Under the diagram, the steps: `| # | Step | What happens |`.
- **Database migrations** (changes to the structure) run before the new code; a migration gives up quickly when it waits for a lock, and a failed one leaves the previous version serving; a column is dropped only in a release whose previous release no longer uses it (expand, then contract), so a rollback still works.
- **Rollback** (back to the previous version): in seconds, from the images the server keeps, each started by its digest (the hash of its content), not by a tag, which can be moved. Name **the release that can't be rolled back** (in an offline app, one that raises the device's database version) and what you do instead: fix forward, kept rare.
- **The pause at each deploy** with one server: how long, how many deploys a month, against the availability budget; accepted or removed.
- **When there's no deploy:** the secrets store down, the CI minutes spent, half the month's availability budget spent (only fixes).
- **Secrets outside the code**, and **the restore:** a script rebuilds a lost server within the RTO, tried at the restore drill.
- A diagram of the road from a push to production, with the rollback: a UML activity diagram (who does each step as a swimlane, the decisions as diamonds).

### 12. Providers
For each need (hosting, database, file storage, a second backup copy, AI, payments, email, login, monitoring, secrets), pick one against the PRD's requirements: where the data is, data processing agreement (DPA), no training on your data, price, and **how you'd leave** if you had to (put it behind one interface in the code). Build or buy: build only what makes the product different. The list feeds `/compliance`.
- **Every outside service is a row,** those that see no person's data too (the domain, the certificates, the code hosting and CI, the code checks, the data sources), saying so; "How I'd leave" filled for every one. If a system runs today, a "Today" column, and what leaves with the reason.
- **Under the table, every provider outside the required region,** each with why it's kept (it sees only code, or it's the exception the PRD allows).
- **The provider you can't do without gets a plan B** behind the same interface, switched by hand, its DPA signed before it's needed.

Check that the analytics tool can compute the PRD's metrics (retention by sign-up week needs to follow one person over time, which privacy-first web analytics don't do). A provider that depends on a risk test can be chosen before it when the test only picks the model; the rule for choosing is written before the test and includes the PRD's response time, not only accuracy.

### 13. Monthly cost
Per part, at three sizes: until the beta (only you), at the target and at 10×, with a total and a per-paying-user row; each price from the provider's official page, the day it was read in its row, an exchange rate marked as a guess. Cost per paying user compared with the money check in the brief, line by line (`| A month, per paying user | Brief | Now |`). If the margin doesn't hold, go back to the brief.
- **Divide by the paying users,** not all users: people in a trial cost without paying.
- **The expensive parts start when other people's data arrives** (the beta), not on day one: while only the builder uses it, a cheaper setup carries the same risk. Define the moment exactly (the first person other than the builder using it with their own data; tests on accounts you prepared don't count), write the rule ("before the first beta tester"), what you accept until then, and the monthly cost from the beta, before any revenue.
- **Around the table:** what stays free at these sizes; a known risk priced as a line (for example "if the API doesn't fit the small server: +€4 a month in every column"); what isn't per user (the admin's AI, requests that fail but are still paid, test runs); a price that changes on a known date, the table on the later one; a cost not measured yet carried through as a second case, not dropped; the tools you build with kept out, as the business's cost.
- **AI: pick the model per kind of request,** the expensive one only where accuracy matters. When a risk test picks the model, write the rule for choosing before the test runs.

### 14. The big decisions become ADRs
An ADR (Architecture Decision Record) is one short file per decision, in `docs/00-project/adr/`: context, the options (lettered A, B, C, with a cost column when they differ in money), the decision, the consequences, when to revisit. Only one-way doors: the database, the payments provider (paying subscribers would have to move), the offline level, monolith or not, the AI provider, a product rule that decides what data is stored; the hosting only when the code is tied to it (with containers it runs the same elsewhere, so it isn't one). One at a time: you give the options and your recommendation, **the user chooses**. Note what each decision pulls along ("offline level 2 means deciding what happens when the same entry is changed on two devices"). **After each ADR, re-read the earlier files it changes:** a managed database makes the failure, scale and monitoring files stale. **When a later step changes an ADR's facts but not its decision,** an "Updated" line under its date says what changed and that the decision doesn't change; a changed decision is a new ADR that replaces it.

### 15. Check it
- every non-functional requirement has a mechanism in the design that covers it;
- every PRD journey passes through the diagram;
- the After-MVP High ideas in `docs/00-project/ideas.md` aren't blocked by the design (for example an import needs a background job and large uploads); don't build them, just don't close the door;
- someone outside reads the main flow and understands it. Nobody at hand? `/system-design validate <folder>`, run by a separate agent that has only the documents, not this conversation;
- `diagrams.sh` passes: the counts (`facts.py`) and the arrows against their tables.

Write as you go: each step's file once the user confirms it, with a journal line in the README.

**After the later Design steps, bring it in line.** Every later step changes something here: the data model measures the rows, the API counts the requests, security moves the secrets, the AI design prices the thinking. Each change comes back at once, in the same commit, with a journal line naming its step ("from 05 API design's sync, with my yes: …"). Once every Design step is done, walk this folder through file by file (the Design walkthrough): each file read whole against what the later steps decided and brought in line, one commit per file ("07-failures in line with the later steps"); then read again as a newcomer would, since explaining a file finds what the edit missed; the README last, rewritten from the files as they now stand; the ADRs' "Updated" lines; and after a day of big changes, the outside check again.

This is the first Design step, so it also creates `docs/02-design/README.md` if it doesn't exist: the map of the Design steps from `FLOWS.md` (each step, its question, high-level or low-level design, status), with a short note translating HLD and LLD, and **a map for a reader who knows arc42**: a table with the 12 arc42 sections (checked on docs.arc42.org) and, for each, the files that cover it, linked; the steps stay ordered by when each decision is taken, the map is how a reader used to arc42 finds each section. Then **a Diagrams section:** each notation, its drawings and their text source, and where each C4 level is (level 4, the code, isn't drawn: C4 itself doesn't recommend it for long-lived documentation). Every later Design step adds its files to the maps. At the end, set this step's row to done, with the date; after the walkthrough, "brought in line in the Design walkthrough, [date]".

```
docs/02-design/01-system-design/
  README.md            the entry: status, next, in one page, files, what we skip, open questions, ADRs, glossary, journal
  01-requirements.md   02-calculation.md   03-context.md   04-containers.md
  05-flows.md          06-data.md          07-failures.md  08-scale.md
  09-monitoring.md     10-deployment.md    11-providers.md 12-cost.md
  diagrams/            c4-context, c4-containers, data (SVG, from the C4 model); one per flow, deployment (.puml + SVG)
docs/02-design/c4/workspace.dsl   the C4 model, shared with /architecture; c4/views.txt: each view's SVG and the file with its table
docs/02-design/diagrams.sh        draws every diagram, after checks/facts.py (both set up by /docs-setup)
docs/00-project/adr/
  0001-[title].md …
```

The README:

````markdown
# System design – [Product]
| | |
|---|---|
| **Status** | draft / confirmed by me, [date] (steps 1–15, all N ADRs accepted); checked by an outside reader (`/system-design validate`), the findings fixed; later: brought in line, file by file, in the Design walkthrough ([dates]), with my yes; waiting for [a risk test: planned for [date], not run yet on [date]] |
| **Author** | |
| **Updated** | |
| **Next** | 02 Compliance, which takes the providers and where the data lives from here; once every Design step is done: Planning, then what Build owes here, by moment (slice 1, before the beta) |
## In one page
The design as the files stand today, without the history of its corrections (that's the journal), one line each with a bold label: What it is (the target's users, peak requests, data a year), What matters most (the top 3, the constraints), The shape (the parts, with their ADRs), Safety nets (RPO and RTO as they really are, period by period), AI (the model per job, the cap, plan B), Running it (monitoring and the road to production), Cost (until the beta, from the beta, at the target, at 10×, per paying user against the brief).
## The files
| File | What it answers |
Then one line: the diagrams, their notations, drawn by `diagrams.sh`; where the ADRs are.
## Not doing, and why
| Not doing | Why | It comes back when |
(every "no" the files decide; each Why links the file or ADR that argues it; It comes back when: a trigger, a moment or "never")
## Open questions
| Question | Answered by | When |
(When is a moment: before slice 1, slice 1, before the beta, a planned date with "not run yet on [date]". An answered question stays, struck through, with where and when it was answered.)
## Decisions (ADRs)
| ADR | Decision |
Decided before, and shaping this design: [the ADRs that already existed, if any].
Later ADRs that shape this design, from the steps after it:
| ADR | Decision |
## Glossary
- **Term:** what it is, compared with something the reader already knows (every term the README and the files use)
## Journal
- [date]: [what was confirmed, decided or changed, in my voice ("confirmed by me", "with my yes", "decided by me, option A"); from a later step, its name ("from 05 API design's sync, with my yes"); what it changed, file by file]
````

Each topic file starts with `# NN – [Topic]` and a link back to the README, then:

| File | Holds |
|---|---|
| `01-requirements.md` | the functional requirements (main jobs, with codes); `\| Quality (non-functional requirement) \| Number \| Source \|`; top 3; constraints, legal and organizational |
| `02-calculation.md` | the calculation, written out, guesses marked; the AI per job, `\| Use \| Model \| Per user a day \| Cost per request \| Why \|`, a typical and a heavy user against the budget; later measurements written back; what it means |
| `03-context.md`, `04-containers.md` | the diagram (a view of the C4 model), `\| # \| From → to \| What \| How \|`; in 03 and 04 what's left out of the drawing; in 04 a paragraph per container, the offline level, the scheduled jobs, what changes from the system running today |
| `05-flows.md` | per flow: a one-line scene, the sequence diagram, `\| # \| Where \| What happens \|`, right away vs later, the offline path, the failure paths |
| `06-data.md` | the deployment diagram with `\| # \| From → to \| What \|`; `\| Data \| Lives in \| Source of truth \| Sensitive \| Backup \|`; encryption, the device, deletion and the backups |
| `07-failures.md` | the three rules; `\| Dependency \| Slow \| Down \| Garbage \| What the user sees \|`; the after-restore job; single points of failure; idempotency |
| `08-scale.md` | `\| What breaks first \| At \| Trigger number \| What I do \|`, by kind; checked and holds at 100×; doors kept open |
| `09-monitoring.md` | logs, errors, golden signals, the outside check, how alerts arrive; `\| Alert \| When \| What I do \|`; the weekly report; budget alerts and caps; reminders; SLO |
| `10-deployment.md` | `\| Today \| Keep or change \| Why \|` if a pipeline runs; the activity diagram, `\| # \| Step \| What happens \|`; the decisions |
| `11-providers.md` | `\| Need \| Today \| Provider \| Where the data is \| DPA, training on our data \| How I'd leave \|` (Today only if a system runs); the providers outside the required region, and why |
| `12-cost.md` | `\| Part \| Until the beta (only me) \| Target \| 10× \|`, a total and a per-paying-user row; what stays free; `\| A month, per paying user \| Brief \| Now \|`; the notes around the table |

And one file per decision in `docs/00-project/adr/NNNN-[title].md`, the next number from the index `docs/00-project/adr/README.md`, with its row added there in the same commit (| # | Decision | Status | Decided in | Last change |) and the next number moved on; every Design step's ADRs do the same:

```markdown
# ADR-NNNN: [Decision]
- **Status:** accepted | replaced by ADR-NNNN (linked both ways)
- **Date:** [date] (decided in [step], e.g. "01 System design"; two steps: "03 Architecture → 07 Security")
- **Updated:** [date]: [what changed]; [date]: …; the decision doesn't change. (one line, every dated change in the body listed, only once one exists; the body marks each "(added [date])" or "(corrected [date]: it said …)"; a flipped decision is a new ADR, not an Updated entry)
## Context
## Options
| Option | For | Against |
(A., B., C., the chosen one in bold; a cost column when the options differ in money)
## Decision
## Consequences
## Revisit when
```

## Validate mode
`/system-design validate <folder>`: judge an existing system design, change nothing.
1. Read the design folder, its ADRs and the README's journal, the PRD, the brief's money check and `docs/00-project/ideas.md`.
2. Check the template and "Done when" item by item, citing the lines.
3. Then ask: does every number trace back to the PRD? Does the calculation justify every part beyond one API and one database? Does every dependency have a failure row? Does every provider appear in the context? Do the C4 drawings come from one model, and do the flows' and the cost's numbers match the calculation and the scale file? Does every non-functional requirement have a mechanism? Does the cost fit the brief? Is every one-way door an ADR? Is every term explained? Is every price, limit and provider fact linked to its page and dated, every guess and assumption marked, every count taken from its source? Is every scale trigger read by an alert or the weekly report? Does every scheduled job have a failure row and a heartbeat? Does a restore redo what it undoes? Is the README in the user's voice, its "In one page" true of the files today? Does `diagrams.sh` pass?
4. Report: findings by severity, each with the line, what's wrong and what to change; then what the design does well; then what you couldn't evaluate. The user picks what to apply.

## The bad version and why not
- Microservices and Kubernetes for 300 users, because "that's what big companies do".
- Picking the technology first and looking for requirements after.
- Only the happy path: nothing about the AI or payments failing.
- No numbers: "it must scale" is not a requirement.
- Deployment decided at the end → "works on my machine".
- Nice diagrams with no decisions and no reasons.
- Diagrams in a home-made style, each drawn separately: the next company can't read them, and the same part has two names in two drawings.
- Finding out the AI or cloud bill at the end of the month.
- Prices and limits from memory, with no page and no date: the first invoice or the first refused request disagrees.
- Trigger numbers nobody watches: the scale file says 70% CPU, and no alert or report reads it.

## What breaks if you skip it
The architecture becomes whatever the first PRs made it. The first outage shows there's no tested backup, the first invoice shows the AI costs more than the subscription, and a GDPR requirement forces a move to another region after launch.

## The principle behind it
There is no best solution, only trade-offs (the first law of software architecture, Richards and Ford). Design for the numbers you have, know what you'd do at the next 10×, and write down why you chose.

## How to apply it at work
Before a new service or data flow, write a short design doc with `/design-doc change "<name>"`: requirements with numbers, the C4 drawings, the flows with their failures, the cost, the alternatives, a written decision. Discuss it with the team before the code; the big decisions go into the repo as ADRs.

## Done when
- [ ] requirements with numbers, the top 3 qualities in order, the constraints (legal and organizational), confirmed by the user
- [ ] the calculation written out, guesses marked, its conclusion consistent with the scale file
- [ ] the context and container diagrams, the offline level, the shape confirmed by the user
- [ ] 2–3 flows traced end to end, with what's immediate and what's later, each with a sequence diagram
- [ ] the data: where it lives, source of truth, sensitive data, encryption, backups, with a diagram; every kind of personal data a row, what lives only at a provider too
- [ ] backups tested before they're trusted (each copy, and a timed restore drill); a deletion's way into the backups
- [ ] a failure row for every dependency, the unseen ones too (monitoring, backup job, registry, domain, certificate, secrets store, log shipper, scheduled jobs, migrations, disk, CI minutes), single points of failure, idempotency
- [ ] after a restore: what it undoes, and the job that redoes it before the app opens
- [ ] every offline flow has a "server says no" path; nothing unsent is deleted without asking
- [ ] nothing only on the server's disk or in one server's memory (login keys included); every scheduled job listed once, with a place to run and a lock
- [ ] what breaks, from the providers' plans to 100×, with trigger numbers that an alert or the weekly report reads
- [ ] monitoring, alerts tied to the SLO, a heartbeat per scheduled job, budget alerts in the app and at the provider, reminders for what expires
- [ ] deployment and CI/CD decided, with a diagram of the road to production; the release that can't be rolled back named
- [ ] providers chosen against the requirements, every outside service a row, with a way to leave; the ones outside the required region named, with why
- [ ] monthly cost at three sizes, per paying user, compared with the brief; when the expensive parts start
- [ ] every price, limit and provider fact linked and dated; guesses `(guess)`, untried facts `[ASSUMPTION]`; counts from their sources
- [ ] every one-way door an ADR, chosen by the user; the earlier files re-read after each one
- [ ] checked against the requirements, the journeys and the High ideas
- [ ] a glossary for every term the README and the files use
- [ ] the README: status and journal in the user's voice, Next, "In one page" as the files stand, what we skip and why, open questions with their moments, the ADR tables (this step's, decided before, later)
- [ ] every provider in the context drawing or its "left out" list
- [ ] every diagram in a standard notation, drawn by `diagrams.sh` (C4 from the model), opened, no text overlapping; the counts and the arrows-vs-tables check passing
- [ ] once the later Design steps are done: walked through file by file, the README last

## Next
Compliance (`/compliance`): it takes the list of providers and the data locations from here.
