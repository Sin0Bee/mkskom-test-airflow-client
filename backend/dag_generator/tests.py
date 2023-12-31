from dag_generator.utils import DAGManager

fake_update_data_example = {
    "name": "observer",
    "context": "print('Base PARAM')",
    "file_path": "/backend/dags/observer.py",
    "interval": 10,
    "id": 2
}

fake_db_data_example = {
    "name": "observer",
    "context": "print('Base')",
    "file_path": "/backend/dags/observer.py",
    "interval": 10,
    "id": 2
}


def test_update():
    c = DAGManager()
    update_response = c.update(filename=fake_update_data_example['name'],
                               data=fake_update_data_example,
                               db_data=fake_db_data_example)

    if update_response is not None and update_response.get('data', None) is not None:
        assert update_response['data'] == {'name': 'observer', 'context': "print('Base PARAM')", 'interval': 10}
        return "Test success"
    else:
        return "Test fall", update_response


print(test_update())
