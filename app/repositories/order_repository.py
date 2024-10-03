# app/repositories/order_repository.py
from sqlalchemy.orm import Session
from app.models.order import Order, OrderItem
from app.schemas.order_schema import OrderCreate
from app.repositories.product_repository import get_and_lock_product
import uuid

from decimal import Decimal
import uuid
from sqlalchemy.orm import Session

def create_order(db: Session, order: OrderCreate):
    try:
        # total_amount Decimal olarak başlatılmalı 
        total_amount = Decimal('0.00')

        db_order = Order(
            order_id=str(uuid.uuid4()),
            customer_id=order.customer_id,
            total_amount=total_amount 
        )
        db.add(db_order)

        for item in order.order_items:
            product = get_and_lock_product(db, item.product_uuid)
            if not product:
                raise Exception(f"Product {item.product_uuid} not found.")
            if product.stock_quantity < item.quantity:
                raise Exception(f"Product {product.name} is not available in sufficient quantity.")

            unit_price = Decimal(product.price) * (Decimal('1') - (Decimal(product.discount or 0) / Decimal('100')))
            tax_amount = unit_price * (Decimal(product.tax or 0) / Decimal('100'))

            total_price = (unit_price + tax_amount) * Decimal(item.quantity)

            total_amount += total_price

            order_item = OrderItem(
                order_item_id=str(uuid.uuid4()),
                order_id=db_order.order_id,
                product_uuid=product.product_uuid,
                quantity=item.quantity,
                unit_price=unit_price,
                tax_amount=tax_amount,
                discount=product.discount,
                total_price=total_price
            )
            db.add(order_item)

            product.stock_quantity -= item.quantity

        db_order.total_amount = total_amount

        db.commit()
        db.refresh(db_order)

        return db_order

    except Exception as e:
        db.rollback()
        raise e



def get_order(db: Session, order_id: str):
    try:
        order = db.query(Order).filter(Order.order_id == order_id).first()
        return order
    except Exception as e:
        print(f"An error occurred while retrieving the order: {e}")
        raise Exception("We encountered an issue while retrieving your order. Please try again later or contact our support team if the issue persists.")
