# Migration

- **Use it when:**
  - you change something in production that others depend on: a database schema, existing data, an API contract;
  - you move to a new library, framework or system;
  - you run a one-off data fix.
- **Not when:** a package version changes → `/wow-upgrade`.
- **Reads:** the data model, the API consumers, the runbook.
- **Writes:** the migration scripts, the plan with its steps, a runbook entry, an ADR for big moves.

## The pattern: expand, migrate, contract
1. **Expand:** add the new next to the old (a new column, table, endpoint, or code path). The old one keeps working. Deploy.
2. **Migrate:**
   - write to both, or keep them in sync;
   - copy the old data in batches;
   - move the readers and callers one at a time;
   - check the counts.
3. **Contract:** when nothing uses the old anymore, remove it. Deploy.

Each step is its own deploy, and each one can be undone on its own.

## Steps
1. **Inventory:** who reads or writes what will change. Search the code, the logs of API calls, the queries.
   - Skip it → you break a consumer you didn't know about.
2. **The plan:** the expand, migrate and contract steps, and how to undo each one.
   - STOP: approve the plan.
3. **Locks:** on big tables, check which statements lock or rewrite the table. Create indexes concurrently, and copy data in batches, off-peak.
   - Skip it → the migration locks the table and the app stops answering.
4. **Verify after each step:** counts, sample comparisons, error rates.
5. **Remove the old** only after a quiet period.

## One-off data fix
- Write it as a script in the repo, and get it reviewed.
- Run it on a copy first.
- Take a backup, or write the undo.
- Run it in a transaction when you can, and log what changed (the ids).
- STOP: you run it, not the skill.

## Moving to a new library or framework
The same pattern: the new next to the old, one screen or module at a time, then remove the old.

## A breaking API change
- Add a new version or a new field.
- Announce the deprecation with a date.
- Watch how much the old one is still used, and remove it when nobody uses it.

## Done when
- [ ] every step is deployed and verified
- [ ] the old is removed
- [ ] the runbook is updated

## Concepts if you get stuck
- Migrations, locks, transactions → [Backend 04 Databases](https://claude.ai/artifact/Knm6iRsYMHy6b8nJbZxcEE)
- API versioning → [Backend 03 REST API design](https://claude.ai/artifact/YLjb5zpeL3ZT1zjvPWf95y)
- Migrations in the real world → [S17 Design in the Real World](https://claude.ai/artifact/LaCpLgDSkShGP185VnvTqC)
- Moving a big frontend step by step → [F14 Frontend architecture at scale](https://claude.ai/artifact/Gur1WgSsBwhrSBQMNmHBNS)

## Next level
- `staff` Migrations across teams, with a tracker of who has moved.

## Next
`/wow-deploy` for each step. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
