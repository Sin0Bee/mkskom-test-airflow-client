# mkskom-test-airflow-client

### swagger: http://localhost:8000/api/v1/docs
### ui: http://localhost
### airflow-ui: http://localhost:8080
### meta database: localhost:5433

## Требования
```
Docker && Docker-compose
```

## Подготовка к запуску
```
#Создать новые директории в корне проекта:
 mkdir ./plugins ./dags ./logs ./config
 
#Генерируем .env файл для airflow:
 echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
 
#Инициализируем зависимости airflow:
 docker-compose up airflow-init
```
# Создаем ENV файлы
## .env -> dir(config)
```
META_STORAGE_LOGIN="postgres"
META_STORAGE_PASS="PASSWORD" # ТУТ НУЖНО УКАЗАТЬ ПАРОЛЬ КОТОРЫЙ ЗАДАЕТСЯ В docker-compose.yaml
META_STORAGE_HOST="meta-storage"
META_STORAGE_PORT="5432"
META_STORAGE_NAME="postgres"

SECRET_TOKEN='SECRET_KEY'

REDIS_LOGIN="none"
REDIS_PASS="none"
REDIS_HOST="redis"
REDIS_PORT="6379"

AIRFLOW_L='airflow'
AIRFLOW_P='airflow'

```
## .env -> root_project (auto generate)
```
AIRFLOW_UID=1000
AIRFLOW_GID=0

```

## Запуск
```
#Из корневой папки приложения:
    docker-compose up
```
