from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


def uuid_as_string():
    return str(uuid4())


class User(BaseModel):
    id: str = Field(default_factory=uuid_as_string)
    name: str
