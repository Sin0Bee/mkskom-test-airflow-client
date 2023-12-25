from django.test import TestCase

from dag_generator.utils import DAGManager

test_example = {
    "name": "observer",
    "context": "print('Base PARAM')",
    "file_path": "/backend/dags/observer.py",
    "interval": 10,
    "id": 2,
    "update_param": {"context": "print('Hello World update')"}
}

success_test = {'name': 'observer', 'context': "print('Hello World update')", 'interval': 10}


def test_update():
    c = DAGManager()
    update_response = c.update(filename=test_example['name'], data=test_example)
    if update_response is not None and update_response.get('data', None) is not None:
        assert update_response['data'] == {'name': 'observer', 'context': "print('Hello World update')", 'interval': 10}
        return "Test success"
    else:
        return "Test fall", update_response


print(test_update())
