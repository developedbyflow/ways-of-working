# Data model

- **Use it when:** you design new tables, or a change to existing ones, for a feature or a system.
- **Not when:** the design is done and the tables already in production must change → `/wow-migration`.
- **Reads:** `GLOSSARY.md`, the acceptance criteria, the current schema.
- **Writes:** the table diagram (in the ticket or the design doc), the migration code, `GLOSSARY.md`.

## Steps
1. **Entities:** the nouns of the domain, named with the words from the glossary, each with one line.
   - Skip it → the same thing gets two names ("order" and "purchase") in the code and in the database.
2. **Relations:** one-to-many, many-to-many (through a join table), and ownership: who deletes what.
3. **Tables:**
   - columns with their types, `NOT NULL` by default;
   - a primary key, plus unique constraints on the natural keys;
   - foreign keys and check constraints.
   - Money as an integer in minor units, or `numeric`; never a float. Time as `timestamptz`, in UTC.
   - Normalize first; denormalize only when a measurement gives you a reason.
   - Skip it → bad data gets in, and you clean it forever.
4. **The queries the app will run:** list them from the screens and the endpoints. Each one gets an index plan, checked with `EXPLAIN ANALYZE` on realistic data.
   - Skip it → it works on 100 rows and times out on a million.
5. **Two writes at once:** what happens if two requests change the same row (stock, balance)? Use a transaction, a version column (optimistic concurrency), or a constraint.
   - Skip it → one update silently overwrites the other.
6. **Lifecycle:**
   - soft delete or hard delete;
   - how long personal data is kept, and how one user's data gets deleted;
   - `created_at` and `updated_at` columns.
7. **How it reaches production** → `/wow-migration`.
   - STOP: review the schema before the migration is written.

## Done when
- [ ] the table diagram exists
- [ ] every query has an index plan
- [ ] the constraints enforce the rules
- [ ] personal data has a retention rule

## Frontend · Backend · Fullstack
- **Backend:** you own the model.
- **Frontend:** the API returns what the screen needs, not the shape of the tables.
- **Fullstack:** the table shape never leaks into the contract.

## Concepts if you get stuck
- Relations, normalization, constraints, indexes, transactions, migrations → Backend 04 Databases
- How storage engines work → S03 Storage Internals
- Two writes at once → Backend 10 Concurrency

## Next level
- `staff` Data ownership across services: one owner per table.

## Next
`/wow-migration`, `/wow-api-design`. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
