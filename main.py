import datetime

from models.message import Message

message = Message(text="banana", datetime=datetime.datetime.utcnow())

print(message.dict())
