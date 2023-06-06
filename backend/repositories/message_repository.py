import uuid
from datetime import datetime
from typing import List, Dict
from uuid import UUID
import json
import bson

from models.message import Message
import pymongo


client = pymongo.MongoClient('mongodb://127.0.0.1:27017/big_time_database')
db = client["big_time_database"]
collection = db["messages"]

class MessageRepository:
    def __init__(self):
        self.messages: List[Message] = []

    def add(self, message: Message):
        dictionary: Dict = json.loads(json.dumps(message.json()))
        collection.insert_one(dictionary)

    def get_all(self) -> List[Message]:
        return self.messages

    def get_all_for_thread(self, thread_id: UUID):
        print(self.messages)
        return [message for message in self.messages if message.thread_id == thread_id]

message_repository = MessageRepository()
bson_thread_id = bson.Binary.from_uuid(uuid.uuid4())
message = Message(thread_id=bson_thread_id, text="banana", datetime=datetime.utcnow())
message_repository.add(message)
