
# 📊 Executive KPI Command Center

**An end-to-end analytics engineering build that turns fragmented B2B SaaS data into a governed, executive-ready KPI system.**

[![Status](https://img.shields.io/badge/status-in%20progress-yellow)]()
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)]()
[![SQL](https://img.shields.io/badge/warehouse-DuckDB%2FSQL-orange)]()
[![BI](https://img.shields.io/badge/dashboard-Power%20BI%20%2F%20Tableau-purple)]()

---

## 📌 Project Snapshot

| Field | Detail |
|---|---|
| **Project type** | Portfolio capstone — analytics engineering, SQL, Python, data modeling, KPI design, executive reporting |
| **Business scenario** | Northstar Analytics (fictional B2B SaaS company) needs one trusted view of revenue, customers, sales, product usage, and customer success (including support) |
| **Core tools** | GitHub · VS Code · Python (pandas, NumPy) · DuckDB/SQL · Draw.io · Power BI / Tableau |
| **Current status** | Phases 1–2 complete · Phase 3 data generated (11 datasets, incl. 106,112 revenue transactions) with 3 realism fixes open · monthly revenue, subscription, and customer-success summaries built and reconciled |
| **Portfolio goal** | Demonstrate the full path from business requirements → architecture → modeled data → KPI logic → dashboards → validation → executive insight |

---

## 🧩 What This Project Demonstrates

| Capability | What I Built |
|---|---|
| Business Analysis | Translated executive questions into measurable KPIs |
| Data Architecture | Designed a multi-source analytics architecture across 4 operational domains (CRM, billing, product, customer success) |
| Data Modeling | Built a dimensional model spanning 7 business processes |
| Python | Generated reproducible, seeded synthetic business data |
| SQL / DuckDB | *Planned* — warehouse transformations and KPI logic |
| Data Quality | Implemented validation and business-rule checks on generated data, plus a cross-layer reconciliation that caught and fixed a billing logic error |
| BI | *Planned* — executive decision-support dashboard |
| Communication | Documenting architecture, findings, and business recommendations as the build progresses |

---

## 🎯 The Business Problem

Northstar Analytics has customer, subscription, sales, product, and customer-success data spread across separate operational systems. Leadership can't answer basic questions from a single trusted source:

- How much recurring revenue do we have, and how is it trending?
- Which customers are at risk of churn?
- Which sales opportunities are likely to close?
- Is product usage strong enough to support renewal?

This project builds a small analytics platform that unifies those domains into one governed source of truth — preserving data lineage and validation logic behind every KPI, rather than relying on scattered dashboard-level calculations.

---

## 🏆 Business Outcome

The completed command center will give Northstar leadership a single analytical view across the full customer lifecycle — from sales pipeline through subscription revenue, product engagement, support load, renewal risk, and churn.

Instead of reviewing disconnected operational reports, leadership will be able to identify where revenue is growing, which customers require intervention, where pipeline is stalling, and which business activities are contributing to recurring revenue.

*This section will be updated with specific, data-backed findings once Phases 6–8 (KPI layer, dashboard, and analysis) are complete.*

---

## 🎥 Project Walkthrough

*Coming soon: a 5–7 minute Loom walkthrough covering the business problem, architecture, data model, KPI logic, dashboard, and the decisions an executive could make from the analysis.*

---

## 🖥️ Dashboard Preview

*Coming soon — screenshots of the executive overview and supporting analytical views will be added here once Phase 7 is complete.*

---
---

## 🏗️ Architecture — How the Project Fits Together

The system follows a standard analytics engineering pipeline: business questions drive the source data model, which is transformed through staging and validation into a dimensional warehouse, exposed through a governed KPI layer, and surfaced to leadership through an executive dashboard.

<img width="3380" height="1679" alt="architecture_flow" src="https://github.com/user-attachments/assets/04e8ba26-f909-4d78-b0c8-a17d9a355e78" />


```
Business Questions → Source Systems → Raw Data → Python → SQL/DuckDB →
Dimensional Model → KPI Layer → Dashboard → Insights
```

### Source Systems Feeding the Model

| Source Domain | Example Operational System | Contributes |
|---|---|---|
| CRM | Salesforce-style CRM | Accounts, opportunities, stages, sales ownership |
| Billing / Subscriptions | Stripe-style billing platform | Plans, subscriptions, recurring revenue, transactions |
| Product Analytics | Application event tracking | Feature usage and engagement |
| Customer Success | CS platform | CSM ownership, health, satisfaction, renewal risk, monthly support-ticket volume |

---

## ⭐ Dimensional Model — Star Schema

The model uses shared dimensions surrounding multiple business-process fact tables. `dim_customer` is the central business entity; `dim_date` supports time-based analysis across every fact.

<img width="4739" height="863" alt="star_schema" src="https://github.com/user-attachments/assets/87fc0580-9f3f-4ca1-8f67-9ddfae90486f" />


> **Scope note (v1):** marketing is out of scope for this version, and support is tracked as monthly ticket volume within customer success rather than as a separate ticket-level fact. The diagram above still shows `fact_marketing_campaign` and `dim_marketing_campaign`; they will be removed in the next diagram update.

### Key Concepts

| Concept | Definition |
|---|---|
| **Fact table** | Represents a measurable business process at a defined grain (e.g., subscriptions, revenue transactions, product usage, sales opportunities, customer success activity) |
| **Dimension table** | Descriptive context used to filter and group facts (e.g., customer, date, plan, sales rep, sales stage, CSM, product feature) |
| **Grain** | What one row in a fact table represents — must be defined before building keys, measures, or validation rules |
| **Star schema** | Fact tables surrounded by reusable, shared dimensions — simplifies analytical SQL and BI relationships |
| **Raw vs. Processed layers** | Raw preserves source-like data; processed holds cleaned/transformed outputs — separating them keeps the pipeline auditable and reproducible |
| **Synthetic data** | A seeded Python generator produces realistic, reproducible data without exposing confidential employer information |

---

## 🔄 Data Pipeline

```bash
# 1. Clone the repository
git clone https://github.com/shirleylandondata/Executive-KPI-Command-Center.git
cd Executive-KPI-Command-Center

# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate the synthetic raw datasets (seeded — fully reproducible)
python python/generate_data.py

# 4. Build the processed monthly summaries
python python/process_data.py

# 5. Inspect output
ls data/raw/ data/processed/
```

Raw CSVs are **not committed** (the largest is ~43 MB). They are regenerated from the seeded script. The small processed summaries in `data/processed/` are committed so results can be reviewed without running anything.

`requirements.txt` tracks: `pandas`, `numpy`, `duckdb`. The generator uses `SEED = 42` so anyone who clones the repo can reproduce identical datasets.

---

## 🧪 Data Quality & Validation

| Validation Category | Example Check |
|---|---|
| Uniqueness | No duplicate `opportunity_id`, `account_id`, `subscription_id`, `usage_id`, `cs_activity_id`, or `transaction_id` where the grain requires uniqueness |
| Referential integrity | Every `customer_key`, `plan_key`, `sales_stage_key`, `sales_rep_key`, `product_feature_key`, `customer_success_manager_key`, and date key resolves to a valid dimension row |
| Date logic | End/close/renewal dates never precede creation/start dates |
| Status logic | Won/lost/open flags agree with sales stage and actual close date |
| Financial logic | Revenue and recurring-price fields are non-negative and consistent with subscription state |
| Completeness | Required IDs and business-critical fields are not null |
| Reasonableness | Distributions, totals, and row counts are checked for implausible values |

**Validation checkpoints completed so far:**

`customers.csv` (5,000 rows)

| Check | Result |
|---|---|
| Segment mix | SMB 1,776 · Mid-Market 1,453 · Startup 1,002 · Enterprise 769 |
| Status mix | Active 3,485 · Churned 743 · Prospect 504 · Inactive 268 |
| Duplicate account IDs | 0 |
| Missing account IDs | 0 |

`subscriptions.csv`

| Check | Result |
|---|---|
| Every subscription resolves to a valid `account_id` and `plan_id` | ✅ Passed |
| Subscription status agrees with lifecycle/renewal fields | ✅ Passed |

`revenue_transactions.csv` (106,112 rows)

| Check | Result |
|---|---|
| Every transaction resolves to a valid customer/subscription | ✅ Passed |
| Revenue amounts are non-negative | ✅ Passed |
| Transaction dates fall within valid subscription date ranges | ✅ Passed (0 before start, 0 after cancellation) |
| No duplicate transaction IDs | ✅ Passed |

**Cross-layer reconciliation** (`revenue_monthly.csv` vs. `subscription_monthly.csv`)

| Check | Result |
|---|---|
| Subscriptions billed each month = active subscriptions that month | ✅ Passed — 0 difference in all 31 months (Jan 2024 – Jul 2026) |
| Billed revenue vs. MRR | ✅ Explained — billed runs ~1.5% above MRR because upgrades bill at +25% and add-ons at +10% of the base plan price |

**Generated datasets**

| Dataset | Rows | Type |
|---|---|---|
| `customers.csv` | 5,000 | Core |
| `subscriptions.csv` | 4,496 | Core |
| `revenue_transactions.csv` | 106,112 | Core |
| `product_usage.csv` | 567,831 | Core |
| `opportunities.csv` | 5,000 | Core |
| `customer_success_activity.csv` | 120,750 | Core |
| `subscription_plans.csv`, `sales_representatives.csv`, `sales_stages.csv`, `customer_success_managers.csv`, `product_features.csv` | 4–8 each | Reference |

**Open data-realism issues** (Phase 3 is not marked complete until these are fixed)

| Issue | Why it matters |
|---|---|
| No new subscriptions start after Jan 20, 2026 | The last six months would show zero new business |
| 105 subscriptions have cancellation dates after the reporting period ends (some in 2028) | Future-dated events should not exist in historical data |
| Customer-success activity counts all 4,496 subscriptions in Jul 2026, while only 3,822 are active | Health and risk metrics would include customers who have already left |

---

## 📈 KPI Definitions

| KPI Group | Candidate Metrics |
|---|---|
| **Revenue** | MRR · ARR · revenue growth · recurring revenue by segment · expansion/contraction |
| **Customers** | Active / new / churned customers · customer mix · churn rate |
| **Sales** | Open pipeline · weighted pipeline · win rate · avg. deal size · pipeline by stage · sales cycle |
| **Product** | Active users/accounts · feature adoption · usage frequency · engagement by segment |
| **Customer Success** | Health/risk distribution · satisfaction · support-ticket volume · upcoming renewals · at-risk revenue · CSM portfolio |

> **Design rule:** every KPI will have a business definition, SQL logic, grain, date context, and a clear owner. No metric will be built in the dashboard that doesn't already exist in the documented KPI layer. *(Status: KPI layer not yet built — Phase 6, Planned.)*

---

## 💡 Executive Findings & Recommended Actions

*Not yet available — this section will be populated once Phase 8 (Analysis & Insights) is complete. It will follow this format:*

> Example (illustrative only — not real findings yet):
>
> - Enterprise accounts represent X% of ARR but Y% of at-risk recurring revenue.
> - Product adoption falls materially in the 90 days preceding churn.
> - Customers with high support-ticket volume show a higher concentration of renewal risk.
> - **Recommendation:** prioritize CSM outreach to accounts meeting all three risk conditions.

---

## 🛠️ Technical Implementation

| Skill | Evidence |
|---|---|
| Business requirements | Translated executive questions into KPIs, dimensions, facts, and dashboard requirements |
| Data architecture | Defined source systems, dataset inventory, raw/processed layers, project folders |
| Dimensional modeling | Designed a star schema with shared customer/date dimensions and multiple fact tables |
| Python | Generated reproducible synthetic source data with an automated, seeded generator |
| SQL | *Planned* — transform raw data, build dimensional tables, validate joins, calculate KPIs |
| Data quality | Defined and applied uniqueness, referential-integrity, date, status, and business-rule checks |
| BI / visualization | *Planned* — executive KPI command center with drill-down analysis |
| Documentation | Field dictionary, ERD, README, and portfolio walkthrough maintained alongside the build |

---

## 📁 Repository Structure

```
executive-kpi-command-center/
├── architecture/        # ERD, system-flow diagrams
├── dashboard/           # BI files, screenshots
├── data/
│   ├── raw/             # Source-like generated CSVs (not committed — regenerate locally)
│   └── processed/       # Cleaned / modeled warehouse outputs
├── docs/                # Dataset inventory, field dictionary, KPI definitions
├── loom/                # Walkthrough recordings
├── python/
│   ├── generate_data.py # Synthetic data generator (seeded, reproducible)
│   └── process_data.py  # Monthly revenue, subscription, and CS summaries
├── sql/                 # Staging, dimensional model, KPI SQL
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ▶️ Reproduction Instructions

```bash
git clone https://github.com/shirleylandondata/Executive-KPI-Command-Center.git
cd Executive-KPI-Command-Center
pip install -r requirements.txt
python python/generate_data.py
python python/process_data.py
```

All generated data is reproducible via a fixed random seed (`SEED = 42`). Running the generator on two different machines (Windows and Linux) produced row-for-row identical datasets.

---

## 🗺️ Project Roadmap

| Phase | Purpose | Major Deliverable | Status |
|---|---|---|---|
| 1. Project Foundation | Define the business case and organize the repository | Project folders, README foundation, business questions, GitHub repo | ✅ Complete |
| 2. Data Architecture & Modeling | Design how data should be organized before coding transformations | Source systems, dataset inventory, star schema, ERD, field dictionary, validation rules | ✅ Complete |
| 3. Synthetic Data Generation | Create realistic raw source datasets in Python | `generate_data.py` + raw CSV files | 🟡 In Progress — all 11 datasets generated and validated; 3 realism fixes open (see Data Quality) |
| 4. Warehouse Build | Load, clean, standardize, and model data with SQL/DuckDB | Dimension and fact tables in processed/warehouse layer | 🟡 Started — monthly revenue, subscription, and CS summaries built in pandas (`process_data.py`); DuckDB star schema planned |
| 5. Data Quality & Validation | Prove the model is reliable | Automated checks and validation queries | ⬜ Planned |
| 6. KPI / Semantic Layer | Create reusable business metrics | Executive KPI SQL views or tables | ⬜ Planned |
| 7. Executive Dashboard | Turn modeled data into decision-ready reporting | Command-center dashboard with executive and functional views | ⬜ Planned |
| 8. Analysis & Insights | Explain what the metrics mean and identify actions | Written findings and recommendations | ⬜ Planned |
| 9. Portfolio Packaging | Make the work easy for recruiters and hiring managers to review | README, screenshots, architecture image, Loom walkthrough, LinkedIn case study | ⬜ Planned |

### Master Completion Checklist

- [x] Repository and folder structure created
- [x] Business problem and executive questions defined
- [x] Source systems documented
- [x] `dataset_inventory.md` created
- [x] Star schema designed
- [x] Field dictionary and validation rules documented
- [ ] ERD relationship lines finished and exported (marketing tables removed for v1 scope)
- [x] Python environment and `requirements.txt` prepared
- [x] Reference CSVs generated
- [x] `customers.csv` generated and validated
- [x] `subscriptions.csv` generated and validated
- [x] `revenue_transactions.csv` generated and validated (106,112 rows)
- [x] `product_usage`, `opportunities`, and `customer_success_activity` generated
- [x] Monthly processed summaries built and reconciled (revenue vs. subscriptions, 0 difference in 31 months)
- [ ] Data-realism fixes: new subscriptions through Jul 2026, no future cancellation dates, CS activity limited to active customers
- [ ] DuckDB staging and warehouse model built
- [ ] Automated data-quality checks completed
- [ ] KPI layer completed and documented
- [ ] Executive dashboard completed and validated
- [ ] Executive findings written
- [ ] README, screenshots, Loom, and final portfolio packaging completed

---

## 📚 Lessons Learned

**1. Row-level checks passed, but the numbers were still wrong.**
Every revenue transaction passed its individual checks: valid IDs, non-negative amounts, dates in range. Comparing the monthly revenue summary against the monthly subscription summary told a different story. Revenue billed a flat ~4,160 subscriptions every month for 31 months while active subscriptions grew from 2,677 to 3,822. The generator was billing subscriptions that had not started yet and dropping upgrade and add-on pricing. *Takeaway: validate across layers, not just within a table.*

**2. Two definitions of "active" created a smaller, hidden gap.**
After the first fix, billed subscriptions still ran 33–73 below active subscriptions each month. The gap exactly matched the number of subscriptions that started mid-month: the subscription summary counted them active in their start month, while billing waited for the next 1st. I chose to bill in the start month (first invoice dated on the start date, never before it), and the two layers now reconcile to zero in every month. *Takeaway: write the business rule down before building the metric, because "active" can mean more than one thing.*

**3. Scope cut to finish.**
Marketing was removed from v1, and support is tracked inside customer success, so the project reaches a working dashboard sooner. Both are documented as scope decisions rather than left as silent gaps.

---

## 🎤 Interview / Portfolio Summary

> *I built an end-to-end executive KPI command center for a fictional B2B SaaS company. I started by defining the business questions and source systems, designed a dimensional model and data dictionary, generated reproducible source data in Python, and am now transforming and validating it in SQL/DuckDB before building an executive reporting layer across revenue, customers, sales, product, and customer success.*

This project is presented as an **executive decision-support system**, not simply a dashboard — the technical story spans architecture design, multi-domain data modeling, reproducible data generation, validated analytics, governed KPI definitions, and executive-level insight delivery.

---

## 📎 License

This project uses synthetic, fictional data for portfolio and educational purposes only. No real company or customer data is included.
