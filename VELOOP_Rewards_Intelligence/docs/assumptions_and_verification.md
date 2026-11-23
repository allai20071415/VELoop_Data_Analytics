# Assumption & verification register

| ID | Unknown | Why it matters | Evidence / owner | Status |
|---|---|---|---|---|
| A01 | Stable user ID across modules | Cross-feature joins | Backend schema / Engineering | To verify |
| A02 | VE, XP, Gems and Tokens semantics | Prevent invalid aggregation | Product + Finance | To verify |
| A03 | Reward credits have ledger references | Reconciliation | Wallet schema / Engineering | To verify |
| A04 | Withdrawal status history exists | Queue ageing and SLA | Wallet team | To verify |
| A05 | Referral conversion criteria | Correct conversion KPI | Growth / Product | To verify |
| A06 | Timestamps are UTC | Consistent time windows | Instrumentation contract | To verify |
| A07 | Proposed events exist in product | Event coverage | Engineering | Proposed |
| A08 | Roles and dashboard audience | Access control | Company authorization | To verify |
| A09 | Retention and deletion policy | Privacy compliance | Security / Privacy | To verify |
| A10 | Currency/unit and precision | Financial reporting | Finance / Product | To verify |
