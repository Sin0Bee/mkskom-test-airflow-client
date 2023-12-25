import requests
from config.backend_env import config


class AirflowAPI:
    _BASE_URL = "http://localhost:8080/api/v1/"
    # _BASE_URL = "http://airflow-webserver:8080/api/v1/"
    _HEADERS = {
        "Content-type": "application/json",
        "Accept": "application/json"
    }

    def __init__(self):
        self.session = requests.session()

    def get_dags(self) -> dict:
        try:
            req = self.session.get(url=self._BASE_URL + "dags",
                                   headers=self._HEADERS,
                                   auth=(config.AUTH_CONFIG.login,
                                         config.AUTH_CONFIG.password))
            return {"data": req.json(),
                    "response": "success"}
        except Exception as e:
            return {"response": e}

    def unpause_dag(self, dag_id: str) -> dict:
        try:
            res = self.session.patch(url=self._BASE_URL + f"dags/{dag_id}",
                                     headers=self._HEADERS,
                                     auth=(config.AUTH_CONFIG.login,
                                           config.AUTH_CONFIG.password),
                                     json={'is_paused': False})
            if res.status_code == 200:
                return {"data": res.json(),
                        "response": "success"}
            else:
                return {"data": res.json(),
                        "response": "fall"}
        except Exception as e:
            return {"response": e}

    def delete_dag(self, dag_id: str) -> dict:
        try:
            req = self.session.delete(url=self._BASE_URL + f"dags/{dag_id}",
                                      headers=self._HEADERS,
                                      auth=(config.AUTH_CONFIG.login,
                                            config.AUTH_CONFIG.password))
            return {"data": req.json(),
                    "response": "success"}
        except Exception as e:
            return {"data": e,
                    "response": "fall"}

    def update_dag(self, dag_id: str, **param) -> dict:
        print(param)
        try:
            res = self.session.patch(url=self._BASE_URL + f"dags/{dag_id}",
                                     headers=self._HEADERS,
                                     auth=(config.AUTH_CONFIG.login,
                                           config.AUTH_CONFIG.password),
                                     json=param)
            if res.status_code == 200:
                return {"data": res.json(),
                        "response": "success"}
            else:
                return {"data": res.json(),
                        "response": "fall"}
        except Exception as e:
            return {"response": e}
