from io import BytesIO
from typing import Annotated

from fastapi import APIRouter, status, UploadFile, Depends, Query, Header
from sqlalchemy.orm import Session
from starlette.responses import StreamingResponse

from auth.handlers import get_current_auth_user_info
from database.db import get_db
from orders.db_utils import add_model, add_order, get_model_by_id, get_models_db, get_model_by_file, get_user_models_db, \
    delete_model_by_id
from orders.models_utils import save_upload_file
from schemas.model_schemas import ModelCreate
from schemas.order_schemas import OrderForm, OrderCreate
from schemas.user_schemas import UserInfo

router = APIRouter(
    tags=["models"]
)


@router.post("/models", status_code=status.HTTP_201_CREATED)
def upload_model(
        name: Annotated[str | None, Header()],
        file: UploadFile,
        user_info: UserInfo = Depends(get_current_auth_user_info),
        db: Session = Depends(get_db)
):
    path = save_upload_file(file)
    model_id = add_model(
        ModelCreate(
            user_id=user_info.id,
            filepath=path,
            name=name
        ),
        db
    )

    return {
        "data": get_model_by_id(model_id, db)
    }


@router.get("/models", status_code=status.HTTP_200_OK)
def get_user_models(
        user_info: UserInfo = Depends(get_current_auth_user_info),
        db: Session = Depends(get_db)
):
    return {
        "data": get_user_models_db(
            user_info.id,
            db
        )
    }


@router.get("/models/all", status_code=status.HTTP_200_OK)
def get_all_models(
        user_info: UserInfo = Depends(get_current_auth_user_info),
        db: Session = Depends(get_db)
):
    return {
        "data": get_models_db(db)
    }


@router.get("/models/{id}/file", status_code=status.HTTP_200_OK)
def model_file(
        id: int,
        db: Session = Depends(get_db),
        user_info: UserInfo = Depends(get_current_auth_user_info)
):
    memfile = BytesIO(get_model_by_file(id, db))
    response = StreamingResponse(memfile, media_type='application/octet-stream')

    return response


@router.delete("/models/{id}", status_code=status.HTTP_200_OK)
def delete_model(
        id: int,
        db: Session = Depends(get_db),
        user_info: UserInfo = Depends(get_current_auth_user_info)
):
    delete_model_by_id(id, db)

# @router.get("/models/{model_id}/settings", status_code=status.HTTP_200_OK)
# def model_settings(
#         model_id: int,
#         db: Session = Depends(get_db),
#         user_info: UserInfo = Depends(get_current_auth_user_info)
# ):
#     return get_model_by_id(model_id, db)
#
# @router.post("/models/{model_id}/settings", status_code=status.HTTP_201_CREATED)
# def model_settings(
#         model_id: int,
#         form: OrderForm = Query(),
#         db: Session = Depends(get_db),
#         user_info: UserInfo = Depends(get_current_auth_user_info)
# ):
#     order = OrderCreate(
#             user_id=user_info.id,
#             queue_id=1,  # заглушка
#             model_id=model_id,
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
