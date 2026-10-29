
from datetime import date
from pydantic import BaseModel


class CreateSession(BaseModel):
    topic_id: int | None = None
    topic_name: str | None = None
    session_date: date
    session_time: str


class AvailableSessionsQuery(BaseModel):
    session_date: date
    topic_id: int | None = None
    topic_name: str | None = None