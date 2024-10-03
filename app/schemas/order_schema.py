# app/schemas/order.py
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class OrderItemBase(BaseModel):
    product_uuid: str
    quantity: int

class OrderItemCreate(OrderItemBase):
    pass

class OrderItem(OrderItemBase):
    order_item_id: str
    unit_price: float
    tax_amount: float
    discount: Optional[float]
    total_price: float

    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    customer_id: int

class OrderCreate(OrderBase):
    order_items: List[OrderItemCreate]

class Order(OrderBase):
    order_id: str
    order_date: datetime
    total_amount: float
    status: str
    order_items: List[OrderItem] = []

    class Config:
        orm_mode = True
