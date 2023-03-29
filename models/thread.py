from datetime import datetime
from typing import List
from uuid import UUID, uuid4
from pydantic import BaseModel, Field


class Thread(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    users: List[UUID]
    created_at: datetime
    last_used_at: datetime
