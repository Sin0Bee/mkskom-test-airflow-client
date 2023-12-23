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

    def generate(self) -> str:
        env = Environment(loader=FileSystemLoader(self._DAG_TEMPLATE_PATH))
        template = env.get_template('/templates/dag_templates.jinja2')

        filename = self._check_filename(f"{{self.params.get('name', 'noname')}}.py")

        if self.params is not None:
            with open(f"{self._BASE_DAG_DIRECTORY}/{filename}.py", "w") as f:
                f.write(template.render(self.params))

        return f"{self._BASE_DAG_DIRECTORY}/{filename}.py"

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

    def __init__(self):
        self.airflow_api = AirflowAPI()

    def add(self, data: dict) -> dict:
        new_dag_state = {}

        generator = _GeneratorDAG(data)
        path = generator.generate()

        new_dag_state['path'] = path


