from fastapi import FastAPI
from routers import router

app = FastAPI(title="Orders")

app.include_router(router, prefix="/api/v1/orders")  # tags=[""]
