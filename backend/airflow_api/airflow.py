import requests
from dag_generator.models import DAGTransfer


class Airflow:

    _BASE_URL = "http://loaclhost:8080/api/v1/dag"
    _HEAD = {

    }

    def __init__(self, dag: DAGTransfer):
        self.dag = dag

