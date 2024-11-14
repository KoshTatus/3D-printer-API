from fastapi import APIRouter, status, UploadFile, Depends
import shutil
from auth.handlers import get_current_auth_user_info
from orders.utils import save_upload_file
from schemas.user_schemas import UserInfo

router = APIRouter(
    tags=["models_upload"]
)


@router.post("/model/upload", status_code=status.HTTP_201_CREATED)
def upload_model(
        file: UploadFile,
        user_info: UserInfo = Depends(get_current_auth_user_info)
):
    save_upload_file(file, user_info.id)
    return {
        "status": "OK"
    }
