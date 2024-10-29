from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from schemas.user_schemas import UserCreate, UserForm
from database.utils import user_exist, get_users, add_user
from utils.password_hashing import hash_password

router = APIRouter(
    tags=["/auth"]
)

@router.post("/register")
def register_user(user: UserForm, db: Session = Depends(get_db)):
    if user_exist(user.email, db):
        raise HTTPException(status_code=400, detail="User with this email already exists")
    password_hash = hash_password(user.password)
    add_user(UserCreate(email=user.email, password_hash=password_hash), db)
    return {"data" : user.model_dump()}

@router.get("/users")
def users(db: Session = Depends(get_db)):
    return get_users(db)

