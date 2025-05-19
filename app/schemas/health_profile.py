from pydantic import BaseModel
from typing import Optional

class HealthProfileBase(BaseModel):
    age: int
    allergies: Optional[str] = None
    health_conditions: Optional[str] = None

class HealthProfileCreate(HealthProfileBase):
    pass

class HealthProfileUpdate(HealthProfileBase):
    pass

class HealthProfile(HealthProfileBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True