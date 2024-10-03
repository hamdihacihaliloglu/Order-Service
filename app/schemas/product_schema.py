# app/schemas/product.py
from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class ProductBase(BaseModel):
    name: str
    price: float
    tax: float
    discount: Optional[float] = 0.0
    stock_quantity: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    product_uuid: str

    class Config:
        orm_mode = True
