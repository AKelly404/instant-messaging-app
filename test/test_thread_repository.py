from datetime import datetime
from uuid import UUID, uuid4
from models.thread import Thread
from repositories.thread_repository import ThreadRepository


class TestThreadRepository:
    def test_thread_add(self):
        thread_repository = ThreadRepository()
        date = datetime.utcnow()
        thread = Thread(users=[uuid4()], created_at=date, last_used_at=date)
        thread_repository.add(thread)
        assert thread_repository.threads[0].created_at == date
