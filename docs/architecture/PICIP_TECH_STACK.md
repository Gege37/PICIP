# PICIP Technology & Engineering Stack
Version: 1.2
Status: Approved
Phase: 3.5 – Architecture Consolidation

---

# 1. Architecture Philosophy

PICIP follows a **simplicity-first engineering philosophy**.

The platform is intentionally designed to remain as simple, robust,
maintainable and reliable as possible.

Every technology included in the platform must have a clear operational
purpose.

New frameworks, libraries or infrastructure components are introduced only
when they provide measurable functional or operational value.

The preferred solution is always the simplest solution that satisfies the
requirements while remaining secure, maintainable and scalable.

---

# 2. Engineering Principles

PICIP is developed according to the following engineering principles.

• Simplicity before complexity.

• Reliability before optimization.

• Maintainability before cleverness.

• Modularity before monoliths.

• Standards before custom implementations.

• Security by design.

• Documentation accompanies implementation.

• Features are introduced only when they solve a real operational problem.

---

# 3. Core Technology Stack

PICIP intentionally uses a small, proven and stable technology stack.

| Layer | Technology |
|--------|------------|
| Operating System | Ubuntu Server |
| Container Platform | Docker |
| Container Orchestration | Docker Compose |
| Backend | Python 3 |
| Database | PostgreSQL |
| Frontend | React |
| Notification Service | Node.js |
| Secure Communication | HTTPS |
| Version Control | Git & GitHub |

---

# 4. Container Strategy

PICIP is composed of multiple independent services.

Docker provides isolated containers.

Docker Compose orchestrates the complete platform by:

- Starting all services
- Creating the internal network
- Managing dependencies
- Managing persistent volumes
- Managing environment variables
- Applying restart policies

The complete platform can therefore be started with:

docker compose up -d

---

# 5. Backend Technologies

Current Python modules include:

- requests
- beautifulsoup4
- feedparser
- psycopg2-binary
- python-dotenv

Backend responsibilities:

- Information collection
- Source detection
- Source parsing
- Processing
- Intelligence generation
- Database interaction

---

# 6. Artificial Intelligence

Current implementation:

- Rule-based Intelligence
- Modular Intelligence Pipeline
- Provider-independent Architecture

Current capabilities:

- Summary
- Sentiment Analysis
- Classification
- Topic Detection
- Risk Analysis

Possible AI Providers

The Intelligence Layer is provider-independent.

Potential providers include:

- Rule-based Engine
- Ollama
- OpenAI Compatible APIs
- Azure OpenAI
- Local LLMs
- Future enterprise AI services

The choice of provider is a deployment decision rather than an architectural dependency.

---

# 7. Database

Engine

PostgreSQL

Responsibilities

- Source management
- Article storage
- Intelligence persistence
- Processing status
- Notification history
- Audit information

---

# 8. Frontend

Technology

React

Responsibilities

- Dashboard
- Search
- Filtering
- Intelligence visualization
- Monitoring

---

# 9. Notification Service

Technology

Node.js

Responsibilities

- Alert generation
- Notification delivery
- Integration with future messaging platforms

---

# 10. Design Principles

PICIP follows these design principles.

- Keep the architecture simple.
- Prefer proven technologies.
- Minimize dependencies.
- Separate responsibilities clearly.
- Keep services loosely coupled.
- Maintain provider-independent AI.
- Keep deployment straightforward.
- Design for maintainability before complexity.

---

# 11. Future Considerations

Additional technologies may be introduced only when justified by project
requirements.

Examples include:

- Redis
- RabbitMQ
- Elasticsearch
- Vector Databases
- Kubernetes
- Prometheus
- Grafana

These technologies are intentionally **not part of the current architecture**
and should only be adopted when they provide a measurable operational benefit.

