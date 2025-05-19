from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AnalyticsData(BaseModel):
    id: int
    user_id: int
    action: str
    timestamp: datetime
    details: Optional[str] = None

    class Config:
        orm_mode = True

class SalesAnalytics(BaseModel):
    id: int
    product_id: int
    total_sales: int
    revenue: float
    last_updated: datetime

    class Config:
        orm_mode = True

class UserActivity(BaseModel):
    id: int
    user_id: int
    activity_type: str
    activity_time: datetime

    class Config:
        orm_mode = True