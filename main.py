from typing import Union
from uuid import UUID
from fastapi import FastAPI, status

from models.thread import Thread
from services.thread_service import ThreadService

app = FastAPI()

thread_service = ThreadService()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/threads/{thread_id}")
def get_thread(thread_id: UUID):
    return thread_service.get_thread(thread_id)


@app.get("/threads/")
def get_threads():
    return thread_service.get_all_threads()


@app.post("/threads/", status_code=status.HTTP_201_CREATED)
def post_thread(thread: Thread):
    thread_service.create_thread(thread)
