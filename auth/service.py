from fastapi import Depends
from sqlalchemy.orm import Session
from auth.errors import AuthErrors
from auth.jwt_auth.base.auth import JWTAuth
from database.utils import user_exist, add_user, get_user_id, email_exist, password_exist
from schemas.user_schemas import UserForm, UserCreate, UserModel
from utils.password_hashing import hash_password

class AuthService:
    def __init__(self, jwt_auth: JWTAuth):
        self.jwt_auth = jwt_auth

    def register(self, user: UserForm, db: Session):
        if user_exist(user.email, db):
            raise AuthErrors.get_email_occupied_error()
        add_user(
            UserCreate(
                email=user.email,
                password_hash=hash_password(user.password)
            ),
            db
        )
        token = self.jwt_auth.generate_token(
            payload={
                "id" : get_user_id(user.email, db),
                "group_id" : None,
            }
        )
        return token

    def login(self, user: UserForm, db: Session):
        if not email_exist(user.email, db):
            raise AuthErrors.get_email_not_found_error()
        if not password_exist(user.password, db):
            raise AuthErrors.get_password_not_found_error()

        token = self.jwt_auth.generate_token(
            payload={
                "id": get_user_id(user.email, db),
                "group_id": None,
            }
        )
        return token


