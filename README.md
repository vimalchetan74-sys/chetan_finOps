# PACEX 21-Day Internship Project
## Data Engineering & Cloud FinOps

This repository is a learning/reference implementation aligned to the supplied PACEX 21-working-day plan. It contains starter implementations, reproducible sample data, SQL, Python modules, infrastructure examples, and submission templates.

### Important evidence note
The included datasets and execution outputs are **synthetic demonstration data**. They do not represent access to PACEX systems, AWS/Azure/GCP billing accounts, a live cloud environment, or work that has actually been executed by the intern. Replace sample evidence with your own screenshots, run logs, dates, hours, and GitHub commit links after completing each task.

### Requirements
- Python 3.10+
- Packages: `pandas`, `numpy`, `matplotlib`, `streamlit`, `openpyxl`
- Optional: Docker, PostgreSQL, Apache Airflow, Terraform, Infracost, kubectl, Power BI/Tableau, cloud provider account

Install core dependencies:
```bash
pip install -r requirements.txt
```

### Quick start
1. Start with `Day_01_Data_Modeling/` and follow `Documentation/21_Day_Sequential_Guide.pdf`.
2. Work through one day at a time. Each folder has a `README.md` with the task, commands, outputs and evidence checklist.
3. For SQLite-compatible SQL, use:
```bash
python scripts/run_sqlite.py Day_01_Data_Modeling/schema.sql
```
4. Run the Day 3 ingestion:
```bash
python Day_03_Python_ETL/ingest_billing.py --input Datasets/raw_billing.csv --output Day_03_Python_ETL/output/clean_billing.csv
```
5. Run the anomaly example:
```bash
python Day_12_Anomaly_Detection/anomaly_engine.py --input Datasets/daily_costs.csv
```
6. Run the dashboard:
```bash
streamlit run Day_18_BI_Dashboard/app.py
```

### Folder map
- `Day_01`–`Day_21`: day-wise deliverables
- `Datasets/`: synthetic source datasets
- `Documentation/`: sequential guide and evidence guidance
- `Work_Log/`: editable 21-day Excel work log template
- `scripts/`: helper scripts

### SQL dialect
Most SQL examples use SQLite-compatible SQL for easy local practice. Day 10 includes separate BigQuery-style DDL; adapt it for your chosen warehouse. PostgreSQL-only performance commands are clearly labelled.

### Completion rule
A folder being present does not mean the task is complete. Mark a day complete only after running, validating, understanding, and capturing your own evidence.
