from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    nutritionist_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    appointment_time = Column(DateTime, nullable=False)
    status = Column(String, default="scheduled")  # e.g., "scheduled", "completed", "canceled"
    notes = Column(String)  # Any additional notes or details about the appointment

    customer = relationship("User", foreign_keys=[customer_id], back_populates="customer_appointments")
    nutritionist = relationship("User", foreign_keys=[nutritionist_id], back_populates="nutritionist_appointments")