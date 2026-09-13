# 🌤️ Real-Time Automated Air Quality Data Pipeline

An end-to-end, lightweight Modern Data Stack (MDS) pipeline built to collect, store, transform, and validate real-time air quality & weather data for major cities in Indonesia.

---

## 🏗️ Architecture & Data Lineage

```

[Open-Meteo Public API]
│
▼ (1. Extractor & Ingestion - Python / Polars)
[Local Data Lake - Partitioned Parquet Files]
│
▼ (2. Data Warehousing & Transformation - DuckDB + dbt)
[DuckDB Data Warehouse (Staging -> Marts)]
│
▼ (3. Analytics & Visualization)
[Streamlit Interactive Dashboard]

# =======================================================
Orchestrator: Prefect (Scheduled Hourly Executions & Data Quality Checks)

```

---

## 🛠️ Tech Stack

- **Ingestion & Data Lake:** Python 3.x, Polars, Apache Parquet (Partitioned by Year/Month)
- **Data Warehousing:** DuckDB (In-Process OLAP Engine)
- **Data Transformation & Quality:** dbt-duckdb (Staging Views, Data Marts Tables, `schema.yml` Assertions)
- **Orchestration:** Prefect 3.x (DAG Workflows, Retry Mechanism, Local Scheduler)
- **Data Visualization:** Streamlit

---

## 📁 Repository Structure

```text
├── data_lake/               # Local Parquet storage (ignored in git)
├── warehouse/               # DuckDB warehouse storage (ignored in git)
├── dbt_project/             # dbt models, profiles, and data quality tests
│   ├── models/
│   │   ├── staging/        # Data Cleaning & Type Casting
│   │   └── marts/          # Business Aggregations & Analytical Marts
│   └── dbt_project.yml
├── ingest_weather.py        # API Ingestion logic (Polars)
├── flow.py                  # Prefect Orchestration DAG
├── dashboard.py             # Streamlit Interactive Dashboard
└── requirements.txt         # Project Dependencies

```

---

## 🚀 Quick Start & How to Run

1. **Clone Repository & Setup Environment:**

```bash
git clone [https://github.com/ahmadchoms/weather-de-pipeline.git](https://github.com/ahmadchoms/weather-de-pipeline.git)
cd weather-de-pipeline
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt

```

2. **Run Pipeline Orchestration:**

```bash
python flow.py

```

3. **Launch Streamlit Dashboard:**

```bash
streamlit run dashboard.py

```
