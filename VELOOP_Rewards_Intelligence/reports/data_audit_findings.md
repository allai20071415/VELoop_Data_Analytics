# Synthetic dataset profiling and audit findings

All findings below describe the generated test pack, not VELOOP production data.

| Dataset | Rows | Notes |
|---|---:|---|
| Users | 1,000 | Synthetic user/account records |
| Task activity | 6,000 | Synthetic task outcomes |
| Rewards | 5,000 | Synthetic reward states and units |
| Wallet transactions | 3,500 | Synthetic ledger activity |
| Withdrawals | 1,200 | Synthetic payout requests and states |
| Referrals | 900 | Synthetic referral funnel records |
| Feature events | 12,000 | Synthetic product events |
| Messy data | 515 | Deliberate test defects: duplicated rows, missing user IDs and invalid statuses |

The deliberately messy table contains 15 exact duplicate rows, 24 null `user_id` cells and 13 invalid status values. These totals include overlap introduced by deliberately duplicating sample rows. The withdrawals table contains 417 blank `processed_at` values because unsettled statuses have no final processing timestamp; these are expected lifecycle nulls, not automatically data defects. The profiler output is available in `profiling_summary.csv`. The clean demonstration tables are used by the dashboard; the messy table is loaded separately for the quality monitor.

## Important limitations
The generated dataset is suitable for testing profiling and dashboard behavior. It is not a source of actual VELOOP performance insights. KPI calculations that require event history, ingestion timestamps, currency definitions, stable state transitions, or agreed cohort windows remain partially testable until approved production fields are confirmed.
