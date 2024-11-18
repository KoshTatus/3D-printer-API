from sqlalchemy.orm import Session

from database.orm import OrdersOrm
from schemas.order_schemas import OrderCreate


def add_order(
        order: OrderCreate,
        db: Session
):
    new_order = OrdersOrm(**order.model_dump())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)