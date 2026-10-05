# Testing audit

- **Bar:** the critical flows are tested at the right level, and the suite is fast and trusted.
- **Tools:** CI test reports and timings, coverage on the critical modules, the list of flaky tests.

## Checklist
- [ ] Every critical user flow has a test at the right level: unit, integration, component or end-to-end.
- [ ] 1–3 end-to-end golden paths, and they are stable.
- [ ] Integration tests use a real database in a container, not a mocked ORM.
- [ ] No flaky tests. Each one is fixed, or quarantined with an owner and a date.
- [ ] Tests check behavior, not implementation. No test only checks a mock.
- [ ] Test data comes from factories. No shared data that tests change.
- [ ] The PR checks run under the time limit you set.
- [ ] Contract tests fail when the API breaks its contract.
- [ ] Tests run on every PR, and failing tests block the merge.

## Concepts
- Testing in .NET → [Backend 06 Testing](https://claude.ai/artifact/Xigv1zTb1mCCjUE4DDxxtV)
- Testing the frontend → [F10 Frontend testing](https://claude.ai/artifact/CXApqj7VD4udwnpzWQcfpU)

## Changelog
- 2026-10-05: v1
