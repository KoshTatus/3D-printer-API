from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from auth.handlers import get_current_auth_user_info
from database.db import get_db
from orders.db_utils import add_model, add_order, get_model_by_id, get_models_db, get_model_by_file, get_user_models_db, \
    delete_model_by_id, get_user_orders_db, get_orders_db, get_order_by_id
from orders.models_utils import save_upload_file
from schemas.model_schemas import ModelCreate
from schemas.order_schemas import OrderForm
from schemas.user_schemas import UserInfo

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


# @router.post("/models/{model_id}/settings", status_code=status.HTTP_201_CREATED)
# def model_settings(
#         modelId: int,
#         form: OrderForm = Query(),
#         db: Session = Depends(get_db),
#         user_info: UserInfo = Depends(get_current_auth_user_info)
# ):
#     order = OrderCreate(
#             user_id=user_info.id,
#             queue_id=1,  # заглушка
#             model_id=modelId,
#             occupancy=form.occupancy,
#             notes=form.notes
#         )
#     add_order(
#         order,
#         db
#     )
#
#     return {
#         "OK" : "True"
#     }