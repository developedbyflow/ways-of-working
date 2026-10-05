# Performance audit

- **Bar:**
  - **Frontend:** the "good" Core Web Vitals at the 75th percentile: LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 (web.dev).
  - **Backend:** the p95 latency target you set for each endpoint.
- **Tools:**
  - **Frontend:**
    - PageSpeed Insights: real-user data from CrUX, plus a lab run;
    - Lighthouse;
    - the DevTools Performance panel;
    - a bundle analyzer.
  - **Backend:**
    - traces or logs with durations;
    - `EXPLAIN ANALYZE`;
    - a load test (k6) on the critical endpoints.

Measure before and after, on data shaped like production's.

## Frontend
- [ ] **The largest element (LCP):** the image is sized, in a modern format, loaded with high priority, and not lazy-loaded. The server answers fast.
- [ ] **JavaScript:** a size per route, split by route, with no heavy library you don't need.
- [ ] **Interactions (INP):** no long tasks when the user clicks or types. Heavy work is split up or moved off the main thread.
- [ ] **Layout shift (CLS):** images and embeds have dimensions, late content has space reserved, fonts have fallbacks with matching metrics.
- [ ] **Data:** no request waterfalls; HTTP cache headers and a CDN for static files.
- [ ] **Long lists** are virtualized.

## Backend
- [ ] No N+1 queries.
- [ ] No sequential scans on big tables: every frequent query has its index.
- [ ] Every list query is paginated.
- [ ] Every outgoing call has a timeout. Slow work that can wait goes to a background job.
- [ ] Data that is read far more often than it's written is cached, with a clear rule for when the cache gets updated.
- [ ] Connection pool size and memory use are checked under load.

## Concepts
- Web performance → [F12 Web performance](https://claude.ai/artifact/HmfCtXjvx5CPXY2tPHt8Mc)
- The browser rendering pipeline → [F00 The browser from the inside](https://claude.ai/artifact/D7a4dJ8BLUPYQ6rmWM8dfi)
- React rendering → [F05 React from the inside](https://claude.ai/artifact/F91AQzCWCkvxBBYicoN8Gu)
- Backend performance → [Backend 07 Performance](https://claude.ai/artifact/HDsFaNVTSoZC3EkyVTRngm)
- Indexes and query plans → [Backend 04 Databases](https://claude.ai/artifact/Knm6iRsYMHy6b8nJbZxcEE)
- Scaling → [S10 Scaling in Practice](https://claude.ai/artifact/GwF4qx1zxYxaqyPkFGhCmn)

## Changelog
- 2026-10-05: v1
