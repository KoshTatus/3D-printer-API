from fastapi import APIRouter, status, UploadFile, Depends, Query
from sqlalchemy.orm import Session
from auth.handlers import get_current_auth_user_info
from database.db import get_db
from orders.db_utils import add_model, add_order, get_model_by_id
from orders.models_utils import save_upload_file
from schemas.model_schemas import ModelCreate
from schemas.order_schemas import OrderForm, OrderCreate
from schemas.user_schemas import UserInfo

router = APIRouter(
    tags=["models_upload"]
)


@router.post("/models", status_code=status.HTTP_201_CREATED)
def upload_model(
        file: UploadFile,
        user_info: UserInfo = Depends(get_current_auth_user_info),
        db: Session = Depends(get_db)
):
    path = save_upload_file(file)
    model_id = add_model(
        ModelCreate(
            user_id=user_info.id,
            filepath=path
        ),
        db
    )

    return {
        "body" : path,
        "model_id" : model_id
    }


@router.get("/models/{model_id}/settings", status_code=status.HTTP_200_OK)
def model_settings(
        model_id: int,
        db: Session = Depends(get_db),
        user_info: UserInfo = Depends(get_current_auth_user_info)
):
    return get_model_by_id(model_id, db)

@router.post("/models/{model_id}/settings", status_code=status.HTTP_201_CREATED)
def model_settings(
        model_id: int,
        form: OrderForm = Query(),
        db: Session = Depends(get_db),
        user_info: UserInfo = Depends(get_current_auth_user_info)
):
    order = OrderCreate(
            user_id=user_info.id,
            queue_id=1,  # заглушка
            model_id=model_id,
            occupancy=form.occupancy,
            notes=form.notes
        )
    add_order(
        order,
        db
    )

    return {
        "OK" : "True"
    }