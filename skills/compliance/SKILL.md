---
name: compliance
description: "What the law requires, turned into product decisions before the code. The record of processing (what data, why, legal basis, where, who, how long), consent and minimum age, the providers' data processing agreements and transfers outside the EU, retention, the user's rights as mechanisms (export, delete, correct), a short DPIA, the other laws (cookies, consumer law, medical devices, the AI Act, accessibility, data licences, the legal entity, the site's legal notice, the Digital Services Act, the Cyber Resilience Act, other countries), a breach plan with its register, and the public texts as drafts (privacy policy, terms, consent texts, accessibility statement, breach notifications) with the questions for a lawyer. Writes a folder with a README, one file per topic and a public-texts/ folder, and the new requirements into the PRD. Use right after system design, and again before launch as a checklist; at work before a feature that collects personal data, a new provider or a new market. Also judges an existing one: /compliance validate <folder>."
argument-hint: "[the product or the feature] or validate <folder>"
---

# Compliance

## When to use it
Right after System design, before Architecture, the data model, the API and the screens. It needs the providers and the data map from the system design, and what it decides changes the tables (consent records, retention), the API (export, deletion) and the screens (consent, age, disclaimers).

Run it **a second time before launch**, as a checklist: everything decided here exists and works.

The later steps come back here: when the architecture, the data model, the API, the screens, security or the AI design change what's stored, kept, sent or told, the change lands in this folder in the same commit, with a journal line naming the step it came from.

At work: before a feature that collects personal data, a new provider, or a new country to sell in.

## The problem it solves
An app that works perfectly can still be illegal: health data collected without the right consent, a provider without a contract, data kept forever, no way to delete an account. GDPR fines reach 4% of turnover or €20 million, but for a small product the real problem comes earlier: a complaint, a large customer asking for proof, or a payment provider that won't approve the account without a privacy policy and terms.

Compliance says **what you're obliged to do** and turns each obligation into a product decision, while there's no code yet to redo.

## How to run it
- **The bar:** do what a well-prepared founder, CTO or the data protection lead at a well-run company would accept, in the simplest form that meets it. Use the real method and its real names (record of processing, legal basis, DPIA) and explain each one, so the user learns it. Say what you leave out and why.
- **Not legal advice.** You make the map, the decisions and the drafts; say once, plainly, that a lawyer should check them when the stakes are high (health data, children, finance), and propose a one-hour review before launch. Never present a draft as final legal text. **Every point the files can't settle becomes a numbered question in the README's "For the lawyer"**, and the file that raises it names it ("the lawyer's question 3"); a later step that finds a new one adds it, dated, so the hour goes to the real doubts.
- **Teach while you go:** every term gets one line on what it is and what it brings, compared with something the user knows (a frontend developer knows the cookie banner, the privacy link in the footer, the "I agree" checkbox; compliance is everything behind them). Compliance is what the law and the contracts require; security (07) is how you defend against someone who wants to do harm. They meet in one place: GDPR requires "appropriate security"; compliance says you must, security says how.
- **Where the documents are:** the `Project documents:` line in `CLAUDE.md` gives the documents folder; without it, use `docs/` in the current folder. Write into `docs/02-design/02-compliance/`, and decisions that are hard to undo into `docs/00-project/adr/`; create them if they don't exist.
- **Read first:** the system design (`docs/02-design/01-system-design/`: the data, the providers, the flows, the open questions marked "02 Compliance"), the PRD (the GDPR and operations requirements, the open decisions), the brief (where you sell, the price, the business model), and the running app if there is one (what it already stores, its sign-up screen, its privacy page). Ask only what's missing: the countries you sell in, the legal entity, the age of the users.
- **The user decides** every legal basis, every retention period and every new requirement. You give the options and a recommendation; they choose. One decision at a time. **A real choice is written as options, A and B,** each with why and when it wins; the file and the journal keep the letter and the date ("decided 2026-11-09, option A"), with when B would win. A choice changed later keeps the old letter in the journal, with what made it change. When every argument points one way, it isn't a choice: write it as decided and move on.
- **New requirements go into the PRD,** with a journal line, after the user says yes: a consent screen, an export button, a deletion job.
- **Collect less before you protect more.** For each piece of data, first ask whether you need it at all; data you don't keep can't leak, be requested or be fined (data minimisation).
- **Every claim checked at its source, with the date.** A law's article, a deadline, a provider's setting or term is read on its official page (EUR-Lex, the authority's site, the provider's docs and DPA) and written with the day it was read ("checked 2026-10-30"). Read only through a law firm's summary or the press? Say so ("read through …; the guidance itself not read"), and try the official page another way before calling anything an assumption. Why: laws move during the step (in July 2026 the AI Act's Digital Omnibus softened article 4 and moved the high-risk dates), and a provider's terms change without notice.
- **The law quoted in full, never cut.** When a decision rests on an article's words, quote the whole condition; a quote shortened to fit can change whom it covers. Found on 2026-11-10: an exception in the AI Act's article 50(2), quoted without "provided by the deployer", made a doubtful case look settled; quoted in full, it became a question for the lawyer.
- **What isn't checked yet is marked:** a fact you couldn't confirm (a provider's behaviour, a tax period, a date known only from a summary) is written `[ASSUMPTION: …, checked at setup]`, with who checks it and when, and gets a row in the open questions.
- **A later change says what it replaced:** a line changed after its step carries the date and, for a correction, the old words ("added 2026-11-09"; "corrected 2026-11-10: it said 'the person confirms every value'"), and the README's journal gets its line.
- **The journal in one voice:** the voice of the person who decides, in the first person ("confirmed by me", "with my yes", "decided by me, option A"), never mixed with their name in the third person. Each line: the date, where it came from (the step, a later step, a check), what changed, and the files that changed with it.
- **A number or a rule decided earlier changes everywhere at once** (decided 2026-10-21, after a whole-design check found ~160 stale mentions left behind by later steps): before committing, `grep` all of `docs/` for the old value and its wording (the number, the name, the phrase) and fix every place in the same commit, or say why one stays (a journal line keeps what was true that day; a past count kept on purpose goes into `docs/02-design/checks/facts-history.txt`). `diagrams.sh` runs `checks/facts.py`, which counts the main facts from their sources (tables, addresses, threats, secrets, screens, ADRs, alerts) and stops on a document that states another number; a new fact that many files repeat gets a line in it. **The public texts too:** a decision that changes in 01–08 changes the text that tells people in the same commit, and a change to what's processed or why raises the consent texts' version, so people are asked again.
- **What this step puts off or rules out goes to `docs/00-project/ideas.md`:** a feature this step puts off for later becomes an idea there with the next ID, and the file that puts it off cites it; an idea this step rules out moves to "Dropped" with the date and the decision that forbids it (an ADR, the DPIA: MacroMate's F-33 streaks, banned by the DPIA); either way the file's Next free ID, Updated and History follow.

## The laws and rules
Use this list at step 8. Name the ones that apply; for each one you name, one line on what it asks. The dates were read at the sources in October and November 2026; read them again at the source when you run this, since laws move.

| What | What it asks, in plain words | Usually applies when |
|---|---|---|
| **GDPR** (EU General Data Protection Regulation) | a legal basis for every use of personal data, only the data you need, kept only as long as needed, protected, and the person has rights over it | any personal data of people in the EU |
| **Special category data** (GDPR, article 9) | health, religion, ethnicity, sexual life, biometrics…: forbidden unless an exception applies; for apps, usually **explicit consent** | weight, food logs, symptoms, menstrual data, mood |
| **ePrivacy** (the cookie rule) | anything stored on or read from the user's device (cookies, local storage) needs consent, except what's strictly necessary for the service they asked for | analytics or ad cookies, trackers |
| **Consumer law** (EU) | clear terms, prices with VAT, a 14-day withdrawal right for distance sales (digital services started at once have their own rules) and, from 19 June 2026, a withdrawal button (Directive 2023/2673); no unfair terms; no false claim that a product cures (Directive 2005/29, Annex I, point 17); no ODR link any more (the link to the EU's online dispute resolution platform, closed on 20 July 2025). A merchant of record is the trader for the sale: its duties first, your promises on top | selling to consumers |
| **Medical devices** (MDR, EU) | software meant to diagnose, prevent or treat a disease is a medical device, with costly certification; software for lifestyle and well-being isn't (recital 19). The intended purpose decides, read from your texts and marketing too (MDCG 2019-11 rev.1, June 2025, the guidance of the EU's medical device experts) | health and nutrition apps that give advice or claims |
| **AI Act** (EU, Regulation 2024/1689) | duties by role (provider, deployer) and risk. **AI literacy** for whoever operates the AI (article 4, since 2 February 2025; from 27 July 2026 "take measures to support" it, by the Digital Omnibus on AI, Regulation (EU) 2026/1744, the law that amended the AI Act). **Transparency** from 2 August 2026 (article 50): people told they deal with an AI unless it's obvious, and generated content marked machine-readable, its exceptions read word for word; the marking's grace until 2 December 2026 covers only systems placed on the market before 2 August 2026. **High-risk** only in Annex III's eight areas, or as a product whose own law needs a third party's check (Annex I: a medical device from class IIa); those duties from 2 December 2027 (Annex III) and 2 August 2028 (Annex I), moved by the same regulation. The model's own duties sit with the model provider | any AI feature (article 4); AI that talks to users or generates content (article 50) |
| **Accessibility** (European Accessibility Act) | from 28 June 2025, online shops and services must be accessible; micro-enterprises (fewer than 10 people and at most €2 million a year) providing services are exempt. The bar in practice is EN 301 549, the European accessibility standard: V3.2.1, cited today, asks WCAG 2.1 AA; V4.1.1, published on 2 September 2026, asks WCAG 2.2 AA | selling online in the EU |
| **Data licences** | data taken from others comes with rules: attribution, share-alike (what you derive, you publish under the same licence) | open datasets, scraped or imported data |
| **Children** (GDPR, article 8) | online consent from a child needs a parent below an age set by each country (16 by default, 13–16 by country) | apps young people may use |
| **Who runs the site** (e-commerce directive, 2000/31/EC, article 5) | the name, a postal address and an email, shown on the website and in the app; hiding the domain's registration (WHOIS privacy) doesn't remove it | any online service in the EU |
| **Digital Services Act** (Regulation 2022/2065) | a hosting service (it stores what people put) needs a point of contact, a way to report illegal content, acted on without undue delay, a reason given before content is removed or an account closed, and terms saying how content is moderated; an online platform (content shown to the public) has more; micro-enterprises skip the transparency reports | people can store content: posts, recipes, files, shared spaces |
| **Cyber Resilience Act** (Regulation 2024/2847) | "products with digital elements" sold in the EU: software reached only remotely stays outside, unless it's a covered product's remote data processing, but the Commission's guidance, as law firms report it, counts software running on the person's device, locally installed web apps among it. Reporting an actively exploited vulnerability or a severe incident, an early warning within 24 hours through the single reporting platform of ENISA, the EU's cybersecurity agency, from 11 September 2026; the rest from 11 December 2027 | an app installed on the device (mobile, desktop, perhaps an installable web app) |
| **Other countries** | the UK: UK GDPR, the Children's Code and the Online Safety Act, which reach a controller outside the UK when it targets people there (UK GDPR, article 3(2)); then a UK representative, complaints first to the controller, the Online Safety Act's assessments. The US: the state consumer health data laws (Washington, Nevada, Connecticut): a health data privacy policy, consent to collect and a separate one to share, an answer within 45 days with an appeal; every state's breach law | people from there use it; health data of US residents |
| **Tax and the legal entity** | who sells, who charges and pays VAT, which entity receives the money | any paid product |
| **Sector rules** | finance, health care, education, employment add their own; NIS2, the EU's cybersecurity law, for its listed sectors (rarely a micro-enterprise) | when the product sits in one of them |

## The GDPR terms
| Term | What it is |
|---|---|
| **Controller** | who decides why and how the data is used: the product's owner |
| **Processor** | who processes the data on the controller's behalf: the hosting, the email, the AI provider |
| **Separate controller** | a company that decides about the data for its own purposes (a merchant of record selling in its own name, a "Sign in with" provider): named in the privacy policy, keeps its own records, told of a deletion or a correction (article 19) |
| **DPA** (data processing agreement) | the contract required with every processor: what it does with the data, where, for how long, its sub-processors |
| **Legal basis** | the reason the law accepts: contract, consent, legal obligation, legitimate interest (vital interest and public task rarely apply) |
| **Record of processing** (RoPA, article 30) | the table of every processing: what, why, basis, where, who, how long; required as soon as special category data is processed, however small you are |
| **DPIA** (data protection impact assessment, article 35) | a written analysis of the risks to people, required when processing is likely high-risk (for example health data at scale) |
| **Prior consultation** (article 36) | asking the authority before processing, needed only when a risk stays high after the measures |
| **Data subject rights** | access, correction, deletion, portability (export), restriction, objection, withdrawing consent, and not being subject to a decision made only by a machine with legal or similarly significant effects (article 22); answered within one month, two more for complex requests with the reason told in the first month, free (article 12) |
| **Pseudonymised data** | data that points to a person only with something kept apart (a hash of an IP address, a keyed fingerprint of an email): still personal data, unlike anonymous data |
| **Transfers outside the EU** | allowed to countries with an EU adequacy decision, or with standard contractual clauses; the US through the Data Privacy Framework for certified companies |
| **Personal data breach** | personal data destroyed, lost, changed, unavailable for a time, or seen by people who shouldn't, by accident or on purpose (article 4(12)): tell the supervisory authority within 72 hours of becoming aware, unless it's unlikely to be a risk to people; the people affected without undue delay when the risk is high; every one written in a register (article 33(5)) |
| **Lead authority** | the supervisory authority where the controller is established; it handles people from every EU country, so a breach is notified to it alone |
| **Privacy by design** (article 25) | data protection built into the design from the start, not added at the end |
| **DPO** (data protection officer) | required when the core activity is large-scale special category processing or monitoring; usually not for a small product, revisit at scale |

## Steps

### 1. Read what exists
The system design's data map, providers, flows and open questions; the PRD's GDPR and operations requirements; the brief. **The running app too:** its data model (preferences, reports, soft-deleted rows, invites and display names slip out of the documents) and what it does in production today (providers, open sign-up). If it's public with real users, whatever isn't compliant is urgent: say so first. List what's missing (countries, legal entity, users' age) and ask only that.

### 2. The record of processing
Article 30's record. **First the header:** the controller and its contact, whose data (users, invited people, a waitlist, people writing to support, visitors), the transfers outside the EU with their basis, the security in short, and the legal bases used, each in one line. **Then one row per purpose, not per table:** what data, **why** (the purpose), **the legal basis**, special category or not, where it lives, who touches it (processors and separate controllers). **The periods live in retention** and the record links them, so each is written in one place. Start from the system design's data map and add the legal columns; then check it against the running app's tables. Each AI feature is its own row, with exactly what it sends and what it never sends (a recipe generator may send remaining calories and preferences, not only a photo). The rows that slip out: the proof of consent, the notes of requests answered, the ids of deleted accounts, the export file, bounced addresses, counters of attempts (a hash of an IP is still pseudonymised data), an incident's evidence and the breach register, an admin's audit log, an analytics tool that reads the IP for a moment. Under the table: what the AI provider keeps, the backups as they are, and the uses without personal data, named so nobody asks again.

| # | Data | Purpose | Legal basis | Special | Where | Who touches it |
|---|---|---|---|---|---|---|
| 1 | account email and password | the account, login | contract | no | database (EU) | hosting, email |
| 2 | weight and food log | tracking progress | explicit consent | **health** | phone, database (EU) | hosting, AI (photo only) |

### 3. Consent and age
- Valid consent is freely given, specific, informed and unambiguous (articles 4(11) and 7): which consents, when, with what text; separate, not pre-ticked; the person told before ticking that they can withdraw, as easily as they gave it (7(3)). Whether a required consent may be a condition of using the app (7(4)) is a lawyer question.
- **What's recorded as proof** (7(1)): who, which box, which version of the text, when (UTC), the app's language, given or withdrawn, and how (sign-up, settings, asked again); the exact words of each version kept once, in every language; no IP address. After an account's deletion, a keyed fingerprint of the email (an HMAC: a hash only the holder of a secret key can make) lets a complaint naming an email find its proof without keeping the email.
- **A new version of a text** that changes what's processed or why is asked again, before anything else; declined, the app offers the export and the deletion. A typo fix makes a new version without asking anyone.
- What happens when consent is refused or withdrawn (for health data in a health app, usually: the feature can't work, say so honestly, offer the export, then deletion; withdrawing a required consent is then the account's deletion).
- **Purposes the app doesn't need** (usage metrics, measuring the AI's accuracy, improving the product) get their own **optional**, unticked box; bundled into the required one, the required consent isn't freely given. The required box's text names every use, the AI features and support included.
- The minimum age, and how the app asks for it: **before the account exists**, so "nothing kept" is true. A birth year alone can't tell whether someone born in the boundary year has had their birthday: ask ("Have you turned 16 yet?"), and "not yet" stops the same way. Whether a minor may pay alone is a civil-law question for the lawyer.
- A waitlist or a newsletter: consent with double opt-in (an address joins only once its owner confirms).

### 4. The providers
One row per provider, `| Provider | Role | DPA | Data leaves the EU? | Trains on it? | What it keeps | To do |`: the role (processor, or separate controller), the DPA (signed or accepted in the account), where the data goes and the transfer basis outside the EU, whether it trains on your data, what it keeps and for how long, its sub-processors, and what's left to do (the settings to turn on before any data flows: an EU-only endpoint, a cache off, training off, a retention setting; each also in the README's "Before launch"). **Check the company's country, not only the data region:** a US company storing in the EU still needs a transfer basis. **A tool that only reads personal data for a moment** (an analytics script reading the IP to count visitors) is still a processor. A merchant of record is a separate controller: write what you send it, and tell it when an account is deleted or its email changes (article 19). A last row names the providers that get no user data, and what keeps it so (no real data in tests, fixtures or eval sets). The list of processors is published for users (in the privacy policy). A provider that can't meet the requirements is replaced now, not after launch.

### 5. Retention
One row per kind of data, `| Data | Kept | What deletes it |`: a period, and **what deletes it** (a job, the action itself, a provider setting, a storage bucket's expiration rule), never "someone remembers". A clean-up by hand is a written exception: listed at the top of the file, each a reminder in a calendar and a line in the README's "Before launch". The rows that are easy to forget: inactive accounts (deleted after a period, with a warning email first), unconfirmed accounts, one-time links, sessions, invites, the AI's requests and proposals (those never saved too), uploaded files nothing uses, the export file, the consent proof and the notes of requests answered, the ids of deleted accounts, logs (yours and the log provider's), the email provider's own logs, bounced addresses, counters of attempts, support messages, a waitlist, an admin's audit log, an incident's evidence, the breach register, what the AI provider receives, analytics, a restore drill's copy, payment events and tax records (accounting law usually asks years for invoices; the merchant of record may keep them for you). A last line names what holds no personal data, so it needs no period.
- **Soft-deleted rows** lose their values at once; keep only the marker other devices need.
- **Backups age out by an expiration rule on the storage itself,** when the backup job's key can't delete (it shouldn't: then a stolen key can't wipe them).
- **A backup restore brings deleted accounts back:** keep the deleted ids as long as the oldest backup, run the deletions again after any restore (yours, or one the provider makes by itself), and make the restore refuse a copy older than the ids. A deletion inside an account (an entry, a withdrawn optional consent) comes back too when only account ids are kept: accept it knowingly or keep those ids too, and write which.
- **An incident's evidence** is the one exception to the backups' period: kept until the incident is closed, at most a set number of months, longer only while the authority still asks, with the reason in the breach register.
- **A minimal proof** (consents, requests answered), without the special category data, may stay after deletion for the limitation period, to answer a complaint (article 17(3)(e)).

### 6. The rights, as mechanisms
Article 12's rules first: an answer without undue delay, within one month; two more for complex or many requests, with the reason told in the first month; free, unless a request is manifestly unfounded or excessive (and you show why); a refusal with its reason and the right to complain to the authority and to go to court. Then one row per right, `| Right | Where the person asks | What happens behind it | How long |`:
- **access** ("what do you have about me?"), including what's outside the export, sent on request;
- **portability:** a machine-readable export, with the list of who received the data;
- **erasure:** the database, files, the providers told (article 19), the backups within their retention; refused only in a written case (the app's last admin), with the reason;
- **rectification** and **withdrawing consent**;
- **objection**, only for what rests on legitimate interest; **restriction**, on its four grounds;
- **automated decisions** (article 22): only decisions made solely by a machine with legal or similarly significant effects. Say why none apply with the law's own reason, true everywhere: "the person confirms every value" fails as soon as one AI output is saved at once.

Then: what stays after a deletion, and why; who may ask and how you know it's them (article 12(6)), people without an account included; a note of each request answered (date, type, when done) as the proof. Each right becomes a requirement for the data model, the API and the screens.

### 7. The DPIA, short
Article 35(7) sets its minimum content: what's processed and why, whether it's necessary and proportionate, the risks to people, and the measures. Kept short, linking the files that hold the details:
- **A header:** carried out by, written and reviewed (dates), approved by, the people's views.
- **Why one is needed:** the 9 criteria of the European authorities' guidelines (WP248 rev.01, endorsed by the EDPB, the board of the EU's data protection authorities), one by one, `| Criterion (WP248) | Met | Why |` ("in most cases" two met need a DPIA); the lead authority's own list, and another country's if you target it; whether a DPO is required (article 37).
- **What's processed** (whose, what, why, where, how long) and **necessary and proportionate** (the basis, only what's needed, kept only as long as needed, told plainly, the rights, the providers and transfers).
- **A scale written before the risks:** how likely, how bad for the person, each low, medium or high, and what remains after the measures. A remaining high goes to the authority before processing (prior consultation, article 36); a remaining medium is accepted only in writing, with who accepted it.
- **The risks:** `| What could hurt people | Likely | How bad | What reduces it | Remaining |`: someone seeing another's data, an account taken over, a leak, a lost device, the AI provider keeping data, the AI's answer harming someone, vulnerable people, health data in support emails, small totals pointing to one person, a restore bringing deleted data back, data lost or changed, data kept too long, the owner reaching everything.
- **The people's views** (article 35(9), "where appropriate"): before there are users, write why not and when they'll be asked.
- **The conclusion** (prior consultation or not) and **when it's done again** (before launch, after an incident, at 10×, a new health data feature or provider, a new market or legal entity).

Decide whether it's required and write why; when in doubt with health data, write it anyway.

### 8. The other laws
Go through the table above, one row per law in `| Law | Applies | Decision |`, each named with its number and a link to its official text, its dates read at the source with the day. For each one that applies, the decision: cookies (banner or not, and why: what's stored on or read from the device), consumer law (who is the trader, the terms, withdrawal and its button, refunds, prices), medical devices (what the app must never claim; a list of words never used, in every language, checked by a test on the translation files and on what the AI writes), the AI Act (the role: provider, deployer or both; what's labelled as made by AI and what's marked machine-readable; the Commission's code of practice and guidelines on article 50; AI literacy), accessibility, data licences (attribution, what must be published), the legal entity and tax, who runs the site, the Digital Services Act, the Cyber Resilience Act (a service used in the browser, or an installed app?), and the terms' main promises (the governing law, without taking away the protection of the consumer's own country: Rome I, the EU rule on which law governs a contract, article 6(2)). **Other countries:** selling in the UK or the US adds the UK GDPR and Children's Code, the ICO, and the US state health data and breach laws. UK GDPR reaches a controller outside the UK when it targets people there (article 3(2)); serving people in the UK without targeting them (no marketing there, no prices in pounds, no UK authority in the texts) is a real option, decided with the user, the lawyer asked whether it's enough. What the law leaves doubtful goes to the lawyer's questions.

### 9. The breach plan
A breach is wider than a leak: personal data destroyed, lost, changed, unavailable for a time, or seen by people who shouldn't (article 4(12); EDPB Guidelines 9/2022). The 72 hours run from becoming **aware**, reasonably certain it happened, and for a processor's breach from when it tells you. One page, a table `| When | What I do |`, written now, not during the incident:
- **How you'd find out:** the security and monitoring alerts, a provider telling you, a person or a researcher writing (`security.txt`, the file on the website that says where to report a vulnerability), a scanner flagging a leaked key.
- **First hour: the evidence first, then stop it.** A restart or a key rotation can erase what happened: export the logs and a copy of the data first, encrypted, into a place of its own (never a laptop); then rotate what leaked as the secrets' inventory says, sign everyone out, take the affected part offline.
- **First 24 hours:** which data, how many people, how bad for them, on the DPIA's scale and the EDPB's factors; when it's unlikely to be a risk (an encrypted copy whose key is safe), not notified, the reason in the register.
- **Within 72 hours:** the lead authority, through its form, even with gaps; the rest as a supplement; after 72 hours, the reasons for the delay. Other countries' rules where people there are affected (the US states' deadlines).
- **The people:** without undue delay when the risk is high (article 34), or more often if the user decides so; in their language: what happened, the likely consequences, what was done, what they can do; another channel if the app or the email provider is down.
- **The providers** (their contacts written in advance), **a crime** (the police), **a restore or a long outage** (an availability breach), and **who acts if the person in charge can't** (for a team of one: nobody, accepted and written, a late notice giving the reason).
- **Always: the register** (article 33(5)): every incident, even the ones not reported, in its own file, `breach-register.md`, created before the first outside users, with these columns: started, aware, what happened and its cause, data and people, effects, risk and why, authority told (when, its number) or why not, people told (when, how) or why not, the reasons for a delay, the fix, **the evidence taken** (each file's SHA-256, who took it and when: the chain of custody, so you can show the evidence is the one taken; a SHA-256 is a file's fingerprint, and any change gives another), the evidence's deletion date (any extension and why). Kept in a git repository, it holds no personal data, since git's history never forgets: a reporter is named by a reference (the support thread's date), never by an email.
- **After:** the cause, the fix, the DPIA updated, a threat or a test added in security, the evidence deleted on its date.

Ready in advance: the texts for the authority and the people, in `public-texts/`. Tried once before launch, with the restore drill. Say what isn't this plan: NIS2 (its listed sectors), ePrivacy's breach rule (telecom providers); the Cyber Resilience Act's reports join it if that act applies.

### 10. The public texts
What people outside read or receive goes into `public-texts/`, with a README: `| Text | Who reads it | Where | Required |`, the status, what's left before the first outside users and before launch, and **the rule**: a decision that changes in 01–08 changes the text that tells people in the same commit. The texts: the privacy policy (what, why, basis, where, who, how long, rights, contact, the list of processors), the terms, the consent texts (each with a version), an accessibility statement, the breach notifications (the authority's form fields, with the four that article 33(3) asks marked; the people's email; the register's columns), and any text another law asks for (a US consumer health data policy). Each starts with "DRAFT, not checked by a lawyer", carries a version and a "Last updated", and marks the placeholders in [brackets]. Written for the user's reading level, in every language the app supports (drafted in one, translated after the lawyer's review). An accessibility statement says "aims to conform" until a full check. Any new promise in the terms (notice periods, refunds) is shown to the user before it's written, and goes into the PRD.

### 11. What changes in the design
The list of new requirements, each with where it lands (PRD, data model, API, screens); on the user's yes, into the PRD with a journal line. Hard-to-undo choices (the legal basis for health data, a provider replaced) become ADRs, one at a time, chosen by the user.

### 12. Check it
- every kind of data has a purpose, a legal basis, a place and a retention period with a mechanism;
- every processor has a DPA and a transfer basis;
- every right has a mechanism and a deadline;
- every health-related text stays clear of medical claims;
- every claim about a law or a provider has its source and date, every quoted article is whole, every unchecked fact is marked `[ASSUMPTION]`;
- the public texts say what 01–08 say, number for number;
- nothing contradicts the system design or the PRD.

Run the check with a **separate agent** that has only the documents (`/compliance validate <folder>`), then verify its findings in the files before showing them: it can be wrong. Look especially for **contradictions left by a changed decision**, above all in the files the step didn't touch and in the public texts. Show the verified findings by severity, with a recommendation; the user decides each, and every fix gets a journal line.

**Done when** every finding is fixed, or answered with its reason, and every item of "Done when" below is ticked. Before launch, run the step again as a checklist: each item exists and works.

Write as you go: each step's file once the user confirms it, with a journal line in the README; **the README's summary, the lawyer's questions and the glossary grow with the steps**, not at the end. At the end, set this step's row in `docs/02-design/README.md` (the map of the Design steps) to done, with the date, and link the folder.

```
docs/02-design/02-compliance/
  README.md              status, summary, the laws that apply, the files, the ADRs, open questions,
                         the lawyer's questions, before launch, glossary, journal
  01-record.md           the record of processing (article 30): the header, one row per purpose
  02-consent.md          consents and what makes them valid, the proof recorded, asked again,
                         withdrawing, the minimum age
  03-processors.md       each provider's role, DPA, transfers, training, what it keeps, what's left to do
  04-retention.md        periods, what deletes the data, the clean-ups by hand, deletions after a restore
  05-rights.md           each right as a mechanism, the deadlines, who may ask, what stays after a deletion
  06-dpia.md             the impact assessment, as article 35(7) asks
  07-other-laws.md       every other law, each with its decision
  08-breach-plan.md      from finding out to the register; the evidence first; the 72 hours
  breach-register.md     every incident, even the ones not reported; created before the first outside users
  public-texts/          what people outside read or receive (drafts until a lawyer checks them)
    README.md            each text's reader, where it appears, whether it's required, what's left
    privacy-policy.md    terms.md    consent-texts.md    accessibility-statement.md
    breach-notifications.md          and one per other law that asks for its own text
```

Each topic file starts with `# NN – [Topic]` and a link back to the README ("Part of the [compliance](README.md)."), then a paragraph on what the law asks, with its article.

The README:

````markdown
# Compliance – [Product]
| | |
|---|---|
| **Status** | draft / confirmed by me, steps 1–12, [date]; checked by an outside reader (`/compliance validate`), [date], the findings fixed / checked by a lawyer on [date] |
| **Controller** | [legal entity, country] |
| **Updated** | [date] |
| **Next** | 03 Architecture; again before launch, as a checklist |

Not legal advice: [who made the map, the decisions and the drafts; the lawyer review planned before launch].
## In one page
What the product is and who may use it (age, countries), the laws that apply, the special categories and their basis, what the running app already does right, what the new version adds, the risks the DPIA leaves: 5–7 lines.
## The laws that apply
| Law | Applies | What it means here |
## The files
| File | What it answers |
## Decisions (ADRs)
| ADR | Decision |
Used here, decided elsewhere: [ADR-NNNN] ([what it decides]) …
## Open questions
| Question | Answered by | When |
## For the lawyer (one hour, before launch)
1. [each point the files can't settle, with its article; the files name it "the lawyer's question 1"; one added later carries its date]
## Before launch
- [ ] each item that must exist and work: the providers' settings, the clean-ups by hand in a calendar, the drills, the texts published
## Glossary
- **Term:** what it is, compared with something the reader already knows
## Journal
- [date]: [where it came from: step n, a later step, a check]: [what was decided or changed], with my yes / decided by me, option A; [the files that changed with it]
````

## Validate mode
`/compliance validate <folder>`: judge an existing compliance folder, change nothing.
1. Read the folder (`public-texts/` and the breach register included), its ADRs, the system design's data and providers, the PRD and the running app's privacy texts if any.
2. Check the template and "Done when" item by item, citing the lines.
3. Then ask: does every kind of data in the system design appear in the record? Does every purpose have a basis that fits (no "legitimate interest" for health data)? Is consent for special category data explicit, separate and recorded? Does every processor have a DPA, a transfer basis and a known retention? Does every right have a mechanism that reaches the backups and the providers? Does any text read like a medical claim? Is every new requirement in the PRD? Does the record match the running app's tables? Is any non-essential purpose bundled into a required consent? Does every provider's company country have a transfer basis? Do deletions survive a backup restore? Is every claim about a law or a provider dated at its source, every quoted article whole, every unchecked fact marked `[ASSUMPTION]`? Is each "doesn't apply" given the law's own reason, true everywhere (article 22: no decision with legal or similarly significant effect, not "the person confirms every value" when one output is saved at once)? Do the public texts say what 01–08 say? Does the breach register, kept in git, hold any personal data? **Then the decisions that changed during the steps:** is the old version still written anywhere, above all in files the step didn't touch?
4. Report: findings by severity, each with the line, what's wrong and what to change; then what's done well; then what needs a lawyer. The user picks what to apply.

## The bad version and why not
- A privacy policy copied from another app: it describes other data and other providers, so it's worse than none, because it's false.
- One "I agree to everything" checkbox, already ticked: consent for health data isn't valid.
- No retention periods: data stays forever, and a "deleted" account lives on in backups for years.
- Compliance left to the end: the export button, the consent table and deletion from backups get added to finished code, at many times the cost.
- Marketing that promises medical results ("lowers your blood sugar"): the app can become a medical device.
- "We're too small for GDPR": the size exemptions don't cover special category data.
- A law cited from memory, from a summary, or cut short: its dates and exceptions move (the AI Act's moved in July 2026), and a shortened condition decides the wrong case.

## What breaks if you skip it
The payment provider won't approve the account without a privacy policy and terms. The first user who asks "what data do you have about me?" doesn't get an answer within the month the law gives. A leak finds you without a plan, and 72 hours pass fast. Health data collected without explicit consent can't be fixed afterwards: you must ask everyone again.

## The principle behind it
Privacy by design: collect only what you need, know why you have it, keep it only as long as needed, and be able to show it or delete it at any time. Data you don't collect can't be lost, stolen or requested.

## How to apply it at work
Before a feature with personal data, ask: which data, why, on what basis, at which provider, for how long, how does the person delete it. If the company has a DPO, bring them in at design, not at the final review. Before a new provider, ask for its DPA and its list of sub-processors.

## Done when
- [ ] every kind of data in the system design and in the running app's tables is in the record, with purpose, basis, place and who touches it; each AI feature with what it sends; the header with the controller, whose data, the transfers and the security
- [ ] special category data has explicit, separate consent, recorded with the text version, the time, the language and how it was given; non-essential purposes in their own optional box; a new text asks again
- [ ] the minimum age decided, asked before the account exists, the boundary year handled
- [ ] every processor with its role, a DPA, a transfer basis (by the company's country, not only the data region), training and retention known, the settings to turn on in "To do"
- [ ] every retention period has a mechanism that deletes, backups included; deletions re-run after a restore; every clean-up by hand a written exception with a reminder
- [ ] every right is a mechanism with a deadline, article 12's rules written, what stays after a deletion written
- [ ] the DPIA as article 35(7) asks, or why it isn't required; a remaining medium risk accepted in writing, a remaining high sent to the authority first
- [ ] the other laws gone through, each with a decision, every law and date checked at its source, with the day it was read
- [ ] the breach plan, one page; the register's columns with the evidence's chain of custody; a drill planned before launch
- [ ] the public texts in `public-texts/` with its README, marked as drafts, saying what 01–08 say
- [ ] the new requirements in the PRD, with journal lines; the hard-to-undo choices as ADRs, chosen by the user
- [ ] every point the files can't settle in the README's numbered questions for the lawyer; a one-hour review proposed for before launch
- [ ] every unchecked fact marked `[ASSUMPTION]`, with who checks it; every quoted article whole
- [ ] the journal in one voice; a changed fact fixed everywhere in the same commit
- [ ] a glossary for every term

## Next
Architecture (`/architecture`): it takes the requirements from here (consent records, export and deletion jobs, retention) into the modules. Before launch: `/compliance` again, as a checklist.
