# ============================================================
# EXECUTIVE KPI COMMAND CENTER
# Processed Analytics Layer
# ============================================================

from pathlib import Path
import pandas as pd
import numpy as np

# ============================================================
# PROJECT PATHS
# ============================================================

# process_data.py is stored inside the /python folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"

# Make sure the processed data directory exists
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

print("Executive KPI Command Center - Data Processing")
print(f"Raw data directory: {RAW_DATA_DIR}")
print(f"Processed data directory: {PROCESSED_DATA_DIR}")

# ============================================================
# LOAD RAW DATASETS
# ============================================================

print("\nLoading raw datasets...")

customers = pd.read_csv(RAW_DATA_DIR / "customers.csv")
subscriptions = pd.read_csv(RAW_DATA_DIR / "subscriptions.csv")
subscription_plans = pd.read_csv(RAW_DATA_DIR / "subscription_plans.csv")
revenue_transactions = pd.read_csv(
    RAW_DATA_DIR / "revenue_transactions.csv"
)

product_usage = pd.read_csv(RAW_DATA_DIR / "product_usage.csv")
opportunities = pd.read_csv(RAW_DATA_DIR / "opportunities.csv")
customer_success_activity= pd.read_csv(
    RAW_DATA_DIR / "customer_success_activity.csv"
)

print("Raw datasets loaded successfully.")

# ============================================================
# VALIDATE RAW DATASETS
# ============================================================

print("\nRaw Dataset Row Counts:")

datasets = {
    "Customers": customers,
    "Subscriptions": subscriptions,
    "Subscription Plans": subscription_plans,
    "Revenue Transactions": revenue_transactions,
    "Product Usage": product_usage,
    "Opportunities": opportunities,
    "Customer Success Activity": customer_success_activity
}

for dataset_name, dataframe in datasets.items():
    print(f"{dataset_name}: {len(dataframe):,} rows")

# ============================================================
# INSPECT REVENUE TRANSACTIONS
# ============================================================

print("\nRevenue Transaction Columns:")

for column in revenue_transactions.columns:
    print(f"- {column}")

# ============================================================
# PREPARE REVENUE TRANSACTIONS
# ============================================================

print("\nPreparing revenue transactions...")

# Work from a copy so the raw imported dataset remains unchanged
revenue_clean = revenue_transactions.copy()

# Convert transaction date to datetime
revenue_clean["transaction_date"] = pd.to_datetime(
    revenue_clean["transaction_date"],
    errors="coerce"
)

# Create month-level reporting field
revenue_clean["reporting_month"] = (
    revenue_clean["transaction_date"]
    .dt.to_period("M")
    .dt.to_timestamp()
)

print(
    "Invalid Transaction Dates:",
    revenue_clean["transaction_date"].isna().sum()
)

print(
    "Revenue Date Range:",
    revenue_clean["transaction_date"].min().date(),
    "to",
    revenue_clean["transaction_date"].max().date()
)

# ============================================================
# CREATE MONTHLY REVENUE SUMMARY
# ============================================================

print("\nCreating monthly revenue summary...")

revenue_monthly = (
    revenue_clean
    .groupby("reporting_month", as_index=False)
    .agg(
        total_billed_revenue=("billed_amount", "sum"),
        total_collected_revenue=("collected_amount", "sum"),
        transaction_count=("transaction_id", "count"),
        unique_customers=("account_id", "nunique"),
        unique_subscriptions=("subscription_id", "nunique")
    )
)

# Calculate collection rate
revenue_monthly["collection_rate"] = (
    revenue_monthly["total_collected_revenue"]
    / revenue_monthly["total_billed_revenue"]
)

# Round financial and percentage fields
revenue_monthly["total_billed_revenue"] = (
    revenue_monthly["total_billed_revenue"].round(2)
)

revenue_monthly["total_collected_revenue"] = (
    revenue_monthly["total_collected_revenue"].round(2)
)

revenue_monthly["collection_rate"] = (
    revenue_monthly["collection_rate"].round(4)
)

print(f"Monthly revenue records: {len(revenue_monthly):,}")

print(
    "Monthly reporting period:",
    revenue_monthly["reporting_month"].min().date(),
    "to",
    revenue_monthly["reporting_month"].max().date()
)

# ============================================================
# VALIDATE MONTHLY REVENUE SUMMARY
# ============================================================

print("\nValidating monthly revenue summary...")

raw_billed_total = revenue_clean["billed_amount"].sum()
monthly_billed_total = revenue_monthly["total_billed_revenue"].sum()

raw_collected_total = revenue_clean["collected_amount"].sum()
monthly_collected_total = revenue_monthly["total_collected_revenue"].sum()

raw_transaction_count = len(revenue_clean)
monthly_transaction_count = revenue_monthly["transaction_count"].sum()

print(f"Raw Billed Revenue: ${raw_billed_total:,.2f}")
print(f"Monthly Billed Revenue: ${monthly_billed_total:,.2f}")

print(f"Raw Collected Revenue: ${raw_collected_total:,.2f}")
print(f"Monthly Collected Revenue: ${monthly_collected_total:,.2f}")

print(f"Raw Transaction Count: {raw_transaction_count:,}")
print(f"Monthly Transaction Count: {monthly_transaction_count:,}")

print(
    "Billed Revenue Reconciled:",
    round(raw_billed_total, 2) == round(monthly_billed_total, 2)
)

print(
    "Collected Revenue Reconciled:",
    round(raw_collected_total, 2) == round(monthly_collected_total, 2)
)

print(
    "Transaction Count Reconciled:",
    raw_transaction_count == monthly_transaction_count
)

# ============================================================
# SAVE MONTHLY REVENUE DATASET
# ============================================================

revenue_monthly_path = (
    PROCESSED_DATA_DIR / "revenue_monthly.csv"
)

revenue_monthly.to_csv(
    revenue_monthly_path,
    index=False
)

print(f"\nSaved processed dataset: {revenue_monthly_path}")
print(f"Rows: {len(revenue_monthly):,}")

# ============================================================
# PREPARE SUBSCRIPTION DATA
# ============================================================

print("\nPreparing subscription data...")

# Inspect subscription columns
print("\nSubscription Columns:")

for column in subscriptions.columns:
    print(f" - {column}")

# Convert subscription date columns to datetime
# subscription_date_columns = [
#     "subscription_start_date",
#     "subscription_end_date",
#     "cancellation_date"
# ]

# for column in subscription_date_columns:
#     subscriptions[column] = pd.to_datetime(
#         subscriptions[column],
#         errors="coerce"
#     )

# print("Subscription data prepared successfully.")

# print(
#     "Subscription Date Range:",
#     subscriptions["subscription_start_date"].min().date(),
#     "to",
#     subscriptions["subscription_start_date"].max().date()
# )

# print(
#     "Subscription Records:",
#     f"{len(subscriptions):,}"
# )

# Convert subscription date columns to datetime
subscription_date_columns = [
    "subscription_start_date",
    "renewal_date",
    "cancellation_date"
]

for column in subscription_date_columns:
    subscriptions[column] = pd.to_datetime(
        subscriptions[column],
        errors="coerce"
    )

print("Subscription data prepared successfully.")

print(
    "Subscription Start Date Range:",
    subscriptions["subscription_start_date"].min().date(),
    "to",
    subscriptions["subscription_start_date"].max().date()
)

print(
    "Subscription Records:",
    f"{len(subscriptions):,}"
)

# ============================================================
# CREATE MONTHLY SUBSCRIPTION REPORTING CALENDAR
# ============================================================

print("\nCreating monthly subscription reporting calendar...")

subscription_reporting_start = pd.Timestamp("2024-01-01")
subscription_reporting_end = pd.Timestamp("2026-07-01")

subscription_months = pd.date_range(
    start=subscription_reporting_start,
    end=subscription_reporting_end,
    freq="MS"
)

print(
    "Subscription Reporting Months:",
    len(subscription_months)
)

print(
    "Subscription Reporting Period:",
    subscription_months.min().date(),
    "to",
    subscription_months.max().date()
)

# ============================================================
# BUILD MONTHLY SUBSCRIPTION SNAPSHOT
# ============================================================

print("\nBuilding monthly subscription snapshot...")

subscription_snapshot_records = []

for reporting_month in subscription_months:

    # Month-end date for the reporting period
    month_end = reporting_month + pd.offsets.MonthEnd(0)

    # Subscription must have started by the end of the month
    started_mask = (
        subscriptions["subscription_start_date"] <= month_end
    )

    # Subscription is considered active if it had not yet been
    # cancelled by the beginning of the reporting month
    not_cancelled_mask = (
        subscriptions["cancellation_date"].isna()
        | (subscriptions["cancellation_date"] >= reporting_month)
    )

    active_subscriptions = subscriptions[
        started_mask & not_cancelled_mask
    ].copy()
    # Define reporting month boundaries
    month_start = reporting_month
    month_end = reporting_month + pd.offsets.MonthEnd(0)

    # Subscriptions that started during the reporting month
    new_subscriptions = subscriptions[
        subscriptions["subscription_start_date"].between(
            month_start,
            month_end
        )
    ]

    # Subscriptions that were cancelled during the reporting month
    cancelled_subscriptions = subscriptions[
        subscriptions["cancellation_date"].between(
            month_start,
            month_end
        )
    ]
    subscription_snapshot_records.append({
    "reporting_month": reporting_month.date(),
    "active_subscriptions": len(active_subscriptions),
    "active_customers": active_subscriptions[
        "account_id"
    ].nunique(),
    "monthly_recurring_revenue": active_subscriptions[
        "monthly_recurring_revenue"
    ].sum(),
    "annual_recurring_revenue": active_subscriptions[
        "annual_recurring_revenue"
    ].sum(),
    "new_subscriptions": len(new_subscriptions),
    "cancelled_subscriptions": len(cancelled_subscriptions)
})
subscription_monthly = pd.DataFrame(
subscription_snapshot_records
)
# Calculate net subscription change
subscription_monthly["net_subscription_change"] = (
    subscription_monthly["new_subscriptions"]
    - subscription_monthly["cancelled_subscriptions"]
)
# Calculate beginning-of-month subscriptions
subscription_monthly["beginning_subscriptions"] = (
    subscription_monthly["active_subscriptions"].shift(1)
)

# Calculate monthly subscription churn rate
subscription_monthly["subscription_churn_rate"] = (
    subscription_monthly["cancelled_subscriptions"]
    / subscription_monthly["beginning_subscriptions"]
)

# Convert churn rate to percentage
subscription_monthly["subscription_churn_rate"] = (
    subscription_monthly["subscription_churn_rate"] * 100
).round(2)

# Calculate monthly subscription growth rate
subscription_monthly["subscription_growth_rate"] = (
    (
        subscription_monthly["active_subscriptions"]
        - subscription_monthly["beginning_subscriptions"]
    )
    / subscription_monthly["beginning_subscriptions"]
    * 100
).round(2)

print(
    "Monthly subscription snapshot records:",
    len(subscription_monthly)
)

print("\nFirst 5 monthly subscription snapshots:")
print(subscription_monthly.head())
print("\nSubscription Snapshot Detail:")

print(
    subscription_monthly.head().to_string(
        index=False
    )
)

# ============================================================
# SAVE MONTHLY SUBSCRIPTION DATASET
# ============================================================

subscription_monthly_path = (
    PROCESSED_DATA_DIR / "subscription_monthly.csv"
)

subscription_monthly.to_csv(
    subscription_monthly_path,
    index=False
)

print(
    f"\nSaved processed dataset: {subscription_monthly_path}"
)
print(f"Rows: {len(subscription_monthly):,}")

# ============================================================
# PREPARE CUSTOMER SUCCESS DATA
# ============================================================

print("\nPreparing customer success data...")

# Display available customer success columns
print("\nCustomer Success Columns:")

for column in customer_success_activity.columns:
    print(f" - {column}")

# Convert customer success activity month to datetime
customer_success_activity["activity_month"] = pd.to_datetime(
    customer_success_activity["activity_month"],
    errors="coerce"
)

# Validate activity dates
invalid_cs_dates = (
    customer_success_activity["activity_month"]
    .isna()
    .sum()
)

print(
    "\nInvalid Customer Success Activity Dates:",
    invalid_cs_dates
)

print(
    "Customer Success Date Range:",
    customer_success_activity["activity_month"].min().date(),
    "to",
    customer_success_activity["activity_month"].max().date()
)

print(
    "Customer Success Records:",
    f"{len(customer_success_activity):,}"
)

# ============================================================
# CREATE MONTHLY CUSTOMER SUCCESS SUMMARY
# ============================================================

print("\nCreating monthly customer success summary...")

customer_success_monthly = (
    customer_success_activity
    .groupby("activity_month")
    .agg(
        active_customers=("account_id", "nunique"),
        average_health_score=("health_score", "mean"),
        average_satisfaction_score=("satisfaction_score", "mean"),
        total_support_tickets=("support_tickets", "sum")
    )
    .reset_index()
)

# Rename activity month for consistent reporting
customer_success_monthly = customer_success_monthly.rename(
    columns={"activity_month": "reporting_month"}
)

# Round executive KPI measures
customer_success_monthly["average_health_score"] = (
    customer_success_monthly["average_health_score"].round(2)
)

customer_success_monthly["average_satisfaction_score"] = (
    customer_success_monthly["average_satisfaction_score"].round(2)
)

print(
    "Monthly customer success records:",
    len(customer_success_monthly)
)

print(
    "Customer Success Reporting Period:",
    customer_success_monthly["reporting_month"].min().date(),
    "to",
    customer_success_monthly["reporting_month"].max().date()
)

# Create monthly customer health category counts
health_category_monthly = (
    customer_success_activity
    .groupby(
        ["activity_month", "health_category"]
    )["account_id"]
    .nunique()
    .unstack(fill_value=0)
    .reset_index()
)

# Rename columns for reporting
health_category_monthly = health_category_monthly.rename(
    columns={
        "activity_month": "reporting_month",
        "Healthy": "healthy_customers",
        "Monitor": "monitor_customers",
        "At Risk": "at_risk_customers",
        "Critical": "critical_customers"
    }
)

# Merge health counts into monthly customer success summary
customer_success_monthly = customer_success_monthly.merge(
    health_category_monthly,
    on="reporting_month",
    how="left"
)

# Calculate total customers requiring intervention
customer_success_monthly["customers_requiring_intervention"] = (
    customer_success_monthly["at_risk_customers"]
    + customer_success_monthly["critical_customers"]
)

# Calculate at-risk customer rate
customer_success_monthly["at_risk_customer_rate"] = (
    customer_success_monthly["customers_requiring_intervention"]
    / customer_success_monthly["active_customers"]
    * 100
).round(2)

print("\nFirst 5 monthly customer success records:")
print(customer_success_monthly.head())

# Save processed monthly customer success dataset
customer_success_monthly_path = (
    PROCESSED_DATA_DIR / "customer_success_monthly.csv"
)

customer_success_monthly.to_csv(
    customer_success_monthly_path,
    index=False
)

print(
    f"\nSaved processed dataset: "
    f"{customer_success_monthly_path}"
)
print(f"Rows: {len(customer_success_monthly):,}")

# ============================================================
# PREPARE SALES OPPORTUNITY DATA
# ============================================================

print("\nPreparing sales opportunity data...")

print("\nOpportunity Columns:")
for column in opportunities.columns:
    print(f" - {column}")

# Convert opportunity date columns to datetime
opportunity_date_columns = [
    "created_date",
    "expected_close_date",
    "actual_close_date"
]

for column in opportunity_date_columns:
    opportunities[column] = pd.to_datetime(
        opportunities[column],
        errors="coerce"
    )

# Validate opportunity dates
print(
    "\nInvalid Opportunity Created Dates:",
    opportunities["created_date"].isna().sum()
)

print(
    "Opportunity Created Date Range:",
    opportunities["created_date"].min().date(),
    "to",
    opportunities["created_date"].max().date()
)

print(f"Opportunity Records: {len(opportunities):,}")

# Create monthly sales reporting calendar
print("\nCreating monthly sales reporting calendar...")

sales_reporting_months = pd.date_range(
    start="2024-01-01",
    end="2026-07-01",
    freq="MS"
)

print(
    "Sales Reporting Months:",
    len(sales_reporting_months)
)

print(
    "Sales Reporting Period:",
    sales_reporting_months.min().date(),
    "to",
    sales_reporting_months.max().date()
)

# Build monthly sales pipeline snapshot
print("\nBuilding monthly sales pipeline snapshot...")

sales_snapshot_records = []

for reporting_month in sales_reporting_months:

    month_end = reporting_month + pd.offsets.MonthEnd(0)

    # Opportunities created during the month
    created_this_month = opportunities[
        (opportunities["created_date"] >= reporting_month)
        & (opportunities["created_date"] <= month_end)
    ]

    # Opportunities won during the month
    won_this_month = opportunities[
        (opportunities["won_opportunity_flag"] == True)
        & (opportunities["actual_close_date"] >= reporting_month)
        & (opportunities["actual_close_date"] <= month_end)
    ]

    # Opportunities lost during the month
    lost_this_month = opportunities[
        (opportunities["lost_opportunity_flag"] == True)
        & (opportunities["actual_close_date"] >= reporting_month)
        & (opportunities["actual_close_date"] <= month_end)
    ]

    # Open pipeline as of month end
    open_pipeline = opportunities[
        (opportunities["created_date"] <= month_end)
        & (
            opportunities["actual_close_date"].isna()
            | (opportunities["actual_close_date"] > month_end)
        )
    ]

    sales_snapshot_records.append({
        "reporting_month": reporting_month,
        "new_opportunities": len(created_this_month),
        "new_pipeline_value": created_this_month["opportunity_value"].sum(),
        "open_opportunities": len(open_pipeline),
        "open_pipeline_value": open_pipeline["opportunity_value"].sum(),
        "won_opportunities": len(won_this_month),
        "won_opportunity_value": won_this_month["opportunity_value"].sum(),
        "lost_opportunities": len(lost_this_month),
        "lost_opportunity_value": lost_this_month["opportunity_value"].sum()
    })

sales_monthly = pd.DataFrame(sales_snapshot_records)

# Calculate closed opportunities
sales_monthly["closed_opportunities"] = (
    sales_monthly["won_opportunities"]
    + sales_monthly["lost_opportunities"]
)

# Calculate win rate
sales_monthly["win_rate"] = (
    sales_monthly["won_opportunities"]
    / sales_monthly["closed_opportunities"]
    * 100
).round(2)

# Calculate average won deal size
sales_monthly["average_won_deal_size"] = (
    sales_monthly["won_opportunity_value"]
    / sales_monthly["won_opportunities"]
).round(2)

# Replace undefined values when no deals were closed/won
sales_monthly["win_rate"] = (
    sales_monthly["win_rate"].fillna(0)
)

sales_monthly["average_won_deal_size"] = (
    sales_monthly["average_won_deal_size"].fillna(0)
)

print(
    "Monthly sales snapshot records:",
    len(sales_monthly)
)

print("\nFirst 5 monthly sales snapshots:")
print(sales_monthly.head())