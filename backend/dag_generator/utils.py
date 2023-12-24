import os
import random

from jinja2 import Environment, FileSystemLoader

from airflow_api.airflow import AirflowAPI


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

        except_words = [' ', '$', '\\', '&', '#', '!', '<', '>']

        for c in fn:
            if c in except_words:
                fn = fn.replace(c, "_")
            else:
                continue

        for filename in files:
            if filename == fn:
                new_filename = f'{"".join(fn.split(".")[:-1])}_{random.randint(1, 100)}.py'
                return self._check_filename(new_filename)
            else:
                return fn


class DAGManager:
    _BASE_PATH = os.path.dirname(os.path.abspath(f"{__file__}/../")).split("/")
    _BASE_DAG_DIRECTORY = "/".join(_BASE_PATH) + "/dags"

    def __init__(self):
        self.airflow_api = AirflowAPI()

    def add(self, data: dict) -> dict:
        dag_data = {}

        generator = _GeneratorDAG(data)
        path, filename = generator.generate()

        dag_data['path'] = path
        dag_data['filename'] = filename

        self.airflow_api.unpause_dag(dag_id=filename)

        return {"response": "success",
                "data": dag_data}

    def delete_dag_file(self, filename: str) -> dict:
        if self.check_dag_file(filename=filename):
            os.remove(self._BASE_DAG_DIRECTORY + f"/{filename}")
            return {"status": "success"}
        return {"status": "fall"}

    def check_dag_file(self, filename: str) -> bool:
        files = os.listdir(self._BASE_DAG_DIRECTORY)
        for fn in files:
            if fn == filename:
                return True
        return False
