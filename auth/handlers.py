from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from auth.jwt_auth.base.config import JWTConfig
from auth.jwt_auth.base.auth import JWTAuth
from auth.service import AuthService
from auth.jwt_auth.utils import try_to_decode_token
from database.db import get_db
from schemas.user_schemas import UserForm, UserInfo
from auth.utils import get_users
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

http_bearer = HTTPBearer()

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


def get_auth_service():
    return AuthService(jwt_auth=JWTAuth(config=JWTConfig()))

def get_current_auth_user_info(
        credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
        auth_service: AuthService = Depends(get_auth_service),
) -> UserInfo:
    token = credentials.credentials
    payload = try_to_decode_token(auth_service.jwt_auth, token)
    result = UserInfo(
        id=payload.get("id"),
        group_id=payload.get("group_id")
    )

    return result

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(
        user: UserForm,
        auth_service: AuthService = Depends(get_auth_service),
        db: Session = Depends(get_db)
):
    data = auth_service.register(user, db)
    return {
        "data" : {
            "token": data
        }
    }


@router.post("/login", status_code=status.HTTP_200_OK)
def login_user(
        user: UserForm,
        auth_service: AuthService = Depends(get_auth_service),
        db: Session = Depends(get_db)
):
    data = auth_service.login(user, db)
    return {
        "data" : {
            "token": data
        }
    }


@router.get("/users")
def users(db: Session = Depends(get_db)):
    return get_users(db)

@router.get("/test")
def auth_user_check(
        user: UserInfo = Depends(get_current_auth_user_info)
):
    return user
