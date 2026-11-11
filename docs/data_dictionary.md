# Data Dictionary

## Overview

The Executive KPI Command Center uses a standardized data dictionary to document every business entity, field, data type, business definition and validation rule used throughout the analytics platform.

The purpose of the data dictionary is to:

- Standardize business terminology
- Improve data quality
- Support consistent KPI calculations
- Reduce abiguity across departments
- Provide documentation for analysts, engineers, and business stakeholders

The dictionary documents all dimension and fact tables included in the dimensional model.

## Table Name

Business Purpose

Grain

Primary Key

Business Owner

Source Dataset

# dim_customer

## Business Purpose

Stores descriptive information about each B2B customer account.

## Grain

One row per customer account.

## Primary Key

customer_key

## Source

customers.csv

### Field Definitions

| Field | Data Type | Business Definition | Example | Required |
|--------|-----------|---------------------|---------|----------|
| customer_key | Integer | Warehouse surrogate key | 1025 | Yes |
| account_id | Varchar | Source system customer identifier | ACC-10025 | Yes |
| account_name | Varchar | Customer company name | Acme Manufacturing | Yes |
| industry | Varchar | Customer industry | Manufacturing | Yes |
| region | Varchar | Geographic sales region | Northeast | Yes |
| country | Varchar | Customer country | United States | Yes |
| customer_segment | Varchar | Customer size segment | Enterprise | Yes |
| employee_band | Varchar | Employee size category | 500–1000 | No |
| annual_revenue_band | Varchar | Estimated revenue range | $50M–$100M | No |
| account_start_date | Date | Original customer start date | 2023-04-01 | Yes |
| customer_status | Varchar | Current customer status | Active | Yes |
| sales_rep_id | Varchar | Assigned sales representative | SR-021 | Yes |
| customer_success_manager_id | Varchar | Assigned CSM | CSM-008 | Yes |
| effective_start_date | Date | SCD Type 2 start date | 2025-01-01 | Yes |
| effective_end_date | Date | SCD Type 2 end date | 9999-12-31 | Yes |
| current_record_flag | Boolean | Indicates current record | True | Yes |

---

## fact_subscription

## Business Purpose

Stores subscription-level revenue information.

## Grain

One row per subscription contract.

## Primary Key

subscription_fact_key

## Source

subscription.csv

### Field Definitions

| Field                       | Data Type | Business Definition        | Example  | Required |
| --------------------------- | --------- | -------------------------- | -------- | -------- |
| subscription_fact_key       | Integer   | Warehouse surrogate key    | 58022    | Yes      |
| subscription_id             | Varchar   | Subscription identifier    | SUB-9082 | Yes      |
| customer_key                | Integer   | Links to dim_customer      | 1025     | Yes      |
| plan_key                    | Integer   | Links to dim_plan          | 5        | No       |
| subscription_start_date_key | Integer   | Date dimension key         | 20250101 | Yes      |
| subscription_end_date_key   | Integer   | Subscription end date      | 20260101 | Yes      |
| cancellation_date_key       | Integer   | Cancellation date          | 20250715 | No       |
| monthly_recurring_revenue   | Decimal   | Monthly contract value     | 750.00   | Yes      |
| annual_recurring_revenue    | Decimal   | Annual contract value      | 9000.00  | Yes      |
| subscription_status         | Varchar   | Current subscription state | Active   | Yes      |
| payment_status              | Varchar   | Current payment status     | Paid     | Yes      |
| auto_renewal_flag           | Boolean   | Auto-renew enabled         | True     | Yes      |
| active_subscription_flag    | Boolean   | Currently active           | True     | Yes      |
| canceled_subscription_flag  | Boolean   | Subscription canceled      | False    | Yes      |

---

# fact_revenue_transaction

## Business Purpose

Stores individual financial transactions and recurring revenue movements for customer subscriptions.

## Grain

One row per financial transaction.

## Primary Key

revenue_transaction_key

## Source

finance_transactions.csv

### Field Definitions

| Field | Data Type | Business Definition | Example | Required |
|---|---|---|---|---|
| revenue_transaction_key | Integer | Warehouse surrogate key for the transaction record | 72501 | Yes |
| transaction_id | Varchar | Unique source-system transaction identifier | TXN-072501 | Yes |
| subscription_id | Varchar | Source subscription associated with the transaction | SUB-009082 | No |
| customer_key | Integer | Foreign key linking the transaction to dim_customer | 1025 | Yes |
| plan_key | Integer | Foreign key linking the transaction to dim_plan | 5 | No |
| transaction_date_key | Integer | Foreign key linking the transaction date to dim_date | 20250715 | Yes |
| transaction_type | Varchar | Classification of the financial or recurring revenue movement | Expansion | Yes |
| invoice_amount | Decimal(12,2) | Total amount invoiced to the customer | 1500.00 | No |
| payment_amount | Decimal(12,2) | Amount received from the customer | 1500.00 | No |
| recurring_revenue_amount | Decimal(12,2) | Monthly recurring revenue associated with the transaction | 250.00 | No |
| adjustment_amount | Decimal(12,2) | Financial correction, credit, or manual adjustment | -50.00 | No |
| net_transaction_amount | Decimal(12,2) | Final transaction value after adjustments | 1450.00 | Yes |
| currency | Varchar | Currency used for the transaction | USD | Yes |
| payment_status | Varchar | Current payment status of the transaction | Paid | Yes |

### Accepted Transaction Types

- New Revenue
- Expansion
- Contraction
- Renewal
- Churn
- Refund
- Adjustment

### Accepted Payment Status Values

- Paid
- Pending
- Failed
- Past Due
- Refund
- Partially Paid

### Validation Rules

- `transaction_id` must be unique.
- `customer_key` must match a valid record in `dim_customer`.
- `transaction_date_key` must match a valid record in `dim_date`.
- `currency` must equal `USD` in the first project version.
- `net_transaction_amount` should equal invoice amount plus adjustment amount when applicable.
- Negative recurring revenue amounts are permitted only for contraction or churn transactions.
- Refund transactions should have a negative payment or net transaction amount.
- A paid transaction should have a payment amount greater than zero.

---

# fact_sales_opportunity

## Business Purpose

Stores sales opportunities throughout the sales pipeline, from initial prospecting through closed-won or closed-lost outcomes. This table supports sales performance reporting, pipeline management, forecasting, and conversion analysis.

## Grain

One row per sales opportunity.

## Primary Key

sales_opportunity_key

## Source

sales_opportunities.csv

### Field Definitions

| Field | Data Type | Business Definition | Example | Required |
|---|---|---|---|---|
| sales_opportunity_key | Integer | Warehouse surrogate key for the sales opportunity | 15001 | Yes |
| opportunity_id | Varchar | Source-system opportunity identifier | OPP-15001 | Yes |
| customer_key | Integer | Foreign key linking the opportunity to dim_customer | 1025 | Yes |
| sales_rep_key | Integer | Foreign key linking the opportunity to dim_sales_rep | 18 | Yes |
| sales_stage_key | Integer | Foreign key linking the opportunity to dim_sales_stage | 4 | Yes |
| marketing_campaign_key | Integer | Foreign key linking the opportunity to dim_marketing_campaign | 12 | No |
| created_date_key | Integer | Foreign key linking the opportunity creation date to dim_date | 20250210 | Yes |
| expected_close_date_key | Integer | Foreign key linking the expected close date to dim_date | 20250430 | Yes |
| actual_close_date_key | Integer | Foreign key linking the actual close date to dim_date | 20250502 | No |
| opportunity_value | Decimal(12,2) | Estimated contract value of the opportunity | 85000.00 | Yes |
| opportunity_status | Varchar | Current status of the opportunity | Open | Yes |
| lead_source | Varchar | Original source that generated the opportunity | Webinar | No |
| loss_reason | Varchar | Reason the opportunity was lost | Budget Constraints | No |
| days_in_sales_cycle | Integer | Number of days from creation to close | 81 | No |
| open_opportunity_flag | Boolean | Indicates whether the opportunity is currently open | True | Yes |
| won_opportunity_flag | Boolean | Indicates whether the opportunity closed successfully | False | Yes |
| lost_opportunity_flag | Boolean | Indicates whether the opportunity was lost | False | Yes |

### Accepted Opportunity Status Values

- Open
- Closed Won
- Closed Lost

### Accepted Sales Stages

- Prospecting
- Qualification
- Discovery
- Proposal
- Negotiation
- Closed Won
- Closed Lost

### Accepted Lead Sources

- Website
- Referral
- Webinar
- Paid Search
- Paid Social
- Email Campaign
- Industry Event
- Partner
- Outbound Sales

### Validation Rules

- `opportunity_id` must be unique.
- `customer_key` must exist in `dim_customer`.
- `sales_rep_key` must exist in `dim_sales_rep`.
- `sales_stage_key` must exist in `dim_sales_stage`.
- `created_date_key` must exist in `dim_date`.
- `expected_close_date_key` must be greater than or equal to `created_date_key`.
- `actual_close_date_key` may only be populated when the opportunity is closed.
- `opportunity_value` must be greater than zero.
- `won_opportunity_flag` must be `True` for Closed Won opportunities.
- `lost_opportunity_flag` must be `True` for Closed Lost opportunities.
- Open opportunities cannot have an `actual_close_date_key`.

---

# dim_customer

## Business Purpose

Stores descriptive information about each B2B customer account. This dimension serves as the central conformed dimension across the Executive KPI Command Center, enabling consistent reporting across sales, finance, customer success, product usage, and support.

## Grain

One row per customer account.

## Primary Key

customer_key

## Source

customers.csv

### Field Definitions

| Field | Data Type | Business Definition | Example | Required |
|---|---|---|---|---|
| customer_key | Integer | Warehouse surrogate key for the customer | 1025 | Yes |
| account_id | Varchar | Unique source-system customer identifier | ACC-10025 | Yes |
| account_name | Varchar | Official customer company name | Acme Manufacturing | Yes |
| industry | Varchar | Customer's primary industry | Manufacturing | Yes |
| region | Varchar | Geographic sales region | Northeast | Yes |
| country | Varchar | Customer's country | United States | Yes |
| customer_segment | Varchar | Customer size classification | Enterprise | Yes |
| employee_band | Varchar | Employee size category | 500–1000 | No |
| annual_revenue_band | Varchar | Estimated annual company revenue range | $50M–$100M | No |
| account_start_date | Date | Date the customer relationship began | 2023-04-01 | Yes |
| customer_status | Varchar | Current customer lifecycle status | Active | Yes |
| sales_rep_id | Varchar | Assigned sales representative | SR-021 | Yes |
| customer_success_manager_id | Varchar | Assigned customer success manager | CSM-008 | Yes |
| effective_start_date | Date | Start date of the current dimension record | 2025-01-01 | Yes |
| effective_end_date | Date | End date of the current dimension record | 9999-12-31 | Yes |
| current_record_flag | Boolean | Indicates the active version of the customer record | True | Yes |

### Accepted Customer Status Values

- Active
- Prospect
- Inactive
- Churned

### Accepted Customer Segments

- Startup
- SMB
- Mid-Market
- Enterprise

### Validation Rules

- `customer_key` must be unique.
- `account_id` must be unique.
- `account_name` cannot be null.
- `customer_status` must contain an approved value.
- `customer_segment` must contain an approved value.
- `account_start_date` cannot be a future date.
- `effective_start_date` must be less than or equal to `effective_end_date`.
- Only one record per `account_id` may have `current_record_flag` = `True`.
- `sales_rep_id` should reference a valid sales representative.
- `customer_success_manager_id` should reference a valid customer success manager.

---

# dim_date

## Business Purpose

Provides a standardized calendar dimension used for time-based reporting across all business processes. This dimension enables consistent daily, monthly, quarterly, yearly, and fiscal reporting throughout the Executive KPI Command Center.

## Grain

One row per calendar date.

## Primary Key

date_key

## Source

Generated using Python during the data generation process.

### Field Definitions

| Field | Data Type | Business Definition | Example | Required |
|---|---|---|---|---|
| date_key | Integer | Warehouse surrogate key in YYYYMMDD format | 20250729 | Yes |
| full_date | Date | Full calendar date | 2025-07-29 | Yes |
| day_number | Integer | Day of the month | 29 | Yes |
| day_name | Varchar | Name of the weekday | Tuesday | Yes |
| day_of_week | Integer | Numeric day of week (1–7) | 2 | Yes |
| week_number | Integer | Week number within the year | 31 | Yes |
| month_number | Integer | Calendar month number | 7 | Yes |
| month_name | Varchar | Full month name | July | Yes |
| month_short_name | Varchar | Three-letter month abbreviation | Jul | Yes |
| year_month | Varchar | Year and month combination | 2025-07 | Yes |
| quarter_number | Integer | Calendar quarter number | 3 | Yes |
| quarter_name | Varchar | Quarter label | Q3 | Yes |
| calendar_year | Integer | Calendar year | 2025 | Yes |
| fiscal_month | Integer | Fiscal month number | 7 | Yes |
| fiscal_quarter | Varchar | Fiscal quarter label | Q3 | Yes |
| fiscal_year | Integer | Fiscal reporting year | 2025 | Yes |
| month_start_date | Date | First day of the month | 2025-07-01 | Yes |
| month_end_date | Date | Last day of the month | 2025-07-31 | Yes |
| quarter_start_date | Date | First day of the quarter | 2025-07-01 | Yes |
| quarter_end_date | Date | Last day of the quarter | 2025-09-30 | Yes |
| year_start_date | Date | First day of the calendar year | 2025-01-01 | Yes |
| year_end_date | Date | Last day of the calendar year | 2025-12-31 | Yes |
| weekend_flag | Boolean | Indicates whether the date falls on a weekend | False | Yes |

### Validation Rules

- `date_key` must be unique.
- `full_date` must be unique.
- `date_key` must follow the YYYYMMDD format.
- `month_number` must be between 1 and 12.
- `quarter_number` must be between 1 and 4.
- `day_of_week` must be between 1 and 7.
- `month_start_date` must be the first day of the month.
- `month_end_date` must be the last day of the month.
- `quarter_start_date` must be the first day of the quarter.
- `quarter_end_date` must be the last day of the quarter.
- `year_start_date` must equal January 1.
- `year_end_date` must equal December 31.
- `weekend_flag` must be `True` only for Saturday and Sunday.

### Design Notes

The `dim_date` table is a **conformed dimension** shared across all fact tables in the warehouse.

Although each fact table may contain multiple business dates (such as created date, close date, renewal date, or resolution date), they all reference the same `dim_date` table through **role-playing relationships** in Power BI.

Using a shared calendar dimension ensures that all reports use consistent definitions for weeks, months, quarters, and fiscal periods.

---

# dim_plan

## Business Purpose

Stores standardized information about Northstar Analytics subscription plans, pricing tiers, billing structures, and customer eligibility. This dimension supports revenue analysis, plan-level performance reporting, and subscription segmentation.

## Grain

One row per subscription plan.

## Primary Key

plan_key

## Natural Key

plan_id

## Source

Derived from `subscriptions.csv` or generated as a separate reference dataset named `subscription_plans.csv`.

### Field Definitions

| Field | Data Type | Business Definition | Example | Required |
|---|---|---|---|---|
| plan_key | Integer | Warehouse surrogate key for the subscription plan | 3 | Yes |
| plan_id | Varchar | Unique source-system identifier for the plan | PLAN-003 | Yes |
| plan_name | Varchar | Business-facing name of the subscription plan | Professional | Yes |
| plan_tier | Varchar | Standardized plan level used for reporting | Professional | Yes |
| billing_frequency | Varchar | Frequency at which customers are billed | Monthly | Yes |
| standard_monthly_price | Decimal(12,2) | Standard monthly list price for the plan | 1499.00 | Yes |
| included_users | Integer | Number of users included in the standard plan | 50 | Yes |
| target_customer_segment | Varchar | Primary customer segment targeted by the plan | Mid-Market | Yes |
| active_plan_flag | Boolean | Indicates whether the plan is currently available for sale | True | Yes |

### Accepted Plan Tiers

- Starter
- Growth
- Professional
- Enterprise

### Accepted Billing Frequencies

- Monthly
- Quarterly
- Annual

### Accepted Customer Segments

- Startup
- SMB
- Mid-Market
- Enterprise

### Validation Rules

- `plan_key` must be unique.
- `plan_id` must be unique.
- `plan_name` cannot be null.
- `plan_tier` must contain an approved value.
- `billing_frequency` must contain an approved value.
- `standard_monthly_price` must be greater than zero.
- `included_users` must be greater than zero.
- `target_customer_segment` must contain an approved value.
- `active_plan_flag` must contain either `True` or `False`.
- Inactive plans may remain in the dimension to support historical reporting.

### Design Notes

The `dim_plan` table standardizes plan names and pricing attributes across subscription and revenue reporting.

The same plan dimension will be reused by:

- `fact_subscription`
- `fact_revenue_transaction`

Keeping plan information in a dimension prevents repeated descriptive values across fact tables and ensures consistent plan-level reporting.

---

# dim_sales_rep

## Business Purpose

Stores standardized information about Northstar Analytics sales representatives, teams, territories, managers, and annual quotas. This dimension supports sales performance analysis, pipeline reporting, and quota attainment calculations.

## Grain

One row per sales representative.

## Primary Key

sales_rep_key

## Natural Key

sales_rep_id

## Source

Generated as a reference dataset named `sales_representatives.csv`.

### Field Definitions

| Field | Data Type | Business Definition | Example | Required |
|---|---|---|---|---|
| sales_rep_key | Integer | Warehouse surrogate key for the sales representative | 18 | Yes |
| sales_rep_id | Varchar | Unique source-system identifier for the sales representative | SR-018 | Yes |
| sales_rep_name | Varchar | Full name of the sales representative | Jordan Lee | Yes |
| sales_team | Varchar | Sales team assigned to the representative | Enterprise Sales | Yes |
| sales_region | Varchar | Geographic region assigned to the representative | Northeast | Yes |
| manager_name | Varchar | Name of the representative's sales manager | Morgan Davis | Yes |
| hire_date | Date | Date the representative joined the company | 2022-06-13 | Yes |
| annual_quota | Decimal(12,2) | Annual closed-won revenue target assigned to the representative | 1500000.00 | Yes |
| active_rep_flag | Boolean | Indicates whether the representative is currently active | True | Yes |

### Accepted Sales Teams

- SMB Sales
- Mid-Market Sales
- Enterprise Sales
- Strategic Accounts

### Accepted Sales Regions

- Northeast
- Southeast
- Midwest
- West
- International

### Validation Rules

- `sales_rep_key` must be unique.
- `sales_rep_id` must be unique.
- `sales_rep_name` cannot be null.
- `sales_team` must contain an approved value.
- `sales_region` must contain an approved value.
- `hire_date` cannot be a future date.
- `annual_quota` must be greater than or equal to zero.
- `active_rep_flag` must contain either `True` or `False`.
- Inactive representatives may remain in the dimension to support historical reporting.
- Every `sales_rep_key` used in `fact_sales_opportunity` must exist in `dim_sales_rep`.

### Design Notes

The `dim_sales_rep` table separates descriptive sales-representative information from opportunity-level activity.

This dimension supports reporting by:

- Sales representative
- Sales team
- Region
- Manager
- Quota attainment
- Closed-won revenue
- Pipeline coverage

Keeping quota values in the sales representative dimension allows the warehouse to compare closed-won revenue against assigned annual targets.

---

# dim_sales_stage

## Business Purpose

Stores standardized sales pipeline stages used throughout the Northstar Analytics sales process. This dimension ensures consistent reporting on pipeline progression, conversion rates, sales velocity, and win/loss analysis.

## Grain

One row per sales stage.

## Primary Key

sales_stage_key

## Natural Key

sales_stage_id

## Source

Generated as a reference dataset named `sales_stages.csv`.

### Field Definitions

| Field | Data Type | Business Definition | Example | Required |
|---|---|---|---|---|
| sales_stage_key | Integer | Warehouse surrogate key for the sales stage | 4 | Yes |
| sales_stage_id | Varchar | Unique source-system identifier for the sales stage | STG-004 | Yes |
| sales_stage_name | Varchar | Standardized sales pipeline stage | Proposal | Yes |
| stage_order | Integer | Sequential order of the sales stage | 4 | Yes |
| stage_category | Varchar | High-level sales pipeline category | Active Pipeline | Yes |
| probability_to_close | Decimal(5,2) | Estimated probability of closing at this stage (%) | 65.00 | Yes |
| active_stage_flag | Boolean | Indicates whether the stage is currently used in the sales process | True | Yes |

### Accepted Sales Stages

- Prospecting
- Qualification
- Discovery
- Proposal
- Negotiation
- Closed Won
- Closed Lost

### Accepted Stage Categories

- Early Pipeline
- Active Pipeline
- Closed

### Validation Rules

- `sales_stage_key` must be unique.
- `sales_stage_id` must be unique.
- `sales_stage_name` must contain an approved value.
- `stage_order` must be unique.
- `stage_order` must be greater than zero.
- `probability_to_close` must be between 0 and 100.
- Closed Won must have a `probability_to_close` of 100.
- Closed Lost must have a `probability_to_close` of 0.
- `active_stage_flag` must contain either `True` or `False`.
- Every `sales_stage_key` referenced in `fact_sales_opportunity` must exist in `dim_sales_stage`.

### Design Notes

The `dim_sales_stage` table standardizes the organization's sales pipeline and provides a consistent framework for opportunity reporting.

This dimension supports analysis of:

- Pipeline value by stage
- Sales funnel conversion rates
- Average days spent in each stage
- Win and loss trends
- Sales forecasting
- Pipeline velocity

Using a dedicated dimension ensures that stage names, ordering, and close probabilities remain consistent across dashboards and analytical reports.

---

# dim_marketing_campaign

## Business Purpose

Stores descriptive information about marketing campaigns used to generate leads and opportunities. This dimension enables consistent reporting on campaign performance, lead generation, customer acquisition, and return on marketing investment (ROMI).

## Grain

One row per marketing campaign.

## Primary Key

marketing_campaign_key

## Natural Key

campaign_id

## Source

Generated as a reference dataset named `marketing_campaigns.csv`.

### Field Definitions

| Field | Data Type | Business Definition | Example | Required |
|---|---|---|---|---|
| marketing_campaign_key | Integer | Warehouse surrogate key for the marketing campaign | 15 | Yes |
| campaign_id | Varchar | Unique source-system campaign identifier | CMP-015 | Yes |
| campaign_name | Varchar | Marketing campaign name | Q3 AI Summit | Yes |
| campaign_type | Varchar | Marketing channel or campaign type | Webinar | Yes |
| campaign_start_date | Date | Campaign launch date | 2025-07-01 | Yes |
| campaign_end_date | Date | Campaign end date | 2025-07-31 | Yes |
| campaign_budget | Decimal(12,2) | Planned campaign budget | 50000.00 | Yes |
| target_audience | Varchar | Primary audience targeted by the campaign | Enterprise | Yes |
| campaign_status | Varchar | Current campaign status | Completed | Yes |

### Accepted Campaign Types

- Webinar
- Email
- Paid Search
- Paid Social
- Referral
- Conference
- Content Marketing

### Accepted Campaign Status

- Planned
- Active
- Completed
- Cancelled

### Validation Rules

- `marketing_campaign_key` must be unique.
- `campaign_id` must be unique.
- `campaign_name` cannot be null.
- `campaign_budget` must be greater than or equal to zero.
- `campaign_start_date` must be before or equal to `campaign_end_date`.
- `campaign_status` must contain an approved value.
- `campaign_type` must contain an approved value.

### Design Notes

The `dim_marketing_campaign` table supports campaign attribution and marketing performance reporting. It enables analysis of lead generation, opportunity creation, revenue attribution, campaign ROI, and customer acquisition trends across marketing channels.

---

# dim_customer_success_manager

## Business Purpose

Stores descriptive information about Customer Success Managers (CSMs) responsible for onboarding customers, improving adoption, reducing churn, and maintaining customer health.

## Grain

One row per Customer Success Manager.

## Primary Key

customer_success_manager_key

## Natural Key

customer_success_manager_id

## Source

Generated as a reference dataset named `customer_success_managers.csv`.

### Field Definitions

| Field | Data Type | Business Definition | Example | Required |
|---|---|---|---|---|
| customer_success_manager_key | Integer | Warehouse surrogate key | 8 | Yes |
| customer_success_manager_id | Varchar | Unique CSM identifier | CSM-008 | Yes |
| customer_success_manager_name | Varchar | Full name of the Customer Success Manager | Taylor Morgan | Yes |
| team | Varchar | Customer Success team assignment | Enterprise Success | Yes |
| region | Varchar | Geographic territory | Northeast | Yes |
| hire_date | Date | Date hired | 2023-02-15 | Yes |
| active_manager_flag | Boolean | Indicates whether the manager is currently active | True | Yes |

### Accepted Teams

- SMB Success
- Mid-Market Success
- Enterprise Success

### Accepted Regions

- Northeast
- Southeast
- Midwest
- West
- International

### Validation Rules

- `customer_success_manager_key` must be unique.
- `customer_success_manager_id` must be unique.
- `customer_success_manager_name` cannot be null.
- `hire_date` cannot be a future date.
- `active_manager_flag` must contain either `True` or `False`.
- Every manager assigned to a customer must exist in this dimension.

### Design Notes

The `dim_customer_success_manager` table enables reporting by Customer Success Manager, region, and team. It supports customer health analysis, renewal performance, product adoption metrics, customer retention, and churn reporting.

---

# dim_product_feature

## Business Purpose

Stores descriptive information about individual software features available within the Northstar Analytics platform. This dimension supports feature adoption analysis, product engagement reporting, and customer usage analytics.

## Grain

One row per product feature.

## Primary Key

product_feature_key

## Natural Key

product_feature_id

## Source

Generated as a reference dataset named `product_features.csv`.

### Field Definitions

| Field | Data Type | Business Definition | Example | Required |
|---|---|---|---|---|
| product_feature_key | Integer | Warehouse surrogate key | 21 | Yes |
| product_feature_id | Varchar | Unique feature identifier | FEAT-021 | Yes |
| feature_name | Varchar | Name of the software feature | Executive Dashboard | Yes |
| feature_category | Varchar | Functional product area | Analytics | Yes |
| release_version | Varchar | Product version where the feature became available | v4.2 | Yes |
| release_date | Date | Feature release date | 2025-05-15 | Yes |
| active_feature_flag | Boolean | Indicates whether the feature is currently active | True | Yes |

### Accepted Feature Categories

- Analytics
- Reporting
- AI
- Administration
- Integrations
- Security
- Collaboration

### Validation Rules

- `product_feature_key` must be unique.
- `product_feature_id` must be unique.
- `feature_name` cannot be null.
- `release_date` cannot be a future date.
- `active_feature_flag` must contain either `True` or `False`.
- `feature_category` must contain an approved value.
- Every feature referenced in `fact_product_usage` must exist in this dimension.

### Design Notes

The `dim_product_feature` table enables product analytics by standardizing software feature definitions across the platform. It supports reporting on feature adoption, user engagement, product usage trends, customer adoption rates, and feature popularity.
