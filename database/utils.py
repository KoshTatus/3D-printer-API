from sqlalchemy import select
from sqlalchemy.orm import Session
from orm import UsersOrm
from schemas.user_schemas import UserCreate, UserModel


def user_exist(email: str, db: Session):
    res = db.execute(select(UsersOrm).where(UsersOrm.email == email)).all()
    print(res)
    return bool(len(res))

def get_users(db: Session):
    return [UserModel.model_validate(row, from_attributes=True) for row in db.execute(select(UsersOrm)).scalars().all()]

def add_user(user: UserCreate, db: Session):
    new_user = UsersOrm(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
