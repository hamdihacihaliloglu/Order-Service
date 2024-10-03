# app/routers/orders.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import order_schema as order_schema
from app.schemas import base_schema as base_schema
from app.services import order_services as order_service
from app.dependencies import get_db
from uuid import UUID

router = APIRouter()

@router.post("/", response_model=base_schema.ResponseWithMessage)
def create_order(order: order_schema.OrderCreate, db: Session = Depends(get_db)):
    try:
        order_service.create_new_order(db, order)
        return base_schema.ResponseWithMessage(status=True,message="Order created successfully")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{order_id}", response_model=order_schema.Order)
def read_order(order_id: UUID, db: Session = Depends(get_db)):
    try:
        db_order = order_service.get_single_order(db, order_id)
        if db_order is None:
            raise HTTPException(status_code=404, detail="Order not found")
        return db_order
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))