import os

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class DBData(BaseModel):
    login: str
    password: str
    host: str
    port: str
    name: str


class Config:
    DB_CONFIG: DBData

    def __init__(self):
        self.DB_CONFIG = self._db()

    def _db(self) -> DBData:
        db_login = os.environ.get('META_STORAGE_LOGIN')
        db_password = os.environ.get('META_STORAGE_PASS')
        db_host = os.environ.get('META_STORAGE_HOST')
        db_port = os.environ.get('META_STORAGE_PORT')
        db_name = os.environ.get('META_STORAGE_NAME')

        return DBData(login=db_login,
                      password=db_password,
                      host=db_host,
                      port=db_port,
                      name=db_name)


config = Config()
