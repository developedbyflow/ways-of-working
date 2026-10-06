# Code review

- **Use it when:**
  - you review a colleague's PR or code written by AI;
  - you check your own diff before a PR (`/wow-pr` runs this).
- **What you get:** comments labelled by severity, each blocker with what breaks, plus the checks AI-written code needs.
- **Run it:** `/wow-review PR #42`
- **Not when:** you want to check a whole area of the app → `/wow-audit`.
- **Reads:** the ticket and its criteria, the diff, `docs/definition-of-done.md`, the conventions in `CLAUDE.md`, the ADRs in `docs/adr/` that the change touches, the design doc in `docs/design/` if there is one, `REPO-MAP.md`.
- **Writes:** comments labelled by severity; `docs/tech-debt.md` for accepted shortcuts.

## Steps
1. **What was asked:** read the ticket before the diff.
   - Skip it → you review style and miss that it doesn't do the job.
2. **Spec pass:** for each criterion, where it is in the code and which test covers it. Question anything that wasn't asked for.
   - Skip it → missing requirements and extra scope both get in.
3. **Standards pass**, done separately, with the list below.
   - Skip it → bugs hide behind "it does what was asked".
4. **Run it** when CI can't show it: UI changes in the browser (states, keyboard), risky logic locally.
5. **Comments:**
   - label each one: blocker, should, nit, question;
   - a blocker says what breaks and suggests the fix;
   - say what's good, too.
   - STOP: blockers must be fixed; the author decides on should and nit.
6. **Can you explain every line?** If not, ask. Never approve what you can't explain.

## Standards
- **Correctness:** empty lists, null, two requests at once, pagination, time zones, rounding.
- **Errors:**
  - no empty `catch`, no swallowed errors;
  - no `any`, `!` or `as` hiding a problem;
  - the user sees a clear state.
- **Security:**
  - validation on the server;
  - authorization per operation and per object;
  - no secrets, no SQL built from strings, no unsanitized user content in `dangerouslySetInnerHTML`.
  - The full list: `audits/security.md`.
- **Data:** the migration is safe for the running version; no N+1 queries; an index for each new query.
- **Tests:**
  - they test behavior, not mocks;
  - a changed test comes with a reason;
  - no deleted or skipped tests.
- **Design:**
  - reuses what exists, follows the conventions and the ADRs, adds no layer nobody asked for;
  - if the structure changed, `REPO-MAP.md` is updated.
- **Logs:** errors logged with context, no personal data.

## Code written by AI: check also
- **Invented APIs:** methods or options that don't exist in your version. Check the types or the docs.
- **New packages:** each one exists, is maintained, and has exactly the right name. Look-alike names are a known attack.
- **Silently dropped requirements:** it says "done" and skipped one.
- **Fake tests:** they mock the very thing under test, or only check the mock.
- **Plausible but wrong:** code that looks right. Run it.

## Done when
- [ ] every criterion is matched to code and a test
- [ ] every blocker says what breaks
- [ ] you can explain every line

## Concepts if you get stuck
- Review as a lead
- Principles and patterns
- Security
- Tests

## Next level
- Review within one working day, and keep PRs small.
- `staff` Turn comments you keep repeating into lint rules or CI checks.

## Next
`/wow-pr` on the author side, `/wow-refactor` for larger fixes. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
