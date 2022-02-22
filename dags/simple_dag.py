from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

default_args = {"retry": 5, "retry_delay": timedelta(seconds=90)}

with DAG(
    dag_id="simple_dag",
    schedule_interval="@daily",
    start_date=days_ago(3),
    catchup=True,
    max_active_runs=1,
    default_args=default_args,
) as dag:

    task_1 = DummyOperator(task_id="task_1", retry_delay=timedelta(minutes=5))

    task_1 = DummyOperator(task_id="task_2")

    task_1 = DummyOperator(task_id="task_3")
