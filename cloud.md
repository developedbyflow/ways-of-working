# Cloud and infrastructure

- **Use it when:** servers, containers, databases, DNS, TLS certificates, storage, secrets or networking are created or changed.
- **Not when:** you ship a new version of the app → `/wow-deploy`.
- **Reads:** `docs/architecture.md`, `docs/runbook.md`, the provider's docs and pricing.
- **Writes:** the infrastructure as code, the runbook, an ADR for each provider choice, a cost alert.

The skill gives you every command. You run them.

## Steps
1. **What and why:** the change, its cost per month, and what depends on it.
   - STOP: confirm the cost.
2. **Written as code, in the repo:**
   - Terraform or OpenTofu, or Docker Compose plus a setup script for a single server;
   - no manual clicks, except to look;
   - reviewed like code.
   - Skip it → nobody can rebuild it after a failure.
3. **Plan before apply:** read the diff (`terraform plan`). A destroy or a replace on a database is a stop sign.
   - STOP: you approve the plan, and you run the apply.
4. **Security:**
   - least privilege: roles, not root keys;
   - the database is never public;
   - the firewall opens only what's needed;
   - secrets live in a secret manager and get rotated;
   - TLS everywhere, with certificates that renew automatically.
5. **Data:** automated backups, encryption at rest, and a restore you have tested.
   - Skip it → the first restore you try is during an outage.
6. **Environments:** staging and production come from the same code, with different variables.
7. **Cost:** a budget alert, labels per environment, and nothing left running unused.
8. **Runbook:** how to rebuild, restore, rotate a secret and renew a certificate.

## Done when
- [ ] the change is code, and it was reviewed
- [ ] you approved the plan
- [ ] backups and alerts are set
- [ ] the runbook is updated

## Frontend · Backend · Fullstack
- **Frontend:** CDN, cache headers, domain and TLS.
- **Backend:** database, compute, networking.
- **Fullstack:** CORS and cookie domains match where things are hosted.

## Concepts if you get stuck
- Infrastructure, deploy, observability → [Backend 08 Infrastructure, deploy and observability](https://claude.ai/artifact/WqBR1zmfYkwSPwatLnhhjN)
- Cloud on AWS → [Backend 14 Cloud on AWS](https://claude.ai/artifact/4bAfWqV5qzggpBByBkPqGr)
- Infrastructure as a design problem → [S15 Infrastructure as a Design Problem](https://claude.ai/artifact/1o1vXu2ap4sHCEYphd41pK)
- Cost → [S11 Security, Multi-tenancy and Cost](https://claude.ai/artifact/QfiYqZe1T5h1Y2NMkKMV9S)

## Next level
- A written plan for losing the server or the region: what you restore, where, and how long it takes.
- `staff` Platform templates other teams can reuse.

## Next
`/wow-deploy`, `/wow-audit production-readiness`, `/wow-audit cost`. End with `/wow-retro`.

## Changelog
- 2026-10-05: v1
