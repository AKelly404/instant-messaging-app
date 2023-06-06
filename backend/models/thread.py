from datetime import datetime
from typing import List
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

from utils.model_utils import to_camel_case


def uuid_as_string():
    return str(uuid4())


class Thread(BaseModel):
    id: str = Field(default_factory=uuid_as_string)
    users: List[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_used_at: datetime

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
