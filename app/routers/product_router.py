# app/routers/products.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import product_schema as product_schema
from app.services import product_services as product_service
from uuid import UUID
from app.dependencies import get_db

router = APIRouter()

@router.post("/", response_model=product_schema.Product)
def create_product(product: product_schema.ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_new_product(db, product)

@router.get("/", response_model=list[product_schema.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = product_service.get_all_products(db, skip, limit)
    return products

@router.get("/{product_uuid}", response_model=product_schema.Product)
def read_product(product_uuid: str, db: Session = Depends(get_db)):
    db_product = product_service.get_single_product(db, product_uuid)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
