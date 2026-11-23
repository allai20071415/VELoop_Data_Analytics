# VELOOP Rewards – Analytics Intelligence Dashboard

**Business Intelligence & Operations Analytics | Internship Project**

A web-based analytics dashboard designed as a proof of concept for monitoring user engagement, task activity, rewards, wallet transactions, withdrawals, referrals and data quality.

---

## 1. Project Overview

VELOOP Rewards Analytics Intelligence is a business intelligence prototype that demonstrates how operational data can be organized, monitored and analyzed through a centralized dashboard.

The project aims to help business and product teams understand important operational indicators, identify data-quality issues and make informed decisions using structured analytics.

**Important:** This project currently uses synthetic demonstration data. It is not connected to VELOOP's production database or live business systems. Actual company metrics require authorized data access and integration.

## 2. Key Features

### Dashboard Overview
- Registered users
- Active accounts
- Task completion rate
- Credited rewards
- Pending rewards
- Wallet transactions
- Pending and processing withdrawals
- Converted referrals

### User & Engagement Analytics
- User registration overview
- Active and inactive account indicators
- Platform distribution
- User engagement insights

### Rewards & Tasks Analytics
- Task activity monitoring
- Task completion status
- Reward status distribution
- Reward activity indicators

### Wallet & Withdrawals
- Wallet transaction overview
- Withdrawal status monitoring
- Recent withdrawal records
- Withdrawal status filtering

### Referral Intelligence
- Total referral records
- Converted referrals
- Referral conversion rate
- Referral measurement considerations

### Data Quality Monitoring
- Duplicate activity ID detection
- Missing user ID detection
- Orphan user ID detection
- Unknown or invalid task status detection
- Self-referral detection

Data-quality findings are investigation signals, not proof of fraud or user misconduct.

## 3. Technology Stack

| Component | Technology |
|---|---|
| Frontend | HTML5, CSS3, JavaScript |
| Dashboard charts | Chart.js |
| Backend | Python, Flask |
| Database | SQLite |
| Data processing | Pandas, NumPy |
| Testing | Pytest |
| Backend hosting | Render |
| Frontend hosting | Netlify |
| Version control | Git and GitHub |

## 4. Project Structure

```text
VELOOP_Rewards_Intelligence/
│
├── backend/
│   ├── app.py
│   ├── seed_database.py
│   └── __init__.py
│
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── app.js
│
├── data/
│   ├── users.csv
│   ├── task_activity.csv
│   ├── rewards.csv
│   ├── wallet_transactions.csv
│   ├── withdrawals.csv
│   ├── referrals.csv
│   ├── feature_events.csv
│   └── messy_data.csv
│
├── reports/
│   ├── EXECUTIVE_SUMMARY.md
│   ├── kpi_catalogue.csv
│   ├── data_dictionary.csv
│   ├── event_tracking_plan.csv
│   ├── data_quality_rules.csv
│   └── analytics_gaps.csv
│
├── docs/
│   ├── architecture.md
│   ├── data_model.mmd
│   ├── privacy_governance.md
│   ├── implementation_backlog.md
│   └── submission_checklist.md
│
├── tests/
│   ├── test_api.py
│   ├── test_data_integrity.py
│   └── test_deployment_config.py
│
├── netlify/
│   └── functions/
│       └── api-proxy.mjs
│
├── netlify.toml
├── render.yaml
├── requirements.txt
├── verify_offline.py
└── README.md
```

*The Netlify Function and deployment configuration shown above must be included in the repository for the documented Netlify proxy deployment.*

## 5. Installation and Local Setup

### Requirements
- Python 3.10 or later
- VS Code
- Git
- Internet connection for installing Python dependencies

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd VELOOP_Rewards_Intelligence
```

### Step 2: Create a virtual environment

Windows:

```powershell
py -m venv .venv
.venv\Scripts\activate
```

### Step 3: Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Initialize the database

```bash
python backend/seed_database.py
```

### Step 5: Start the application

```bash
python backend/app.py
```

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

Local demonstration login:

```text
Email: admin@demo.veloop
Password: DemoOnly!2026
```

The local demonstration credentials are not intended for production deployment.

## 6. Testing and Verification

Run the offline data-integrity tests:

```bash
python -m pytest tests/test_data_integrity.py -q
```

Run deployment configuration tests:

```bash
python -m pytest tests/test_deployment_config.py -q
```

Run all tests, including Flask API integration tests:

```bash
python -m pytest -q
```

Run Python profiling:

```bash
python profile_veloop.py
```

The Flask API integration tests require the project dependencies to be installed. Do not report them as passed unless the test command completes successfully.

## 7. Deployment Architecture

The application uses two hosting services because Netlify serves the frontend while Flask requires a Python backend host.

**Frontend:** Netlify

**Backend:** Render

**API communication:** Netlify Function proxy

### Step 1: Deploy the backend on Render

1. Push the project to GitHub.
2. Open Render.
3. Select **New → Blueprint**.
4. Connect the GitHub repository.
5. Select the repository containing `render.yaml`.
6. Deploy the Flask web service.
7. Configure the required environment variables.

Required Render environment variables:

```text
SECRET_KEY = A strong private secret
DEMO_ADMIN_PASSWORD = A strong private demo password
COOKIE_SECURE = true
```

After deployment, verify:

```text
https://YOUR-RENDER-SERVICE.onrender.com/api/health
```

Expected response:

```json
{
  "status": "ok",
  "data_mode": "SIMULATED",
  "production_connected": false
}
```

### Step 2: Deploy the frontend on Netlify

1. Open Netlify.
2. Select **Add new project**.
3. Import the GitHub repository.
4. Set the publish directory to:

```text
frontend
```

5. Confirm that `netlify.toml` and the Netlify Function are included.
6. Deploy the site.

### Step 3: Configure the API connection

In Netlify, open:

**Site configuration → Environment variables**

Add:

```text
VELOOP_API_URL=https://YOUR-RENDER-SERVICE.onrender.com
```

Use the actual Render service URL, without an `/api` suffix.

Redeploy the Netlify site after configuration.

### Step 4: Verify the deployed application

Check these addresses:

```text
https://YOUR-RENDER-SERVICE.onrender.com/api/health
```

```text
https://YOUR-NETLIFY-SITE.netlify.app/
```

```text
https://YOUR-NETLIFY-SITE.netlify.app/api/health
```

The Netlify dashboard should load, and the API health endpoint should return a successful response.

Follow `docs/netlify_render_deployment.md` for the complete deployment procedure.

## 8. Analytics Documentation

The project includes supporting analytical documentation:

- KPI Catalogue
- Event Tracking Plan
- Data Dictionary
- Data Quality Rules
- Data Profiling Summary
- Source Coverage Matrix
- Analytics Gaps
- Data Audit Findings
- Executive Summary
- Implementation Backlog
- Privacy and Governance Recommendations

These materials provide a foundation for future company-approved analytics implementation.

## 9. Privacy and Security

- No real VELOOP customer records are included.
- Synthetic data is used for demonstration purposes.
- Do not upload API keys, passwords or confidential information to GitHub.
- Use HTTPS for hosted environments.
- Use strong private deployment secrets.
- Obtain company authorization before accessing or processing production information.
- Production deployment requires appropriate authentication, authorization, audit logging and security review.

## 10. Current Project Limitations

This project is an analytics proof of concept, not a production-ready company system.

The following activities require further company access or approval:

- Integration with VELOOP's actual database or API.
- Verification of business-approved KPI definitions.
- Production authentication and role management.
- Managed production database and backups.
- Deployment and operational security review.
- Validation with company stakeholders.

## 11. Future Enhancements

- Authorized live data integration
- Advanced user engagement analysis
- Reward and task performance trends
- Withdrawal processing analysis
- Referral funnel analysis
- Automated data-quality reporting
- Role-based analytics access
- Scheduled management reports
- Advanced anomaly investigation

## 12. Project Objective

The objective is to demonstrate how a centralized analytics solution can support operational visibility, product analysis, data-quality monitoring and business decision-making for a rewards platform.

The proposed system can be extended into a company-specific analytics solution after authorized data integration and technical review.

---

**Project:** VELOOP Rewards – Analytics Intelligence Dashboard  
**Category:** Business Intelligence / Data Analytics  
**Project Type:** Internship Proof of Concept  
**Data:** Synthetic Demonstration Data  
**Backend:** Flask  
**Frontend:** HTML, CSS, JavaScript  
**Deployment Design:** Netlify + Render  
**Repository:** Add your GitHub repository URL here

**Developed as an internship project to demonstrate practical analytics, dashboard development, data validation and deployment architecture.**
