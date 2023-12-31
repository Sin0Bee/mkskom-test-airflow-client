import json

from airflow_api.airflow import AirflowAPI
from celery_app import app
from dag_generator.models import MetaDAG


@app.task
def unpause():
    airflow_api = AirflowAPI()

    dags_in_db = MetaDAG.objects.all()
    data = airflow_api.get_dags()

    if data['response'] == 'success':
        for dag in dags_in_db:
            status = dag.status
            db_dag_name = dag.name
            for air_dag in data['data']['dags']:
                if air_dag['dag_id'] == db_dag_name and status == False:
                    MetaDAG.objects.filter(pk=dag.pk).update(status=True)
