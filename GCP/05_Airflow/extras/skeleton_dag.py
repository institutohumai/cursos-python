import datetime
import random

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import BranchPythonOperator
from airflow.utils.edgemodifier import Label
from airflow.utils.trigger_rule import TriggerRule

with DAG(
    dag_id='random_walker',
    schedule='* * * * *',
    start_date=datetime.datetime(2022, 1, 1),
    catchup=False,
    tags=['experimentos'],
    params={"N": "50"},
) as dag:
    # Lanzamos los dados y la moneda
    tirar_dados = EmptyOperator(
        task_id='tirar_dados',
    )

    # Dependiendo del resultado vamos a avanzar o permanecer quietos
    resultados = ['avanzar', 'permanecer']

    branching = BranchPythonOperator(
        task_id='branching',
        python_callable=lambda: random.choice(resultados),
    )

    # Vamos a tirar los dados antes de analizar sus resultados
    tirar_dados >> branching

    # No importa que camino se haya tomado, vamos a registrar en donde está el walker
    loggear_posicion = EmptyOperator(
        task_id='loggear_posición',
        trigger_rule=TriggerRule.NONE_FAILED_MIN_ONE_SUCCESS,
    )

    # En este caso, para ambos caminos vamos a calcularla la nuevo posición
    for option in resultados:
        t = EmptyOperator(
            task_id=option,
        )

        nueva_posicion = EmptyOperator(
            task_id='nueva_posicion_' + option,
        )

        # Las Label son opcionales pero nos sirven para entender el flujo
        branching >> Label(option) >> t >> nueva_posicion >> loggear_posicion
