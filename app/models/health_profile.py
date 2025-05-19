from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class HealthProfile(Base):
    __tablename__ = "health_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    age = Column(Integer, nullable=False)
    allergies = Column(String)  # Comma-separated list of allergies
    health_conditions = Column(String)  # Comma-separated list of health conditions

    user = relationship("User", back_populates="health_profile")