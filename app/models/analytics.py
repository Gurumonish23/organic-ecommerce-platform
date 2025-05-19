from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime

class AnalyticsData(Base):
    __tablename__ = "analytics_data"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    action = Column(String, nullable=False)  # e.g., "purchase", "browse", "login"
    timestamp = Column(DateTime, default=datetime.utcnow)
    details = Column(String)  # JSON string or any additional details about the action

    user = relationship("User", back_populates="analytics")

class SalesAnalytics(Base):
    __tablename__ = "sales_analytics"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    total_sales = Column(Integer, default=0)
    revenue = Column(Float, default=0.0)
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    product = relationship("Product", back_populates="sales_analytics")

class UserActivity(Base):
    __tablename__ = "user_activity"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    activity_type = Column(String, nullable=False)  # e.g., "login", "purchase"
    activity_time = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="activities")