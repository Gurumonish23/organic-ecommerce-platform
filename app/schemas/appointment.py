from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AppointmentBase(BaseModel):
    appointment_time: datetime
    status: Optional[str] = "scheduled"
    notes: Optional[str] = None

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentUpdate(AppointmentBase):
    status: Optional[str] = None

class Appointment(AppointmentBase):
    id: int
    customer_id: int
    nutritionist_id: int

    class Config:
        orm_mode = True