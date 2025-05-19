from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.db.database import Base

# Association table for many-to-many relationship between packages and products
package_product_association = Table(
    'package_product_association',
    Base.metadata,
    Column('package_id', Integer, ForeignKey('packages.id')),
    Column('product_id', Integer, ForeignKey('products.id'))
)

class Package(Base):
    __tablename__ = "packages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    family_size = Column(Integer, nullable=False)  # e.g., 3, 4, or 5

    products = relationship(
        "Product",
        secondary=package_product_association,
        back_populates="packages"
    )