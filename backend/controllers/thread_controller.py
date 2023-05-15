from uuid import UUID
from fastapi import FastAPI, status
from models.thread import Thread
from services.thread_service import ThreadService
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
thread_service = ThreadService()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/threads/{thread_id}")
def get_thread(thread_id: UUID):
    return thread_service.get_thread(thread_id)


@app.get("/threads/")
def get_threads():
    return thread_service.get_all_threads()


@app.post("/threads/", status_code=status.HTTP_201_CREATED)
def post_thread(thread: Thread):
    thread_service.create_thread(thread)
    return thread


@app.get("/threads/{thread_id}/messages")
def get_messages(thread_id: UUID):
    return thread_service.get_messages(thread_id)
