from sqlalchemy.orm import Session
from app.repositories import order_repository
from app.schemas.order_schema import OrderCreate
from app.repositories.product_repository import increase_stock
import uuid
import httpx

# docker networkünde diğer servisimin yolu
 
INVOICE_SERVICE_URL = "http://case_invoice_module:9000/api/v1/invoices/"

def create_new_order(db: Session, order: OrderCreate):
    try:
        db_order = order_repository.create_order(db, order)
        
        invoice_created = create_invoice_for_order(db_order)
        if not invoice_created:
            compensate_order(db, db_order)
            raise Exception("We encountered an issue while processing your invoice. Please try again in a few moments, and if the issue persists, contact our support team for assistance.")

        db_order.status = 'completed'
        db.commit()
        
        return db_order
    except Exception as e:
        print(f"An error occurred while creating order: {e}", flush=True)
        db.rollback()
        raise Exception("We're sorry, but we're unable to process your order at the moment. Please check if the product(s) are still in stock and try again. If you continue to experience issues, feel free to reach out to our support team for assistance."
)


def create_invoice_for_order(order):

    invoice_data = {
        "order_id": order.order_id,
        "total_amount": float(order.total_amount),
        "details": {
            "customer_id": order.customer_id,
            "order_date": order.order_date.isoformat(),
            "order_items": [
                {
                    "product_uuid": item.product_uuid,
                    "quantity": item.quantity,
                    "unit_price": float(item.unit_price),
                    "tax_amount": float(item.tax_amount),
                    "discount": float(item.discount or 0),
                    "total_price": float(item.total_price)
                }
                for item in order.order_items
            ]
        }
    }
    try:
        response = httpx.post(INVOICE_SERVICE_URL, json=invoice_data)
        response.raise_for_status()     
        json_response = response.json()
        return json_response
    except httpx.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}",flush=True) 
        return False
    except ValueError as json_err:
        print(f"Error parsing JSON response: {json_err}",flush=True)
        print(f"Raw response content: {response.content}",flush=True)
        return False
    except Exception as err:
        print(f"An error occurred while creating invoice: {err}",flush=True)
        return False


def compensate_order(db: Session, order):
    try:
        # Siparişin durumunu güncelle
        order.status = 'cancelled'
        db.commit()
        
        # Ürün stoklarını geri artır
        for item in order.order_items:
            increase_stock(db, item.product_uuid, item.quantity) 
    except Exception as e:
        db.rollback()
        print(f"An error occurred during compensation: {e}",flush=True)

def get_single_order(db: Session, order_id: str):
    return order_repository.get_order(db, order_id)
