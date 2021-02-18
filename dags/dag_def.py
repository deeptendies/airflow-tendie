from airflow.models import DAG
from datetime import datetime, timedelta
from airflow.operators.dummy_operator import DummyOperator

import json

# https://bigdata-etl.com/apache-airflow-create-dynamic-dag/

def create_dag(dag_id,
               schedule,
               default_args,
               conf):
    dag = DAG(dag_id, default_args=default_args, schedule_interval=schedule)

    with dag:
        init = DummyOperator(
            task_id='start_tasks',
            dag=dag
        )

        clear = DummyOperator(
            task_id='end_tasks',
            dag=dag
        )

        for table in conf['tables']:
            tab = DummyOperator(
                task_id=table,
                dag=dag
            )
            init >> tab >> clear

        return dag


with open('/opt/airflow/dags/config.json') as json_data:
    conf = json.load(json_data)
    schedule = conf['schedule']
    dag_id = conf['name']

    args = {
        'owner': 'deeptendies',
        'depends_on_past': False,
        'start_date': datetime.now(),
        'email': ['deeptendies@gmail.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
        'concurrency': 1,
        'max_active_runs': 1
    }
    globals()[dag_id] = create_dag(dag_id, schedule, args, conf)