import os
import random

from jinja2 import Environment, FileSystemLoader

from airflow_api.airflow import AirflowAPI
from dag_generator.models import DAGData


class _GeneratorDAG:
    _BASE_PATH = os.path.dirname(os.path.abspath(f"{__file__}/../")).split("/")
    _BASE_DAG_DIRECTORY = "/".join(_BASE_PATH) + "/dags"
    _DAG_TEMPLATE_PATH = "/".join(_BASE_PATH) + "/dag_generator"

    def __init__(self, params: dict = None) -> None:
        self.params = params

    def generate(self) -> tuple[str, str | None]:
        env = Environment(loader=FileSystemLoader(self._DAG_TEMPLATE_PATH))
        template = env.get_template('/templates/dag_templates.jinja2')

        filename = self._check_filename(f"{self.params.get('name', 'noname')}")
        self.params['name'] = filename

        if self.params is not None:
            with open(f"{self._BASE_DAG_DIRECTORY}/{filename}.py", "w") as f:
                f.write(template.render(self.params))

        return f"{self._BASE_DAG_DIRECTORY}/{filename}.py", filename

    def _check_filename(self, fn: str) -> None | str:
        files = os.listdir(self._BASE_DAG_DIRECTORY)

        except_words = [' ', '$', '\\', '&', '#', '!', '<', '>', ':',
                        ';', '^', '%', '*', '@', '[', ']', '"', "'", '~', '`',]

        for c in fn:
            if c in except_words:
                fn = fn.replace(c, "_")
            else:
                continue

        for filename in files:
            if filename == fn + ".py":
                new_filename = f'{fn}{"".join(fn.split(".")[:-1])}_{random.randint(1, 100)}'
                return self._check_filename(new_filename)
            else:
                continue

        return fn


class DAGManager:
    _BASE_PATH = os.path.dirname(os.path.abspath(f"{__file__}/../")).split("/")
    _BASE_DAG_DIRECTORY = "/".join(_BASE_PATH) + "/dags"

    def __init__(self):
        self.airflow_api = AirflowAPI()

    def add(self, data: DAGData) -> dict | None:
        dag_data = {}

        generator = _GeneratorDAG(data.to_dict())
        path, filename = generator.generate()

        try:
            interval = int(data.interval)
            if interval < 1:
                dag_data['interval'] = 1
            else:
                dag_data['interval'] = interval
        except Exception:
            return None

        dag_data['path'] = path
        dag_data['filename'] = filename

        return {"data": dag_data}

    def delete(self, data: dict) -> None:
        delete_status = self.delete_dag_file(filename=data['name'])

        if delete_status:
            self.airflow_api.delete_dag(dag_id=data['name'])

    def update(self, filename: str, data: DAGData, db_data: dict) -> dict | None:

        interval = self._check_param(param_name="interval", data=data.to_dict(), db_data=db_data)
        context = self._check_param(param_name="context", data=data.to_dict(), db_data=db_data)

        update_data = {
            "name": filename,
            "context": context,
            "interval": interval
        }

        response = {}

        delete_status = self.delete_dag_file(filename=filename)

        if delete_status:
            self.airflow_api.delete_dag(dag_id=filename)
            generator = _GeneratorDAG(update_data)
            generator.generate()

            response['status'] = 'fall'
            response['data'] = update_data

            return response

    def _check_param(self, param_name: str, data: dict, db_data: dict):
        if data[param_name] != db_data[param_name]:
            return data[param_name]
        else:
            return db_data[param_name]

    def delete_dag_file(self, filename: str) -> dict:
        if self.check_dag_file(filename=filename):
            os.remove(self._BASE_DAG_DIRECTORY + f"/{filename}.py")

            return {"status": "success"}
        return {"status": "fall"}

    def check_dag_file(self, filename: str) -> bool:
        files = os.listdir(self._BASE_DAG_DIRECTORY)
        for fn in files:
            if fn == filename + ".py":
                return True
        return False
