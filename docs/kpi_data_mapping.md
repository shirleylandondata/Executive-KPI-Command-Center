# KPI Data Mapping

## Purpose

This document connects each KPI in `kpi_dictionary.md` to the data that produces it: the source table, the fields used, the calculation and where the result lives today.

It also shows which KPIs can't be calculated yet and what's missing. The rule from the README applies: **no metric goes into the dashboard unless it's mapped here and calculated in the KPI layer.**

## Status Key

- ✅ **Available**: calculated in a processed output today
- 🟡 **Derivable**: the source fields exist; the calculation is not built yet
- 🔴 **Gap**: the data needed doesn't exist yet, or a business definition is missing

## Summary

| KPI | Owner | Status |
|---|---|---|
| Monthly Recurring Revenue (MRR) | CFO | ✅ |
| Annual Recurring Revenue (ARR) | CFO | ✅ |
| Customer Churn Rate | VP Customer Success | ✅ (one definition conflict to resolve) |
| Collection Rate | CFO | ✅ (supporting metric, not yet in the KPI dictionary) |
| Win Rate | CRO | 🟡 |
| Pipeline Coverage | CRO | 🟡 |
| Customer Health Score | VP Customer Success | 🟡 |
| Product Adoption Rate | VP Product | 🔴 Threshold not defined |
| Net Revenue Retention (NRR) | CFO / VP Customer Success | 🔴 No expansion or contraction MRR history |
| Gross Revenue Retention (GRR) | VP Customer Success | 🔴 No contraction MRR history |

---

## Revenue KPIs

### Monthly Recurring Revenue (MRR) ✅

| Item | Detail |
|---|---|
| Source table | `subscriptions.csv` → `fact_subscription` |
| Fields | `monthly_recurring_revenue`, `subscription_start_date`, `cancellation_date` |
| Logic | Sum of `monthly_recurring_revenue` for subscriptions that started by month end and were not cancelled before the month began |
| Grain | Month |
| Output | `subscription_monthly.csv` → `monthly_recurring_revenue` |
| Built in | `python/process_data.py` (monthly subscription snapshot) |

### Annual Recurring Revenue (ARR) ✅

| Item | Detail |
|---|---|
| Source table | `subscriptions.csv` → `fact_subscription` |
| Fields | `annual_recurring_revenue` (same active-subscription filter as MRR) |
| Logic | Sum of `annual_recurring_revenue` for active subscriptions. This equals MRR × 12, which matches the KPI dictionary (Jan 2024: $3,464,223 × 12 = $41,570,676). |
| Grain | Month |
| Output | `subscription_monthly.csv` → `annual_recurring_revenue` |

### Collection Rate ✅ (supporting metric)

| Item | Detail |
|---|---|
| Source table | `revenue_transactions.csv` → `fact_revenue_transaction` |
| Fields | `billed_amount`, `collected_amount`, `transaction_date` |
| Logic | Total collected ÷ total billed, by month |
| Output | `revenue_monthly.csv` → `collection_rate` |
| Note | Not in `kpi_dictionary.md` yet. Add a definition and owner before it goes on the dashboard. |

### Net Revenue Retention (NRR) 🔴

| Item | Detail |
|---|---|
| Needs | Beginning MRR, Expansion MRR, Contraction MRR, Churned MRR |
| Available | Beginning MRR (prior month's `monthly_recurring_revenue`), Churned MRR (MRR of subscriptions with a `cancellation_date` in the month) |
| Missing | Expansion and contraction MRR. Each subscription has one fixed `monthly_recurring_revenue` value with no history of plan changes. Upgrades and add-ons appear only as one-time transaction types in `revenue_transactions.csv`, not as recurring MRR changes. |
| To close the gap | Add a subscription change history (plan change date, old MRR, new MRR) to `generate_data.py`, or define expansion as the MRR effect of `Upgrade` transactions and document that assumption |

### Gross Revenue Retention (GRR) 🔴

| Item | Detail |
|---|---|
| Needs | Beginning MRR, Contraction MRR, Churned MRR |
| Missing | Contraction MRR (same gap as NRR) |
| Interim option | Until contraction exists, GRR equals (Beginning MRR − Churned MRR) ÷ Beginning MRR. Label it as "GRR (churn only)" if it's shown. |

---

## Customer KPIs

### Customer Churn Rate ✅

| Item | Detail |
|---|---|
| Source table | `subscriptions.csv` → `fact_subscription` |
| Fields | `cancellation_date`, active-subscription snapshot |
| Logic | Subscriptions cancelled in the month ÷ active subscriptions at the start of the month |
| Output | `subscription_monthly.csv` → `subscription_churn_rate` (%) |
| Note | The KPI dictionary defines churn by **customer**. The current output measures **subscriptions**. These are equal today because each customer has one subscription (`active_subscriptions` = `active_customers` in every month). If multiple subscriptions per customer are ever added, the calculation must switch to customers. |
| Definition conflict | `customers.csv` has its own `customer_status` field (743 customers marked Churned). The KPI layer should treat the subscription data as the source of truth for churn and document that choice. |

### Customer Health Score 🟡

| Item | Detail |
|---|---|
| Source table | `customer_success_activity.csv` |
| Fields | `health_score`, `health_category`, `renewal_risk`, `satisfaction_score`, `support_tickets`, `activity_month` |
| Current output | `customer_success_monthly.csv` → `average_health_score`, health category counts, `customers_requiring_intervention` (At Risk + Critical), `at_risk_customer_rate` |
| Gap 1 | The KPI dictionary describes a **composite** score built from usage, feature adoption, support tickets, subscription status, payment status and renewal proximity. Today `health_score` is a generated value, not calculated from those components. |
| Gap 2 | Customer success activity includes customers without an active subscription (Jul 2026: 4,496 customers vs. 3,822 active subscriptions). See rule ST-02 in `data_quality_rules.md`. |
| To close the gap | Filter to active subscriptions each month, then build the composite score from the components listed in the KPI dictionary |

---

## Sales KPIs

### Win Rate 🟡

| Item | Detail |
|---|---|
| Source table | `opportunities.csv` → `fact_sales_opportunity` |
| Fields | `won_opportunity_flag`, `lost_opportunity_flag`, `actual_close_date` |
| Logic | Count of won ÷ (count of won + count of lost), by close month |
| Output | Not built yet. Planned for the SQL KPI layer. |
| Validation first | Rule ST-01: won and lost flags must agree with sales stage and close date |

### Pipeline Coverage 🟡

| Item | Detail |
|---|---|
| Source tables | `opportunities.csv`, `sales_representatives.csv` |
| Fields | `opportunity_value`, won/lost flags (open = neither flag set), `expected_close_date`; `annual_quota` |
| Logic | Open pipeline value ÷ remaining revenue target |
| Target source | Sum of `annual_quota` across active reps (`active_rep_flag` = True), less revenue already won in the period |
| Decision needed | Confirm that rep quota is the right stand-in for the company revenue target |

---

## Product KPIs

### Product Adoption Rate 🔴

| Item | Detail |
|---|---|
| Source tables | `product_usage.csv`, `product_features.csv` |
| Fields | `account_id`, `product_feature_id`, `usage_month`, `active_users`, `active_days`, `engagement_score` |
| Logic | Accounts meeting the adoption threshold ÷ active accounts |
| Missing | A business definition of the **adoption threshold**, such as "used at least 3 core features with 4 or more active days in the month." The data supports this, but the VP Product needs to set the rule before it's built. |

---

## Shared Definitions

These apply to every KPI above.

| Term | Definition |
|---|---|
| Reporting period | Jan 1, 2024 – Jul 31, 2026 (31 months) |
| Reporting grain | Calendar month, keyed on the first of the month |
| Active subscription | Started on or before the month end, and not cancelled before the month start |
| Active customer | A customer with at least one active subscription in the month. This is the single definition for all outputs. Customer success outputs don't follow it yet (see ST-02). |

## Next Steps

1. Agree the active-customer definition and apply it to customer success outputs
2. Decide the product adoption threshold and the pipeline target source
3. Decide how to model expansion and contraction MRR, then build NRR and GRR
4. Build Win Rate and Pipeline Coverage in the SQL KPI layer (Phase 6)
