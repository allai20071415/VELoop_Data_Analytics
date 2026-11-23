# Privacy, security and governance proposal

- Use pseudonymous user IDs; never ingest passwords, payment credentials or unnecessary personal identifiers.
- Production access must use company-managed authentication and role-based authorization.
- Keep secrets in environment variables or a managed secret store; never commit credentials.
- Encrypt data in transit and at rest using hosting/database controls.
- Define approved purpose, retention, deletion, incident response and access review with VELOOP.
- Maintain provenance, schema versions, lineage and audit logs.
- Treat anomaly flags as investigation signals, not proof of fraud or automatic grounds for penalties.
- Production launch requires privacy, security, product and engineering approval.
