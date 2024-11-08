from sqlalchemy import Column, String, Integer, TIMESTAMP

# Project
from src.models.Base import Base


class EventType(Base):
  __tablename__ = 'event_type'

  id = Column('event_type_id', Integer, primary_key=True)
  description = Column(String)
  created_at = Column(TIMESTAMP)
  updated_at = Column(TIMESTAMP)
