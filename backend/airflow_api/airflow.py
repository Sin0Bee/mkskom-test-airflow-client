import requests


class AirflowAPI:

    _BASE_URL = "http://loaclhost:8080/api/v1/"
    _HEAD = {

    }

    def __init__(self, dag):
        self.dag = dag
