import pydantic
import sqlalchemy as sa
from sqlalchemy import orm


class Config(pydantic.BaseSettings):
    URL: str
    STATEMENT_TIMEOUT: int = pydantic.Field(2000)
    POOL_SIZE: int = pydantic.Field(20)
    MAX_OVERFLOW: int = pydantic.Field(10)
    POOL_RECYCLE: int = pydantic.Field(600)
    POOL_TIMEOUT: int = pydantic.Field(300)
    
    class Config:
        env_prefix = "DATABASE_"

config = Config()
engine = sa.create_engine(
    config.URL,
    pool_size=config.POOL_SIZE, max_overflow=config.MAX_OVERFLOW,
    pool_recycle=config.POOL_RECYCLE, pool_timeout=config.POOL_TIMEOUT,
)
session = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)