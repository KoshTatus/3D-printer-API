from fastapi import FastAPI, APIRouter
from auth.handlers import router as auth_router

api_router = APIRouter(
    prefix="/api"
)

api_router.include_router(auth_router)

app = FastAPI(
    title="3D_Printer"
)
app.include_router(api_router)

