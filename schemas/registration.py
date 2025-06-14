from pydantic import BaseModel
from datetime import datetime

class RegistrationBase(BaseModel):
    user_id: int
    event_id: int

class RegistrationCreate(RegistrationBase):
    pass

class Registration(RegistrationBase):
    id: int
    registration_date: datetime
    attended: bool = False
