from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from admin.db_utils import approve_order_db, pause_order_db, continue_order_db
from auth.handlers import get_current_auth_user_info
from database.db import get_db
from orders.db_utils import get_orders_db
from schemas.user_schemas import UserInfo

router = APIRouter(
    tags=["admin"]
)


@router.get("/admin/orders", status_code=status.HTTP_200_OK)
def get_all_orders(
        user_info: UserInfo = Depends(get_current_auth_user_info),
        db: Session = Depends(get_db)
):
    return {
        "data": get_orders_db(db)
    }

@router.patch("/admin/orders/{id}/approve")
def approve_order(
        id: int,
        db: Session = Depends(get_db)
):
    approve_order_db(id, db)

@router.patch("/admin/orders/{id}/pause")
def pause_order(
        id: int,
        db: Session = Depends(get_db)
):
    pause_order_db(id, db)

@router.patch("/admin/orders/{id}/continue")
def continue_order(
        id: int,
        db: Session = Depends(get_db)
):
    continue_order_db(id, db)