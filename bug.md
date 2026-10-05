# Bug

- **Use it when:** something that should work doesn't, and nobody is blocked right now.
- **Not when:**
  - users are affected right now → `/wow-incident`;
  - you want to check a whole area → `/wow-audit`.
- **Reads:** the report, logs, the error tracker, recent deploys.
- **Writes:** a failing test that becomes the regression test, the fix, the cause in the PR; `docs/tech-debt.md` when the real fix has to wait.

## Steps
1. **Reproduce:** the exact steps, data and environment.
   - STOP: if you can't reproduce it, get the logs first. Don't fix by guessing.
   - Skip it → you fix what you think the bug is, and the real one stays.
2. **A failing test** that shows the bug. It must be red → `/wow-tdd`.
   - Skip it → you can't prove the fix works, and the bug can come back unnoticed.
3. **Fix** the smallest thing that turns it green.
   - Fix more than that → the fix brings new bugs with it.
4. **Cause and prevention:**
   - one sentence in the PR on why the bug got through;
   - if a check was missing (a validation, a test, a type), add it.
   - Skip it → the same kind of bug comes back somewhere else.

## Hard bugs
When you haven't found the cause in 30 minutes:
1. **A loop that fails every time:** a test or a script you can run in seconds.
2. **Make it smaller:** remove code and data until it still fails with the least of both (a minimal repro).
3. **One guess at a time:** write the guess down, then confirm it with a log line or a breakpoint, without changing the code.
4. **Find the commit:** when it used to work, `git bisect` finds the commit that broke it.
5. **"It got slow":** measure first (a profiler, the query plan), then change one thing and measure again.

## Flaky tests
- **Run it many times** to make it fail.
- **Look for** time, test order, shared state, the network, or a missing `await`.
- **Fix the cause.** Quarantine the test only if it blocks everyone, with an owner and a date.

## Done when
- [ ] the test was red before the fix and is green after
- [ ] the PR states the cause

## Frontend · Backend · Fullstack
- **Frontend:** open the Network tab first. Is the UI wrong, or the API response?
- **Backend:** reproduce with a request in the `.http` file, then find the logs by request id.
- **Fullstack:** compare the API response with the contract. That tells you which side to fix.

## Concepts if you get stuck
- Can't see where it fails → logs and tracing → [Backend 08 Infrastructure, deploy and observability](https://claude.ai/artifact/WqBR1zmfYkwSPwatLnhhjN)
- Errors that only users see in the browser → [F16 The frontend in production](https://claude.ai/artifact/46i2EYDtDsXGonv52HDA7C)
- Breaks only when two requests run at once → [Backend 04 Databases](https://claude.ai/artifact/Knm6iRsYMHy6b8nJbZxcEE) · [Backend 10 Concurrency](https://claude.ai/artifact/RGHBDGActWbfWtioz9vm6r)
- Slow in the browser → [F00 The browser from the inside](https://claude.ai/artifact/D7a4dJ8BLUPYQ6rmWM8dfi) · [F12 Web performance](https://claude.ai/artifact/HmfCtXjvx5CPXY2tPHt8Mc)
- Slow on the server → [Backend 07 Performance](https://claude.ai/artifact/HDsFaNVTSoZC3EkyVTRngm)
- How to write the failing test → [F10 Frontend testing](https://claude.ai/artifact/CXApqj7VD4udwnpzWQcfpU) · [Backend 06 Testing](https://claude.ai/artifact/Xigv1zTb1mCCjUE4DDxxtV)

## Next level
- In production: check how many users were hit before you set the priority.
- Look for the same mistake in other places in the code.

## Next
`/wow-pr`. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
- 2026-10-05: v2 — the shared page shape, hard bugs, flaky tests.
