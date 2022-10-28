import datetime
import glob
import os

import numpy as np
from airflow import DAG
from airflow.operators.python import BranchPythonOperator, PythonOperator
from airflow.utils.edgemodifier import Label
from airflow.utils.trigger_rule import TriggerRule


# Utils
def get_last_file(path: str) -> str:
    """Get the name of last created file in a given path

    Args:
        path (str): Path to the explore

    Returns:
        str: Name of the last created file
    """
    list_of_files = glob.glob(f"{path}*")
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file


# Funciones
def tirar_dados_func(N: str):

    # Convertimos N a int
    N = int(N)

    # A partir de la fecha generamos una etiqueta
    time_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Tiro dados
    dados = np.random.randint(1, 7, size=N)

    # Tiro monedas
    monedas = np.random.choice([-1, 1], size=N)

    # Guardamos valores
    if not os.path.isdir("/home/airflow/gcs/data/dados/"):
        os.makedirs("/home/airflow/gcs/data/dados/")
    with open(f"/home/airflow/gcs/data/dados/{time_name}.npy", "wb") as f:
        np.save(f, dados)

    if not os.path.isdir("/home/airflow/gcs/data/monedas/"):
        os.makedirs("/home/airflow/gcs/data/monedas/")
    with open(f"/home/airflow/gcs/data/monedas/{time_name}.npy", "wb") as f:
        np.save(f, monedas)


def branching_func(
    **context,
):  # Agregamos el contexto para poner mandar mensajes entre tareas

    # Obtengo los ultimos dados y monedas
    ultimos_dados = get_last_file("/home/airflow/gcs/data/dados/")
    ultimas_monedas = get_last_file("/home/airflow/gcs/data/monedas/")

    dados = np.load(ultimos_dados)
    monedas = np.load(ultimas_monedas)

    # Calculo la suma total de pasos en ambas direcciones
    suma = (dados * monedas).sum()

    # Mandamos el mensaje de cuanto fue la suma
    task_instance = context["task_instance"]
    task_instance.xcom_push(key="suma_de_pasos", value=str(suma))

    # Si el walker debe avanzar
    if suma >= 0:
        return "avanzar"

    # Caso contrario
    return "permanecer"


def avanzar_func(
    **context,
):

    # Recibimos el mensaje de `branching`
    task_instance = context["task_instance"]
    suma = task_instance.xcom_pull(task_ids="branching", key="suma_de_pasos")

    # "Procesamos" la nueva suma.
    print(f"El walker avanza {suma} pasos!")


def nueva_posicion_avanzar_func(
    **context,
):

    # Recibimos el mensaje de `branching`
    task_instance = context["task_instance"]
    suma = task_instance.xcom_pull(task_ids="branching", key="suma_de_pasos")

    # Ultima posicion
    if not os.path.isdir("/home/airflow/gcs/data/posiciones/"):
        os.makedirs("/home/airflow/gcs/data/posiciones/")
        posicion = 0
    else:
        ultima_posicion = get_last_file("/home/airflow/gcs/data/posiciones/")
        with open(ultima_posicion, "r+") as f:
            posicion = f.read()

    # Calculamos la nueva posicion
    nueva_posicion = int(suma) + int(posicion)

    # Guardamos la ultima posicion
    time_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"/home/airflow/gcs/data/posiciones/{time_name}.txt", "w") as f:
        f.write(str(nueva_posicion))


def permanecer_func(
    **context,
):

    # Recibimos el mensaje de `branching`
    task_instance = context["task_instance"]
    suma = task_instance.xcom_pull(task_ids="branching", key="suma_de_pasos")

    # "Procesamos" la nueva suma.
    print(f"El walker no va a moverse porque la suma fue {suma}!")


def nueva_posicion_permanecer_func():

    # Ultima posicion
    if not os.path.isdir("/home/airflow/gcs/data/posiciones/"):
        os.makedirs("/home/airflow/gcs/data/posiciones/")
        posicion = 0
    else:
        ultima_posicion = get_last_file("/home/airflow/gcs/data/posiciones/")
        with open(ultima_posicion, "r+") as f:
            posicion = f.read()

    # Calculamos la "nueva" posicion
    nueva_posicion = int(posicion)

    # Guardamos la "nueva" posicion
    time_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"/home/airflow/gcs/data/posiciones/{time_name}.txt", "w") as f:
        f.write(str(nueva_posicion))


def loggear_posicion_func():

    # Obtengo la ultima posicion
    ultima_posicion = get_last_file("/home/airflow/gcs/data/posiciones/")
    with open(ultima_posicion, "r") as f:
        posicion = f.read()

    # "Proceso" la última posicion
    print(f"En este momento, el walker está en {posicion}!")


# DAG
with DAG(
    dag_id="random_walker_composer",
    schedule_interval="* * * * *",
    start_date=datetime.datetime(2022, 1, 1),
    catchup=False,
    tags=["experimentos"],
    params={"N": "50"},
) as dag:

    # Lanzamos los dados y la moneda
    tirar_dados = PythonOperator(
        task_id="tirar_dados",
        op_args=[
            "{{ params.N }}",  # Acá usamos el formato de templating
        ],
        python_callable=tirar_dados_func,
    )

    # Dependiendo del resultado vamos a avanzar o permanecer quietos
    branching = BranchPythonOperator(
        task_id="branching",
        python_callable=branching_func,
        provide_context=True,  # Proveemos el contexto para enviar mensajes entre tareas
    )

    # Vamos a tirar los dados antes de analizar sus resultados
    tirar_dados >> branching

    # Avanzamos
    avanzar = PythonOperator(
        task_id="avanzar",
        python_callable=avanzar_func,
        provide_context=True,
    )

    # Brancheamos y luego avanzamos
    branching >> Label("avanzar") >> avanzar

    # Calculamos la nueva posicion
    nueva_posicion_avanzar = PythonOperator(
        task_id="nueva_posicion_avanzar",
        python_callable=nueva_posicion_avanzar_func,
        provide_context=True,
    )

    # Luego de procesar el avance, calculamos la nuva posicion
    avanzar >> nueva_posicion_avanzar

    # Permanecemos quietos
    permanecer = PythonOperator(
        task_id="permanecer",
        python_callable=permanecer_func,
        provide_context=True,
    )

    # Brancheamos y luego avanzamos
    branching >> Label("permanecer") >> permanecer

    # Calculamos la nueva posicion
    nueva_posicion_permanecer = PythonOperator(
        task_id="nueva_posicion_permanecer",
        python_callable=nueva_posicion_permanecer_func,
    )

    # Luego de procesar el avance, calculamos la nuva posicion
    permanecer >> nueva_posicion_permanecer

    # No importa que camino se haya tomado, vamos a registrar en donde está el walker
    loggear_posicion = PythonOperator(
        task_id="loggear_posicion",
        python_callable=loggear_posicion_func,
        trigger_rule=TriggerRule.NONE_FAILED_MIN_ONE_SUCCESS,
    )

    # Si se avanzo o no, se loggea
    [nueva_posicion_avanzar, nueva_posicion_permanecer] >> loggear_posicion
