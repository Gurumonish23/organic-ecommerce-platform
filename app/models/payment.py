from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    amount = Column(Float, nullable=False)
    payment_method = Column(String, nullable=False)  # e.g., "credit_card", "paypal"
    status = Column(String, default="pending")  # e.g., "pending", "completed", "failed"
    transaction_id = Column(String, unique=True, nullable=False)
    payment_date = Column(DateTime, default=datetime.utcnow)

    order = relationship("Order", back_populates="payments")