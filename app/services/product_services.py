# app/services/product_service.py
from sqlalchemy.orm import Session
from app.repositories import product_repository
from app.schemas.product_schema import ProductCreate
import uuid

def create_new_product(db: Session, product: ProductCreate):
    return product_repository.create_product(db, product)

def get_all_products(db: Session, skip: int = 0, limit: int = 100):
    return product_repository.get_products(db, skip, limit)

def get_single_product(db: Session, product_uuid: str):
    return product_repository.get_product(db, product_uuid)
