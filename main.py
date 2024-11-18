from fastapi import FastAPI, APIRouter
from auth.handlers import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

from database.db import create_db
from orders.handlers import router as order_router

api_router = APIRouter(
    prefix="/api"
)

api_router.include_router(auth_router)
api_router.include_router(order_router)


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