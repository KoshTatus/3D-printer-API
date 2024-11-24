from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from auth.handlers import get_current_auth_user_info
from database.db import get_db
from schemas.order_schemas import OrderForm
from schemas.user_schemas import UserInfo
from orders.db_utils import (
    add_order,
    get_user_orders_db,
    get_orders_db,
    get_order_by_id
)

router = APIRouter(
    tags=["orders"]
)

@router.get("/orders", status_code=status.HTTP_200_OK)
def get_user_orders(
        user_info: UserInfo = Depends(get_current_auth_user_info),
        db: Session = Depends(get_db)
):
    return {
        "data": get_user_orders_db(
            user_info.id,
            db
        )
    }

@router.post("/orders", status_code=status.HTTP_201_CREATED)
def create_order(
        order: OrderForm,
        user_info: UserInfo = Depends(get_current_auth_user_info),
        db: Session = Depends(get_db)
):
    order_id = add_order(order, user_info.id, db)

    return {
        "data" : get_order_by_id(order_id, db)
    }

@router.get("/orders/all", status_code=status.HTTP_200_OK)
def get_all_orders(
        user_info: UserInfo = Depends(get_current_auth_user_info),
        db: Session = Depends(get_db)
):
    return {
        "data": get_orders_db(db)
    }
