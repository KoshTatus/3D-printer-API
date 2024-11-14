import shutil
from pathlib import Path
from fastapi import UploadFile
from sqlalchemy.orm import Session
from orm import OrdersOrm
from schemas.order_schemas import OrderCreate

PATH = "./uploads/"

def add_order(order: OrderCreate, db: Session):
    new_order = OrdersOrm(**order.model_dump())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)


def save_upload_file(file: UploadFile, user_id: int) -> None:
    path = f"{PATH}/{user_id}_{file.filename}"
    try:
        with open(path, "wb+") as destination:
            destination.write(file.file.read())
    finally:
        file.file.close()
