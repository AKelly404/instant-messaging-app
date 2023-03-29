from typing import List

from models.thread import Thread


class ThreadRepository:
    def __init__(self):
        self.threads: List[Thread] = []

    def add(self, thread: Thread):
        self.threads.append(thread)
