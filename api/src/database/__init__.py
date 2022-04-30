from urllib.parse import urlparse

import pydantic
import pymysql


class Config(pydantic.BaseSettings):
    URL: str
    
    class Config:
        env_prefix = "DATABASE_"

config = Config()


url = urlparse(config.URL)


def generate_conn() -> pymysql.Connection:
    connection = pymysql.connect(
        host=url.hostname,
        user=url.username,
        password=url.password,
        database=url.path[1:],
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection