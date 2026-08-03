# PICIP Architecture
Version: 1.0
Status: Draft
Phase: 3.5 – Architecture Consolidation

---

# 1. Purpose

PICIP (Plataforma Inteligente de Comunicação e Informação Presidencial) is an
intelligence platform that continuously collects, processes, analyses and
distributes strategic information from multiple trusted sources.

The platform is designed as a processing pipeline rather than a traditional
web application.

---

# 2. High-Level Architecture

                  +----------------------+
                  |   Information Sources |
                  | RSS / Websites / APIs |
                  +----------+-----------+
                             |
                             v
                   +--------------------+
                   | Collection Layer   |
                   | collector.py       |
                   | web_collector.py   |
                   +---------+----------+
                             |
                             v
                   +--------------------+
                   | Source Detection   |
                   | website_detector.py|
                   +---------+----------+
                             |
                             v
                   +--------------------+
                   | Source Dispatcher  |
                   | source_dispatcher  |
                   +---------+----------+
                             |
                             v
                   +--------------------+
                   | Source Parsers     |
                   | angop_parser.py    |
                   | future parsers     |
                   +---------+----------+
                             |
                             v
                   +--------------------+
                   | Processing Layer   |
                   | processor.py       |
                   +---------+----------+
                             |
                             v
                   +--------------------+
                   | Intelligence Layer |
                   | summarizer         |
                   | sentiment          |
                   | classifier         |
                   | topic detection    |
                   | risk analysis      |
                   +---------+----------+
                             |
                             v
                   +--------------------+
                   | Persistence Layer  |
                   | PostgreSQL         |
                   | database.py        |
                   +---------+----------+
                             |
                 +-----------+------------+
                 |                        |
                 v                        v
        Notification Layer        Frontend / Dashboard
             (Node.js)                 (React)

---

# 3. Processing Flow

1. Scheduler starts collection jobs.
2. Collector retrieves articles.
3. Website detector identifies the source.
4. Dispatcher selects the correct parser.
5. Parser extracts structured article data.
6. Processor normalizes the article.
7. Intelligence layer performs:
   - Summary
   - Sentiment
   - Classification
   - Topic detection
   - Risk analysis
8. Processed article is stored in PostgreSQL.
9. Notification service publishes important events.
10. Frontend presents intelligence dashboards.

---

# 4. Core Components

## Collection

Responsible for acquiring raw information from supported sources.

Current modules:
- collector.py
- web_collector.py

---

## Source Management

Responsible for source registration, availability and health.

Current modules:
- source_manager.py
- source_health.py
- source_health_manager.py

---

## Parsing

Responsible for transforming raw HTML/XML into structured data.

Current modules:
- angop_parser.py

Future:
- BBC
- Reuters
- VOA
- Presidency
- Ministry sources

---

## Processing

Responsible for validation and normalization before AI analysis.

Current module:
- processor.py

---

## Intelligence

Responsible for transforming structured information into actionable intelligence.

Current capabilities:
- Summary
- Sentiment
- Classification
- Topic detection
- Risk analysis

Designed to support multiple AI providers through a provider abstraction layer.

---

## Persistence

Responsible for storing all structured information in PostgreSQL.

Current module:
- database.py

---

## Notifications

Responsible for distributing alerts and important intelligence.

Implementation:
Node.js notification service.

---

## Frontend

Responsible for visualization, dashboards and user interaction.

Implementation:
React.

---

# 5. Design Principles

- Modular architecture
- Provider-independent AI
- Source-independent parsing
- Database-first persistence
- Docker-based deployment
- Extensible intelligence pipeline
- Separation of concerns
- High cohesion and low coupling

---

# 6. Current Development Phase

Infrastructure ............. Complete
Collection Layer ........... Complete
Ingestion Layer ............ Complete
Architecture Consolidation . In Progress
Intelligence Layer ......... In Progress
Notification Layer ......... Planned
Dashboard & Analytics ...... Planned

---

# 7. Next Milestone

Complete Phase 3.5 documentation before continuing Phase 4 implementation.

