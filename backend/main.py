from typing import Union
from uuid import UUID
from fastapi import FastAPI, status

from models.thread import Thread
from services.thread_service import ThreadService


