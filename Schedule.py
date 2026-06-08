from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from main import run_etl_pipeline


default_args = {
    "owner": "rohan",
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}


with DAG(
    dag_id="ecommerce_api_etl_pipeline",
    default_args=default_args,
    description="ETL pipeline for e-commerce API data into MySQL",
    start_date=datetime(2026, 6, 8),
    schedule_interval="@daily",
    catchup=False,
    tags=["ecommerce", "etl", "mysql", "airflow"],
) as dag:

    run_pipeline = PythonOperator(
        task_id="extract_transform_load_ecommerce_data",
        python_callable=run_etl_pipeline
    )

    run_pipeline