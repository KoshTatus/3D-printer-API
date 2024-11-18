from sqlalchemy import select
from sqlalchemy.orm import Session
from database.orm import UsersOrm
from schemas.user_schemas import UserCreate, UserModel
from utils.password_hashing import hash_password


def user_exist(email: str, db: Session):
    res = db.execute(select(UsersOrm).where(UsersOrm.email == email)).first()
    return True if res else False

def get_users(db: Session):
    return [UserModel.model_validate(row, from_attributes=True) for row in db.execute(select(UsersOrm)).scalars().all()]

def add_user(user: UserCreate, db: Session):
    new_user = UsersOrm(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

def get_user_id(email: str, db: Session):
    return db.execute(select(UsersOrm.id).where(UsersOrm.email == email)).scalars().first()

def get_user_by_id(id: int, db: Session):
    return UserModel.model_validate(
        db.execute(select(UsersOrm).where(UsersOrm.id == id)).scalars().first(),
        from_attributes=True
    )

def email_exist(email: str, db: Session):
    return True if db.execute(select(UsersOrm.email).where(UsersOrm.email == email)).scalars().first() else False

def password_exist(password: str, db: Session):
    password_hash = hash_password(password)
    return True if db.execute(select(UsersOrm.password_hash).where(UsersOrm.password_hash == password_hash)).scalars().first() else False