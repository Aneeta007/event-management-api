from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EventBase(BaseModel):
    title: str
    location: str
    date: datetime
    is_open: Optional[bool] = True

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
