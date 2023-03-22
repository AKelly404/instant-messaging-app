from datetime import datetime

from models.message import Message
from repositories.message_repository import MessageRepository


class TestMessageRepository:
    def test_add(self):
        message_repository = MessageRepository()
        message = Message(text="banana", datetime=datetime.utcnow())
        message_repository.add(message)
        assert message_repository.messages[0].text == "banana"
