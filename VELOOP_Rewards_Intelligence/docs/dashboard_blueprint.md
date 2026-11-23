# Dashboard blueprint

| View | Primary cards / visuals | Intended stakeholder |
|---|---|---|
| Overview | Registered/active users, task completion, credited/pending rewards, wallet activity, pending withdrawals, referrals; monthly trend and status distributions | Management / Product |
| Users & engagement | Account lifecycle, platform split, acquisition and retention cohorts (cohort view requires production event history) | Product / Growth |
| Rewards & tasks | Task starts/completions/failures, reward states and unit-separated totals | Product / Operations |
| Wallet & withdrawals | Wallet ledger statuses, pending/processing queue, request status table, processing time when history is available | Finance / Operations |
| Referrals | Created → registered → activated → converted funnel | Growth |
| Data quality | Duplicate IDs, missing/orphan user references, invalid statuses, freshness and reconciliation exceptions | Engineering / Data |

Current UI implements the core demo cards, charts, request table and synthetic quality checks. Cohort analysis, real-time refresh, exports, role management and scheduled reports are production backlog items.
