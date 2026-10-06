# Dependency upgrade

- **Use it when:** a new version of a framework or package comes out, a security advisory appears, or something you use is deprecated.
- **What you get:** the breaking changes found before production, one upgrade per PR.
- **Run it:** `/wow-upgrade React to the next major version`
- **Not when:** your own schema, data or API changes → `/wow-migration`.
- **Reads:** the release notes, the migration guide, the changelog, the advisory.
- **Writes:** the upgrade PR, with the breaking changes it handles.

## Steps
1. **Why, and how big:**
   - the reason: a security fix, a feature you need, or the end of support;
   - the size: patch, minor or major.
   - Skip it → you take on a major version's risk for nothing.
2. **Read the release notes and the migration guide.** List the breaking changes that touch your code.
   - Skip it → you find them in production.
3. **One upgrade per PR.** Major versions one at a time, never mixed with features.
4. **Upgrade:**
   - use the official codemod if there is one;
   - fix the deprecation warnings;
   - build and run all the tests.
5. **Try the critical paths by hand.**
   - Frontend: the bundle size before and after.
   - Backend: startup, logs, memory.
6. **A way back:** a revert is easy, unless the upgrade changes stored data (a serialization format, a database driver, migrations it runs). Then it's a `/wow-migration`.
   - STOP: a major version gets a risk line in the PR.

Commit the lockfile. To check what you have:
- `npm audit`, `npm outdated`
- `dotnet list package --vulnerable`, `dotnet list package --outdated`

## Done when
- [ ] the release notes are read
- [ ] the tests are green and the critical paths were tried
- [ ] the lockfile is committed

## Frontend · Backend · Fullstack
- **Frontend:** React, Next.js and Vite major versions come with codemods; check browser support.
- **Backend:** .NET has LTS and STS releases, with support dates on Microsoft's .NET support policy page. Upgrade EF Core with it.
- **Fullstack:** regenerate the API types if the OpenAPI tooling changed.

## Concepts if you get stuck
- Packages, lockfiles, builds
- The supply chain
- .NET project and tools

## Next level
- Renovate or Dependabot: patch updates grouped, and merged automatically when the tests pass.
- `staff` A dependency policy: allowed licenses, and how fast security fixes go in.

## Next
`/wow-pr`, `/wow-deploy`. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
