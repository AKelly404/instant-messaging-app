import uuid
from datetime import datetime
from uuid import uuid4, UUID
from models.thread import Thread
from models.message import Message
from repositories.thread_repository import ThreadRepository
from repositories.message_repository import MessageRepository


class ThreadService:
    def __init__(self):
        self.thread_repository = ThreadRepository()
        self.message_repository = MessageRepository()

    def add_thread(self):
        thread = Thread(users=[str(uuid4())], created_at=datetime.utcnow(), last_used_at=datetime.utcnow())
        self.thread_repository.add(thread)

    def get_thread(self, thread_id):
        thread = Thread(id="e9858f68-b987-48de-9e9a-be4957dc165a", users=[str(uuid4())],
                        created_at=datetime.utcnow(), last_used_at=datetime.utcnow())
        self.thread_repository.add(thread)
        return self.thread_repository.get_thread(thread_id)

    def get_all_threads(self):
        thread = Thread(id="e9858f68-b987-48de-9e9a-be4957dc165a", users=[str(uuid4())],
                        created_at=datetime.utcnow(), last_used_at=datetime.utcnow())
        self.thread_repository.add(thread)
        return self.thread_repository.get_all_threads()

    def create_thread(self, thread: Thread):
        self.thread_repository.add(thread)

    def create_message(self, message: Message):
        self.message_repository.add(message)

    def get_messages(self, thread_id: UUID):
        message = Message(text="banana", datetime=datetime.utcnow(), thread_id="e9858f68-b987-48de-9e9a-be4957dc165a")
        self.message_repository.add(message)
        return self.message_repository.get_all_for_thread(thread_id)
