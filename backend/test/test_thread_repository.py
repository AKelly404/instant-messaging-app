from datetime import datetime
from uuid import uuid4
from models.thread import Thread
from repositories.thread_repository import ThreadRepository


class TestThreadRepository:
    def test_thread_add(self):
        thread_repository = ThreadRepository()
        date = datetime.utcnow()
        thread = Thread(users=[uuid4()], last_used_at=date)
        thread_repository.add(thread)
        assert thread_repository.threads[0].created_at == date

    def test_thread_get_all(self):
        thread_repository = ThreadRepository()
        thread = Thread(users=[uuid4()], last_used_at=datetime.utcnow())
        thread_repository.threads.insert(0, thread)
        all_threads = thread_repository.get_all_threads()
        assert len(thread_repository.get_all_threads()) == 1
        assert all_threads[0].id == thread.id

    def test_thread_get_one(self):
        thread_repository = ThreadRepository()
        thread = Thread(users=[uuid4()], last_used_at=datetime.utcnow())
        thread_repository.threads.insert(0, thread)
        one_thread = thread_repository.get_thread(thread.id)
        assert one_thread.id == thread.id
