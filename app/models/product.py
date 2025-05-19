from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    origin = Column(String)  # Information about the origin of the product
    ingredients = Column(String)  # Comma-separated list of ingredients

    orders = relationship("Order", back_populates="product")
    packages = relationship(
        "Package",
        secondary="package_product_association",
        back_populates="products"
    )