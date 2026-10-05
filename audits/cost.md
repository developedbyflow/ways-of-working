# Cost audit

- **Bar:** you know the monthly cost and the cost per user, and an alert fires before a surprise.
- **Tools:** the providers' billing dashboards, cost by tag or label, the AI provider's usage page.

## Checklist
- [ ] **Monthly cost** by service and environment, plus the cost per active user or per order.
- [ ] **Budget alerts** on every account: cloud and AI APIs.
- [ ] **Unused resources:** idle servers, old snapshots, unattached volumes.
- [ ] **Right size:** the CPU and memory you use vs what you pay for.
- [ ] **Outgoing traffic** (egress) and CDN usage.
- [ ] **AI:**
  - tokens per request;
  - answers cached where they repeat;
  - a cheaper model wherever the quality holds;
  - limits per user.
- [ ] **Logs and metrics:** how long they're kept. It's often the hidden cost.

## Concepts
- Security, multi-tenancy and cost → S11 Security, Multi-tenancy and Cost
- Cloud on AWS → Backend 14 Cloud on AWS
- Scaling in practice → S10 Scaling in Practice
- AI in the backend → Backend 17 AI in the backend

## Changelog
- 2026-10-05: v1
