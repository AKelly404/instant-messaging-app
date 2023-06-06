import uuid
from datetime import datetime
from typing import List, Dict
from uuid import UUID
from models.message import Message
import pymongo


client = pymongo.MongoClient('mongodb://127.0.0.1:27017/big_time_database')
db = client["big_time_database"]
collection = db["messages"]


class MessageRepository:
    def __init__(self):
        self.messages: List[Message] = []

    def add(self, message: Message):
        collection.insert_one(message.dict())

    def get_all(self) -> List[Message]:
        return self.messages

    def get_all_for_thread(self, thread_id: UUID):
        print(self.messages)
        return [message for message in self.messages if message.thread_id == thread_id]


message_repository = MessageRepository()
message = Message(thread_id=str(uuid.uuid4()), text="banana", datetime=datetime.utcnow())
message_repository.add(message)
