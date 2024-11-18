from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from starlette import status

from database.orm import OrdersOrm, ModelsOrm
from schemas.model_schemas import ModelCreate, ModelModel
from schemas.order_schemas import OrderCreate


def add_order(
        order: OrderCreate,
        db: Session
):
    new_order = OrdersOrm(**order.model_dump())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

def add_model(
        model: ModelCreate,
        db: Session
):
    new_model = ModelsOrm(**model.model_dump())
    db.add(new_model)
    db.commit()
    db.refresh(new_model)
    return new_model.id

def get_model_by_id(
        id: int,
        db: Session
):
    query = text(f"""
        SELECT * FROM models
            WHERE models.id = {id};
    """)
    result = db.execute(query).first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Model not found!")
    else:
        return ModelModel.model_validate(result, from_attributes=True)
