from sqlalchemy import Column, Integer, DECIMAL, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import BINARY
import uuid
from datetime import datetime
from app.models.base_model import Base

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(
        String(36), 
        unique=True, 
        nullable=False,
    )
    customer_id = Column(Integer, nullable=False)
    order_date = Column(DateTime, default=datetime.now)
    total_amount = Column(DECIMAL(10, 2), nullable=False)
    status = Column(String(50), default='pending')

    order_items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_item_id = Column(
        String(36),
        unique=True, 
        nullable=False,
    )
    order_id = Column(String(36),ForeignKey("orders.order_id"))
    product_uuid = Column(String(36), ForeignKey("products.product_uuid"))
    quantity = Column(Integer, nullable=False)
    unit_price = Column(DECIMAL(10, 2), nullable=False)
    tax_amount = Column(DECIMAL(10, 2), nullable=False)
    discount = Column(DECIMAL(5, 2), nullable=True)
    total_price = Column(DECIMAL(10, 2), nullable=False)

    order = relationship("Order", back_populates="order_items")
