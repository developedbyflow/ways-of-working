# TDD

- **Use it when:** you write code yourself: logic, an endpoint, a bug fix, a refactor.
- **Not when:**
  - a screen you've never built → try it first (`/wow-spike`), then write the tests;
  - a throwaway prototype.
- **Reads:** the acceptance criteria, or the bug's failing case.
- **Writes:** tests and code, in small commits.

## The loop
1. **The list:** the behaviors to build, written as test names, simplest first.
2. **Red:** one test for the next behavior. Run it and watch it fail for the right reason.
   - Skip it → a test that passes no matter what.
3. **Green:** the simplest code that makes it pass.
   - Skip it → code that no test asked for.
4. **Clean up:** remove duplication, improve names. The tests stay green.
   - Skip it → the code gets worse one green test at a time.
5. **Commit**, then back to the next test on the list.

STOP: when a test is hard to write, the design is telling you something, usually that there are too many dependencies. Run `/wow-grill` on it, or refactor first.

## Which test where
- **Logic:** a unit test, no mocks needed.
- **Endpoint:** an integration test with a real database in a container (`WebApplicationFactory` in .NET).
- **Component:** React Testing Library with the API mocked by MSW. Find elements by role and label, the way a user would.
- **The whole flow:** one Playwright test for the golden path.

Test the behavior (inputs and outputs), not the implementation (private methods, internal calls).

## Done when
- [ ] every criterion has a test
- [ ] all tests are green
- [ ] no test only checks a mock

## Concepts if you get stuck
- Testing in .NET
- Testing the frontend

## Next level
- Mutation testing on critical logic (Stryker): it checks that your tests catch a changed line.
- `staff` Test conventions for the team.

## Next
Back to `/wow-feature`, `/wow-bug` or `/wow-refactor`, then `/wow-pr`.

## Changelog
- 2026-10-05: v1
