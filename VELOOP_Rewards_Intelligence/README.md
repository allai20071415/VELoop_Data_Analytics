# VELOOP Rewards — Analytics & Operations Intelligence

**Internship-ready proof of concept and proposed company analytics foundation.**

> **SIMULATED DATA — CREATED FOR ANALYTICAL TESTING.** All dashboard values and CSV records are synthetic, not VELOOP production facts.

## Features
- Overview, user engagement, tasks/rewards, wallet/withdrawals, referrals and data-quality views.
- Flask API with demo login and read-only analytics endpoints.
- SQLite database seeded from seven labelled datasets.
- 38 proposed events, 104 data dictionary fields, 46 KPI definitions, 20 quality controls and a logical data model.
- Profiling output, acceptance traceability, privacy proposal and prioritized backlog.

## Run locally (Windows / VS Code)
1. Extract the ZIP and open the `VELOOP_Rewards_Intelligence` folder in VS Code.
2. Open Terminal → New Terminal and run:

```powershell
py -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
python backend/seed_database.py
python backend/app.py
```

3. Open `http://127.0.0.1:5000`. Demo login: `admin@demo.veloop` / `DemoOnly!2026`. Change this before any deployment.

## Tests and profiling
```powershell
pytest -q
python profile_veloop.py
```

## Deployment
- **Backend:** deploy Flask to Render or another Python host. Set `SECRET_KEY`, `DEMO_ADMIN_PASSWORD`, `CORS_ORIGINS`, and a persistent database path as environment variables.
- **Frontend:** deploy `frontend/` to Netlify. Update `netlify.toml` placeholder with the actual backend host and configure exact CORS origin.
- The included demo login is not enterprise authentication. Do not connect production data until VELOOP approves access and security/privacy controls.

## Production readiness gap
Before company operations: company SSO, role authorization, audit logs, managed PostgreSQL, secret management, TLS, retention/deletion, backups, monitoring, incident response and stakeholder-approved KPI/event definitions are required.
