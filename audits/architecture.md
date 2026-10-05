# Architecture audit

- **Bar:** changes stay local: a typical feature touches one module, there are no dependency cycles, and the boundaries are enforced.
- **Tools:**
  - a dependency graph: dependency-cruiser or madge for TypeScript, NetArchTest or the project references for .NET;
  - co-change from git: files that always change together;
  - file size and complexity;
  - the bug list, by module.

## Checklist
- [ ] UI, domain and data are separated, and dependencies point one way.
- [ ] No dependency cycles.
- [ ] No deep imports across features. Each module has a public entry point.
- [ ] Modules are deep (a lot of behavior behind a small interface), not chains of small layers that only pass calls through.
- [ ] Each business rule lives in one place.
- [ ] The files that change most often and are also the most complex are listed. They are the first candidates for a refactor.
- [ ] Tests can reach each module's behavior through its public interface.
- [ ] The ADRs are still true.

Each finding → `/wow-refactor`. Each debt you accept → `docs/tech-debt.md`.

## Concepts
- Principles and patterns → [Backend 09 Principles and design patterns](https://claude.ai/artifact/5VQW732q4HnJh5QBQApgAz)
- Application architectures → [Backend 11 Application architectures](https://claude.ai/artifact/2TucUS8p9GBDP2FvaxKJHQ)
- Frontend architecture → [F14 Frontend architecture at scale](https://claude.ai/artifact/Gur1WgSsBwhrSBQMNmHBNS) · [F18 Frontend system design](https://claude.ai/artifact/AGaPnkiHcDTebbT56VyUC3)

## Changelog
- 2026-10-05: v1
