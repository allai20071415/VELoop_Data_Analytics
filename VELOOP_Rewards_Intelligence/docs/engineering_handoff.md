# Engineering analytics handoff

## Event contract (proposed)
Each event should include `event_id` (immutable unique ID), `user_id` (pseudonymous stable key), `event_name`, `event_at` (UTC ISO-8601), `feature`, `source`, `schema_version`, and event-specific properties. Use server-side events for authoritative outcomes such as reward credits and withdrawal settlement. Client events describe user intent, not financial settlement.

## Transaction contract
Wallet, reward and withdrawal rows should carry immutable transaction IDs, unit/currency, amount precision, status, timestamps, source/reference IDs, idempotency keys and reversal linkage. Store state transitions append-only where possible.

## Acceptance checks
- Duplicate event/transaction IDs are rejected or quarantined idempotently.
- Required identifiers and timestamps are present and valid.
- Status values follow an approved state machine.
- Units and currencies are never added together.
- Reward credits can be reconciled to ledger references.
- Withdrawal processing time uses request and final-state timestamps from the same lifecycle.
- KPI numerator, denominator, time zone, cohort and exclusions are documented.
- Every record has source provenance and simulated/production classification.
