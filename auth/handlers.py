from fastapi import APIRouter, Depends, Response, HTTPException
from sqlalchemy.orm import Session
from auth.jwt_auth.base.config import JWTConfig
from auth.jwt_auth.base.auth import JWTAuth
from auth.service import AuthService
from database.db import get_db
from schemas.user_schemas import UserForm, UserModel
from database.utils import get_users, get_user_by_id
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt.exceptions import InvalidTokenError

http_bearer = HTTPBearer()

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
    return {"data": data}

@router.post("/login")
def register_user(
        user: UserForm,
        auth_service: AuthService = Depends(get_auth_service),
        db: Session = Depends(get_db)
):
    data = auth_service.login(user, db)
    return {"data": data}


@router.get("/users")
def users(db: Session = Depends(get_db)):
    return get_users(db)


def get_current_auth_user(
        credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
        auth_service: AuthService = Depends(get_auth_service),
        db: Session = Depends(get_db)
) -> UserModel:
    token = credentials.credentials
    try:
        payload = auth_service.jwt_auth.verify_token(token)
        id = payload["id"]
        user = get_user_by_id(id, db)

    except InvalidTokenError:
        raise HTTPException(
            status_code=400,
            detail="Invalid token!"
        )
    return user

@router.get("/test")
def auth_user_check(
        user: UserModel = Depends(get_current_auth_user)
):
    return user
