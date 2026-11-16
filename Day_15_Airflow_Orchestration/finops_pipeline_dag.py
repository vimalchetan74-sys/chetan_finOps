from datetime import datetime
try:
    from airflow import DAG
    from airflow.operators.bash import BashOperator
except ImportError:
    raise SystemExit("Install Apache Airflow in a supported environment to load this DAG.")

with DAG(
    dag_id="finops_daily_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["finops", "data-engineering"],
) as dag:
    ingest = BashOperator(task_id="ingest_billing", bash_command="python /opt/pacex/Day_03_Python_ETL/ingest_billing.py --input /opt/pacex/Datasets/raw_billing.csv --output /opt/pacex/Day_03_Python_ETL/output/clean_billing.csv")
    quality = BashOperator(task_id="data_quality", bash_command="python /opt/pacex/Day_06_Data_Quality/validate_billing.py")
    anomaly = BashOperator(task_id="anomaly_detection", bash_command="python /opt/pacex/Day_12_Anomaly_Detection/anomaly_engine.py --input /opt/pacex/Datasets/daily_costs.csv")
    ingest >> quality >> anomaly
