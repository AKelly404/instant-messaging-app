from uuid import UUID
from fastapi import FastAPI, status
from services.thread_service import ThreadService
from models.message import Message
from services.thread_service import ThreadService

app = FastAPI()
thread_service = ThreadService()


@app.post("/send/", status_code=status.HTTP_200_OK)
def send_message(message: Message):
    thread_service.create_message(message)
