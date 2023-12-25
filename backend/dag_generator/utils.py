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

    def add(self, data: dict) -> dict:
        dag_data = {}

        generator = _GeneratorDAG(data)
        path, filename = generator.generate()

        dag_data['path'] = path
        dag_data['filename'] = filename

        return {"response": "success",
                "data": dag_data}

    def delete(self, data: dict) -> dict:
        response = {}

        delete_status = self.delete_dag_file(filename=data['name'])

        if delete_status:
            response_airflow = self.airflow_api.delete_dag(dag_id=data['name'])
            if response_airflow['response'] == 'success':
                response['status_code'] = 200
                response['status'] = 'success'

                return response
            else:
                response['status_code'] = 400
                response['status'] = 'fall'

                return response
        else:
            response['status_code'] = 400
            response['status'] = 'fall'

            return response

    def update(self, filename: str, data: dict) -> dict:

        interval = data['update_param'].get('interval', None)
        context = data['update_param'].get('context', None)

        if interval is not None:
            interval = data['update_param'].get('interval', None)
        else:
            interval = data['interval']

        if context is not None:
            context = data['update_param'].get('context', None)
        else:
            context = data['context']

        update_data = {
            "name": filename,
            "context": context,
            "interval": interval
        }

        generator = _GeneratorDAG(update_data)
        response = {}

        delete_status = self.delete_dag_file(filename=filename)

        if delete_status:
            response_airflow = self.airflow_api.delete_dag(dag_id=filename)

            path, filename = generator.generate(update_data)
            response['path'] = path

            if response_airflow['response'] == 'success':
                response['status_code'] = 200
                response['status'] = 'success'

                return response
            else:
                response['status_code'] = 400
                response['status'] = 'fall'

                return response



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


c = DAGManager()
# c.update()
