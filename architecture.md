# Architecture

- **Use it when:** a new system, or a big change to how the parts fit together: a new service, a new data flow, a new need for scale or reliability.
- **Not when:**
  - one feature's tables or endpoint → `/wow-data-model`, `/wow-api-design`;
  - checking code that already exists → `/wow-audit architecture`.
- **Reads:** the problem and its numbers, `docs/adr/`, `REPO-MAP.md`.
- **Writes:** `docs/architecture.md` with the C4 diagrams, ADRs, `docs/risks.md`.

## Steps
1. **Requirements:**
   - the 3–7 main jobs of the system;
   - the qualities, with numbers: users, requests per second at peak, data size, latency target, availability, and what must never be lost.
   - STOP: confirm the numbers.
   - Skip it → you design for a scale you don't have, or miss the one you do.
2. **Estimates:** a quick calculation of storage per year, peak traffic and bandwidth.
   - Skip it → choosing a cache or a queue becomes a guess.
3. **Context and containers (C4 levels 1 and 2):**
   - who uses the system and which external systems it talks to;
   - the parts you deploy (web app, API, database, queue, workers) and how they talk to each other.
   - Default: one API and one database, until a number says otherwise.
4. **Data:** where each piece of data lives, who owns it, and how it flows. What must be correct right away, and what can be correct a little later. The details → `/wow-data-model`.
5. **Frontend:**
   - how each type of page is rendered (CSR, SSR, SSG, ISR);
   - which state is server data and which is UI state;
   - how the frontend talks to the API.
6. **Failure modes:** for each dependency, what happens when it's slow, down, or returns garbage. Timeouts, retries, fallbacks, and what the user sees.
7. **Threats:** what you protect (personal data, money, accounts), what can go wrong, and how you prevent it. Use STRIDE as the checklist.
8. **Scale and cost:** what breaks first at 10× the traffic, and what the system costs per month now and at 10×.
9. **Decisions:** the 2–3 big choices go through `/wow-grill` and become ADRs.
   - STOP: you choose.
   - Skip it → the architecture is whatever the first PRs made it.

## Done when
- [ ] the context and container diagrams exist
- [ ] the numbers, the failure modes and the threats are written
- [ ] the ADRs and risks are written

## Frontend · Backend · Fullstack
- **Frontend:** rendering, routing, state, the size budget for the JavaScript bundle.
- **Backend:** modules and their boundaries, the data store, what runs now and what goes to a queue, background jobs.
- **Fullstack:** where the logic lives, the contract, the login flow end to end.

## Concepts if you get stuck
- Numbers and estimates
- Requirements and trade-offs
- The building blocks
- Reliability
- Scaling
- Security and cost
- Application architectures
- Scaling and distributed systems
- System design
- Frontend architecture

## Next level
- Lint rules or tests that enforce the module boundaries.
- `staff` A one-year technical vision for the system.

## Next
`/wow-data-model`, `/wow-api-design`, `/wow-ui-design`, `/wow-design-doc`, `/wow-plan`. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
