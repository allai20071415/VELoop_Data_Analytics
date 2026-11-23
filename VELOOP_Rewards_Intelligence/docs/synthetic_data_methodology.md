# Synthetic data methodology

The eight CSV datasets were generated locally with NumPy's fixed random seed `42` (the withdrawal processing timestamp correction uses seed `43`). The generated tables contain 1,000 users, 6,000 task activities, 5,000 reward records, 3,500 wallet transactions, 1,200 withdrawals, 900 referrals, 12,000 feature events and 515 deliberately messy test rows.

The generator uses controlled categorical distributions to create varied account, task, reward, wallet, withdrawal and referral states. The messy table intentionally duplicates rows, removes some user IDs and inserts invalid status values to test quality controls. Unsettled withdrawals intentionally have no final processing timestamp. The records are not derived from real VELOOP customers, transactions, revenue or product telemetry.

The dataset pack is a testing fixture. It must not be mixed with production data or cited as actual company performance. Production metrics must be recomputed from approved, verified sources.
