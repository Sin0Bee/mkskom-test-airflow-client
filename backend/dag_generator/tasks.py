from airflow_api.airflow import AirflowAPI
from celery_app import app
from dag_generator.models import MetaDAG

from django.db.utils import DataError


@app.task
def unpause():
    airflow_api = AirflowAPI()

    dags_in_db = MetaDAG.objects.all()
    dags_in_airflow = airflow_api.get_dags()

    for dag in dags_in_db:
        print(dag)
