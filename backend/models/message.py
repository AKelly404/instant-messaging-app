from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, validator

from utils.model_utils import to_camel_case



class Message(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    text: str
    datetime: datetime
    thread_id: UUID

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
