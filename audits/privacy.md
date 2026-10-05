# Privacy audit

- **Bar:** the GDPR basics:
  - a lawful reason for each kind of data;
  - only the data you need;
  - a retention limit;
  - users can exercise their rights.
- **Tools:**
  - a data inventory table;
  - a search of the logs for emails and tokens;
  - the Network tab, to see which third-party calls happen before consent.

This is an engineering checklist, not legal advice. A lawyer or the DPO confirms the legal part.

## Checklist
- [ ] **Inventory:** every kind of personal data, where it's stored (database, logs, backups, vendors), why, on which lawful basis, and for how long.
- [ ] **Only what you need:** each field is used by a feature.
- [ ] **Special categories:** health data falls under GDPR Article 9. Nutrition and weight data may count. Check which Article 9 condition you rely on, often explicit consent.
- [ ] **Consent:** analytics and marketing trackers start only after consent where it's required. Rejecting is as easy as accepting.
- [ ] **Users' rights:** users can export their data and delete it. Deletion reaches backups and vendors on a known schedule.
- [ ] **No personal data where it leaks:** not in URLs, logs, error reports, or prompts sent to AI providers, unless the feature needs it. Mask it.
- [ ] **Vendors:** every vendor that receives the data is listed, with a data processing agreement, and you know where they store it.
- [ ] **The privacy policy** matches what the app actually does.
- [ ] **A plan for a breach:** who decides, and the 72-hour notification. See `incident.md`.

## Concepts
- Security, personal data in logs → Backend 05 Security
- Privacy in the browser, consent → F13 Security in the browser
- Tracking and consent → F23 The product-minded engineer
- Security, multi-tenancy and cost → S11 Security, Multi-tenancy and Cost

## Changelog
- 2026-10-05: v1
