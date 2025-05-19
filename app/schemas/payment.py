from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PaymentBase(BaseModel):
    order_id: int
    amount: float
    payment_method: str
    status: Optional[str] = "pending"
    transaction_id: str

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(PaymentBase):
    status: Optional[str] = None

class Payment(PaymentBase):
    id: int
    payment_date: datetime

    class Config:
        orm_mode = True