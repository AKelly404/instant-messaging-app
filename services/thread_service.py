import uuid
from datetime import datetime
from uuid import uuid4
from models.thread import Thread
from repositories.thread_repository import ThreadRepository


class ThreadService:
    def __init__(self):
        self.thread_repository = ThreadRepository()

    def add_thread(self):
        thread = Thread(users=[uuid4()], created_at=datetime.utcnow(), last_used_at=datetime.utcnow())
        self.thread_repository.add(thread)

    def get_thread(self, thread_id):
        thread = Thread(id=uuid.UUID("e9858f68-b987-48de-9e9a-be4957dc165a"), users=[uuid4()],
                        created_at=datetime.utcnow(), last_used_at=datetime.utcnow())
        self.thread_repository.add(thread)
        return self.thread_repository.get_thread(thread_id)

    def get_all_threads(self):
        thread = Thread(id=uuid.UUID("e9858f68-b987-48de-9e9a-be4957dc165a"), users=[uuid4()],
                        created_at=datetime.utcnow(), last_used_at=datetime.utcnow())
        self.thread_repository.add(thread)
        return self.thread_repository.get_all_threads()

    def create_thread(self, thread:Thread):
        self.thread_repository.add(thread)
