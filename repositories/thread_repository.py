from typing import List
from uuid import UUID

from models.thread import Thread


class ThreadRepository:
    def __init__(self):
        self.threads: List[Thread] = []

    def add(self, thread: Thread):
        self.threads.append(thread)

    def get_all_threads(self):
        return self.threads

    def get_thread(self, thread_id: UUID):
        return next(thread for thread in self.threads if thread.id == thread_id)

    #   Above next() code essentially operates as below
    #     for threads in self.threads:
    #         if threads.id == id:
    #             return threads

