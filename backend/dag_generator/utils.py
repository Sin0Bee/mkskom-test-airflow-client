import os

from jinja2 import Environment, FileSystemLoader


class _GeneratorDAG:
    _BASE_PATH = os.path.dirname(os.path.abspath(f"{__file__}/../")).split("/")
    _BASE_DAG_DIRECTORY = "/".join(_BASE_PATH[:-1]) + "/dags"
    _DAG_TEMPLATE_PATH = "/".join(_BASE_PATH) + "/dag_generator"

    def __init__(self, params: dict = None) -> None:
        self.params = params

    def generate(self):
        env = Environment(loader=FileSystemLoader(self._DAG_TEMPLATE_PATH))
        template = env.get_template('/templates/dag_templates.jinja2')

        if self.params is not None:
            with open(f"{self._BASE_DAG_DIRECTORY}/dag_config_{self.params.get('name', 'noname')}.py", "w") as f:
                f.write(template.render(self.params))


class DAGManager:
    def add(self, data: dict):
        generator = _GeneratorDAG(data)
        return generator.generate()
