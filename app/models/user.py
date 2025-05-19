from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    role = Column(String, nullable=False)  # e.g., "customer", "nutritionist", "admin"

    health_profile = relationship("HealthProfile", uselist=False, back_populates="user")
    orders = relationship("Order", back_populates="user")
    customer_appointments = relationship("Appointment", foreign_keys="[Appointment.customer_id]", back_populates="customer")
    nutritionist_appointments = relationship("Appointment", foreign_keys="[Appointment.nutritionist_id]", back_populates="nutritionist")
    analytics = relationship("AnalyticsData", back_populates="user")
    activities = relationship("UserActivity", back_populates="user")