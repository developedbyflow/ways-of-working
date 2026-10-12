---
name: compliance
description: "What the law requires, turned into product decisions before the code. The record of processing (what data, why, legal basis, where, who, how long), consent and minimum age, the providers' data processing agreements and transfers outside the EU, retention, the user's rights as mechanisms (export, delete, correct), a short DPIA, the other laws (cookies, consumer law, medical devices, the AI Act, accessibility, data licences, the legal entity), a breach plan and the drafts of the privacy policy and terms. Writes a folder with a README and one file per topic, and the new requirements into the PRD. Use right after system design, and again before launch as a checklist; at work before a feature that collects personal data, a new provider or a new market. Also judges an existing one: /compliance validate <folder>."
argument-hint: "[the product or the feature] or validate <folder>"
---

# Compliance

## When to use it
Right after System design, before Architecture, the data model, the API and the screens. It needs the providers and the data map from the system design, and what it decides changes the tables (consent records, retention), the API (export, deletion) and the screens (consent, age, disclaimers).

Run it **a second time before launch**, as a checklist: everything decided here exists and works.

At work: before a feature that collects personal data, a new provider, or a new country to sell in.

## The problem it solves
An app that works perfectly can still be illegal: health data collected without the right consent, a provider without a contract, data kept forever, no way to delete an account. GDPR fines reach 4% of turnover or €20 million, but for a small product the real problem comes earlier: a complaint, a large customer asking for proof, or a payment provider that won't approve the account without a privacy policy and terms.

Compliance says **what you're obliged to do** and turns each obligation into a product decision, while there's no code yet to redo.

## How to run it
- **The bar:** do what a well-prepared founder, CTO or the data protection lead at a well-run company would accept, in the simplest form that meets it. Use the real method and its real names (record of processing, legal basis, DPIA) and explain each one, so the user learns it. Say what you leave out and why.
- **Not legal advice.** You make the map, the decisions and the drafts; say once, plainly, that a lawyer should check them when the stakes are high (health data, children, finance), and propose a one-hour review before launch. Never present a draft as final legal text.
- **Teach while you go:** every term gets one line on what it is and what it brings, compared with something the user knows (a frontend developer knows the cookie banner, the privacy link in the footer, the "I agree" checkbox; compliance is everything behind them). Compliance is what the law and the contracts require; security (07) is how you defend against someone who wants to do harm. They meet in one place: GDPR requires "appropriate security"; compliance says you must, security says how.
- **Where the documents are:** the `Project documents:` line in `CLAUDE.md` gives the documents folder; without it, use `docs/` in the current folder. Write into `docs/02-design/02-compliance/`, and decisions that are hard to undo into `docs/00-project/adr/`; create them if they don't exist.
- **Read first:** the system design (`docs/02-design/01-system-design/`: the data, the providers, the flows, the open questions marked "02 Compliance"), the PRD (the GDPR and operations requirements, the open decisions), the brief (where you sell, the price, the business model), and the running app if there is one (what it already stores, its sign-up screen, its privacy page). Ask only what's missing: the countries you sell in, the legal entity, the age of the users.
- **The user decides** every legal basis, every retention period and every new requirement. You give the options and a recommendation; they choose. One decision at a time.
- **New requirements go into the PRD,** with a journal line, after the user says yes: a consent screen, an export button, a deletion job.
- **Collect less before you protect more.** For each piece of data, first ask whether you need it at all; data you don't keep can't leak, be requested or be fined (data minimisation).

## The laws and rules
Use this list at step 8. Name the ones that apply; for each one you name, one line on what it asks.

| What | What it asks, in plain words | Usually applies when |
|---|---|---|
| **GDPR** (EU General Data Protection Regulation) | a legal basis for every use of personal data, only the data you need, kept only as long as needed, protected, and the person has rights over it | any personal data of people in the EU |
| **Special category data** (GDPR, article 9) | health, religion, ethnicity, sexual life, biometrics…: forbidden unless an exception applies; for apps, usually **explicit consent** | weight, food logs, symptoms, menstrual data, mood |
| **ePrivacy** (the cookie rule) | anything stored on the user's device (cookies, local storage) needs consent, except what's strictly necessary for the service they asked for | analytics or ad cookies, trackers |
| **Consumer law** (EU) | clear terms, prices with VAT, a 14-day withdrawal right for distance sales (digital services started at once have their own rules), no unfair terms | selling to consumers |
| **Medical devices** (MDR, EU) | software meant to diagnose, prevent or treat a disease is a medical device, with costly certification | health and nutrition apps that give advice or claims |
| **AI Act** (EU) | duties by risk; for ordinary apps: transparency (people know what the AI made); the heavy duties sit with the model provider | AI that talks to users or generates content |
| **Accessibility** (European Accessibility Act) | from June 2025, online shops and services must be accessible; micro-enterprises providing services are exempt | selling online in the EU |
| **Data licences** | data taken from others comes with rules: attribution, share-alike (what you derive, you publish under the same licence) | open datasets, scraped or imported data |
| **Children** (GDPR, article 8) | online consent from a child needs a parent below an age set by each country (16 by default, 13–16 by country) | apps young people may use |
| **Tax and the legal entity** | who sells, who charges and pays VAT, which entity receives the money | any paid product |
| **Sector rules** | finance, health care, education, employment add their own | when the product sits in one of them |

## The GDPR terms
| Term | What it is |
|---|---|
| **Controller** | who decides why and how the data is used: the product's owner |
| **Processor** | who processes the data on the controller's behalf: the hosting, the email, the AI provider |
| **DPA** (data processing agreement) | the contract required with every processor: what it does with the data, where, for how long, its sub-processors |
| **Legal basis** | the reason the law accepts: contract, consent, legal obligation, legitimate interest (vital interest and public task rarely apply) |
| **Record of processing** (RoPA, article 30) | the table of every processing: what, why, basis, where, who, how long; required as soon as special category data is processed, however small you are |
| **DPIA** (data protection impact assessment, article 35) | a written analysis of the risks to people, required when processing is likely high-risk (for example health data at scale) |
| **Data subject rights** | access, correction, deletion, portability (export), objection, withdrawing consent; answered within one month |
| **Transfers outside the EU** | allowed to countries with an EU adequacy decision, or with standard contractual clauses; the US through the Data Privacy Framework for certified companies |
| **Personal data breach** | data leaked, lost or seen by the wrong people: tell the supervisory authority within 72 hours, and the people affected when the risk is high |
| **Privacy by design** (article 25) | data protection built into the design from the start, not added at the end |
| **DPO** (data protection officer) | required when the core activity is large-scale special category processing or monitoring; usually not for a small product, revisit at scale |

## Steps

### 1. Read what exists
The system design's data map, providers, flows and open questions; the PRD's GDPR and operations requirements; the brief. **The running app too:** its data model (preferences, reports, soft-deleted rows, invites and display names slip out of the documents) and what it does in production today (providers, open sign-up). If it's public with real users, whatever isn't compliant is urgent: say so first. List what's missing (countries, legal entity, users' age) and ask only that.

### 2. The record of processing
One row per purpose, not per table: what data, **why** (the purpose), **the legal basis**, special category or not, where it lives, which processors touch it, **how long** it's kept. Start from the system design's data map and add the legal columns; then check it against the running app's tables. Each AI feature is its own row, with exactly what it sends (a recipe generator may send remaining calories and preferences, not only a photo).

| Example | Purpose | Legal basis | Special | Where | Processors | Kept |
|---|---|---|---|---|---|---|
| account email and password | the account, login | contract | no | database (EU) | hosting, email | while the account exists |
| weight and food log | tracking progress | explicit consent | **health** | phone, database (EU) | hosting, AI (photo only) | while the account exists |

### 3. Consent and age
- Which consents, when, with what text; separate, not pre-ticked, as easy to withdraw as to give.
- **What's recorded as proof:** who, what was accepted, which version of the text, when; withdrawing is recorded the same way.
- What happens when consent is refused or withdrawn (for health data in a health app, usually: the feature can't work, say so honestly, offer deletion).
- **Purposes the app doesn't need** (usage metrics, measuring the AI's accuracy, improving the product) get their own **optional**, unticked box; bundled into the required one, the required consent isn't freely given. The required box's text names every use, the AI features and support included.
- The minimum age, and how the app asks for it: **before the account exists**, so "nothing kept" is true.

### 4. The providers
For each processor: the DPA (signed or accepted in the account), where the data goes, the transfer basis outside the EU, whether it trains on your data, what it keeps and for how long, its sub-processors. **Check the company's country, not only the data region:** a US company storing in the EU still needs a transfer basis. A merchant of record is a separate controller: write what you send it, and tell it when an account is deleted (article 19). The list of processors is published for users (in the privacy policy). A provider that can't meet the requirements is replaced now, not after launch.

### 5. Retention
A period for every kind of data, and **what deletes it** (a job, a provider setting, a backup that ages out), never "someone remembers". Include backups, logs, exports, payment events (accounting law usually asks years for invoices; the merchant of record may keep them for you).
- **Soft-deleted rows** lose their values at once; keep only the marker other devices need.
- **A backup restore brings deleted accounts back:** keep the deleted ids as long as the oldest backup and run the deletions again after any restore.
- **A minimal proof** (consents, requests answered), without the special category data, may stay after deletion for the limitation period, to answer a complaint (article 17(3)(e)).

### 6. The rights, as mechanisms
For each right: where the user triggers it, what happens behind it, how long it takes, how you prove it was done. Export (a machine-readable file), deletion (database, files, providers, backups within their retention), correction, withdrawing consent, access ("what do you have about me?"). Each becomes a requirement for the data model, the API and the screens.

### 7. The DPIA, short
For high-risk processing: what could hurt people (someone sees another's health data, data leaves the EU, a breach), how likely and how bad, and what reduces it. Decide whether it's required and write why; when in doubt with health data, write the short version anyway.

### 8. The other laws
Go through the table above; for each one that applies, the decision (selling in the UK or the US adds the UK GDPR and Children's Code, the ICO, and the US state health data and breach laws): cookies (banner or not, and why), consumer law (terms, withdrawal, prices), medical devices (what the app must never claim; the wording of every health-related text), the AI Act (what's marked as made by AI), accessibility, data licences (attribution, what must be published), the legal entity and tax.

### 9. The breach plan
What to do in the first 72 hours if data leaks: how you'd notice, who decides, what you check, whom you tell (the supervisory authority, the people affected, the processors), with which text. One page, written now, not during the incident.

### 10. The documents before launch
Drafts of the privacy policy (what, why, basis, where, who, how long, rights, contact), the terms, the list of processors, the consent texts. Written for the user's reading level, in every language the app supports. Marked as drafts until a lawyer checks them. An accessibility statement says "aims to conform" until a full check. Any new promise in the terms (notice periods, refunds) is shown to the user before it's written, and goes into the PRD.

### 11. What changes in the design
The list of new requirements, each with where it lands (PRD, data model, API, screens); on the user's yes, into the PRD with a journal line. Hard-to-undo choices (the legal basis for health data, a provider replaced) become ADRs, one at a time, chosen by the user.

### 12. Check it
- every kind of data has a purpose, a legal basis, a place and a retention period with a mechanism;
- every processor has a DPA and a transfer basis;
- every right has a mechanism and a deadline;
- every health-related text stays clear of medical claims;
- before launch, run again as a checklist: each item exists and works. Nobody at hand? `/compliance validate <folder>`.

Write as you go: each step's file once the user confirms it, with a journal line in the README. At the end, set this step's row in `docs/02-design/README.md` (the map of the Design steps) to done, with the date, and link the folder.

```
docs/02-design/02-compliance/
  README.md              status, summary, the laws that apply, open questions, the lawyer review, journal
  01-record.md           the record of processing
  02-consent.md          consents, the proof recorded, the minimum age
  03-processors.md       DPAs, transfers, training, what each keeps
  04-retention.md        periods and what deletes the data
  05-rights.md           each right as a mechanism
  06-dpia.md             the short impact assessment
  07-other-laws.md       cookies, consumer, medical devices, AI Act, accessibility, licences, entity
  08-breach-plan.md      the first 72 hours
  drafts/                privacy policy, terms, consent texts (drafts until checked)
```

The README:

````markdown
# Compliance – [Product]
| | |
|---|---|
| **Status** | draft / confirmed by [who], [date] / checked by a lawyer on [date] |
| **Controller** | [legal entity, country] |
| **Updated** | |
| **Next** | 03 Architecture; again before launch, as a checklist |
## In one page
What data, the special categories, the legal bases, where it lives, the rights offered, what changes in the product: 5–6 lines.
## The laws that apply
| Law | Applies | What it means here |
## The files
| File | What it answers |
## Open questions
| Question | Answered by | When |
## Before launch
- [ ] each item that must exist and work
## Glossary
- **Term:** what it is, compared with something the reader already knows
## Journal
- [date]: [what was decided, by whom, what it changed]
````

## Validate mode
`/compliance validate <folder>`: judge an existing compliance folder, change nothing.
1. Read the folder, its ADRs, the system design's data and providers, the PRD and the running app's privacy texts if any.
2. Check the template and "Done when" item by item, citing the lines.
3. Then ask: does every kind of data in the system design appear in the record? Does every purpose have a basis that fits (no "legitimate interest" for health data)? Is consent for special category data explicit, separate and recorded? Does every processor have a DPA, a transfer basis and a known retention? Does every right have a mechanism that reaches the backups and the providers? Does any text read like a medical claim? Is every new requirement in the PRD? Does the record match the running app's tables? Is any non-essential purpose bundled into a required consent? Does every provider's company country have a transfer basis? Do deletions survive a backup restore?
4. Report: findings by severity, each with the line, what's wrong and what to change; then what's done well; then what needs a lawyer. The user picks what to apply.

## The bad version and why not
- A privacy policy copied from another app: it describes other data and other providers, so it's worse than none, because it's false.
- One "I agree to everything" checkbox, already ticked: consent for health data isn't valid.
- No retention periods: data stays forever, and a "deleted" account lives on in backups for years.
- Compliance left to the end: the export button, the consent table and deletion from backups get added to finished code, at many times the cost.
- Marketing that promises medical results ("lowers your blood sugar"): the app can become a medical device.
- "We're too small for GDPR": the size exemptions don't cover special category data.

## What breaks if you skip it
The payment provider won't approve the account without a privacy policy and terms. The first user who asks "what data do you have about me?" doesn't get an answer within the month the law gives. A leak finds you without a plan, and 72 hours pass fast. Health data collected without explicit consent can't be fixed afterwards: you must ask everyone again.

## The principle behind it
Privacy by design: collect only what you need, know why you have it, keep it only as long as needed, and be able to show it or delete it at any time. Data you don't collect can't be lost, stolen or requested.

## How to apply it at work
Before a feature with personal data, ask: which data, why, on what basis, at which provider, for how long, how does the person delete it. If the company has a DPO, bring them in at design, not at the final review. Before a new provider, ask for its DPA and its list of sub-processors.

## Done when
- [ ] every kind of data in the system design and in the running app's tables is in the record, with purpose, basis, place, processors and retention; each AI feature with what it sends
- [ ] special category data has explicit, separate consent, recorded with the text version and the time; non-essential purposes in their own optional box
- [ ] the minimum age decided, asked before the account exists
- [ ] every processor with a DPA, a transfer basis (by the company's country, not only the data region), training and retention known
- [ ] every retention period has a mechanism that deletes, backups included; deletions re-run after a restore
- [ ] every right is a mechanism with a deadline
- [ ] the DPIA written, or why it isn't required
- [ ] the other laws gone through, each with a decision
- [ ] the breach plan, one page
- [ ] drafts of the privacy policy, terms and consent texts, marked as drafts
- [ ] the new requirements in the PRD, with journal lines; the hard-to-undo choices as ADRs, chosen by the user
- [ ] a lawyer review proposed for before launch
- [ ] a glossary for every term

## Next
Architecture (`/architecture`): it takes the requirements from here (consent records, export and deletion jobs, retention) into the modules. Before launch: `/compliance` again, as a checklist.
