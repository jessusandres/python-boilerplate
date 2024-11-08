import os

from dotenv import load_dotenv

load_dotenv()


def get_service_name() -> str:
  return os.getenv('SERVICE_NAME')


def get_project_id() -> str:
  return os.getenv('PROJECT_ID')


def get_database_env() -> dict[str, str | None]:
  return {
    "host": os.getenv('DB_HOST'),
    "port": os.getenv('DB_PORT'),
    "username": os.getenv('DB_USERNAME'),
    "password": os.getenv('DB_PASSWORD'),
    "database": os.getenv('DB_DATABASE'),
    "dialect": os.getenv('DB_DIALECT'),
    "driver": os.getenv('DB_DRIVER'),
    "logging": os.getenv('DB_LOGGER'),
  }
