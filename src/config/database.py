import re

from sqlalchemy import URL, create_engine, Engine

# Project
from src.common import logger
from src.common.helpers import get_database_env
from src.models.EventTypeModel import Base

database_credentials = get_database_env()
db_dialect = database_credentials.get('dialect')
db_logging = False if not database_credentials.get('logging') else database_credentials.get('logging')


def sync_db(engine: Engine):
  logger.warn('Filling database with demo tables')

  with engine.connect() as conn:
    Base.metadata.drop_all(conn)
    Base.metadata.create_all(conn)


def build_sqlite_engine() -> Engine:
  logger.info('===> DB working with SQlite')
  database = database_credentials.get("database")

  url_object = f"{db_dialect}:///{database}.db"

  db_logger = bool(re.search(db_logging, 'TRUE', re.IGNORECASE))

  engine = create_engine(url_object, echo=db_logger)

  sync_db(engine)

  return engine


def build_default_engine() -> Engine:
  logger.info(f'===> DB working with {db_dialect}')

  driver_name = f"{database_credentials.get('dialect')}+{database_credentials.get('driver')}"

  db_logger = bool(re.search(db_logging, 'TRUE', re.IGNORECASE))

  url_object = URL.create(
    drivername=driver_name,
    username=database_credentials.get("username"),
    password=database_credentials.get("password"),
    host=database_credentials.get("host"),
    port=database_credentials.get("port"),
    database=database_credentials.get("database"),
  )

  return create_engine(url_object, echo=db_logger)


def build_custom_engine(dialect: str, driver: str, username: str, password: str, host: str, port: int,
                        database: str, logging: bool) -> Engine:
  logger.info(f'===> Custom DB working with {db_dialect}')

  driver_name = f"{dialect}+{driver}"

  url_object = URL.create(
    drivername=driver_name,
    username=username,
    password=password,
    host=host,
    port=port,
    database=database,
  )

  return create_engine(url_object, echo=logging)


def build_db_engine():
  if db_dialect == 'sqlite':
    return build_sqlite_engine()

  return build_default_engine()
