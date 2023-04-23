from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Message(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    text: str
    datetime: datetime
    thread_id: UUID
