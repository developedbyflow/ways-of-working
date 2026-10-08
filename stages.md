# Stages of a product (stages)

- **Use it when:**
  - you want the whole road of a product (a SaaS, an app, a service) in front of you, from the first idea to a product that grows;
  - or you need to know what stage an existing project is at, and what it skipped.
- **What you get:** a map in three levels: stage → step → component, each with what it is, why it's needed and what it gives you. For an existing project: its stage, the gaps behind it with what each one breaks, and the next step.
- **Run it:**
  - `/wow-stage`: the eight stages;
  - `/wow-stage foundation`: the steps of one stage;
  - `/wow-stage foundation architecture`: the components of one step;
  - `/wow-stage assess ~/code/my-app`: where a project is.
- **Not when:**
  - you know the situation in front of you → run that skill, or `/wow`;
  - you join a project to work on it → `/wow-join` (it can start with an assess).
- **Reads:** this page, `FLOWS.md`, and the "Steps" of every page the map opens. For an assess: the project's README, `CLAUDE.md`, its docs, its git history, its CI and deploy files.
- **Writes:** nothing in the project it assesses. The report goes in chat, or in a file where the user says.

## How the map works

| Level | What it is | Example | Where it comes from |
|---|---|---|---|
| 1. Stage | a phase of a product's life, with one question it answers | 4. Foundation: "can we build on it safely?" | this page |
| 2. Step | one piece of work inside a stage, usually one page and its skill | 4.2 Architecture | this page |
| 3. Component | one step of that page | 4.2.3 Context and containers | **the page itself**, read at every run |

Level 3 is never copied here. The pages change after every retro, and a copy would fall behind at the first one.

The order is the usual one, not a law. A stage can be skipped. The map then says what that skip breaks, so it's a choice and not an accident.

## The eight stages

| # | Stage | The question it answers | You leave it with |
|---|---|---|---|
| 1 | **Discover** | Is there a problem people pay to solve today? | the problem in their words, what they use now and what it costs |
| 2 | **Decide** | Do we build it, change it, or drop it? | one page with the buyer, the four risks and a dated decision |
| 3 | **Define** | What does the first version do, and what does it not do? | journeys, ranked requirements with criteria, numbers for speed and safety |
| 4 | **Foundation** | Can we build on it safely, from day one? | decisions written down, a repo with gates, a deploy that works, logs and an alert |
| 5 | **Plan** | In what order, and in what slices? | outcomes first, then slices with a time range |
| 6 | **Build** | Does each slice work, in production? | small, tested changes shipped one by one |
| 7 | **Launch** | Do the right people find it and pay? | a message, a price, a launch, the first paying customers |
| 8 | **Grow and run** | Is it getting better, and staying healthy? | a weekly number, fixed leaks, incidents that don't repeat |

After stage 8, the loop goes back to stage 5 every month (`FLOWS.md`, flow 2).

## Each stage, its steps

Every step names its page. The page's "Steps" are the components (level 3).

### 1. Discover
- **What it is:** finding out whether a problem is real, who has it, and what they do about it today.
- **Why:** building something nobody needs is the most common way a product fails. Discovery is the cheapest place to find out.
- **What it gives you:** a problem worth solving, chosen on evidence, not on enthusiasm.
- **Proof it's done:** the problem written as a job story; notes from at least five conversations about people's past; the alternatives, with their prices.
- **Skipped →** you build for an imagined user, and you learn it after months of work.

| Step | What it is | Why | Page |
|---|---|---|---|
| 1.1 Brainstorm | from a problem to many ideas, then 1–2 picked by score, with the riskiest assumption | you pick ideas by evidence, and you know what to test first | `brainstorm.md` |
| 1.2 Customer interviews | five people, asked about what they did, not about your idea | polite "I'd use it" answers hide what people really do and pay for | `interview.md` |
| 1.3 Market research | competitors, alternatives, prices, a size counted from the bottom up | you know who else solves it, for how much, and how many customers exist | `market-research.md` |

### 2. Decide
- **What it is:** one page that everyone agrees on, ending in go, change or drop.
- **Why:** months of work should start from a decision someone wrote down and can check later.
- **What it gives you:** the buyer named, the scope drawn, the four risks (value, usability, feasibility, viability) each with a test.
- **Proof it's done:** a brief with a dated decision; when demand is the open question, a signal such as pre-orders or a fake door.
- **Skipped →** the scope grows without limits, and nobody knows what "worked" would mean.

| Step | What it is | Why | Page |
|---|---|---|---|
| 2.1 Product brief | one page: problem and its cost, who must buy, alternatives, scope, the number, the risks, the decision | a shared, checkable reason to build | `product-brief.md` |
| 2.2 Experiment | a fake door or a pre-order while demand is unclear | proof that people act, not only say | `experiment.md` |

### 3. Define
- **What it is:** what the first version does, for whom, how you'll know each part works, and what it leaves out.
- **Why:** without a defined first version, "almost done" lasts forever.
- **What it gives you:** requirements you can test, a first version small enough to ship.
- **Proof it's done:** journeys; requirements ranked must / should / later, each with acceptance criteria; numbers for speed, availability and data; out of scope written.
- **Skipped →** every conversation re-opens the scope, and nothing is ever finished.

| Step | What it is | Why | Page |
|---|---|---|---|
| 3.1 PRD | goal and number, journeys, ranked requirements with criteria, non-functional numbers, out of scope, the first version | the contract between "why" and "how" | `prd.md` |

### 4. Foundation
- **What it is:** the decisions and the skeleton every feature will stand on: architecture, repository, quality gates, tests, a small design system, environments, a first deploy, logs and alerts.
- **Why:** the first shortcuts become the architecture, and deploy problems found in launch week are the most expensive ones.
- **What it gives you:** every feature starts on the same ground, and a change reaches production through checks.
- **Proof it's done:** ADRs; CI with required checks; a page in production deployed through the pipeline; logs, error tracking and one alert that fires; a definition of done; README says how to run and test.
- **Skipped →** each feature invents its own way, and the first incident is debugged blind.

| Step | What it is | Why | Page |
|---|---|---|---|
| 4.1 Problem, users, numbers | who uses it, how many, what must never break | the stack fits the real scale | `new-project.md` step 1 |
| 4.2 Architecture | the parts of the system, how they talk, what fails, who attacks, what it costs; the big choices as ADRs | the shortcuts of the first PRs don't become the architecture | `architecture.md` |
| 4.3 Repo and workflow | branches, PRs, commit messages, where a feature's files go | no debate at every change about where things go | `new-project.md` step 3 |
| 4.4 Quality gates in CI | lint, format, typecheck, tests, build, dependency and secret scans, required to merge | broken code never reaches main | `new-project.md` step 4 |
| 4.5 Test strategy | what each level tests: unit, integration, component, end to end | fast tests in the right place, none missing where it matters | `new-project.md` step 5 |
| 4.6 Design system | tokens and 4–5 base components | screens look and behave the same | `design-system.md` |
| 4.7 Environments and first deploy | the same build through every environment, secrets outside the code, a "hello" page live | deploy problems show up now, not at launch | `cloud.md`, `deploy.md` |
| 4.8 Observability | logs with a request id, error tracking, a health check, one alert, the runbook | you see a problem before users report it | `new-project.md` step 8 |
| 4.9 Definition of ready and done | when work can start, when it's finished | "done" means the same thing every time | `new-project.md` step 9 |
| 4.10 `CLAUDE.md` | stack, commands, conventions, what the AI must never do | the AI works by your rules | `new-project.md` step 10 |

### 5. Plan
- **What it is:** the order of the work for the next months, and each piece cut into slices that ship one by one.
- **Why:** value shipped often beats everything shipped at the end; an estimate you compare with reality gets better.
- **What it gives you:** Now / Next / Later tied to outcomes; slices with a time range and named risks.
- **Proof it's done:** a roadmap; a plan per feature or initiative with slices and ranges.
- **Skipped →** the loudest request wins, and dates are guesses nobody checks.

| Step | What it is | Why | Page |
|---|---|---|---|
| 5.1 Roadmap | outcomes first, candidates scored in one list, Now / Next / Later | the order follows the number you want to move | `roadmap.md` |
| 5.2 Plan | slices, a range for each, risks; milestones for an initiative | small, believable steps | `plan.md` |

### 6. Build
- **What it is:** one thin slice at a time: designed, tested, reviewed, shipped and measured.
- **Why:** small changes are easy to check and easy to undo.
- **What it gives you:** steady progress in production, with tests that keep it working.
- **Proof it's done:** merged PRs that reached production; a test per acceptance criterion; the slice's number measured.
- **Skipped →** big, risky releases, bugs found by users.

| Step | What it is | Why | Page |
|---|---|---|---|
| 6.1 Feature | problem → criteria → UI and technical design → tests → thinnest slice → ship and measure | the main loop of building | `feature.md` |
| 6.2 UI design | the user's steps, every state of every screen | users don't find the missing states | `ui-design.md` |
| 6.3 API design | the contract first, who is allowed, how it changes without breaking | both sides agree before coding | `api-design.md` |
| 6.4 Data model | tables that keep bad data out, an index per query, a migration plan | the database stays correct and fast | `data-model.md` |
| 6.5 TDD | a failing test, the code that passes it, a clean up | the code does what the test says, nothing more | `tdd.md` |
| 6.6 Pull request | review your own diff, a description with proof and risk | reviewers check the right things | `pr.md` |
| 6.7 Code review | did it do what was asked; does it follow the standards | a second pair of eyes, two separate passes | `review.md` |
| 6.8 Deploy | one build everywhere, watch, roll back fast | shipping is routine, not an event | `deploy.md` |
| As needed | an outside service, an LLM feature, a bug, a refactor, a migration, an upgrade, AI-written code | each has its own risks | `integration.md`, `ai-feature.md`, `bug.md`, `refactor.md`, `migration.md`, `upgrade.md`, `brief.md` |

### 7. Launch
- **What it is:** deciding who it's for and why it's their best choice, setting the price, putting it in front of people, selling.
- **Why:** a product nobody hears about has no users, however good it is.
- **What it gives you:** the first paying customers, and which channel brought them.
- **Proof it's done:** a written positioning; a published price that can be paid; a launch with results per channel; a first payment.
- **Skipped →** a working product with no users, and no idea why.

| Step | What it is | Why | Page |
|---|---|---|---|
| 7.1 Positioning | alternatives, what only you have, best-fit customers, the message | people understand it in five seconds | `positioning.md` |
| 7.2 Pricing | what they pay for, floor and ceiling, the model, taxes | a price above costs that people accept | `pricing.md` |
| 7.3 Launch | ready to sell, landing page, audience, channels, launch week | the first customers, measured by channel | `launch.md` |
| 7.4 Sales | when you sell in conversations: who, first message, discovery call, demo, close | business customers buy from people | `sales.md` |

### 8. Grow and run
- **What it is:** measuring, improving what leaks most, and keeping the product healthy.
- **Why:** a live product gets worse on its own: bugs pile up, dependencies age, users leave quietly.
- **What it gives you:** decisions from numbers, incidents that don't repeat, areas checked before they fail.
- **Proof it's done:** a weekly review of the funnel; monthly product reviews; postmortems; dated audit reports; retros.
- **Skipped →** you find out from the churn numbers, too late.

| Step | What it is | Why | Page |
|---|---|---|---|
| 8.1 Growth | the funnel, one number per step, channels, an experiment backlog, a weekly review | fix the leakiest step first | `growth.md` |
| 8.2 Product review | the outcome, the numbers, what users say, 1–3 picks | the next improvement has evidence | `product-review.md` |
| 8.3 Experiment | proof that a change moved a number | not noise | `experiment.md` |
| 8.4 Incident | stop the damage, communicate, fix, postmortem | users are hurt as little as possible, once | `incident.md` |
| 8.5 Audit | one area checked: security, accessibility, performance and others | problems found before users find them | `audit.md` |
| 8.6 Retro | the pages, the estimate, the impact log | every task improves the next | `retro.md` |

### Side tools, any stage
Not stages: tools you pick up when a situation needs them.

| Tool | When | Page |
|---|---|---|
| Grill | a problem or decision has no clear answer | `grill.md` |
| Research | the docs can answer it | `research.md` |
| Spike | only building can answer it | `spike.md` |
| Design doc | big and hard to undo | `design-doc.md` |
| Comms | someone must know or decide | `comms.md` |
| Explain again | a concept doesn't land | `explain-again.md` |
| Join, repo tour, handoff, mentor | arriving, understanding, leaving, teaching | `join.md`, `repo-tour.md`, `handoff.md`, `mentor.md` |
| What is in front of me | not sure which page fits | `wow.md` |

## Map mode
1. **The level asked for:**
   - no argument: the eight stages;
   - a stage: its "what, why, gives, proof, skipped" and its steps;
   - a stage and a step: the step's components, read now from the "Steps" of its page. Each component gets what it is, why, and what breaks without it, from the page's text.
2. **A picture** of that level, drawn as the "Diagrams" rule in `SKILLS.md` says.
3. **If a project is open,** mark where it is on the picture, from the last assess or by asking.

## Assess mode
1. **The project:** the folder or repo, and what the user already knows about it.
   - STOP: confirm the folder and whether any part is off limits.
2. **Read without changing anything:**
   - README, `CLAUDE.md`, the docs folder and any brief, PRD, ADRs, roadmap, plans, runbook, postmortems, audits;
   - the git history: first and last commit, how often it ships, open branches;
   - CI config, deploy files, infrastructure files, health checks, error tracking setup;
   - for stages 7–8, ask: price, paying customers, metrics. They often live outside the repo.
3. **Each stage, against its "Proof it's done":**
   - done, partial or missing;
   - the evidence for each: a file and line, a commit, or "the user said";
   - for Foundation and Build, go one level deeper, to the steps (4.1–4.10, 6.1–6.8).
4. **The stage:** the furthest stage with work in progress.
5. **The gaps behind it:** every earlier stage that is partial or missing, with its "Skipped →" line. Ordered by what they risk now.
6. **The report**, in this shape:

```markdown
## <project> · stage <n> of 8: <stage> · <date>
| Stage | Status | Evidence | If it stays this way |
|---|---|---|---|
| 1. Discover | partial | market research in docs/…; no interviews | … |
| … | | | |
**Next step:** <from FLOWS.md> · **Gap to close first:** <one, with why>
```

   - STOP: the user picks: continue at the current stage, close a gap first, or stop here.

## Done when
- [ ] map: the level asked for is shown with what, why and what it gives, and level 3 was read from the page, not from memory
- [ ] assess: every stage has a status with evidence, the gaps are ordered, and the next step is named from `FLOWS.md`

## Concepts if you get stuck
- Product discovery and the four risks
- The software lifecycle
- What "done" means at each stage

## Next level
- `staff` Assess every project you own once a quarter; a stage that stalls three quarters is a decision to make, not a backlog.

## Next
The step the report names, through its skill. End with `/wow-retro`.

## Changelog
- 2026-10-08: v1, from Florin's request on Sated: the whole road in three levels, and a way to place an existing project on it.
