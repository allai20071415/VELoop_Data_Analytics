# Proposed analytics architecture

```mermaid
flowchart LR
 A[VELOOP application] --> B[Approved API / secure export] --> C[Raw landing + provenance] --> D[Schema validation / quarantine] --> E[Transform + deduplicate] --> F[Analytics database] --> G[Flask API] --> H[Admin dashboard]
```

Current demo uses labelled synthetic CSVs and SQLite. Production use requires approved source access, secure ingestion, managed database, authentication, audit logging, monitoring and stakeholder sign-off.
