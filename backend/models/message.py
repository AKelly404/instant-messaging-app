from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, validator

from utils.model_utils import to_camel_case


def uuid_as_string():
    return str(uuid4())


class Message(BaseModel):
    id: str = Field(default_factory=uuid_as_string)
    text: str
    datetime: datetime
    thread_id: str

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True

