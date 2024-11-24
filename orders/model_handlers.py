from io import BytesIO
from typing import Annotated
from fastapi import APIRouter, status, UploadFile, Depends, Query, Header, Form
from sqlalchemy.orm import Session
from fastapi.responses import StreamingResponse
from auth.handlers import get_current_auth_user_info
from database.db import get_db
from orders.models_utils import save_upload_file
from schemas.model_schemas import ModelCreate
from schemas.user_schemas import UserInfo
from orders.db_utils import (
    add_model,
    get_model_by_id, get_models_db,
    get_model_by_file,
    delete_model_by_id
)

router = APIRouter(
    tags=["models"]
)


@router.post("/models", status_code=status.HTTP_201_CREATED)
def upload_model(
        name: Annotated[str, Form()],
        file: Annotated[UploadFile, Form()],
        user_info: UserInfo = Depends(get_current_auth_user_info),
        db: Session = Depends(get_db)
):
    path = save_upload_file(file)
    model_id = add_model(
        ModelCreate(
            user_id=user_info.id,
            filepath=path,
            name=name,
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
        "data": get_models_db(db)
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

