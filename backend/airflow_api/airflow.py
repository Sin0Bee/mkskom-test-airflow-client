import requests
from config.backend_env import config


class AirflowAPI:

    _BASE_URL = "http://localhost:8080/api/v1/"
    _HEADERS = {
        "Content-type": "application / json",
        "Accept": "application / json"
    }

    def __init__(self, dag_id: str | None):
        self.dag_id = dag_id
        self.session = requests.session()

    def get_dags(self):
        return self.session.get(url=self._BASE_URL+"dags", headers=self._HEADERS, auth=(config.AUTH_CONFIG.login,
                                                                                        config.AUTH_CONFIG.password))


# c = AirflowAPI(dag_id="")
# a = c.get_dags()
# print(a.text)
