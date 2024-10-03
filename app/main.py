from fastapi import FastAPI, status
from app.routers import order_router
from app.routers import product_router

app = FastAPI(
    title='Case Study Order Module',
    version='0.0.0.1',
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    docs_url="/api/v1/order-module/docs",
    openapi_url="/api/v1/order-module/openapi.json",
    redoc_url="/api/v1/order-module/redoc"
)

app.include_router(order_router.router, prefix="/api/v1/order", tags=["order"])
app.include_router(product_router.router, prefix="/api/v1/products", tags=["products"])