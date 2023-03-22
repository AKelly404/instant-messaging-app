from typing import List

from models.message import Message


class MessageRepository:
    def __init__(self):
        self.messages: List[Message] = []

    def add(self, message: Message):
        self.messages.append(message)
