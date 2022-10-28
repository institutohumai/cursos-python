import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id='random_walker',
    schedule='* * * * *',
    start_date=datetime.datetime(2022, 1, 1),
    catchup=False,
    tags=['experimentos'],
    params={"N": "50"},
) as dag:
    ejemplo = EmptyOperator(
        task_id='prototipo',
    )

    ejemplo
