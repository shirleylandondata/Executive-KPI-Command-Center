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
| **Business scenario** | Northstar Analytics (fictional B2B SaaS company) needs one trusted view of revenue, customers, sales, product usage, marketing, support, and customer success |
| **Core tools** | GitHub · VS Code · Python (pandas, NumPy) · DuckDB/SQL · Draw.io · Power BI / Tableau |
| **Current status** | Phase 1 & 2 complete · Phase 3 in progress — reference, customer, subscription, and revenue-transaction datasets generated and validated (128,977 revenue transaction records) |
| **Portfolio goal** | Demonstrate the full path from business requirements → architecture → modeled data → KPI logic → dashboards → validation → executive insight |

---

## 🧩 What This Project Demonstrates

| Capability | What I Built |
|---|---|
| Business Analysis | Translated executive questions into measurable KPIs |
| Data Architecture | Designed a multi-source analytics architecture across 6 operational domains |
| Data Modeling | Built a dimensional model spanning 7 business processes |
| Python | Generated reproducible, seeded synthetic business data |
| SQL / DuckDB | *Planned* — warehouse transformations and KPI logic |
| Data Quality | Implemented validation and business-rule checks on generated data |
| BI | *Planned* — executive decision-support dashboard |
| Communication | Documenting architecture, findings, and business recommendations as the build progresses |

---

## 🎯 The Business Problem

Northstar Analytics has customer, subscription, sales, product, marketing, support, and customer-success data spread across separate operational systems. Leadership can't answer basic questions from a single trusted source:

- How much recurring revenue do we have, and how is it trending?
- Which customers are at risk of churn?
- Which sales opportunities are likely to close?
- Which marketing campaigns actually generate pipeline?
- Is product usage strong enough to support renewal?

This project builds a small analytics platform that unifies those domains into one governed source of truth — preserving data lineage and validation logic behind every KPI, rather than relying on scattered dashboard-level calculations.

---

## 🏆 Business Outcome

The completed command center will give Northstar leadership a single analytical view across the full customer lifecycle — from marketing acquisition and sales pipeline, through subscription revenue, product engagement, support, renewal risk, and churn.

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

![Architecture Flow](./architecture/architecture_flow.png)

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
| Marketing | Campaign / automation platform | Campaigns, spend, leads, influenced pipeline |
| Customer Success | CS platform | CSM ownership, health, renewal risk, account snapshots |
| Support | Ticketing platform | Tickets, priority, resolution time, customer issues |

---

## ⭐ Dimensional Model — Star Schema

The model uses shared dimensions surrounding multiple business-process fact tables. `dim_customer` is the central business entity; `dim_date` supports time-based analysis across every fact.

![Star Schema](./architecture/star_schema.png)

> **Note on `fact_marketing_campaign`:** the fact table currently shares a name with `dim_marketing_campaign`. This is being revisited against the documented grain in the field dictionary — it may be renamed to something like `fact_marketing_performance` or `fact_campaign_activity` to avoid confusion between the dimension (campaign attributes) and the fact (campaign performance measures). No change has been made yet pending that review.

### Key Concepts

| Concept | Definition |
|---|---|
| **Fact table** | Represents a measurable business process at a defined grain (e.g., subscriptions, revenue transactions, product usage, sales opportunities, marketing activity, support tickets, CS snapshots) |
| **Dimension table** | Descriptive context used to filter and group facts (e.g., customer, date, plan, sales rep, sales stage, CSM, product feature, campaign) |
| **Grain** | What one row in a fact table represents — must be defined before building keys, measures, or validation rules |
| **Star schema** | Fact tables surrounded by reusable, shared dimensions — simplifies analytical SQL and BI relationships |
| **Raw vs. Processed layers** | Raw preserves source-like data; processed holds cleaned/transformed outputs — separating them keeps the pipeline auditable and reproducible |
| **Synthetic data** | A seeded Python generator produces realistic, reproducible data without exposing confidential employer information |

---

## 🔄 Data Pipeline

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/executive-kpi-command-center.git
cd executive-kpi-command-center

# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate the synthetic raw datasets (seeded — fully reproducible)
python python/generate_data.py

# 4. Inspect output
ls data/raw/
```

`requirements.txt` tracks: `pandas`, `numpy`, `duckdb`. The generator uses `SEED = 42` so anyone who clones the repo can reproduce identical datasets.

---

## 🧪 Data Quality & Validation

| Validation Category | Example Check |
|---|---|
| Uniqueness | No duplicate `opportunity_id`, `account_id`, `subscription_id`, `ticket_id`, or transaction ID where the grain requires uniqueness |
| Referential integrity | Every `customer_key`, `plan_key`, `stage_key`, `rep_key`, `feature_key`, `campaign_key`, and `date_key` resolves to a valid dimension row |
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
| Every subscription resolves to a valid `customer_id` and `plan_id` | ✅ Passed |
| Subscription status agrees with lifecycle/renewal fields | ✅ Passed |

`revenue_transactions.csv` (128,977 rows)

| Check | Result |
|---|---|
| Every transaction resolves to a valid customer/subscription | ✅ Passed |
| Revenue amounts are non-negative | ✅ Passed |
| Transaction dates fall within valid subscription date ranges | ✅ Passed |

*Remaining raw datasets (`product_usage.csv`, `sales_opportunities.csv`, `marketing_campaigns.csv`, `support_tickets.csv`, `customer_success_snapshots.csv`) are still to be generated and validated — see [Roadmap](#️-project-roadmap).*

---

## 📈 KPI Definitions

| KPI Group | Candidate Metrics |
|---|---|
| **Revenue** | MRR · ARR · revenue growth · recurring revenue by segment · expansion/contraction |
| **Customers** | Active / new / churned customers · customer mix · churn rate |
| **Sales** | Open pipeline · weighted pipeline · win rate · avg. deal size · pipeline by stage · sales cycle |
| **Product** | Active users/accounts · feature adoption · usage frequency · engagement by segment |
| **Marketing** | Campaign spend · leads/opportunities influenced · pipeline influenced · cost efficiency |
| **Support** | Open tickets · tickets by priority · avg. resolution time · repeat-issue customers |
| **Customer Success** | Health/risk distribution · upcoming renewals · at-risk revenue · CSM portfolio |

> **Design rule:** every KPI will have a business definition, SQL logic, grain, date context, and a clear owner. No metric will be built in the dashboard that doesn't already exist in the documented KPI layer. *(Status: KPI layer not yet built — Phase 6, Planned.)*

---

## 💡 Executive Findings & Recommended Actions

*Not yet available — this section will be populated once Phase 8 (Analysis & Insights) is complete. It will follow this format:*

> Example (illustrative only — not real findings yet):
>
> - Enterprise accounts represent X% of ARR but Y% of at-risk recurring revenue.
> - Product adoption falls materially in the 90 days preceding churn.
> - Customers with high-priority support volume show a higher concentration of renewal risk.
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
│   ├── raw/             # Source-like generated CSVs
│   └── processed/       # Cleaned / modeled warehouse outputs
├── docs/                # Dataset inventory, field dictionary, KPI definitions
├── loom/                # Walkthrough recordings
├── python/
│   └── generate_data.py # Synthetic data generator (seeded, reproducible)
├── sql/                 # Staging, dimensional model, KPI SQL
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ▶️ Reproduction Instructions

```bash
git clone https://github.com/<your-username>/executive-kpi-command-center.git
cd executive-kpi-command-center
pip install -r requirements.txt
python python/generate_data.py
```

All generated data is reproducible via a fixed random seed (`SEED = 42`), so anyone who clones the repository will get identical raw datasets.

---

## 🗺️ Project Roadmap

| Phase | Purpose | Major Deliverable | Status |
|---|---|---|---|
| 1. Project Foundation | Define the business case and organize the repository | Project folders, README foundation, business questions, GitHub repo | ✅ Complete |
| 2. Data Architecture & Modeling | Design how data should be organized before coding transformations | Source systems, dataset inventory, star schema, ERD, field dictionary, validation rules | ✅ Complete |
| 3. Synthetic Data Generation | Create realistic raw source datasets in Python | `generate_data.py` + raw CSV files | 🟡 In Progress — customers, subscriptions, revenue transactions done; product usage, sales opportunities, marketing, support, and CS snapshots remaining |
| 4. Warehouse Build | Load, clean, standardize, and model data with SQL/DuckDB | Dimension and fact tables in processed/warehouse layer | ⬜ Planned |
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
- [ ] ERD relationship lines finished and exported (including `fact_marketing_campaign` naming review)
- [x] Python environment and `requirements.txt` prepared
- [x] Reference CSVs generated
- [x] `customers.csv` generated and validated
- [x] `subscriptions.csv` generated and validated
- [x] `revenue_transactions.csv` generated and validated (128,977 rows)
- [ ] Remaining raw fact/process datasets generated (`product_usage`, `sales_opportunities`, `marketing_campaigns`, `support_tickets`, `customer_success_snapshots`)
- [ ] DuckDB staging and warehouse model built
- [ ] Automated data-quality checks completed
- [ ] KPI layer completed and documented
- [ ] Executive dashboard completed and validated
- [ ] Executive findings written
- [ ] README, screenshots, Loom, and final portfolio packaging completed

---

## 📚 Lessons Learned

*This section will capture engineering and modeling decisions worth calling out to a hiring manager (e.g., grain trade-offs, validation edge cases, modeling naming conventions) as the build progresses.*

---

## 🎤 Interview / Portfolio Summary

> *I built an end-to-end executive KPI command center for a fictional B2B SaaS company. I started by defining the business questions and source systems, designed a dimensional model and data dictionary, generated reproducible source data in Python, and am now transforming and validating it in SQL/DuckDB before building an executive reporting layer across revenue, customers, sales, product, marketing, support, and customer success.*

This project is presented as an **executive decision-support system**, not simply a dashboard — the technical story spans architecture design, multi-domain data modeling, reproducible data generation, validated analytics, governed KPI definitions, and executive-level insight delivery.

---

## 📎 License

This project uses synthetic, fictional data for portfolio and educational purposes only. No real company or customer data is included.
