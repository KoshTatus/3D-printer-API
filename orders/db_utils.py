from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from starlette import status

from database.orm import OrdersOrm, ModelsOrm
from orders.models_utils import delete_file
from schemas.model_schemas import ModelCreate, ModelModel
from schemas.order_schemas import OrderCreate, OrderModel


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
) -> int:
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

def get_model_by_file(
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
        model = ModelModel.model_validate(result, from_attributes=True)
        file = open(model.filepath, "rb")
        binary_file = file.read()
        return binary_file

def get_orders_db(
        db: Session
):
    query = text(f"""
                    SELECT * FROM orders
                """)
    result = db.execute(query).all()
    return [OrderModel.model_validate(row, from_attributes=True) for row in result]

def get_models_db(
        db: Session
):
    query = text(f"""
            SELECT * FROM models
        """)
    result = db.execute(query).all()
    return [ModelModel.model_validate(row, from_attributes=True) for row in result]


def get_user_orders_db(
        id: int,
        db: Session
):
    query = text(f"""
                    SELECT * FROM orders
                        WHERE orders.user_id = {id}
                """)
    result = db.execute(query).all()
    return [OrderModel.model_validate(row, from_attributes=True) for row in result]


def get_user_models_db(
        id: int,
        db: Session
):
    query = text(f"""
                SELECT * FROM models
                    WHERE models.user_id = {id}
            """)
    result = db.execute(query).all()
    return [ModelModel.model_validate(row, from_attributes=True) for row in result]

def delete_model_by_id(
        id: int,
        db: Session
):
    model = get_model_by_id(id, db)
    delete_file(model.filepath)
    query = text(f"""
                DELETE FROM models
                    WHERE models.id = {id}
            """)
    db.execute(query)
    db.commit()