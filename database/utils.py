from sqlalchemy import select
from sqlalchemy.orm import Session
from orm import UsersOrm
from schemas.user_schemas import UserCreate, UserModel


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