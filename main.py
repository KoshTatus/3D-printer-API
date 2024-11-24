from fastapi import FastAPI, APIRouter
from auth.handlers import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

from database.db import create_db
from orders.model_handlers import router as model_router
from orders.order_handlers import router as order_router
from printers.handlers import router as printer_router
from admin.handlers import router as admin_router

#create_db()

api_router = APIRouter(
    prefix="/api"
)

api_router.include_router(auth_router)
api_router.include_router(model_router)
api_router.include_router(order_router)
api_router.include_router(printer_router)
api_router.include_router(admin_router)

app = FastAPI(
    title="3D_Printer"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "http://localhost"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(api_router)