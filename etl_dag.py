from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from movies_webscrape import run_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='Airflow DAG for ETL pipeline',
    schedule_interval=timedelta(days=1),
)

etl_pipeline = PythonOperator(
    task_id='complete_twitter_etl',
    python_callable=run_etl,
    dag=dag, 
)

etl_pipeline