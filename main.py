from fastapi import FastAPI
from routers.auth import router as auth_router
from database.db import create_db


app = FastAPI(
    title="3D_Printer"
)

app.include_router(auth_router)

