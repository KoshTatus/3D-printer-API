from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from auth.jwt.base.config import JWTConfig
from auth.jwt.base.auth import JWTAuth
from auth.service import AuthService
from database.db import get_db
from schemas.user_schemas import UserForm
from database.utils import get_users

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

def get_auth_service():
    return AuthService(jwt_auth=JWTAuth(config=JWTConfig()))

@router.post("/register")
def register_user(
        user: UserForm,
        auth_service: AuthService = Depends(get_auth_service),
        db: Session = Depends(get_db)
):
    data = auth_service.register(user, db)
    return {"data" : data}

@router.get("/users")
def users(db: Session = Depends(get_db)):
    return get_users(db)

