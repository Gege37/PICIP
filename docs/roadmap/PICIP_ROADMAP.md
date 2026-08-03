# PICIP Project Roadmap
Version: 1.0
Status: Draft
Phase: 3.5 – Architecture Consolidation

---

# Vision

PICIP (Plataforma Inteligente de Comunicação e Informação Presidencial) is a
modular intelligence platform designed to continuously collect, process,
analyse and distribute strategic information from multiple trusted sources.

The roadmap is organized into progressive phases, ensuring each stage is
completed, documented and validated before the next begins.

---

# Phase 1 — Infrastructure

Status: Completed

Objectives

- Project structure
- Docker environment
- PostgreSQL integration
- Backend initialization
- Frontend initialization
- Notification service initialization

Deliverables

- Docker Compose
- Python backend
- React frontend
- PostgreSQL database
- Node.js notification service

---

# Phase 2 — Collection Layer

Status: Completed

Objectives

- RSS collection
- Website collection
- Source management
- Source monitoring
- Scheduler

Deliverables

- collector.py
- web_collector.py
- scheduler.py
- source_manager.py
- source_health.py
- source_health_manager.py

---

# Phase 3 — Ingestion Layer

Status: Completed

Objectives

- Website detection
- Source dispatching
- Source parsing
- Article normalization
- Processing pipeline

Deliverables

- website_detector.py
- source_dispatcher.py
- angop_parser.py
- processor.py

Release

v0.3.0

---

# Phase 3.5 — Architecture Consolidation

Status: In Progress

Objectives

- Review implementation
- Review architecture
- Produce technical documentation
- Define processing pipeline
- Define technology stack
- Define MVP
- Define roadmap
- Define database requirements
- Define security requirements

Deliverables

- PICIP_ARCHITECTURE.md
- PICIP_TECH_STACK.md
- MVP_SCOPE.md
- PICIP_ROADMAP.md
- DATABASE_REQUIREMENTS.md
- SECURITY_REQUIREMENTS.md

---

# Phase 4 — Intelligence Layer

Status: In Progress

Objectives

- AI pipeline
- Summary generation
- Sentiment analysis
- Classification
- Topic detection
- Risk analysis
- Provider abstraction

Deliverables

- intelligence/
- services/
- provider abstraction
- structured analysis pipeline

Planned Release

v0.4.0

---

# Phase 5 — Persistence & Notification

Status: Planned

Objectives

- Persist AI analysis
- Notification rules
- Alert engine
- Notification history
- Processing metrics

Deliverables

- Database integration
- Notification workflows
- Monitoring metrics

Planned Release

v0.5.0

---

# Phase 6 — Dashboard & Analytics

Status: Planned

Objectives

- Operational dashboard
- Search
- Filtering
- Risk monitoring
- Source monitoring
- Intelligence visualization
- Reporting

Deliverables

- React dashboard
- Charts
- Analytics
- Reporting

Planned Release

v0.6.0

---

# Phase 7 — Production Readiness

Status: Planned

Objectives

- Performance optimization
- Security hardening
- Automated backups
- Monitoring
- Logging
- Documentation review
- Deployment validation

Deliverables

- Production deployment
- Operational handbook
- Release documentation

Planned Release

v1.0.0

---

# Guiding Principles

The project follows these principles throughout all phases:

- Build incrementally.
- Document before expanding.
- Keep modules independent.
- Prefer composition over coupling.
- Maintain provider-independent AI.
- Validate each phase before moving forward.
- Tag stable releases in Git.

