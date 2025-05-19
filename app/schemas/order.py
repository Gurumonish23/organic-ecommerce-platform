from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OrderBase(BaseModel):
    product_id: int
    quantity: int
    total_price: float
    status: Optional[str] = "pending"

class OrderCreate(OrderBase):
    pass

class OrderUpdate(OrderBase):
    status: Optional[str] = None

class Order(OrderBase):
    id: int
    user_id: int
    order_date: datetime

    class Config:
        orm_mode = True

class OrderStatusUpdate(BaseModel):
    status: str