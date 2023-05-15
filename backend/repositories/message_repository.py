from typing import List
from uuid import UUID
from models.message import Message


class MessageRepository:
    def __init__(self):
        self.messages: List[Message] = []

    def add(self, message: Message):
        self.messages.append(message)

    def get_all(self) -> List[Message]:
        return self.messages

    def get_all_for_thread(self, thread_id: UUID):
        print(self.messages)
        return [message for message in self.messages if message.thread_id == thread_id]
