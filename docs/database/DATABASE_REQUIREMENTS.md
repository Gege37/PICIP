# PICIP Database Requirements
Version: 1.0
Status: Draft
Phase: 3.5 – Architecture Consolidation

---

# 1. Purpose

The PostgreSQL database is the central persistence layer of PICIP.

Its responsibilities are to permanently store collected information,
processing results, AI intelligence, notification history and operational
metadata.

The database is the system of record for all processed information.

---

# 2. Database Engine

Engine

PostgreSQL

Characteristics

- ACID compliant
- Reliable
- Extensible
- Docker deployed
- Suitable for future scaling

---

# 3. Core Entities

The MVP shall include the following logical entities.

## Sources

Stores information about each configured source.

Typical attributes

- id
- name
- type
- base_url
- enabled
- priority
- health_status
- created_at
- updated_at

---

## Articles

Stores normalized articles.

Typical attributes

- id
- source_id
- title
- author
- publication_date
- url
- language
- content
- collected_at
- processed_at

---

## AI Analysis

Stores intelligence generated from articles.

Typical attributes

- article_id
- summary
- sentiment
- sentiment_score
- classification
- topics
- risk_level
- risk_indicators
- ai_provider
- ai_model
- analysed_at

---

## Processing Status

Tracks article processing.

Typical attributes

- article_id
- collection_status
- parsing_status
- intelligence_status
- notification_status
- last_updated

---

## Notifications

Stores notification history.

Typical attributes

- id
- article_id
- notification_type
- destination
- delivery_status
- created_at

---

# 4. Relationships

Logical relationships

Source
    │
    └──< Articles
              │
              ├── AI Analysis
              ├── Processing Status
              └── Notifications

---

# 5. Indexing Strategy

Recommended indexes

Articles

- publication_date
- collected_at
- source_id

AI Analysis

- sentiment
- risk_level
- classification

Sources

- enabled
- health_status

Notifications

- delivery_status
- created_at

---

# 6. Data Retention

The platform should support configurable retention policies.

Recommendations

- Keep articles permanently unless archived.
- Archive historical notifications.
- Preserve AI analysis for auditing.
- Never delete processing logs automatically.

---

# 7. Integrity Requirements

The database shall enforce:

- Primary keys
- Foreign keys
- Unique constraints where applicable
- Transaction consistency
- Referential integrity

---

# 8. Future Expansion

The schema should allow future support for:

- Multiple AI providers
- Additional parsers
- Multiple languages
- User management
- Audit logging
- Workflow history
- Analytics tables
- Vector embeddings (optional)

---

# 9. Design Principles

The database should remain:

- Normalized
- Extensible
- Provider-independent
- Auditable
- Reliable
- Easy to migrate

