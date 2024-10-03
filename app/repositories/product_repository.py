from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product_schema import ProductCreate
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status
import uuid
from sqlalchemy.exc import NoResultFound
def get_product(db: Session, product_uuid: str):
    try:
        return db.query(Product).filter(Product.product_uuid == product_uuid).first()
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while retrieving the products. Please try again later."
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="There was an issue with your request. Please check the provided information and try again."
        )

def get_products(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(Product).offset(skip).limit(limit).all()
    except SQLAlchemyError as e: 
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while retrieving the products. Please try again later."
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="There was an issue with your request. Please check the provided information and try again."
        )

def create_product(db: Session, product: ProductCreate):
    try:
        db_product = Product(
            product_uuid=str(uuid.uuid4()),  
            **product.dict() 
        )
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product
    except SQLAlchemyError as e:
        db.rollback() 
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while creating the product. Please try again later."
        )
    except Exception as e: 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="There was an issue with your request. Please check the provided information and try again."
        )

def update_stock(db: Session, product_uuid: str, quantity: int):
    product = get_product(db, product_uuid)
    if product:
        product.stock_quantity -= quantity
        db.commit()
        db.refresh(product)
        return product
    return None


def increase_stock(db: Session, product_uuid: str, quantity: int):
    product = get_product(db, product_uuid)
    if product:
        product.stock_quantity += quantity
        db.commit()
        db.refresh(product)
        return product
    return None

def get_and_lock_product(db: Session, product_uuid: str):
    try:
        product = db.query(Product).filter(Product.product_uuid == product_uuid).with_for_update().one()
        return product
    except NoResultFound:
        return None
