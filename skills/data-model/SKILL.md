---
name: data-model
description: "What data the product keeps, how it relates, and which rules the database guards by itself. The conceptual model (entities per module, relations), the reads and writes the app will make with their volumes, the tables module by module (columns, types, keys, constraints, each with why, personal and health data marked), the indexes checked with EXPLAIN on generated data, integrity and concurrent writes, the lifecycle of every table (retention, deletion, tombstones, export), the offline model on the device, reference data and languages, the migration plan for live data, test data, and the big choices as ADRs. Writes a folder: a README, one file per topic, one file per module's tables, a schema.sql run on a real database, and diagrams. Use after architecture, before or alongside the API and the screens; at work before new tables, a change to tables with production data, or a slow query. Also judges an existing one: /data-model validate <folder>."
argument-hint: "[the product or the change] or validate <folder>"
---

# Data model

## When to use it
After Architecture, before the API and the screens (05–06), almost in parallel with them. It needs the PRD's glossary, features and criteria, the system design's volume calculation and data map, compliance's retention and rights, and from the architecture the modules (who owns which tables) and the naming conventions. **Before the first migration:** a table is cheap to change on paper and expensive once it holds real data.

At work: a feature that brings new data, a change to tables that hold production data, a report that runs slowly, a GDPR request where nobody knows where all of a person's data is. Also in the first weeks at a new company: the database schema shows what the product does faster than the code.

## The problem it solves
The architecture said who owns what: the Log module has "days, entries, weigh-ins". It didn't say which columns an entry has, what's required, what happens to it when its food is deleted, how to find yesterday among 2 million rows, or how to delete everything about one person.

Without an answer, the classes in the code decide the tables, in a hurry, in the first PR: everything text of 255 characters, nothing required, no link checked. Bad data gets in on day one and stays. Code is rewritten in a week; data in a live database takes months to repair.

The data model decides **what data the product keeps, how it relates, and which rules the database guards by itself**: the tables, their columns and types, the keys and constraints, the indexes for the real questions, how long each row lives, and how a change reaches production without stopping the app.

## How to run it
- **The bar:** do what a senior engineer or the CTO at a well-run company would accept, in the simplest form that meets it. Use the real industry method and name it, so the user learns it. Say what you leave out and why.
- **Teach while you go:** the user may be doing this for the first time. Every term gets one line on what it is and what it brings, compared with something a frontend developer already knows: TypeScript types for the API's data are already a data model; a Zod schema that refuses a bad form is already a constraint; a store that keeps objects by id instead of copying them into every list is already normalization; a `Map` by id is already an index; Dexie's `db.version(2)` is already a migration. When the server is in Java, explain JPA the first time (the Java standard that maps classes to tables; Hibernate implements it), compared with Entity Framework in C#: **the table is designed first, the class follows it.** Show the full picture of the topic, then mark what this product needs. **At a technical chunk, plain words and one example with numbers come first** ("the app counts in grams, the bottle in ml"), then what it means for the user ("nothing to adjust"); the tables after, or only in the file. A sentence that can be read two ways is settled with options A/B before anything is written.
- **One step per message, and big steps in chunks.** Show a step, wait for the user's OK, then the next. Steps 4–11 are big: one module or one sub-topic per chunk (each step below names its usual chunks); **count the chunks before announcing them** and say so if the count changes; save and commit each chunk once it's confirmed. Why: each decision needs to land before the next one builds on it.
- **Ask only when there's a real choice.** When all the arguments point one way and no realistic alternative fits, write it as decided, with its arguments, and move on to the next real choice. Ask when there are at least two options the user could reasonably pick; once chosen, the choice is final. When the user voices a fear or a doubt next to a choice, resolve it before recording the decision.
- **Every number, type and rule with its argument:** a known standard (named, its official page checked on the web), a target set earlier (cited), or a guess marked `[ASSUMPTION]` with its reasoning. For a choice, an argument card: why; the main alternative and who uses it; when the alternative is better; what someone may answer, and the reply; the source. When the industry is split, name the camps. In the docs, every table of columns has a "why" column. Why: the user must be able to defend each choice in a review or a technical discussion.
- **Where the documents are:** the `Project documents:` line in `CLAUDE.md` gives the documents folder; without it, use `docs/` in the current folder. Write into `docs/02-design/04-data-model/` and the ADRs into `docs/00-project/adr/`; create them if they don't exist.
- **Read first:** the PRD (`docs/01-discovery/04-prd.md`: glossary, features and their criteria, journeys, the build order), the system design (`docs/02-design/01-system-design/`: the volume calculation, the data map, offline, the flows), the compliance folder (`docs/02-design/02-compliance/`: retention, rights, what counts as health data, the providers), the architecture (`docs/02-design/03-architecture/`: the modules and the data each owns, the conventions, the requirements in code, the shared rules, the stack, the events), and the ADRs. Ask only what's missing.
- **An existing database is a source of facts, not a model.** Read it for what tables exist, how many rows, what's missing or broken (orphans, duplicates, free text where a rule should be). A shape doesn't become right because it's there, least of all one generated by an ORM in a hurry.
- **The owners and the names come from the architecture; this step decides the shape.** Don't move a table to another module or rename a convention here; if one is wrong, stop, say so, and on a yes fix the architecture with a journal line. **The same for the PRD and compliance:** any change, even one that only closes a gap, is shown to the user first with its exact text.
- **Two forms of the tables, each holding something different:** markdown tables per module (column, type, required, default, rule, **why**, personal or health data) for people to review, and **one `schema.sql`** with every `CREATE SCHEMA`, `CREATE TABLE` and `CREATE INDEX`, **run on a real database of the chosen version** (in Docker, or with the project's test containers) after every chunk. Why: SQL is what the database executes, so a wrong type, a foreign key to a missing table or a broken `CHECK` shows in seconds instead of in Build; in Build the file is split into the first migrations per slice, so nothing is typed twice. Not DBML or another diagram language: one more language, and it may not cover the database's features (DBML's docs list no partial indexes, `INCLUDE` or exclusion constraints). The validation agent compares the markdown and the SQL column by column.
- **Check the indexes in Design only where the table's shape is at stake** (step 5): the big or very frequent tables, on generated data. Why: an index is cheap to add later (`CREATE INDEX CONCURRENTLY` doesn't block writes); what's expensive is a table shape that leaves no room for a good index (an entry that reaches its person only through a join; values hidden in JSON that a report must sum). The SQL written here isn't the SQL the ORM will generate, so the final check of the real queries stays in Build, per slice.
- **The user decides** the conceptual model (step 2), every real choice in the tables (step 4) and every ADR (step 12). You give the options and a recommendation; they choose. One decision at a time.
- **Check the database's behaviour on its official pages,** not from memory: the types, what a constraint or an index does, which `ALTER TABLE` forms rewrite or lock a table, the version's features (PostgreSQL 18 has `uuidv7()` and `NOT NULL … NOT VALID`; earlier versions don't). **Write "tried" only for what the test proved** (a uniqueness error doesn't prove "the last change wins"), and keep every script in `checks/`.
- **ER diagrams in crow's-foot notation** (the usual entity–relationship notation: a line per relation, the "foot" on the many side), written as PlantUML (`.puml` next to its `.svg` in `diagrams/`): one conceptual diagram for the whole product, written by hand, and one per module with its tables, columns, keys and the links to other modules drawn differently (a grey stub for another module's table), **generated from the database `schema.sql` builds** by a script in `checks/` that reads the catalog, with `ORDER BY` everywhere so a rerun writes the same file; the columns marked personal or health data in the tables' pages are shaded. So the drawing can't drift from the SQL. Each with a title and a legend explaining the notation. `docs/02-design/diagrams.sh` (set up by `/docs-setup`) draws every diagram of the design from text, in a standard notation (decided 2026-10-20), so they read the same at any company; never a hand-made SVG, a home style, or a script that draws SVG itself. Open each one before committing: no text overlaps.
- **A number or a rule decided earlier changes everywhere at once** (decided 2026-10-21, after a whole-design check found ~160 stale mentions left behind by later steps): before committing, `grep` all of `docs/` for the old value and its wording (the number, the name, the phrase) and fix every place in the same commit, or say why one stays (a journal line keeps what was true that day; a past count kept on purpose goes into `docs/02-design/checks/facts-history.txt`). `diagrams.sh` runs `checks/facts.py`, which counts the main facts from their sources (tables, addresses, threats, secrets, screens, ADRs, alerts) and stops on a document that states another number; a new fact that many files repeat gets a line in it.
- **What isn't here:** the endpoints and the JSON shape (05 API design: **the table isn't the contract**, a new column doesn't appear in the API by itself), the screens (06 UI design), encryption, database access and Row-Level Security (07 Security), the data for AI evals (08 AI design), the full SQL of the migrations (Build, per slice; here the shape and the plan), backups and restore (decided in the system design).

## The three levels
| Level | What it says | For whom |
|---|---|---|
| Conceptual | the things and how they relate, in the domain's words, no types: "a person has a kitchen; a kitchen has recipes" | anyone, people who don't write code included |
| Logical | the entities with their attributes, keys and exact relations, normalized; still no particular database | whoever designs |
| Physical | how it sits in the chosen database: types, indexes, schemas, partitions | whoever writes the migrations and runs the database |

## Normalization, and when to break it
Use this at step 4. Edgar Codd (IBM, 1970–1971): every fact in one place, so there are never two versions of it.

| Form | The rule | What breaks if you violate it |
|---|---|---|
| First (1NF) | one value per cell: no lists in a column, no repeated columns (`ingredient1`, `ingredient2`) | you can't search, link or count the list's items |
| Second (2NF) | every column depends on the whole key, not part of it | the same fact repeated on many rows |
| Third (3NF) | no column depends on another non-key column | change it in one place, it stays old in another |
| BCNF, 4NF, 5NF | rarer cases with overlapping composite keys | — |

Normalize to the third form; **denormalize only with a written reason:** a measurement of speed, or **history** (a log entry keeps the values of that moment even when the food is corrected later: a deliberate copy, not a mistake).

## The types
Use this at step 4. For PostgreSQL the main source is the official wiki's "Don't Do This" page; for another database, find its equivalent.

| Need | Choose | Not, and why |
|---|---|---|
| Id | `uuid` v7 (sorts by time, can be made on the device offline, reveals no row count), or `bigint GENERATED ... AS IDENTITY` | `serial` (the wiki: it complicates permissions and schema changes) |
| Text | `text`, with a `CHECK` when a maximum length is a real rule | `varchar(255)` out of habit (the limit causes production errors and buys no speed); `char(n)` (pads with spaces) |
| A moment | `timestamptz` (stored in UTC) | `timestamp` without a time zone: the database doesn't know which zone, so arithmetic across daylight saving goes wrong |
| A calendar day | `date` | a moment at midnight: "today" depends on the person's time zone |
| Money | `numeric`, or an integer in the smallest unit | `float` (0.1 + 0.2 ≠ 0.3); `money` (depends on the server's locale setting) |
| Quantities | `numeric(p, s)` for exact amounts, or an integer in the smallest unit; **`double precision` for measurements computed the same way on two platforms** (Java's `double` and JavaScript's `number` are both IEEE 754, strict in Java since 17, JEP 306), with a `CHECK` range per value | `real`; `numeric` where the phone computes in `number`, since a value at a threshold could round differently |
| Texts in several languages that are data (names the admin adds) | `jsonb` with a key per language and a `CHECK` on the required keys: a new language is content, not a migration | a column per language (a migration per language); a translations table (a join on every read), unless dozens of languages |
| Yes or no | `boolean`, named by the conventions (`is_`, `has_`) | a `text` holding 'Y' or 'N' |
| A fixed list of values | `text` with `CHECK (x IN (...))`, or a reference table when the list has its own data or changes often | a PostgreSQL `enum`: a value can be added or renamed, never removed without recreating the type |
| Data without a fixed shape | `jsonb` | `json` (re-parsed on every read); a generic name–value table (EAV) |

## The indexes
Use this at step 5.

| Kind | What it does | Worth it when |
|---|---|---|
| B-tree (the default) | equal, less, greater, sorting | almost always |
| Composite | several columns; the order matters: `(user_id, day)` serves "by person" and "by person and day", not "by day" alone | a question filters on several columns |
| Unique | an index plus a constraint | a "once only" rule (an id made on the device, a barcode) |
| Partial | only the rows that match a condition (`WHERE status = 'pending'`) | a small queue inside a big table |
| Covering (`INCLUDE`) | also holds the columns asked for, so the table isn't visited | a very frequent question, measured |
| GIN | searches inside values: `jsonb`, arrays, text with `pg_trgm` | text search or JSON queries on the server |
| GiST, SP-GiST | geometry, ranges, nearest neighbour | maps, bookings |
| BRIN | tiny: only min and max per block of rows | huge tables naturally ordered by time |

The rules: **a foreign key gets no index by itself** in PostgreSQL, and its documentation says one is often a good idea (deleting a parent row searches the children); one index per real question, never one per column (each slows every write); checked with `EXPLAIN ANALYZE` on realistic volume; in production, `CREATE INDEX CONCURRENTLY`.

## Deletion and history
Use this at step 7.

| Kind | What it is | Worth it when |
|---|---|---|
| Hard delete | the row is gone | the default; GDPR asks for real deletion |
| Soft delete (`deleted_at`) | the row stays, marked | an "undo" window, a legal duty to keep; otherwise avoid: every query must remember the filter and foreign keys stop protecting (Brandur Leach, 2022) |
| Tombstone | only the id and the moment stay; the values are wiped | sync: other devices must learn about the deletion |
| Archive | old rows moved aside | old data, rarely read |
| History or audit table | every change: what, who, when | money, permissions, legal proof |
| Temporal tables (system-versioned) | the database keeps every version of a row | SQL Server, MariaDB; PostgreSQL has none built in |

## Ways to model data
Name only what this product needs; explain each one you name.

| Style | What it is | Worth it when |
|---|---|---|
| Normalized relational (OLTP, transaction processing) | tables in third form, keys, constraints | almost every application |
| Dimensional (star schema, Ralph Kimball) | a fact table in the middle, dimension tables around it | reports and analysis (OLAP), in a separate data warehouse |
| Data Vault | hubs, links and satellites, full history | big warehouses with many sources and audit |
| Document (MongoDB, or `jsonb`) | a whole object in one row | data always read whole, with a shape that varies |
| Key–value (Redis) | a value by key, in memory | caches, queues, fast counters |
| Wide-column (Cassandra, DynamoDB) | one table per question, data copied | huge scale, questions known in advance |
| Graph (Neo4j) | the nodes and links are the data | social networks, recommendations, fraud |
| Time series (TimescaleDB) | frequent measurements by time | sensors, metrics |
| EAV (entity–attribute–value) | one generic table (thing, name, value) instead of columns | almost never: it loses types, constraints and speed |
| Multi-tenant | a shared table with a tenant column, a schema per tenant, or a database per tenant; plus Row-Level Security (the database itself filters rows per tenant) | every SaaS product |

## Steps

### 1. Read what exists
The PRD's glossary, features and criteria; the system design's volume calculation, data map and offline decisions; compliance's retention, rights and what counts as health data; the architecture's modules with the data each owns, the conventions, the requirements in code, the shared rules (ids, dates, concurrency), the technical tables its libraries bring (jobs, sessions, rate limits, events) and the events; the ADRs. List what's missing and ask only that.

**If a database exists,** read it for facts: the tables, the row counts, what's missing or broken. Not as a model. The user decides what is kept.

### 2. The conceptual model
The entities, grouped by module, named with the glossary's words, one sentence each; the relations and their cardinality; one diagram for the whole product. **Every entity has exactly one owner module**; a word with two meanings ("portion" for a food and for a recipe) becomes two entities. **The user decides.**

### 3. The questions and the volumes, before the tables
From the system design's flows, the PRD's criteria and the screens you can foresee, list the important reads and writes per module: what it looks for, how often, over how many rows today and at 10×, from the system design's calculation. Why first: the physical model is built for these questions; a table designed without them is designed for none. Mark the **big or very frequent** ones: they get the index check at step 5.

### 4. The tables, module by module
**Chunk 1, the rules every table follows,** decided once for the whole product, before any module:
- the shared columns (id, `created_at`, `updated_at`), the types (the table above), `NOT NULL` unless empty means something;
- **links to another module:** a real foreign key across schemas or only the id, with its argument card (integrity guarded by the database, against a boundary the database also enforces). A middle way worth naming: foreign keys only towards the person and the other anchors (a kitchen, a team) with `RESTRICT`, so the database proves an account's deletion complete;
- **what happens to something deleted that's used elsewhere** (block, remove silently, or keep it named and marked deleted), decided here with the links, since blocking can't work across modules without a cycle;
- **texts in several languages:** separate the interface's texts (the app's translation files) from the texts that are data, and ask what a new language would cost before choosing the columns.

Then one chunk per module (logical and physical together):
- the columns: type, required or not, default, the rule (`CHECK`, `UNIQUE`), **why**, and whether it's **personal or health data**;
- the keys: the primary key, the natural keys as unique constraints, every foreign key **with its rule on delete** (`CASCADE`, `RESTRICT`, `SET NULL`) and why;
- the conventions from the architecture applied: names (yes-or-no columns included: `is_`, `has_`), ids, the link naming that the personal-data guard test reads;
- a denormalization only with its written reason;
- **minimisation, asked on every table with personal data:** a raw event or a count per day; a provider's whole webhook or only its ids; an IP address with a consent; the email of someone invited; a rate limit's key or its fingerprint;
- **the libraries' tables** (sessions, jobs, events, rate limits) copied exactly as each library publishes them, with the person's id instead of an email; a table that holds a person's data under another name goes on the guard test's written list, and that list must exist in the architecture;
- **the PRD's words checked against the mechanism** ("no login for 2 years" against a session that never expires); a mismatch is shown to the user with the exact new text;
- **every new entity goes back into the conceptual model** of step 2 (a lookup cache, a counter, an origin), with its relations.

Add the module's tables to `schema.sql` and run it on a real database of the chosen version; a chunk isn't done until it runs. **The user decides** each real choice.

### 5. The indexes
- every question from step 3 gets its index, or a written reason it needs none;
- every foreign key is indexed, or has a written reason;
- nothing more.

**The check, for the questions marked big or very frequent:** load `schema.sql` into a real database, generate data for those tables (`generate_series`), run each question with `EXPLAIN ANALYZE` and note the plan (the index used, the time) next to the question. **Measure the size of a row with its indexes on the target volume first:** the system design's guess can be off threefold. The volume: the system design's 10× when it fits on the machine; otherwise the target volume for one year, marked `[ASSUMPTION]` with the reason (from a few million rows up, the choice between reading the whole table and using the index doesn't change for these lookups, and a B-tree grows by at most one level from there to 10×). **Check the free disk first,** and tell the user that Docker Desktop may keep the space after the container is gone. **Check that each query returns rows:** a plan for an empty answer measures nothing. Keep the generator script; delete the data after. The real queries are checked again in Build, per slice.

### 6. Integrity and concurrent writes
- what the database guards (constraints) and what the code guards, each with why (a rule that needs another module's data can't be a constraint); `NOT NULL` on a column guards only new rows: an update that keeps an old value passes, so the code and a test guard it;
- the version column for optimistic locking, where the architecture asked for it: the request carries the version the screen saw and the service compares it (JPA's `@Version` compares only within one request); a change to a child row doesn't raise the parent's version unless forced (`OPTIMISTIC_FORCE_INCREMENT`); "who changed it meanwhile" needs its own column;
- the uniqueness that makes a repeated write harmless (an id made on the device, a provider's event id). **Ids chosen by a client count only among their owner's rows** (the upsert's condition includes the owner, unique keys are per owner); with an id set by the app, Spring Data's `save()` merges and overwrites, so the entity implements `Persistable`. **A thing that exists once per day is identified by its date,** not by an id each device makes: check every natural unique key against ids made on devices;
- **"changed since N" for devices:** a sequence hands out numbers before the commit, so a device can skip a row for good; the known fix is a counter per space (per person) raised at the start of every write (Replicache's per-space version), where taking the number is taking the lock;
- **counts sent by a client** are the day's totals, the greatest kept, never "+1";
- what is written in one transaction, and **which events are heard inside it and which after the commit** (a copy across modules when someone leaves a group: inside, listeners in order, a `copied_from_id`, the other modules' references moved to the copies); then check that the architecture's events, ADRs and conventions say the same;
- a one-time token: using it is deleting it (`DELETE … RETURNING`), no `used_at`.

**Reproduce every race on a real database** with two sessions at once (a number committed out of order, two writes that each see the rule kept), and keep the scripts in `checks/`.

### 7. The lifecycle, per table
- the retention from compliance and **what deletes it** (the clean-up job, a cascade, the account deletion), with the column the job reads; every period counted from a moment the server wrote, never a device's clock;
- what stays after an account is deleted, and why (the list the law keeps, the shared items with "added by" emptied); **a proof kept "for a complaint" must still be findable after the deletion** (a keyed fingerprint of the email, not the email);
- the tombstones for sync and how long they live; **deleting them needs a mark of how far they were deleted** (`purged_up_to`), so a device offline longer reloads instead of bringing a deleted row back (a "zombie", in Cassandra's word); tombstones follow "the last change wins" too;
- **look for the rows nothing deletes:** abandoned flows, addresses with no account, small totals that point to one person;
- **a provider's callback after an account is gone** (a payment webhook after the cancellation) names an id that no longer exists: saved without it, never refused forever;
- a cache of an outside service kept with the service's own limits in mind (requests a minute);
- `created_at` and `updated_at`;
- what goes into the export: everything tied to the person, technical rows included.

Every table with personal data has all of these, or the validation fails.

### 8. The data on the device
For an app that works offline, in chunks: what's written offline (the log), the copies only read, the outbox, the search and the space, a new version's shape.
- the stores, their keys and indexes, **in the API's shape:** only the key and the indexes are declared, so a new field needs no new version;
- what's a copy of the server and what's the source of truth until the server confirms; **every screen the architecture calls "offline" checked against the window kept** (an analytics screen of 90 days against 14 days kept);
- **not copied:** what can be computed from what's already there (recent items), what only an online feature uses;
- the outbox, for "the last change wins" on whole rows: one operation per row, written with the row in one transaction; send first, then receive, skipping the rows still waiting; only the server judges; an operation removed only if it didn't change meanwhile; one tab at a time (Web Locks); another account never sends the previous one's data;
- **measured in a real browser at the largest planned volume:** the search (an index against memory) and the space; a derived row kept is a denormalization with its measured reason;
- **the risk is eviction, not the quota:** the browser deletes the least recently used origin whole; Safari deletes after 7 days without use while the server's cookies stay, so the app can open logged in with an empty database: detect it at start;
- **how the shape changes in a new app version without losing what wasn't sent:** an upgrade may run offline, so the copies are never emptied (a shape number, reloaded online); IndexedDB can't open an older version, so a release that raises it is fixed forward, never rolled back, with a check in CI.

### 9. Reference data and languages
The shared data the product brings (a food database, a list of countries), in chunks: where each list lives and its categories; the sources and licences; what each value means and its unit; any formula the PRD applies to it; the import and the versions; the languages.
- **check each source's current version on its official page first;**
- where each list lives: a table the admin fills, a table written by migrations, the code plus a `CHECK`, or kept by others (time zones, VAT);
- **a source's own classification is made for its purpose:** for the product's uses (exclusions, swaps), an own list mapped from the source's codes, with a test that fails on an unknown code;
- the source and licence per value when sources mix: **a licence per value needs to know which item of the source and which version it came from** (an origins table), and the credit names each version used;
- **one definition per value,** the source's differences in a table (carbohydrates with or without fiber, crude protein); converted values marked as calculated; "traces" and "< x" kept as published; a missing value is never 0;
- units: one stored unit, what's only displayed; liquids labelled per 100 ml stored per 100 g with a density, and a conversion plus rounding can cross a physical limit (`CHECK`), so the code caps it within a margin;
- **try every PRD formula on the whole reference table before writing it** (a calorie check refused 100 correct foods of 3,286);
- how it's imported and versioned: a new version of an approved row waits in its own place, not as a second row that the unique rules refuse; **outside ids can change at every version** (find the stable key, keep the source files);
- names in several languages: search in every language, without diacritics; letters normalised in the code, not by a `CHECK`; the collation tried on the real database; a requirement like "no diacritics" is clarified first: when typing, or when shown?

### 10. The migration plan
In chunks: the tables per slice; the data of a system already running; changing a table that holds data; the locks, the migration tool and CI.
- **which tables land in which slice** of the PRD's build order: **a table lands whole, every column included, in the slice of the first feature that writes to it;** the targets of foreign keys come first. The mapping finds holes in the build order (a feature that needs another slice's feature): shown to the user with the PRD's exact new text. A table a later slice brings that every account needs (a row made at sign-up) means a data migration in that release, for the accounts already there;
- **the data of a system already running:** never a migration (it runs in every database, so personal data would land in the repository) but a one-time command through the modules' doors; the user chooses what moves; check the old data against the new rules (a uniqueness the old table didn't have); counts compared before and after;
- the rules for changes on live data: **expand, migrate, contract** (Danilo Sato, 2014: add the new next to the old, move the code, remove the old in a later release, so the previous version still runs and a rollback stays possible); a column is dropped only in a release whose previous release no longer uses it; a rename costs several releases, so the field is usually renamed in the code only;
- **the migration changes only the shape; filling rows is a job,** in batches by key range, only the empty rows; a row the devices copy takes a new sync number;
- **measured on step 5's volume,** with the scripts kept: one `UPDATE` against batches (the longest wait a person's save sees), a migration waiting behind a long read with and without a short `lock_timeout`, `SET NOT NULL` against `NOT VALID` then `VALIDATE`, `CREATE INDEX` against `CONCURRENTLY`; which `ALTER TABLE` forms rewrite the table, checked on the official page;
- **the migration tool's settings,** checked on its pages: an index built concurrently alone in its file, outside a transaction (and Flyway's PostgreSQL transactional lock off for it); future migrations ignored, so the previous version can start after a rollback; the lock timeout only on the tool's connection; a failed concurrent index leaves an invalid one, so its file drops it first;
- a migration once applied never changes; a mistake is fixed by a new one;
- **what CI flags:** a migration linter (Squawk for PostgreSQL) for the forms that lock, a `DROP` or a rename in the same release as the code that stops using it, a changed applied migration, an `UPDATE` on a table with rows;
- how the documents stay true once the migrations are the truth (compared at the end of each slice).

### 11. Test data
**Invented, never copied from production,** not even masked (pseudonymised data is still personal data, GDPR Recital 26; health data on a laptop is a breach waiting to happen):
- **the seed for the local start:** one invented person per state a screen or a rule must show; written through the modules' doors where the architecture says so; growing with the slices; dates counted back from today, so the screens are never empty; emails on a domain reserved for examples; the reference data through the real import, with a fake AI answering from a file; only in the local profile, checked by a test;
- **the factories in the tests:** one builder per entity (Nat Pryce's test data builders) with defaults that pass every rule, saved through the module's door; states in time reached by moving the fake clock; each test its own person, never the seed's; a few named presets built on the builders; no random values outside property tests;
- the end-to-end tests: the seed's shared part, and each test signs up its own person;
- the volume generator from step 5: SQL straight into the tables, for speed; run by hand at the end of each slice, not in CI.

### 12. The big decisions become ADRs
Only one-way doors (for example foreign keys across modules, the ids, the shape of a large denormalized snapshot, the order of sync, how deletion works). First propose the list, with **what doesn't get an ADR and why** (grouped: rules in the code, the process, what other documents own, what puts no data at risk). When a decision was already taken in the steps, write the ADR and give it to the user to check, a few at a time. Otherwise one at a time: options, your recommendation, **the user chooses**. **After each ADR, re-read the earlier files it changes,** the architecture's and the earlier ADRs included, link each decision to its ADR, and look for the old version of a decision that changed during the steps.

### 13. Check it
- every glossary entity has a table, or a reason it doesn't (a word of the PRD that's computed, not stored, is written as such);
- every table has one owner module, a retention and something that deletes it;
- every table with personal data is in the export and the deletion, and named so the guard test sees it;
- every question has an index and every foreign key is covered; the big ones have a checked plan, on an answer that isn't empty;
- the types follow the rules above; the conventions are applied;
- the markdown tables and `schema.sql` agree, and `schema.sql` runs; the counts the files claim match the database's catalog;
- every new read between modules is in the architecture's list of dependencies, and makes no cycle;
- nothing contradicts the architecture, compliance or the system design.

Run the check with a **separate agent** that has only the documents (`/data-model validate <folder>`), then verify its findings in the files before showing them: it can be wrong. Look especially for **contradictions left by a changed decision**, above all in the files the step didn't touch (another ADR, the conventions, compliance), and for retention periods that differ from compliance's.

Write as you go: each step's file once the user confirms it, with a journal line in the README; **the README's summary, "not doing" and glossary grow with the steps** (a glossary line for every term the files use), not at the end. At the end, set this step's row in `docs/02-design/README.md` to done, with the date, and link the folder.

```
docs/02-design/04-data-model/
  README.md               the entry: status, summary, the conceptual diagram, files, what we skip, open questions, ADRs, glossary, journal
  01-entities.md          02-queries.md            03-integrity.md
  04-lifecycle.md         05-device.md             06-reference-data.md
  07-migrations.md        08-test-data.md
  tables/                 one file per module: [module].md
  schema.sql              every schema, table and index, run on a real database
  checks/                 the volume generator and the EXPLAIN queries of step 5
  diagrams/               the conceptual model (by hand), one per module (generated): .puml + SVG
docs/00-project/adr/
  NNNN-[title].md …
```

The README:

````markdown
# Data model – [Product]
| | |
|---|---|
| **Status** | draft / confirmed by [who], [date] |
| **Author** | |
| **Updated** | |
| **Next** | 05 API design, 06 UI design |
## In one page
The entities, the main choices (ids, types, deletion, the big tables), the volumes: 5–6 lines, and the conceptual diagram.
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
| `01-entities.md` | the diagram; `\| Entity \| Module \| What it is \|`; `\| From \| To \| Cardinality \| Why \|` |
| `02-queries.md` | `\| # \| Module \| Question \| How often \| Rows now / at 10× \| Index \| Checked plan \|` |
| `tables/[module].md` | the module's diagram; per table `\| Column \| Type \| Required \| Default \| Rule \| Why \| Personal / health \|`; the keys with their delete rule; the indexes; the retention and the export |
| `03-integrity.md` | `\| Rule \| Guarded by (database / code) \| Why \|`; concurrency; idempotency; links between modules |
| `04-lifecycle.md` | `\| Table \| Kept \| Deleted by \| Column read \| After account deletion \| In the export \|` |
| `05-device.md` | `\| Store \| Key \| Indexes \| Copy or source of truth \|`; version changes; space |
| `06-reference-data.md` | sources and licences, import and versions, languages, units |
| `07-migrations.md` | `\| Slice \| Tables \|`; the rules for live changes; what CI flags |
| `08-test-data.md` | the seed, the factories, the volume generator |

And one file per decision in `docs/00-project/adr/NNNN-[title].md`, with the same sections as every ADR: status, date, context, options (for and against), decision, consequences, revisit when.

## Validate mode
`/data-model validate <folder>`: judge an existing data model, change nothing.
1. Read the folder, `schema.sql`, its ADRs and the README's journal, the PRD, the system design, the compliance folder, the architecture, and the database or migrations if they exist.
2. Check the template and "Done when" item by item, citing the lines.
3. Then ask: does every glossary entity have a table? Does every table have one owner, a retention and something that deletes it? Is every table with personal data in the export and the deletion, named so the guard test sees it? Does every question have an index, every foreign key a covering index or a reason? Do the types follow the rules (no `timestamp` without a zone, no `float` for money, no `varchar(255)` by habit)? Is every denormalization argued? Do the markdown and `schema.sql` agree, column by column, and does `schema.sql` run? Do the counts the files claim match the database's catalog? Does every checked plan run on an answer that isn't empty? Does any retention differ from compliance's, any owner or read between modules from the architecture's? Is every term explained? **Then the decisions that changed during the steps** (the journal's "changed", "corrected"): is the old version still written anywhere, above all in files the step didn't touch (another ADR, the conventions, compliance, the PRD)?
4. Report: findings by severity, each with the line, what's wrong and what to change; then what's done well; then what you couldn't evaluate. The user picks what to apply.

## The bad version and why not
- Tables generated from the classes at start: nobody sees the change until it's in production, and a column gets dropped by accident.
- Everything `varchar(255)` and nothing required: bad data gets in on day one and you clean it forever.
- `timestamp` without a time zone and `float` for money and grams: the wrong day after daylight saving, cents that go missing.
- No foreign keys "for speed": orphan rows that point at nothing.
- An index on every column, or none: slow writes, or a query that works on 100 rows and times out on a million.
- `deleted_at` everywhere: every query must remember the filter, and GDPR asks for real deletion anyway.
- A generic name–value table, or one `jsonb` for everything: types, constraints and speed lost.
- Denormalized from the start "to be fast": the same fact in three places, with three values.
- A migration that renames a column in the same release as the code: the previous version breaks, and rolling back breaks everything.
- Production data copied for tests: health data on a laptop.
- Filling a big table inside a migration: the app stays down while it fills, and every save waits behind the locked rows.
- A migration waiting for its lock with no timeout: every request on that table queues behind it, and the app stops for as long as the longest transaction lasts.

## What breaks if you skip it
The first PR decides the tables, in a hurry. Bad data gets in on day one and never leaves. A query works on your own data and falls over at the first thousand users. Export and deletion miss a table, so a GDPR request gets an incomplete answer. A table change on live data locks the app or stops it. And when the code moves to another platform, the mistakes in the data move with it.

## The principle behind it
**Data outlives code.** The application gets rewritten; the data stays and moves along with its mistakes. So the important rules live in the database, where every piece of code that writes must respect them, today and in ten years. Fred Brooks made the point in *The Mythical Man-Month* (1975): show the tables, and the rest of the program becomes obvious. Design for the real questions and for how long the data lives, not for a pretty shape on paper.

## How to apply it at work
- At a new company, read the database schema before the code (a diagram generated from the database, for example with DBeaver).
- In code review, for a migration ask: does it lock the table (a linter such as Squawk answers most of it)? Does the previous version of the code still work with it? Does it fill rows that should be a job? Does every new foreign key have an index?
- For a new index, ask for the question and its plan (`EXPLAIN ANALYZE`); for a denormalization, the written reason.
- For a GDPR request, know where every piece of personal data is: the data dictionary, with its "sensitive" column.
- As a senior or CTO: an owner for every data set (data ownership), a data classification (public, internal, personal, special category), retention policies, data contracts between teams that hand each other data, a data catalog; analysis in a separate data warehouse, never on the application's database.

## Done when
- [ ] the conceptual model: entities per module from the glossary, relations and cardinality, one diagram; chosen by the user
- [ ] the important questions per module, with frequency and rows now and at 10×; the big ones marked
- [ ] every table: columns with type, required, default, rule, why, personal or health data; keys with their delete rule; chosen by the user where there was a choice
- [ ] links between modules decided once, with their argument card
- [ ] `schema.sql` holds every table and index and runs on a real database of the chosen version; it agrees with the markdown
- [ ] every question has an index or a reason; every foreign key is covered; the big questions have a plan checked with `EXPLAIN ANALYZE` on generated data, the volume argued
- [ ] what the database guards and what the code guards; optimistic locking and idempotency where needed
- [ ] every table: retention, what deletes it, what stays after account deletion, tombstones, the export
- [ ] the offline model on the device, with how its shape changes between versions
- [ ] reference data, languages and units
- [ ] the migration plan: the tables per slice, the data of a system already running, the rules for live changes measured on generated data, the migration tool's settings, what CI flags
- [ ] invented test data: seed, factories, volume generator
- [ ] every one-way door an ADR, chosen by the user; the earlier files re-read after each one
- [ ] a glossary for every term the files use, grown with the steps
- [ ] the README: status, summary, what we skip and why, open questions, the ADR table
- [ ] the row in `docs/02-design/README.md` set to done
- [ ] every column in the tables' pages exists in `schema.sql` and every column of `schema.sql` has a row, or is marked with the slice that adds it; the generator rerun writes the same files
- [ ] every diagram drawn by `diagrams.sh` (the modules generated from `schema.sql`), opened, no text overlapping

## Next
API design (`/api-design`) and UI design (`/ui-design`): the API exposes what the screens need, not the tables' shape. Then Security (`/security`) checks it all, Row-Level Security and database access included.
