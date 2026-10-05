# Production readiness audit

- **Bar:** you can see it break, undo the change, and get the data back.
- **Tools:**
  - the dashboards;
  - the error tracker;
  - one practice run of the rollback and one of the restore.

## Seeing it break
- [ ] Structured logs, with a request id that follows a request from the frontend through the backend.
- [ ] Error tracking on the frontend and the backend, grouped by release.
- [ ] Health check endpoints.
- [ ] Latency, errors and traffic tracked for the key paths, on a dashboard.
- [ ] Alerts on what users feel (error rate, latency), sent somewhere you will see them.

## Undoing it
- [ ] Deploys go through the pipeline. The rollback command is known, practiced and timed.
- [ ] Migrations are backward compatible.
- [ ] Risky features have a flag that turns them off.

## Getting the data back
- [ ] Automated backups, encrypted, and the restore has been tested. A backup you have never restored doesn't count.

## When something it depends on fails
- [ ] Every outgoing call has a timeout. Retries only where they're safe.
- [ ] You know what the user sees when each dependency is down.
- [ ] Public endpoints have rate limits.

## The rest
- [ ] Security: secrets, HTTPS, dependency scan → `audits/security.md`.
- [ ] Runbook: restart, roll back, restore, rotate a secret, and where the logs are.
- [ ] Cost: budget alerts, plus usage limits on AI APIs.

## Concepts
- Infrastructure, deploy, observability
- The frontend in production
- Reliability
- Build and deploy

## Changelog
- 2026-10-05: v1
