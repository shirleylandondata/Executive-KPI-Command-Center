import pandas as pd
import numpy as np
import random
from pathlib import Path
from datetime import datetime, timedelta

# Reproducibility
SEED = 42

random.seed(SEED)
np.random.seed(SEED)

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"

# Ensure folders exist
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

print("Northstar Analytics data generation environment ready.")
print(f"Raw data directory: {RAW_DATA_DIR}")
print(f"Processed data directory: {PROCESSED_DATA_DIR}")

# ============================================================
# REFERENCE DATASETS
# ============================================================

# ------------------------------------------------------------
# Subscription Plans
# ------------------------------------------------------------
subscription_plans = pd.DataFrame({
    "plan_id": [
        "PLAN-001",
        "PLAN-002",
        "PLAN-003",
        "PLAN-004"
    ],

    "plan_name": [
        "Starter",
        "Growth",
        "Professional",
        "Enterprise"
    ],

    "plan_tier": [
        "Starter",
        "Growth",
        "Professional",
        "Enterprise"
    ],

    "billing_frequency": [
        "Monthly",
        "Monthly",
        "Monthly",
        "Annual"
    ],

    "standard_monthly_price": [
        299.00,
        749.00,
        1499.00,
        3999.00
    ],

    "include_users": [
        5,
        20,
        50,
        150
    ],

    "target_customer_segment": [
        "Startup",
        "SMB",
        "Mid-Market",
        "Enterprise"
    ],

    "active_plan_flag": [
        True,
        True,
        True,
        True
    ]
})

subscription_plans_path = RAW_DATA_DIR / "subscription_plans.csv"

subscription_plans.to_csv(
    subscription_plans_path,
    index=False
)

print(f"Created: {subscription_plans_path}")
print(f"Rows: {len(subscription_plans):,}")

# ------------------------------------------------------------
# Sales Representatives
# ------------------------------------------------------------

sales_representatives = pd.DataFrame({
    "sales_rep_id":[
        "SR-001",
        "SR-002",
        "SR-003",
        "SR-004",
        "SR-005",
        "SR-006",
        "SR-007",
        "SR-008"
    ],

    "sales_rep_name":[
        "Jordan Lee",
        "Alex Morgan",
        "Tyler Brooks",
        "Cameron Davis",
        "Morgan Reed",
        "Casey Parker",
        "Riley Bennett",
        "Jamie Collins"
    ],
    "sales_team": [
        "SMB Sales",
        "SMB Sales",
        "Mid-Market Sales",
        "Mid-Market Sales",
        "Enterprise Sales",
        "Enterprise Sales",
        "Strategic Accounts",
        "Strategic Accounts"
    ],

    "sales_region": [
        "Northeast",
        "Southeast",
        "Midwest",
        "West",
        "Northeast",
        "Southeast",
        "West",
        "International"
    ],

    "manager_name": [
        "Avery Thompson",
        "Avery Thompson",
        "Blake Wilson",
        "Blake Wilson",
        "Morgan Davis",
        "Morgan Davis",
        "Chris Anderson",
        "Chris Anderson"
    ],

    "hire_date": pd.to_datetime([
        "2022-03-14",
        "2023-01-09",
        "2021-08-23",
        "2023-06-12",
        "2020-11-02",
        "2022-09-19",
        "2021-04-05",
        "2024-02-12"
    ]),

    "annual_quota": [
        500000.00,
        500000.00,
        850000.00,
        850000.00,
        1500000.00,
        1500000.00,
        2250000.00,
        2250000.00
    ],

    "active_rep_flag": [
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True
    ]
})

sales_representatives_path = RAW_DATA_DIR / "sales_representatives.csv"

sales_representatives.to_csv(
    sales_representatives_path,
    index=False
)

print(f"Created: {sales_representatives_path}")
print(f"Rows: {len(sales_representatives):,}")

# ------------------------------------------------------------
# Sales Stages
# ------------------------------------------------------------

sales_stages = pd.DataFrame({
    "sales_stage_id": [
        "STG-001",
        "STG-002",
        "STG-003",
        "STG-004",
        "STG-005",
        "STG-006",
        "STG-007"
    ],

    "sales_stage_name": [
        "Prospecting",
        "Qualification",
        "Discovery",
        "Proposal",
        "Negotiation",
        "Closed Won",
        "Closed Lost"
    ],

    "stage_order": [
        1,
        2,
        3,
        4,
        5,
        6,
        7
    ],

    "stage_category": [
        "Early Pipeline",
        "Early Pipeline",
        "Active Pipeline",
        "Active Pipeline",
        "Active Pipeline",
        "Closed",
        "Closed"
    ],

    "probability_to_close": [
        10.00,
        25.00,
        40.00,
        65.00,
        80.00,
        100.00,
        0.00
    ],

    "active_stage_flag": [
        True,
        True,
        True,
        True,
        True,
        True,
        True
    ]
})

sales_stages_path = RAW_DATA_DIR / "sales_stages.csv"

sales_stages.to_csv(
    sales_stages_path,
    index=False
)

print(f"Created: {sales_stages_path}")
print(f"Rows: {len(sales_stages):,}")

# ------------------------------------------------------------
# Customer Success Managers
# ------------------------------------------------------------

customer_success_managers = pd.DataFrame({
    "customer_success_manager_id": [
        "CSM-001",
        "CSM-002",
        "CSM-003",
        "CSM-004",
        "CSM-005",
        "CSM-006"
    ],

    "customer_success_manager_name": [
        "Avery Johnson",
        "Jordan Ramirez",
        "Taylor Chen",
        "Morgan Patel",
        "Casey Williams",
        "Riley Martinez"
    ],

    "team": [
        "SMB Success",
        "SMB Success",
        "Mid-Market Success",
        "Mid-Market Success",
        "Enterprise Success",
        "Enterprise Success"
    ],

    "region": [
        "Northeast",
        "Southeast",
        "Midwest",
        "West",
        "Northeast",
        "International"
    ],

    "hire_date": pd.to_datetime([
        "2022-05-16",
        "2023-02-06",
        "2021-09-20",
        "2023-07-10",
        "2020-08-03",
        "2022-11-14"
    ]),

    "active_manager_flag": [
        True,
        True,
        True,
        True,
        True,
        True
    ]
})

customer_success_managers_path = (
    RAW_DATA_DIR / "customer_success_managers.csv"
)

customer_success_managers.to_csv(
    customer_success_managers_path,
    index=False
)

print(f"Created: {customer_success_managers_path}")
print(f"Rows: {len(customer_success_managers):,}")

# ------------------------------------------------------------
# Product Features
# ------------------------------------------------------------

product_features = pd.DataFrame({
    "product_feature_id": [
        "FEAT-001",
        "FEAT-002",
        "FEAT-003",
        "FEAT-004",
        "FEAT-005",
        "FEAT-006",
        "FEAT-007",
        "FEAT-008"
    ],

    "feature_name": [
        "Executive Dashboard",
        "Custom Reports",
        "AI Insights",
        "Data Export",
        "API Integration",
        "User Management",
        "Automated Alerts",
        "Team Collaboration"
    ],

    "feature_category": [
        "Analytics",
        "Reporting",
        "AI",
        "Reporting",
        "Integrations",
        "Administration",
        "Analytics",
        "Collaboration"
    ],

    "release_version": [
        "v1.0",
        "v1.2",
        "v4.0",
        "v1.5",
        "v2.0",
        "v1.0",
        "v3.1",
        "v2.5"
    ],

    "release_date": pd.to_datetime([
        "2020-01-15",
        "2020-06-10",
        "2024-03-18",
        "2020-09-21",
        "2021-04-12",
        "2020-01-15",
        "2023-02-06",
        "2022-05-16"
    ]),

    "active_feature_flag": [
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True
    ]
})

product_features_path = RAW_DATA_DIR / "product_features.csv"

product_features.to_csv(
    product_features_path,
    index=False
)

print(f"Created: {product_features_path}")
print(f"Rows: {len(product_features):,}")

# ============================================================
# CORE BUSINESS DATASETS
# ============================================================

# ------------------------------------------------------------
# Customers
# ------------------------------------------------------------

NUM_CUSTOMERS = 5000

industries = [
    "Financial Services",
    "Technology",
    "Healthcare",
    "Retail",
    "Manufacturing",
    "Professional Services",
    "Media",
    "Education" 
    
]

regions = [
    "Northeast",
    "Southeast",
    "Midwest",
    "West",
    "International"
]

countries_by_region = {
    "Northeast": ["United States"],
    "Southeast": ["United States"],
    "Midwest": ["United States"],
    "West": ["United States"],
    "International": [
        "Canada",
        "United Kingdom",
        "Germany",
        "Australia"
    ]
}

customer_segments = [
    "Startup",
    "SMB",
    "Mid-Market",
    "Enterprise"
]

segment_attributes = {
    "Startup": {
        "employee_bands": ["1-10", "11-50"],
        "revenue_bands": ["<$1M", "$1M-$5M"]
    },

    "SMB": {
        "employee_bands": ["11-50", "51-200"],
        "revenue_bands": ["$1M-$5M", "$5M-$25M"]
    },

    "Mid-Market": {
        "employee_bands": ["201-500", "501-1000"],
        "revenue_bands": ["$25M-$50M", "$50M-$100M"]
    },

    "Enterprise": {
        "employee_bands": ["1001-5000", "5000+"],
        "revenue_bands": ["$100M-$500M", "$500M+"]
    }
}
customer_records = []

for i in range(1, NUM_CUSTOMERS + 1):

    account_id = f"ACC-{i:05d}"
    account_name = f"Northstar Customer {i:05d}"

    industry = random.choice(industries)

    region = random.choices(
        regions,
        weights=[30, 20, 20, 25, 5],
        k=1
    )[0]

    country = random.choice(countries_by_region[region])

    customer_segment = random.choices(
        customer_segments,
        weights=[20, 35, 30, 15],
        k=1
    )[0]

    employee_band = random.choice(
        segment_attributes[customer_segment]["employee_bands"]
    )

    annual_revenue_band = random.choice(
        segment_attributes[customer_segment]["revenue_bands"]
    )

    start_date = datetime(2020, 1, 1)
    end_date = datetime(2025, 12, 31)

    account_start_date = start_date + timedelta(
        days=random.randint(
            0, 
            (end_date - start_date).days
        )
    )

    customer_status = random.choices(
        ["Active", "Prospect", "Inactive", "Churned"],
        weights=[70, 10, 5, 15],
        k=1
    )[0]

    sales_rep_id = random.choice(
        sales_representatives["sales_rep_id"].tolist()
    )

    customer_success_manager_id = random.choice(
        customer_success_managers[
            "customer_success_manager_id"
        ].tolist()
    )

    effective_start_date = account_start_date
    effective_end_date = datetime(9999, 12, 31)
    current_record_flag = True

    customer_records.append({
        "account_id": account_id,
        "account_name": account_name,
        "industry": industry,
        "region": region,
        "country": country,
        "customer_segment": customer_segment,
        "employee_band": employee_band,
        "annual_revenue_band": annual_revenue_band,
        "account_start_date": account_start_date.date(),
        "customer_status": customer_status,
        "sales_rep_id": sales_rep_id,
        "customer_success_manager_id":
            customer_success_manager_id,
        "effective_start_date":
            effective_start_date.date(),
        "effective_end_date":
            effective_end_date.date(),
        "current_record_flag": current_record_flag
    })

    # Create customer DataFrame
customers = pd.DataFrame(customer_records)

# Save customer dataset
customers_path = RAW_DATA_DIR / "customers.csv"

customers.to_csv(
    customers_path,
    index=False
)

print(f"Created: {customers_path}")
print(f"Rows: {len(customers):,}")

# ------------------------------------------------------------
# Customer Data Quality Checks
# ------------------------------------------------------------

print("\nCustomer Segment Distribution:")
print(customers["customer_segment"].value_counts())

print("\nCustomer Status Distribution:")
print(customers["customer_status"].value_counts())

print(
    "\nDuplicate Account IDs:",
    customers["account_id"].duplicated().sum()
)

print(
    "Missing Account IDs:",
    customers["account_id"].isna().sum()
)

# ============================================================
# GENERATE SUBSCRIPTIONS
# ============================================================

print("\nGenerating subscriptions...")

subscription_records = []

# Create quick Lookup for plan information

plan_Lookup = subscription_plans.set_index(
    "plan_id"
). to_dict("index")

# Plan selection probabilities by customer segment
plan_probabilities = {
    "Startup": {
        "Starter": 0.60,
        "Growth": 0.30,
        "Professional": 0.08,
        "Enterprise": 0.02
    },
    "SMB": {
        "Starter": 0.30,
        "Growth": 0.45,
        "Professional": 0.20,
        "Enterprise": 0.05
    },
    "Mid-Market": {
        "Starter": 0.10,
        "Growth": 0.35,
        "Professional": 0.40,
        "Enterprise": 0.15
    },
    "Enterprise": {
        "Starter": 0.02,
        "Growth": 0.08,
        "Professional": 0.35,
        "Enterprise": 0.55
    }

}
print("Subscription generation setup complete")

# ------------------------------------------------------------
# Create Subscription Records
# ------------------------------------------------------------

subscription_number = 1

for _, customer in customers.iterrows():

    # Prospects do not have subscriptions yet"
    if customer["customer_status"] == "Prospect":
        continue

    account_id = customer["account_id"]
    customer_segment = customer["customer_segment"]
    customer_status = customer["customer_status"]

    subscription_id = f"SUB-{subscription_number:05d}"

    # Select a plan based on customer segment
    probabilities = plan_probabilities[customer_segment]

    selected_plan_name = random.choices(
        list(probabilities.keys()),
        weights=list(probabilities.values()),
        k=1
    )[0]

    # Find the corresponding plan ID
    selected_plan = subscription_plans[
        subscription_plans["plan_name"] == selected_plan_name
    ].iloc[0]

    plan_id = selected_plan["plan_id"]
    monthly_price = selected_plan["standard_monthly_price"]

    account_start_date = pd.to_datetime(
        customer["account_start_date"]
    )

    # Subscription begins shortly after the account is created

    subscription_start_date = (
        account_start_date
            + timedelta(days=random.randint(0, 30))
    )

    # Annual renewal date

    renewal_date = subscription_start_date + pd.DateOffset(years=1)

    # Determine subscription status

    if customer_status == "Active":
        subscription_status = "Active"
        cancellation_date = None
        cancellation_reason = None

    elif customer_status == "Churned":
        subscription_status = "Cancelled"

        cancellation_date = (
           subscription_start_date
           + timedelta(days=random.randint(90, 900))
        )
        cancellation_reason = random.choice([
            "Budget Constraints",
            "Low Product Adoption",
            "Switch Provider",
            "Business Closure",
            "Missing Features"
        ])

    elif customer_status == "Inactive":
        subscription_status = random.choice([
            "Cancelled",
            "Expired"
        ])
    else:
        subscription_status = "Active"
        cancellation_date = None
        cancellation_reason = None

    # Billing frequency comes from the selected plan
    billing_frequency = selected_plan["billing_frequency"]

    # Monthly recurring revenue
    monthly_recurring_revenue = float(monthly_price)

    # Annual recurring revenue
    annual_recurring_revenue = (
        monthly_recurring_revenue * 12
    )

    # Payment behavior
    if subscription_status == "Active":
        payment_status = random.choices(
            ["Paid", "Past Due", "Failed"],
            weights=[90, 7, 3],
            k=1
        )[0]
    else:
        payment_status = random.choice([
            "Paid",
            "Past Due",
            "Failed"
        ])

    # Most active subscriptions automatically renew
    auto_renewal_flag = (
        random.random() < 0.85
        if subscription_status == "Active"
        else False
    )

    subscription_records.append({
        "subscription_id": subscription_id,
        "account_id": account_id,
        "plan_id": plan_id,
        "subscription_start_date":
            subscription_start_date.date(),
        "renewal_date":
            renewal_date.date(),
        "billing_frequency":
            billing_frequency,
        "monthly_recurring_revenue":
            monthly_recurring_revenue,
        "annual_recurring_revenue":
            annual_recurring_revenue,
        "subscription_status":
            subscription_status,
        "cancellation_date":
            cancellation_date.date()
            if cancellation_date is not None
            else None,
        "cancellation_reason":
            cancellation_reason,
        "payment_status":
            payment_status,
        "auto_renewal_flag":
            auto_renewal_flag
    })

    subscription_number += 1

# Create subscription DataFrame
subscriptions = pd.DataFrame(subscription_records)

# Save subscription dataset
subscriptions_path = RAW_DATA_DIR / "subscriptions.csv"

subscriptions.to_csv(
    subscriptions_path,
    index=False
)

print(f"\nCreated: {subscriptions_path}")
print(f"Rows: {len(subscriptions):,}")

# ------------------------------------------------------------
# Validate Subscription Dataset
# ------------------------------------------------------------

print("\nSubscription Status Distribution:")
print(
    subscriptions["subscription_status"].value_counts()
)

print("\nPlan Distribution:")
print(
    subscriptions["plan_id"].value_counts()
)

print(
    "\nDuplicate Subscription IDs:",
    subscriptions["subscription_id"].duplicated().sum()
)

print(
    "Missing Account IDs:",
    subscriptions["account_id"].isna().sum()
)

# ============================================================
# GENERATE REVENUE TRANSACTIONS
# ============================================================

print("\nGenerating revenue transactions...")

revenue_transaction_records = []

transaction_number = 1

# Transaction reporting period

transaction_start_date = pd.Timestamp("2024-01-01")
transaction_end_date = pd.Timestamp("2026-07-31")

print(
    f"Revenue reporting period: "
    f"{transaction_start_date.date()} to "
    f"{transaction_end_date.date()}"
)

for _, subscription in subscriptions.iterrows():

    subscription_id = subscription["subscription_id"]
    account_id = subscription["account_id" ]
    plan_id = subscription["plan_id"]

    subscription_start = pd.to_datetime(
        subscription["subscription_start_date"]
    )

    subscription_status = subscription[
        "subscription_status"
    ]

    monthly_revenue = float(
        subscription["monthly_recurring_revenue"]
    )

    # Determine the last possible billing date
    if pd.notna(subscription["cancellation_date"]):
        subscription_end = pd.to_datetime(
            subscription["cancellation_date"]
        )
    else:
        subscription_end = transaction_end_date

    # Do not generate transactions before our reporting period
    billing_start = max(
        subscription_start.replace(day=1),
        transaction_start_date
    )

    # Do not generate transactions beyond our reporting period
    billing_end = min(
        subscription_end,
        transaction_end_date
    )

    if billing_start > billing_end:
        continue

    billing_dates = pd.date_range(
        start=billing_start,
        end=billing_end,
        freq="MS"
    )

    for billing_date in billing_dates:

        transaction_id = (
            f"TXN-{transaction_number:07d}"
        )

        # Determine payment outcome
        payment_outcome = random.choices(
            ["Successful", "Failed"],
            weights=[95, 5],
            k=1
        )[0]

        transaction_type = random.choices(
            ["Subscription", "Upgrade", "Add-On"],
            weights=[92, 5, 3],
            k=1
        )[0]

        # Billed amount reflects the transaction type
        billed_amount = monthly_revenue
        if transaction_type == "Upgrade":
            billed_amount *= 1.25
        elif transaction_type == "Add-On":
            billed_amount *= 1.10
        billed_amount = round(billed_amount, 2)

        # Only successful payments are collected
        if payment_outcome == "Successful":
            collected_amount = billed_amount
        else:
            collected_amount = 0.0

        # Create invoice ID
        invoice_id = (
            f"INV-{transaction_number:07d}"
        )

        # Select payment method
        payment_method = random.choices(
            [
                "Credit Card",
                "ACH",
                "Wire Transfer"
            ],
            weights=[65, 25, 10],
            k=1
        )[0]

        # Add transaction record
        revenue_transaction_records.append({
            "transaction_id": transaction_id,
            "invoice_id": invoice_id,
            "account_id": account_id,
            "subscription_id": subscription_id,
            "plan_id": plan_id,
            "transaction_date": max(billing_date, subscription_start).date(),
            "transaction_type": transaction_type,
            "payment_method": payment_method,
            "payment_outcome": payment_outcome,
            "billed_amount": billed_amount,
            "collected_amount": collected_amount
        })

        transaction_number += 1
# ------------------------------------------------------------
# Create Revenue Transaction Dataset
# ------------------------------------------------------------

revenue_transactions = pd.DataFrame(
    revenue_transaction_records
)

revenue_transactions_path = (
    RAW_DATA_DIR / "revenue_transactions.csv"
)

revenue_transactions.to_csv(
    revenue_transactions_path,
    index=False
)

print(
    f"\nCreated: {revenue_transactions_path}"
)

print(
    f"Rows: {len(revenue_transactions):,}"
)

# ============================================================
# GENERATE PRODUCT USAGE
# ============================================================

print("\nGenerating product usage...")

usage_records = []

usage_number = 1

# Product usage reporting period
usage_start_date = pd.Timestamp("2024-01-01")
usage_end_date = pd.Timestamp("2026-07-31")

print(
    f"Product usage reporting period: "
    f"{usage_start_date.date()} to {usage_end_date.date()}"
)

# Only customers who have an active or historical subscription
eligible_subscriptions = subscriptions[
    subscriptions["subscription_status"].isin(
        ["Active", "Cancelled", "Expired"]
    )
].copy()

print(
    f"Eligible subscriptions for usage generation: "
    f"{len(eligible_subscriptions):,}"
)


# ------------------------------------------------------------
# Generate monthly feature-level usage
# ------------------------------------------------------------

usage_record_number = 1

for _, subscription in eligible_subscriptions.iterrows():

    account_id = subscription["account_id"]
    subscription_id = subscription["subscription_id"]

    subscription_start = pd.Timestamp(
        subscription["subscription_start_date"]
    )

    subscription_status = subscription["subscription_status"]

    # Usage cannot begin before the subscription starts
    account_usage_start = max(
        subscription_start,
        usage_start_date
    )

    # Determine when product usage should stop
    if (
        subscription_status == "Cancelled"
        and pd.notna(subscription["cancellation_date"])
    ):
        account_usage_end = min(
            pd.Timestamp(subscription["cancellation_date"]),
            usage_end_date
        )

    else:
        account_usage_end = usage_end_date

    # Skip subscriptions outside the reporting period
    if account_usage_start > account_usage_end:
        continue

    # Create monthly observation dates
    usage_months = pd.date_range(
        start=account_usage_start,
        end=account_usage_end,
        freq="MS"
    )

        # Determine how many product features this account adopts
    feature_count = random.choices(
        [2, 3, 4, 5, 6, 7, 8],
        weights=[5, 10, 15, 20, 20, 18, 12],
        k=1
    )[0]

# All generated product features are available for adoption
    available_features = product_features.copy()
    

    feature_count = min(
        feature_count,
        len(available_features)
    )

    adopted_features = available_features.sample(
        n=feature_count,
        random_state=random.randint(1, 100000)
    )

        # Generate monthly usage for each adopted feature
    for usage_month in usage_months:

        for _, feature in adopted_features.iterrows():

            feature_id = feature["product_feature_id"]

            # Generate monthly session activity
            sessions = random.randint(3, 40)

            # Usage events should generally exceed sessions
            usage_events = sessions * random.randint(2, 8)

            # Number of individual users engaging with the feature
            active_users = random.randint(
                1,
                min(25, sessions)
            )

            # Number of days the feature was used during the month
            active_days = random.randint(
                1,
                min(28, sessions)
            )

            # Average session duration in minutes
            avg_session_duration_minutes = round(
                random.uniform(3, 45),
                2
            )

            # Create a simple engagement score from 0 to 100
            engagement_score = round(
                min(
                    100,
                    (
                        (sessions / 40) * 35
                        + (usage_events / 320) * 35
                        + (active_days / 28) * 30
                    )
                ),
                2
            )

            # Store product usage record
            usage_records.append({
                "usage_id": f"USE-{usage_number:07d}",
                "subscription_id": subscription_id,
                "account_id": account_id,
                "product_feature_id": feature_id,
                "usage_month": usage_month.date(),
                "sessions": sessions,
                "usage_events": usage_events,
                "active_users": active_users,
                "active_days": active_days,
                "avg_session_duration_minutes": avg_session_duration_minutes,
                "engagement_score": engagement_score
            })

            usage_number += 1

# ============================================================
# CREATE PRODUCT USAGE DATASET
# ============================================================

product_usage = pd.DataFrame(usage_records)

product_usage_path = RAW_DATA_DIR / "product_usage.csv"

product_usage.to_csv(
    product_usage_path,
    index=False
)

print(f"\nCreated: {product_usage_path}")
print(f"Rows: {len(product_usage):,}")

# ============================================================
# PRODUCT USAGE VALIDATION
# ============================================================

print("\nProduct Usage Validation:")

print(
    "Duplicate Usage IDs:",
    product_usage["usage_id"].duplicated().sum()
)

print(
    "Missing Subscription IDs:",
    product_usage["subscription_id"].isna().sum()
)

print(
    "Missing Account IDs:",
    product_usage["account_id"].isna().sum()
)

print(
    "Missing Product Feature IDs:",
    product_usage["product_feature_id"].isna().sum()
)

print(
    "Average Engagement Score:",
    round(product_usage["engagement_score"].mean(), 2)
)

print(
    "Average Monthly Sessions:",
    round(product_usage["sessions"].mean(), 2)
)

print(
    "Average Monthly Usage Events:",
    round(product_usage["usage_events"].mean(), 2)
)

print(
    "Usage Reporting Period:",
    product_usage["usage_month"].min(),
    "to",
    product_usage["usage_month"].max()
)
usage_number = 1

# ============================================================
# GENERATE SALES OPPORTUNITIES
# ============================================================

print("\nGenerating sales opportunities...")

opportunity_records = []
opportunity_number = 1

# Sales opportunity reporting period
opportunity_start_date = pd.Timestamp("2024-01-01")
opportunity_end_date = pd.Timestamp("2026-07-31")

print(
    f"Opportunity reporting period: "
    f"{opportunity_start_date.date()} to {opportunity_end_date.date()}"
)

# Customers eligible for sales opportunities
eligible_customers = customers[
    customers["customer_status"].isin(
        ["Active", "Churned", "Prospect", "Inactive"]
    )
].copy()

print(
    f"Eligible customers for opportunity generation: "
    f"{len(eligible_customers):,}"
)

# Generate opportunities for each eligible customer
for _, customer in eligible_customers.iterrows():

    account_id = customer["account_id"]
    customer_status = customer["customer_status"]

    # Most customers will have 1-3 opportunities
    opportunity_count = random.choices(
        [1, 2, 3],
        weights=[65, 25, 10],
        k=1
    )[0]

    for _ in range(opportunity_count):

        opportunity_id = f"OPP-{opportunity_number:06d}"

        # Assign a sales representative
        sales_rep = sales_representatives.sample(
            n=1,
            random_state=random.randint(1, 100000)
        ).iloc[0]

        sales_rep_id = sales_rep["sales_rep_id"]

        # Generate opportunity creation date
        created_date = pd.Timestamp(
            random.choice(
                pd.date_range(
                    start=opportunity_start_date,
                    end=opportunity_end_date,
                    freq="D"
                )
            )
        )

    # Assign sales stage
    stage = sales_stages.sample(
        n=1,
        random_state=random.randint(1, 100000)
    ).iloc[0]

    sales_stage_id = stage["sales_stage_id"]
    stage_name = stage["sales_stage_name"]

    # Generate opportunity value based on customer segment
    customer_segment = customer["customer_segment"]

    value_ranges = {
        "Startup": (5000, 25000),
        "SMB": (15000, 75000),
        "Mid-Market": (50000, 250000),
        "Enterprise": (150000, 1000000)
    }

    min_value, max_value = value_ranges[customer_segment]

    opportunity_value = round(
        random.uniform(min_value, max_value),
        2
    )

    # Expected close date occurs after opportunity creation
    expected_close_date = (
        created_date
        + timedelta(days=random.randint(30, 180))
    )

    # Do not allow expected close date beyond reporting period
    expected_close_date = min(
        expected_close_date,
        opportunity_end_date
    )

    # Determine whether the opportunity is closed
    if stage_name == "Closed Won":

        actual_close_date = (
            created_date
            + timedelta(days=random.randint(15, 120))
        )

        actual_close_date = min(
            actual_close_date,
            opportunity_end_date
        )

        won_opportunity_flag = True
        lost_opportunity_flag = False

    elif stage_name == "Closed Lost":

        actual_close_date = (
            created_date
            + timedelta(days=random.randint(15, 120))
        )

        actual_close_date = min(
            actual_close_date,
            opportunity_end_date
        )

        won_opportunity_flag = False
        lost_opportunity_flag = True

    else:

        actual_close_date = None
        won_opportunity_flag = False
        lost_opportunity_flag = False

    # Store opportunity record
    opportunity_records.append({
        "opportunity_id": opportunity_id,
        "account_id": account_id,
        "sales_rep_id": sales_rep_id,
        "sales_stage_id": sales_stage_id,
        "created_date": created_date.date(),
        "expected_close_date": expected_close_date.date(),
        "actual_close_date": (
            actual_close_date.date()
            if actual_close_date is not None
            else None
        ),
        "opportunity_value": opportunity_value,
        "won_opportunity_flag": won_opportunity_flag,
        "lost_opportunity_flag": lost_opportunity_flag
    })

    opportunity_number += 1

# ============================================================
# CREATE OPPORTUNITIES DATASET
# ============================================================

opportunities = pd.DataFrame(opportunity_records)

opportunities_path = RAW_DATA_DIR / "opportunities.csv"

opportunities.to_csv(
    opportunities_path,
    index=False
)

print(f"\nCreated: {opportunities_path}")
print(f"Rows: {len(opportunities):,}")

# ============================================================
# OPPORTUNITIES VALIDATION
# ============================================================

print("\nOpportunity Validation:")

print(
    "Duplicate Opportunity IDs:",
    opportunities["opportunity_id"].duplicated().sum()
)

print(
    "Missing Account IDs:",
    opportunities["account_id"].isna().sum()
)

print(
    "Missing Sales Rep IDs:",
    opportunities["sales_rep_id"].isna().sum()
)

print(
    "Missing Sales Stage IDs:",
    opportunities["sales_stage_id"].isna().sum()
)

print(
    "Total Pipeline Value:",
    round(opportunities["opportunity_value"].sum(), 2)
)

print(
    "Won Opportunities:",
    opportunities["won_opportunity_flag"].sum()
)

print(
    "Lost Opportunities:",
    opportunities["lost_opportunity_flag"].sum()
)

# ============================================================
# GENERATE CUSTOMER SUCCESS ACTIVITY
# ============================================================

print("\nGenerating customer success activity...")

cs_activity_records = []

cs_activity_start_date = pd.Timestamp("2024-01-01")
cs_activity_end_date = pd.Timestamp("2026-07-31")

print(
    f"Customer success reporting period: "
    f"{cs_activity_start_date.date()} to {cs_activity_end_date.date()}"
)

eligible_cs_customers = customers[
    customers["customer_status"].isin(
        ["Active", "Churned", "Inactive"]
    )
].copy()

print(
    f"Eligible customers for customer success activity: "
    f"{len(eligible_cs_customers):,}"
)

cs_activity_number = 1

# Generate customer success activity by account
for _, customer in eligible_cs_customers.iterrows():

    account_id = customer["account_id"]
    customer_status = customer["customer_status"]

    customer_success_manager_id = customer[
        "customer_success_manager_id"
    ]

    account_start_date = pd.Timestamp(
        customer["account_start_date"]
    )

    # Activity cannot begin before the customer account existed
    activity_start = max(
        account_start_date,
        cs_activity_start_date
    )

    if activity_start > cs_activity_end_date:
        continue

    # Generate monthly customer success activity
    activity_months = pd.date_range(
        start=activity_start,
        end=cs_activity_end_date,
        freq="MS"
    )

    for activity_month in activity_months:

    # Generate customer health score based on customer status
        if customer_status == "Active":
            health_score = random.randint(65, 100)

        elif customer_status == "Inactive":
            health_score = random.randint(35, 70)

        else:
            health_score = random.randint(10, 50)

    # Assign health category
        if health_score >= 80:
            health_category = "Healthy"
        elif health_score >= 60:
            health_category = "Monitor"
        elif health_score >= 40:
            health_category = "At Risk"
        else:
            health_category = "Critical"

    # Generate customer satisfaction score
        if health_category == "Healthy":
            satisfaction_score = round(random.uniform(4.0, 5.0), 1)
        elif health_category == "Monitor":
            satisfaction_score = round(random.uniform(3.0, 4.4), 1)
        elif health_category == "At Risk":
            satisfaction_score = round(random.uniform(2.0, 3.5), 1)
        else:
            satisfaction_score = round(random.uniform(1.0, 2.8), 1)

    # Determine renewal risk based on customer health
        if health_category == "Healthy":
            renewal_risk = "Low"
        elif health_category == "Monitor":
            renewal_risk = "Medium"
        elif health_category == "At Risk":
            renewal_risk = "High"
        else:
            renewal_risk = "Critical"

    # Generate support activity
        support_tickets = random.randint(0, 8)

        if health_category in ["At Risk", "Critical"]:
            support_tickets += random.randint(1, 5)

    # Store customer success activity record
        cs_activity_records.append({
                "cs_activity_id": f"CSA-{cs_activity_number:07d}",
                "account_id": account_id,
                "customer_success_manager_id": customer_success_manager_id,
                "activity_month": activity_month.date(),
                "health_score": health_score,
                "health_category": health_category,
                "satisfaction_score": satisfaction_score,
                "renewal_risk": renewal_risk,
                "support_tickets": support_tickets
        })

        cs_activity_number += 1  

# ============================================================
# CREATE CUSTOMER SUCCESS ACTIVITY DATASET
# ============================================================

customer_success_activity = pd.DataFrame(cs_activity_records)

customer_success_activity_path = (
    RAW_DATA_DIR / "customer_success_activity.csv"
)

customer_success_activity.to_csv(
    customer_success_activity_path,
    index=False
)

print(f"\nCreated: {customer_success_activity_path}")
print(f"Rows: {len(customer_success_activity):,}")

# ============================================================
# CUSTOMER SUCCESS ACTIVITY VALIDATION
# ============================================================

print("\nCustomer Success Activity Validation:")

print(
    "Duplicate Activity IDs:",
    customer_success_activity["cs_activity_id"].duplicated().sum()
)

print(
    "Missing Account IDs:",
    customer_success_activity["account_id"].isna().sum()
)

print(
    "Missing CSM IDs:",
    customer_success_activity["customer_success_manager_id"].isna().sum()
)

print(
    "Average Health Score:",
    round(customer_success_activity["health_score"].mean(), 2)
)

print(
    "Average Satisfaction Score:",
    round(customer_success_activity["satisfaction_score"].mean(), 2)
)

print("\nHealth Category Distribution:")
print(
    customer_success_activity["health_category"]
    .value_counts()
)

print("\nRenewal Risk Distribution:")
print(
    customer_success_activity["renewal_risk"]
    .value_counts()
)

print(
    "\nCustomer Success Reporting Period:",
    customer_success_activity["activity_month"].min(),
    "to",
    customer_success_activity["activity_month"].max()
)