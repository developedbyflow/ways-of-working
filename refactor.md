# Refactor and tech debt

- **Use it when:** the code must change shape while the behavior stays the same: to make a feature easier, to remove duplication, to fix a design that hurts.
- **What you get:** cleaner code with the same behavior, in small steps a reviewer can follow.
- **Run it:** `/wow-refactor split the 900-line OrderService`
- **Not when:** the behavior changes → `/wow-feature`.
- **Reads:** `docs/tech-debt.md`, the findings from `/wow-audit architecture`, the code and its tests.
- **Writes:** code, tests, `docs/tech-debt.md` (debt paid or added).

## Steps
1. **Why now:** which change does it make easier, or which kind of bug does it remove?
   - Small cleanups go inside the feature PR. Big ones get their own.
   - STOP: worth it now?
   - Skip it → refactoring for taste: real risk, no gain.
2. **A safety net:** tests that lock in today's behavior, written before you touch anything. If the code can't be tested, the first change is the smallest one that makes it testable.
   - Skip it → you change the behavior without noticing.
3. **Small steps:** one refactoring at a time (rename, extract, move, inline), tests green after each, a commit after each. Use the IDE's automatic refactorings.
   - Skip it → a 2,000-line diff nobody can review.
4. **Big changes:** write the new code next to the old, move the callers one by one, delete the old at the end. No long-lived branch.
5. **Separate PRs:** a refactor PR doesn't change behavior, and a feature PR doesn't refactor much.
   - Skip it → a reviewer can't tell which change caused what.
6. **Update `docs/tech-debt.md`:** what was paid, what remains.

## Done when
- [ ] the behavior is unchanged: the same tests are green, and none were edited except to move them
- [ ] `docs/tech-debt.md` is updated

## Concepts if you get stuck
- Principles and patterns
- Application architectures
- Components and hooks
- Frontend architecture

## Next level
- Deep modules: a lot of behavior behind a small interface, with no layers that only pass calls through.
- `staff` A tech-debt budget each quarter, spent on the debt that costs the most.

## Next
`/wow-tdd`, `/wow-pr`. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
