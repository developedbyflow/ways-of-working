# Coverage check

Checked on 2026-10-05 against six sources, so the list does not depend on memory. Every row says which skill covers it. The rows marked "out" say when they come in.

## Sources
1. The work from start to finish (the lifecycle).
2. My Career Tracker framework: 15 focus areas, 172 competences.
3. My tracks: Backend 00–17, Frontend F00–F23, System Design S00–S19, C# C0–C9.
4. [SWEBOK v4](https://www.computer.org/education/bodies-of-knowledge/software-engineering) (IEEE): the 18 knowledge areas of software engineering.
5. [DORA capabilities](https://dora.dev/capabilities/).
6. [Matt Pocock's skills](https://github.com/mattpocock/skills): 27 skills.

## 1. Lifecycle

| Stage | Covered by |
|---|---|
| Arrive on a project, new or existing | new-project, join, repo-tour |
| Understand the problem | feature (steps 1–2), grill |
| Decide | grill, research, spike |
| Design | architecture, data-model, api-design, ui-design, design-system, integration, ai-feature, design-doc |
| Plan | plan |
| Build | feature, tdd, brief, bug, refactor |
| Check | review, pr, audit |
| Release | deploy, cloud, migration, upgrade |
| Learn from users | experiment, feature (step 7) |
| Operate | incident, audit production-readiness |
| Communicate | comms |
| Grow others | mentor |
| Remove a feature | feature ("Removing a feature") |
| Leave | handoff |
| Grow myself | retro (task, week, quarter), explain-again |

## 2. Career Tracker

| Focus area | Covered by |
|---|---|
| Delivery & Execution | feature, plan, pr, deploy; definition of ready and done set by new-project |
| Observability & Production Operations | new-project, audit production-readiness, incident, runbook |
| Performance Engineering | audit performance, bug (the slow path) |
| Reliability & Resilience | integration (timeouts, retries, fallback), audit production-readiness, deploy (rollback rehearsal) |
| Security & Privacy | audit security, audit privacy, architecture (threat model), review, incident (security incident) |
| Architecture & Technical Direction | architecture, design-doc, grill, research, audit architecture, refactor |
| Data Layer & API Contracts | data-model, api-design, migration |
| Testing Strategy & Quality Engineering | tdd, new-project (test strategy), audit testing |
| Design System & UI Governance | design-system |
| Accessibility as a System | ui-design, design-system, audit accessibility |
| SEO & Discoverability | audit seo, architecture (rendering strategy) |
| UX & Product Thinking | ui-design, feature, experiment, audit ux, audit analytics |
| Developer Experience & Tooling | new-project, audit dx |
| Team Leadership & Influence | comms, mentor, review, design-doc |
| Platform/Infra Awareness | cloud, architecture, audit performance (caching) |

The competences that changed the list:

| Competence | Change |
|---|---|
| Risk register, Tech debt register | two shared files: `docs/risks.md`, `docs/tech-debt.md` |
| Delivery tracking & learning loop | plan writes down the estimate, retro compares it with the actual |
| Stakeholder updates, Exec-ready proposals, Pre-wire, Facilitating decisions, De-escalation | new skill: comms |
| Mentoring & feedback loops | new skill: mentor |
| Tokens, Component API, Semver + deprecations, Contribution model | new skill: design-system |
| Experiment doc: metric, guardrails, stop conditions | new skill: experiment |
| Technology evaluation framework | research: performance, DX, ecosystem, risk, cost, license |
| Migration strategy | migration also covers moving to a new library or framework, step by step |
| FE threat model | architecture and design-doc get a threat-model step |
| Timeout + retry policy, Degrade strategy | integration |
| CI timing, build cache, Renovate config, repo template | audit dx; new-project creates the feature template |
| Formatting dates, numbers and time zones; RTL-safe CSS | audit ux, section "Language and formats" |
| Rollback rehearsal | deploy, audit production-readiness |
| Release management | deploy (release notes) |
| Consent gating for analytics, event taxonomy | audit analytics, audit privacy; `docs/tracking-plan.md` |

## 3. Tracks

| Module | Used by |
|---|---|
| Backend 00 request on the web | bug (network), repo-tour |
| Backend 01 OOP and C#, C# C0–C9 | tdd, review, refactor |
| Backend 02 anatomy of a backend | repo-tour, architecture |
| Backend 03 REST API design | api-design, integration |
| Backend 04 databases | data-model, migration, bug |
| Backend 05 security | audit security, review, architecture |
| Backend 06 testing | tdd, audit testing |
| Backend 07 performance | audit performance, bug |
| Backend 08 infra, deploy, observability | deploy, cloud, incident, audit production-readiness |
| Backend 09 principles and patterns | refactor, review, architecture |
| Backend 10 concurrency | bug, data-model, review |
| Backend 11 application architectures | architecture |
| Backend 12 communication between systems | integration, architecture |
| Backend 13 scaling and distributed systems | architecture, audit performance |
| Backend 14 cloud on AWS | cloud, audit cost |
| Backend 15 system design | architecture, design-doc |
| Backend 16 algorithms for live coding | out: interview prep |
| Backend 17 AI in the backend | ai-feature |
| F00 browser, F05 React internals | bug, audit performance |
| F01 JavaScript, F02 TypeScript, F06 components and hooks | tdd, review, refactor |
| F03 HTML and CSS | ui-design, design-system |
| F04 accessibility | ui-design, audit accessibility |
| F07 application state, F08 server data | architecture (frontend), api-design, feature |
| F09 server rendering and Next.js | architecture (rendering), audit seo |
| F10 testing | tdd, audit testing |
| F11 tooling, build, deploy | new-project, deploy, audit dx |
| F12 web performance | audit performance |
| F13 browser security | audit security, review |
| F14 architecture at scale, F18 frontend system design | architecture, audit architecture |
| F15 design system | design-system |
| F16 the frontend in production | incident, deploy (flags), audit production-readiness |
| F17 technical leadership | comms, mentor, review |
| F19 coding round | out: interview prep |
| F20 AI in the frontend | ai-feature, brief |
| F21 UX | ui-design, audit ux |
| F22 SEO | audit seo |
| F23 product-minded engineer | feature, experiment, plan, audit analytics |
| S00 numbers, S01 requirements and trade-offs | architecture, plan |
| S02 building blocks, S03–S08 storage, replication, partitioning, consistency, correctness, data in motion | architecture, data-model, integration |
| S09 reliability | audit production-readiness, incident, architecture |
| S10 scaling in practice | architecture, audit performance, audit cost |
| S11 security, multi-tenancy, cost | audit security, audit cost, architecture |
| S12 read-heavy, S13 real-time, S14 money and bookings | architecture |
| S15 infrastructure as design | cloud |
| S16 AI systems | ai-feature |
| S17 design in the real world | design-doc, migration |
| S18 system design interview | out: interview prep |
| S19 staff and beyond | plan (initiatives), comms, mentor, design-doc |

Every module is used by at least one skill, except the three interview modules.

## 4. SWEBOK v4

| Knowledge area | Covered by |
|---|---|
| Requirements | feature (steps 1–2), grill, ui-design, architecture (non-functional requirements) |
| Architecture | architecture, design-doc, audit architecture |
| Design | data-model, api-design, ui-design, design-system, integration, ai-feature |
| Construction | tdd, feature, brief, refactor |
| Testing | tdd, new-project (test strategy), audit testing |
| Engineering Operations | deploy, cloud, incident, audit production-readiness |
| Maintenance | bug, refactor, upgrade, migration, feature (removing a feature) |
| Configuration Management | new-project (branching, CI), pr, deploy (versions, release notes), upgrade (lockfile) |
| Engineering Management | plan, comms, retro (estimate vs actual) |
| Engineering Process | this repo and retro |
| Models and Methods | the diagrams in architecture, data-model, repo-tour |
| Quality | review, audit, definition of done |
| Security | audit security, audit privacy, architecture (threat model), incident |
| Professional Practice | comms, mentor, handoff, grill |
| Economics | plan (cost of delay), research (build vs buy), audit cost, ai-feature (cost) |
| Computing, Mathematical and Engineering Foundations | the tracks (the knowledge layer, not a situation) |

## 5. DORA

| Capability | Covered by |
|---|---|
| Version control, trunk-based development, continuous integration | new-project, pr |
| Deployment automation, continuous delivery | deploy |
| Test automation, test data management | tdd, new-project (test strategy), audit testing |
| Database change management | migration |
| Monitoring and observability, proactive failure notification | new-project, audit production-readiness |
| Pervasive security | audit security, review, architecture (threat model) |
| Code maintainability | audit architecture, refactor |
| Documentation quality | repo-tour, ADRs, handoff, audit dx |
| Working in small batches | feature (thin slice), plan, pr |
| Streamlining change approval | review, pr |
| Flexible infrastructure | cloud |
| Customer feedback | wow (incoming feedback), feature (step 1) |
| Monitoring systems to inform business decisions | feature (the number), audit analytics |
| Team experimentation | experiment, spike |
| Visibility of work, work in process limits, visual management | plan, retro (week) |
| Platform engineering, empowering teams to choose tools | audit dx, research |
| AI-accessible internal data | `REPO-MAP.md`, `GLOSSARY.md`, `CLAUDE.md` |
| Clear and communicated AI stance | brief (what the AI may do, what data it never gets) |
| User-centric focus | feature, ui-design, audit ux |
| Healthy data ecosystems | data-model, audit privacy |
| Well-being, job satisfaction | rule: no streaks, no scores |
| Generative culture, learning culture, loosely coupled teams, transformational leadership | team culture, not a skill; blameless postmortems (incident) and retro support it |

## 6. Matt Pocock's skills

| His skill | Ours |
|---|---|
| grill-me, grilling | grill |
| grill-with-docs, domain-modeling | grill and data-model (`GLOSSARY.md`, ADRs) |
| to-questionnaire | grill (questions only someone else can answer) |
| research | research |
| prototype | spike |
| diagnosing-bugs | bug (hard bugs) |
| tdd | tdd |
| code-review | review |
| pr | pr |
| to-tickets | plan |
| wayfinder | plan (initiative) |
| triage | wow (a list of incoming items) |
| codebase-design | architecture, refactor, review |
| improve-codebase-architecture | audit architecture, then refactor |
| wizard | deploy, cloud, migration (the steps only I can do) |
| handoff | handoff |
| wait-what | explain-again |
| teach | the tracks and explain-again |
| retro | retro |
| ask-matt | wow |
| writing-for-agents | the guide I use to write the skills |
| setup-matt-pocock-skills | new-project and join create the shared files |
| to-spec | feature (steps 1–2) |
| implement, implement-spec | not taken: the agent builds alone; ours is tdd and brief, with me in the loop |

## 7. Out for now, and when it comes in

| Out | Comes in when |
|---|---|
| Interview prep (Backend 16, F19, S18) | it stays in the interview playbooks and the Career Tracker; retro (quarter) feeds them |
| Hiring: interviewing candidates | I join an interview loop |
| On-call rotation | I join one; until then, incident covers a single responder |
| Docs website | the docs outgrow README and `docs/` |
| Native mobile | I build a native app |
| Team culture | it is not a skill; blameless postmortems and retro support it |

## 8. What this check changed
- **New skills:** tdd, integration, ai-feature, design-system, experiment, comms, mentor. Plus architecture, data-model, api-design and ui-design, from the design gap.
- **Merged:**
  - estimate becomes plan, for one feature or a whole initiative;
  - triage goes into wow;
  - the weekly and quarterly reviews go into retro.
- **New audit areas:** analytics, testing, dx. Added before this check: privacy, architecture.
- **New shared files:** `docs/risks.md`, `docs/tech-debt.md`, `docs/tracking-plan.md`, `docs/experiments/`, the definition of ready and done.
- **Page changes:**

  | Page | What it gets |
  |---|---|
  | feature | removing a feature; the LLM part moves to ai-feature |
  | migration | moving to a new library or framework; one-off data fixes |
  | incident | security incidents |
  | research | evaluation criteria; build vs buy |
  | deploy | release notes; rollback rehearsal |
  | architecture, design-doc | a threat-model step |
  | new-project | definition of ready and done; CI gates; the feature template |
