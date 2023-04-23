from datetime import datetime
from typing import List
from uuid import UUID, uuid4
from pydantic import BaseModel, Field


class Thread(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    users: List[UUID]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_used_at: datetime
