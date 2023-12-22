Требования.

1. Ubuntu server 22
2. Docker && Docker-compose

Подготовка к запуску.

1. Создать новые директории в корне проекта: mkdir ./plugins ./dags ./logs ./config
2. Генерируем .env файл для airflow: echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
3. Инициализируем зависимости airflow: docker-compose up airflow-init

Гайд по запуску и сама docker-compose file взят с канала: https://www.youtube.com/watch?v=aTaytcxy2Ck

