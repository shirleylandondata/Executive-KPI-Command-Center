# Data Quality Rules

## Purpose

This document defines the data quality rules the Executive KPI Command Center applies before any number reaches an executive. The KPI layer and dashboard (Phases 6–7) can only be trusted if the raw and processed data pass these checks first.

Each rule lists what it checks, where it runs, how severe a failure is and its current status.

## Severity Levels

| Severity | Meaning | Action on Failure |
|---|---|---|
| **Critical** | The number would be wrong or misleading | Stop the pipeline; fix before publishing |
| **High** | The number is likely distorted for some segment or period | Fix before the next release; flag in the README |
| **Medium** | The data is valid but unrealistic or incomplete | Log as an open issue; fix in a planned phase |

## Status Key

- ✅ **Implemented**: check has been run and passed on the current data
- ⚠️ **Open issue**: check has been run and found a problem that is not yet fixed
- ⬜ **Planned**: rule is defined but not yet automated

---

## 1. Uniqueness

| ID | Rule | Dataset | Severity | Status |
|---|---|---|---|---|
| UQ-01 | `account_id` is unique | `customers.csv` | Critical | ✅ 0 duplicates (5,000 rows) |
| UQ-02 | `subscription_id` is unique | `subscriptions.csv` | Critical | ✅ |
| UQ-03 | `transaction_id` is unique | `revenue_transactions.csv` | Critical | ✅ 0 duplicates (106,112 rows) |
| UQ-04 | `opportunity_id` is unique | `opportunities.csv` | Critical | ⬜ |
| UQ-05 | `usage_id` is unique | `product_usage.csv` | Critical | ⬜ |
| UQ-06 | `cs_activity_id` is unique | `customer_success_activity.csv` | Critical | ⬜ |

## 2. Completeness

| ID | Rule | Dataset | Severity | Status |
|---|---|---|---|---|
| CP-01 | `account_id` is never null | `customers.csv` | Critical | ✅ 0 missing |
| CP-02 | `account_id` and `plan_id` are never null | `subscriptions.csv` | Critical | ✅ |
| CP-03 | `transaction_date` parses to a valid date | `revenue_transactions.csv` | Critical | ✅ Checked in `process_data.py` |
| CP-04 | `activity_month` parses to a valid date | `customer_success_activity.csv` | Critical | ✅ Checked in `process_data.py` |
| CP-05 | Required IDs and business-critical fields are not null | All core datasets | High | ⬜ |

## 3. Referential Integrity

| ID | Rule | Dataset | Severity | Status |
|---|---|---|---|---|
| RI-01 | Every subscription resolves to a valid `account_id` and `plan_id` | `subscriptions.csv` | Critical | ✅ |
| RI-02 | Every transaction resolves to a valid customer and subscription | `revenue_transactions.csv` | Critical | ✅ |
| RI-03 | Every fact-table key (`customer_key`, `plan_key`, `sales_stage_key`, `sales_rep_key`, `product_feature_key`, `customer_success_manager_key`, date keys) resolves to a dimension row | Star schema | Critical | ⬜ Runs once the SQL model is built |

## 4. Date Logic

| ID | Rule | Dataset | Severity | Status |
|---|---|---|---|---|
| DT-01 | No transaction is billed before its subscription's start month | `revenue_transactions.csv` | Critical | ✅ 0 violations |
| DT-02 | No transaction is billed after its subscription's cancellation date | `revenue_transactions.csv` | Critical | ✅ 0 violations |
| DT-03 | End, close and renewal dates never precede creation or start dates | Subscriptions, opportunities | High | ⬜ |
| DT-04 | No event is dated after the reporting period ends (Jul 31, 2026) | `subscriptions.csv` | High | ⚠️ 105 cancellation dates fall after the period, some in 2028 |
| DT-05 | New subscriptions continue through the full reporting period | `subscriptions.csv` | Medium | ⚠️ No new subscriptions start after Jan 20, 2026 |

## 5. Financial Logic

| ID | Rule | Dataset | Severity | Status |
|---|---|---|---|---|
| FN-01 | Billed and collected amounts are non-negative | `revenue_transactions.csv` | Critical | ✅ |
| FN-02 | Collected amount never exceeds billed amount | `revenue_transactions.csv` | Critical | ✅ 0 violations |
| FN-03 | Failed payments have a collected amount of 0 | `revenue_transactions.csv` | High | ✅ Enforced in `generate_data.py` |
| FN-04 | Recurring-price fields are consistent with subscription state | `subscriptions.csv` | High | ✅ Status agrees with lifecycle and renewal fields |

## 6. Status and Population Logic

| ID | Rule | Dataset | Severity | Status |
|---|---|---|---|---|
| ST-01 | Won, lost and open flags agree with sales stage and actual close date | `opportunities.csv` | High | ⬜ |
| ST-02 | Customer success metrics include only customers with an active subscription that month | `customer_success_activity.csv` | High | ⚠️ Jul 2026 counts 4,496 customers; only 3,822 subscriptions are active |

## 7. Reconciliation

These checks confirm that numbers agree across layers and tables. They are what caught the revenue billing bug described below.

| ID | Rule | Severity | Status |
|---|---|---|---|
| RC-01 | Raw billed revenue total = sum of monthly billed revenue | Critical | ✅ Reconciled in `process_data.py` |
| RC-02 | Raw collected revenue total = sum of monthly collected revenue | Critical | ✅ Reconciled in `process_data.py` |
| RC-03 | Raw transaction count = sum of monthly transaction counts | Critical | ✅ Reconciled in `process_data.py` |
| RC-04 | Subscriptions billed each month = active subscriptions that month | Critical | ✅ 0 difference in all 31 months (Jan 2024 – Jul 2026) |
| RC-05 | Billed revenue vs. MRR difference is explained | High | ✅ Billed runs about 1.5% above MRR because upgrades bill at +25% and add-ons at +10% |
| RC-06 | "Active customers" uses one definition across revenue, subscription and customer success outputs | High | ⚠️ See ST-02 |

## 8. Reasonableness

| ID | Rule | Severity | Status |
|---|---|---|---|
| RS-01 | Monthly revenue moves with the subscription base (no flat or repeated totals) | High | ✅ |
| RS-02 | Segment and status distributions are plausible | Medium | ✅ Customers: SMB 1,776 · Mid-Market 1,453 · Startup 1,002 · Enterprise 769 |
| RS-03 | Row counts per dataset fall within expected ranges | Medium | ⬜ |

---

## Issue Log

### Resolved: Revenue billing bug (Nov 2026)

**Found by:** RC-04 and RS-01. Monthly billed revenue was identical every month ($5,445,940 across 4,160 transactions), while active subscriptions grew from 2,677 to 3,891.

**Root cause:** In `generate_data.py`, the line that builds each subscription's billing calendar was indented inside a temporary debug block. It only ran for three subscriptions, and every other subscription reused the third one's 31-month calendar.

**Impact before the fix:**
- 17,850 transactions billed before the subscription started
- 5,016 transactions billed after cancellation
- 9,669 transactions where collected exceeded billed (upgrade and add-on pricing was applied to collected but not billed)

**Fix:** Moved the billing calendar out of the debug block, removed the debug code, and set the billed amount from the transaction type first, with collected equal to billed or 0 for a failed payment.

**Result:** 106,112 transactions; 0 violations on DT-01, DT-02 and FN-02; RC-04 passes in all 31 months.

### Open

| Rule | Issue | Planned Fix |
|---|---|---|
| DT-04 | 105 future-dated cancellations | Cap cancellation dates at the reporting period end in `generate_data.py` |
| DT-05 | No new subscriptions after Jan 20, 2026 | Extend the subscription start-date range to Jul 2026 |
| ST-02 / RC-06 | Customer success counts all 4,496 subscriptions | Filter customer success activity to subscriptions active in each month |

Phase 3 is not marked complete until these three issues are closed.

---

## Where the Checks Run

| Stage | Script | Checks |
|---|---|---|
| Generation | `python/generate_data.py` | Duplicate and missing ID counts; status and plan distributions |
| Processing | `python/process_data.py` | Date parsing; raw-to-monthly reconciliation (RC-01 to RC-03) |
| Validation (planned) | SQL data quality queries | Referential integrity, status logic and row-count checks against the star schema |
| Reporting (planned) | Dashboard Page 6: Data Quality | Quality scorecard, errors by source, validation history |
