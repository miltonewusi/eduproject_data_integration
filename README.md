# Education Programme and Finance Data Integration

## 📌 Project Overview

A Python-based data analytics project that integrates education programme performance data with financial records to support school-level and district-level reporting.

The project addresses the challenge of analysing education programme results alongside financial expenditure when school performance data and finance records are maintained separately.

It transforms separate datasets into integrated reporting outputs to support programme monitoring, budget tracking, data quality assurance, and evidence-based decision-making.

## 🎯 Problem Statement

Education programmes generate data on school participation, children reached, mothers trained, and other programme activities. Financial teams separately maintain budget and expenditure records.

When these datasets are disconnected, programme managers may struggle to:

- Link education programme results to financial expenditure.
- Identify schools with missing or unmatched finance records.
- Detect duplicate records and budget irregularities.
- Compare programme reach and spending across districts.
- Produce consistent school-level and district-level reports.

## 💡 Project Objectives

- Integrate education programme and finance datasets.
- Clean and validate school-level records.
- Support school-level and district-level performance reporting.
- Calculate programme and financial performance indicators.
- Identify data quality issues and unmatched financial records.
- Generate structured Excel reporting outputs for programme and management use.

## 📂 Input Datasets

| Dataset | Description |
|---|---|
| `programme_data.csv` | Education programme performance and activity data. |
| `finance_data.csv` | School-level or programme financial records, including budget and expenditure fields where available. |

## ⚙️ Key Features

- **Data Integration:** Combines programme and financial datasets into an integrated dataset.
- **Data Quality Validation:** Checks for missing school records, duplicate records, negative budgets, budget overruns, and missing finance matches.
- **Programme Performance Analysis:** Summarises children reached and mothers trained.
- **Financial Analysis:** Supports budget and expenditure analysis.
- **Cost-Efficiency Analysis:** Calculates cost per child reached.
- **Budget Monitoring:** Calculates budget utilisation.
- **School-Level Reporting:** Summarises programme and financial indicators by school.
- **District-Level Reporting:** Aggregates key indicators for district comparisons.
- **Consolidated Reporting:** Generates a reporting pack for analysis and management review.

## 📊 Key Performance Indicators (KPIs)

| KPI | Description |
|---|---|
| Children Reached | Number of children reached by programme activities. |
| Mothers Trained | Number of mothers trained through programme activities. |
| Cost Per Child | Actual expenditure divided by the number of children reached. |
| Budget Utilisation | Actual expenditure expressed as a percentage of the approved budget. |

## 🔍 Data Validation Rules

The workflow checks for the following data quality issues:

- Missing school records.
- Duplicate records.
- Negative budgets.
- Budget overruns.
- Missing finance matches.

These checks help identify records that may require correction, reconciliation, or further investigation before reporting.

## 📁 Expected Outputs

| Output File | Purpose |
|---|---|
| `integrated_dataset.xlsx` | Consolidated education programme and finance data. |
| `district_summary.xlsx` | District-level performance and financial summaries. |
| `school_summary.xlsx` | School-level performance and financial summaries. |
| `validation_report.xlsx` | Summary of data quality checks and findings. |
| `reporting_pack.xlsx` | Consolidated reporting workbook for programme and management review. |

## 🛠️ Tools and Technologies

- **Python** — Data processing and analysis.
- **pandas** — Data cleaning, transformation, integration, and aggregation.
- **CSV** — Source data format.
- **Excel** — Reporting and delivery format.

## 👥 Intended Users

- Education programme managers.
- NGO and civil society programme teams.
- Monitoring, Evaluation and Learning (MEL) professionals.
- Finance and operations teams.
- Data analysts and programme reporting consultants.

## 📈 Expected Value

The project demonstrates how disconnected education programme and financial datasets can be brought together in a structured reporting workflow.

It supports improved visibility into programme reach, expenditure, budget utilisation, and data quality issues, helping teams prepare more consistent reports and identify records requiring attention.

## 🚀 Project Status

This repository contains the implementation of an education programme data integration and reporting workflow. The availability of individual features and output files should be verified against the current codebase.

