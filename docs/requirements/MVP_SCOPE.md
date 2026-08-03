# PICIP Minimum Viable Product (MVP)
Version: 1.0
Status: Draft
Phase: 3.5 – Architecture Consolidation

---

# 1. Objective

The objective of the PICIP MVP is to deliver a reliable intelligence platform
capable of automatically collecting, processing, analysing and presenting
strategic information from trusted information sources.

The MVP focuses on stability, automation and maintainability rather than
supporting every possible feature.

---

# 2. Functional Scope

The MVP shall support the complete processing pipeline:

Information Sources
        ↓
Collection
        ↓
Source Detection
        ↓
Parsing
        ↓
Normalization
        ↓
AI Intelligence
        ↓
Database
        ↓
Notifications
        ↓
Dashboard

---

# 3. Collection

The platform shall:

- Collect RSS feeds
- Collect supported news websites
- Support scheduled collection
- Detect unavailable sources
- Record collection status

---

# 4. Parsing

The platform shall:

- Detect source automatically
- Dispatch the correct parser
- Produce normalized article objects
- Support future parser expansion

Initially supported:

- ANGOP

Future sources:

- BBC
- Reuters
- VOA
- Government portals

---

# 5. Intelligence

The MVP shall generate:

- Summary
- Sentiment
- Classification
- Topic detection
- Risk analysis

The intelligence layer shall remain provider-independent.

---

# 6. Database

The MVP shall store:

- Sources
- Articles
- Processing status
- AI analysis
- Notification history
- Audit timestamps

---

# 7. Notifications

The MVP shall:

- Detect important articles
- Generate alerts
- Deliver notifications through the Node.js service

---

# 8. Dashboard

The MVP dashboard shall provide:

- Recent articles
- Search
- Filters
- AI summary
- Sentiment
- Categories
- Risk level
- Source information
- Processing status

---

# 9. Administration

Administrators shall be able to:

- Enable or disable sources
- Monitor source health
- Review processing logs
- Monitor collection jobs

---

# 10. Non-Functional Requirements

The MVP shall be:

- Modular
- Docker-based
- Reliable
- Maintainable
- Extensible
- Source-independent
- AI-provider independent

---

# 11. Out of Scope

The following are intentionally excluded from the MVP:

- User management
- Multi-tenancy
- Distributed processing
- Machine learning training
- Predictive analytics
- Mobile application
- Public API
- High availability clustering

These features may be introduced in future releases.

---

# 12. MVP Success Criteria

The MVP is considered complete when the platform can:

1. Collect articles automatically.
2. Detect the source correctly.
3. Parse supported sources.
4. Process articles successfully.
5. Generate AI intelligence.
6. Store processed information.
7. Send notifications.
8. Present processed intelligence in the dashboard.

