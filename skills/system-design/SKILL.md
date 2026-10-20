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
- **Spot risky assumptions for the user:** when a decision rests on something nobody has checked ("the AI answers in 5 s", "the free tier is enough") and being wrong would cost a lot, stop and propose a risk test: what to check, how long it takes, the pass mark, and when. The user only says yes or no; run it with `/risk-tests`.
- **Read first:** the running system if there is one (step 1), `docs/01-discovery/04-prd.md` (journeys, glossary, non-functional requirements, open decisions), the money check in `03-product-brief.md`, the risk tests (`docs/01-discovery/risk-tests/`), and `docs/00-project/ideas.md` (the After-MVP High ideas). Ask only what is missing.
- **The user decides** at three points: the numbers (step 2), the shape of the system (step 5) and every ADR (step 14). You give the options and a recommendation; they choose. One decision at a time.
- **No new requirements here.** If the design needs a requirement the PRD doesn't have (for example how much works offline), stop, propose it, and on a yes add it to the PRD with a journal line.
- **Start with the fewest parts.** Every extra box is one more thing that fails, needs watching and costs money. A part is added only when a number asks for it.
- **Diagrams in standard notations, drawn from text** (decided 2026-10-20), so they read the same at any company and can't drift apart: **C4** levels 1–2 and where the data lives (a C4 deployment view) from **one Structurizr model**, `docs/02-design/c4/workspace.dsl` (Structurizr DSL: the elements and relationships written once, each drawing a view of them); the flows as **UML sequence diagrams**; the road to production as a **UML activity diagram**, each a `.puml` next to its `.svg` in `diagrams/`. `docs/02-design/diagrams.sh` (set up by `/docs-setup`) draws them all with the Structurizr CLI and PlantUML, both free. In C4: drawn in Structurizr's own look (the type under every name: [Person], [Software System], [Container: tech], as C4's notation asks); one relationship per direction (a webhook back is a second arrow); each label short, saying what flows and starting with its row number in the table under the drawing (arc42's diagram + table), the details in the table; the technology as the relationship's technology; the outside systems in one `group`; a title per view; the shared legend. **`diagrams.sh` checks every numbered arrow against its table** (`c4/check-tables.py`: the same numbers, the same two ends) and fails on a difference; add each view's Markdown file as the third field of `c4/views.txt`. Never a hand-made SVG or a home style; not Mermaid in chat (the arrows get lost). Open each one before committing: no text overlaps.
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
- **The qualities, with numbers,** in a table whose column says "Quality (non-functional requirement)": users (at the target and at 10×, from the real costs once step 13 has them, not only the brief's guess), requests per second at peak, data growth per year, response time for the main actions, availability, RPO (how much data you may lose in a failure) and RTO (how long until you're back), what must never be lost.
- **The top 3 qualities, in order** (for example "data is never lost > logging works offline > low cost"). When two conflict, the higher one wins.
- **The constraints, separately:** legal (the law, contracts) and organizational (how many people build and run it, their hours, the budget), each with its source; they aren't ranked, a choice that breaks one is out.
- **The user decides:** confirm the numbers before going on.

### 3. Back-of-the-envelope calculation
Storage per year, peak requests, AI calls per day and their cost, photo traffic. Write the calculation, not only the result: "300 users × 20 entries a day = 6,000 writes a day, about 0.07 per second; one small server is plenty." Without it, a cache or a queue is a guess.
- **Mark every factor you guessed** `(guess)`, with what it's derived from ("from UJ-1: ~4 meals × 3–4 foods"). The peak hour's share of the day has no published standard: say so; interview books use peak = 2 × average (Alex Xu), stricter is fine if argued.
- **Every table that grows,** not only the biggest one, and the large files apart from the database.
- **The conclusion must match step 9:** "one small server carries N×" only up to the limit the scale file gives; past it, a bigger server, then a second one at its trigger.
- **Write back what later steps measure** (the data model's real row sizes, the API's requests counted screen by screen, the AI test's tokens), with a journal line; the old guess stays visible ("first guessed ~3 GB").

### 4. Context (C4, level 1)
C4 draws the system at zoom levels, like a map: level 1 shows the system as one box and the world around it, level 2 opens the box. Here: who uses the system and which outside systems it talks to (payments, email, AI, data sources). A diagram, with the relationship table under it.
- **Name each outside system by its provider once chosen** ("Paddle (payments)"); providers come at step 12, so the context is read again then.
- **Every row has a "How":** for a system, its protocol (HTTPS, a webhook, OpenID Connect); for a person, how they reach the system ("the app (PWA), in a browser"), never an empty cell.
- **The outside systems in one group** (`group "Outside systems"` in the model), so the drawing keeps them together; the context drawn left to right (people on the left, the system in the middle, the group on the right); people as rounded boxes with [Person] under the name (C4 asks for the type, not a shape).
- **Every provider of step 12 appears** in the drawing or in a "left out of the drawing" list with the reason (monitoring, backups, plan B); what's only imported, not called while the app runs, is marked so (a dashed arrow).

### 5. Containers (C4, level 2)
The parts deployed separately and how they talk (HTTP, a queue, a database connection). A diagram, with the relationship table under it.
- **Default: one API and one database** (a monolith), until a number asks for more.
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

Draw each flow as a **UML sequence diagram**: the parts on top, time going down, the numbered steps matching the table; a step inside one part is an arrow back to it; failures as `alt` or `break`.

These flows become the end-to-end tests; the rest of the testing strategy is decided in `/architecture`.

### 7. The data
Where each kind of data lives, which copy is the source of truth (the server, or the phone until sync), what is sensitive (health data, payments), how it's backed up and where the backup copy lives (3-2-1: 3 copies, on 2 kinds of storage, 1 at another company). A diagram of where the data and its copies live: a C4 deployment view of the model (where each part runs, the copies as infrastructure nodes, health data marked). Logs with a user's id or IP address are still personal data under GDPR: never write "no personal data"; write what they hold, for how long and where. Details of tables and fields → `/data-model`.

### 8. What happens when something fails
A table with every dependency (the database, the AI, payments, email, the server itself) × slow, down, returns garbage: timeout, retry, fallback, what the user sees.
- **The parts you don't see count too:** the monitoring itself, the backup job, the image registry, the domain and DNS, the HTTPS certificate.
- **Single points of failure:** list them, and accept each one knowingly or remove it.
- **Idempotency:** the same request received twice (a payment webhook, a retry after a timeout) doesn't do the work twice. Name where you need it and how (an idempotency key, a unique constraint).

### 9. Scale
What breaks first at 10× and at 100×, and **the number at which you change something** ("at 70% CPU for a week, a bigger server"). Don't build for 100× now; know what you'd do then. Bigger server first (vertical), more servers later (horizontal). Name the part from the building blocks you'd add at each threshold.
- **Doors kept open:** nothing only on the server's disk (not even the login keys, or a rebuilt server signs everyone out); scheduled jobs (hourly, daily) with a named place to run and a lock, so two servers don't run them twice.

### 10. Monitoring
- structured logs, without personal data;
- the four golden signals: latency, traffic, errors, saturation;
- errors from the app and the server in one place;
- an outside check that the site answers (uptime);
- alerts that reach the user, tied to the availability target (the SLO, for example "works 99.5% of the time"): alert when you're burning through it, not on every error;
- a budget alert for each paid service, **set at the provider too** (for example a cloud billing alert), not only in the app: a stolen key skips the app's own counter.

### 11. Deployment and CI/CD, as decisions
The implementation comes in Build, with `project-setup`.
- **Where it runs:** PaaS (a platform runs the code for you, for example Render or Fly), a VPS (a rented server you run yourself) or serverless (functions that start only when called). The trade-off: your operating time vs cost vs control.
- **The region**, from the personal-data requirements.
- **Environments:** local, staging (a copy of production to check before release; yes or no, and why), production.
- **The pipeline:** lint, tests, one build, deploy from `main`. Preview deploys per PR if the hosting offers them.
- **Database migrations** (changes to the structure) that run before the new code, **rollback** in minutes (back to the previous version), secrets outside the code, a backup with a tested restore.
- A diagram of the road from a push to production, with the rollback: a UML activity diagram (who does each step as a swimlane, the decisions as diamonds).

### 12. Providers
For each need (hosting, database, AI, payments, email, login, monitoring), pick one against the PRD's requirements: region, data processing agreement (DPA), no training on your data, price, and **how you'd leave** if you had to (put it behind one interface in the code). Build or buy: build only what makes the product different. The list feeds `/compliance`. Check that the analytics tool can compute the PRD's metrics (retention by sign-up week needs to follow one person over time, which privacy-first web analytics don't do). A provider that depends on a risk test can be chosen before it when the test only picks the model; the rule for choosing is written before the test and includes the PRD's response time, not only accuracy.

### 13. Monthly cost
Now, at the target and at 10×, per part, with today's prices from the providers' official pages. Cost per paying user compared with the money check in the brief. If the margin doesn't hold, go back to the brief.
- **Divide by the paying users,** not all users: people in a trial cost without paying.
- **The expensive parts start when other people's data arrives** (the beta), not on day one: while only the builder uses it, a cheaper setup carries the same risk. Write the rule ("before the first beta tester") and what you accept until then.
- **AI: pick the model per kind of request,** the expensive one only where accuracy matters. When a risk test picks the model, write the rule for choosing before the test runs.

### 14. The big decisions become ADRs
An ADR (Architecture Decision Record) is one short file per decision, in `docs/00-project/adr/`: context, the options, the decision, the consequences, when to revisit. Only one-way doors: the database, the hosting, the offline level, monolith or not, the AI provider. One at a time: you give the options and your recommendation, **the user chooses**. Note what each decision pulls along ("offline level 2 means deciding what happens when the same entry is changed on two devices"). **After each ADR, re-read the earlier files it changes:** a managed database makes the failure, scale and monitoring files stale.

### 15. Check it
- every non-functional requirement has a mechanism in the design that covers it;
- every PRD journey passes through the diagram;
- the After-MVP High ideas in `docs/00-project/ideas.md` aren't blocked by the design (for example an import needs a background job and large uploads); don't build them, just don't close the door;
- someone outside reads the main flow and understands it. Nobody at hand? `/system-design validate <folder>`.

Write as you go: each step's file once the user confirms it, with a journal line in the README.

This is the first Design step, so it also creates `docs/02-design/README.md` if it doesn't exist: the map of the Design steps from `FLOWS.md` (each step, its question, high-level or low-level design, status), with a short note translating HLD and LLD, and **a map for a reader who knows arc42**: a table with the 12 arc42 sections (checked on docs.arc42.org) and, for each, the files that cover it, linked; the steps stay ordered by when each decision is taken, the map is how a reader used to arc42 finds each section. Every later Design step adds its files to the map. At the end, set this step's row to done, with the date.

```
docs/02-design/01-system-design/
  README.md            the entry: status, summary, files, what we skip, open questions, ADRs, glossary, journal
  01-requirements.md   02-calculation.md   03-context.md   04-containers.md
  05-flows.md          06-data.md          07-failures.md  08-scale.md
  09-monitoring.md     10-deployment.md    11-providers.md 12-cost.md
  diagrams/            c4-context, c4-containers, data (SVG, from the C4 model); one per flow, deployment (.puml + SVG)
docs/02-design/c4/workspace.dsl   the C4 model, shared with /architecture
docs/00-project/adr/
  0001-[title].md …
```

The README:

````markdown
# System design – [Product]
| | |
|---|---|
| **Status** | draft / confirmed by [who], [date] |
| **Author** | |
| **Updated** | |
| **Next** | 02 Compliance |
## In one page
What it is, the top 3 qualities, the shape, the safety nets, the cost: 5–6 lines.
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
| `01-requirements.md` | the functional requirements (main jobs, with codes); `\| Quality (non-functional requirement) \| Number \| Source \|`; top 3; constraints, legal and organizational |
| `02-calculation.md` | the calculation, written out, guesses marked, later measurements written back |
| `03-context.md`, `04-containers.md` | the diagram (a view of the C4 model), `\| # \| From → to \| What \| How \|`; in 03 what's left out of the drawing; the offline level in 04 |
| `05-flows.md` | per flow: the sequence diagram, `\| # \| Where \| What happens \|`, immediate vs later, offline path |
| `06-data.md` | the deployment diagram, `\| Data \| Lives in \| Source of truth \| Sensitive \| Backup \|` |
| `07-failures.md` | `\| Dependency \| Slow \| Down \| Garbage \| What the user sees \|`; single points of failure; idempotency |
| `08-scale.md` | `\| What breaks first \| At \| Trigger number \| What I do \|`; doors kept open |
| `09-monitoring.md` | logs, golden signals, alerts with what to do, SLO |
| `10-deployment.md` | the activity diagram, the steps, keep or change, decisions |
| `11-providers.md` | `\| Need \| Provider \| Region \| DPA \| How I'd leave \|` |
| `12-cost.md` | `\| Part \| Now \| Target \| 10× \|`; per paying user against the brief |

And one file per decision in `docs/00-project/adr/NNNN-[title].md`:

```markdown
# ADR-NNNN: [Decision]
- **Status:** accepted | replaced by ADR-NNNN
- **Date:**
## Context
## Options
| Option | For | Against |
## Decision
## Consequences
## Revisit when
```

## Validate mode
`/system-design validate <folder>`: judge an existing system design, change nothing.
1. Read the design folder, its ADRs and the README's journal, the PRD, the brief's money check and `docs/00-project/ideas.md`.
2. Check the template and "Done when" item by item, citing the lines.
3. Then ask: does every number trace back to the PRD? Does the calculation justify every part beyond one API and one database? Does every dependency have a failure row? Does every provider appear in the context? Do the C4 drawings come from one model, and do the flows' and the cost's numbers match the calculation and the scale file? Does every non-functional requirement have a mechanism? Does the cost fit the brief? Is every one-way door an ADR? Is every term explained?
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

## What breaks if you skip it
The architecture becomes whatever the first PRs made it. The first outage shows there's no tested backup, the first invoice shows the AI costs more than the subscription, and a GDPR requirement forces a move to another region after launch.

## The principle behind it
There is no best solution, only trade-offs (the first law of software architecture, Richards and Ford). Design for the numbers you have, know what you'd do at the next 10×, and write down why you chose.

## How to apply it at work
Before a new service or data flow, write a one-page design doc: requirements with numbers, the diagram, the failure table, the cost. Discuss it with the team before the code; the big decisions go into the repo as ADRs.

## Done when
- [ ] requirements with numbers, the top 3 qualities in order, the constraints (legal and organizational), confirmed by the user
- [ ] the calculation written out, guesses marked, its conclusion consistent with the scale file
- [ ] the context and container diagrams, the offline level, the shape confirmed by the user
- [ ] 2–3 flows traced end to end, with what's immediate and what's later, each with a sequence diagram
- [ ] the data: where it lives, source of truth, sensitive data, backups, with a diagram
- [ ] a failure row for every dependency, the unseen ones too (monitoring, backup job, registry, domain, certificate), single points of failure, idempotency
- [ ] every offline flow has a "server says no" path; nothing unsent is deleted without asking
- [ ] nothing only on the server's disk (login keys included); scheduled jobs have a place to run
- [ ] what breaks at 10× and 100×, with trigger numbers
- [ ] monitoring, alerts tied to the SLO, budget alerts in the app and at the provider
- [ ] deployment and CI/CD decided, with a diagram of the road to production
- [ ] providers chosen against the requirements, with a way to leave
- [ ] monthly cost at three sizes, per paying user, compared with the brief; when the expensive parts start
- [ ] every one-way door an ADR, chosen by the user; the earlier files re-read after each one
- [ ] checked against the requirements, the journeys and the High ideas
- [ ] a glossary for every term
- [ ] the README: status, summary, what we skip and why, open questions, the ADR table
- [ ] every provider in the context drawing or its "left out" list
- [ ] every diagram in a standard notation, drawn by `diagrams.sh` (C4 from the model), opened, no text overlapping; the arrows-vs-tables check passing

## Next
Compliance (`/compliance`): it takes the list of providers and the data locations from here.
