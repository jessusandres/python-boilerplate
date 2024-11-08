from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

# Project
from src.common import logger
from src.common.helpers import get_service_name, get_project_id
from src.config.database import build_db_engine
from src.models import EventType


def say_welcome(name: str) -> None:
  service_name = get_service_name()
  project_id = get_project_id()

  greeting = f"Welcome {name} to {service_name} allocated in {project_id}"

  logger.info(greeting)


def get_event_types() -> list[dict[str, any]]:
  database_session = sessionmaker(bind=build_db_engine())

  with database_session() as session:
    # session = DatabaseSession()

    # For plain queries
    result_cursor = session.execute(text("SELECT 1")).first()
    logger.info(f"Ping result: {result_cursor[0]}")

    query_ids = [i for i in range(1, 11)]

    # For model queries
    model_result_cursor = (
      session
      .query(EventType)
      .where(EventType.id.in_(query_ids))
      .order_by(EventType.created_at.desc())
      .all()
    )

    records = []

    for item_result in model_result_cursor:
      records.append({
        "id": item_result.id,
        "description": item_result.description,
        "createdAt": item_result.created_at,
        "updatedAt": item_result.updated_at
      })

    return records
