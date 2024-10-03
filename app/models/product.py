# app/models/product.py
from sqlalchemy import Column, String, Integer, DECIMAL
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.types import BINARY
import uuid
from app.models.base_model import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_uuid = Column(
        String(36), 
        unique=True,
        nullable=False,
    )
    name = Column(String(255), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    tax = Column(DECIMAL(5, 2), nullable=False)
    discount = Column(DECIMAL(5, 2), nullable=True)
    stock_quantity = Column(Integer, nullable=False)
