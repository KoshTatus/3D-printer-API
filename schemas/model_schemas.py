import datetime

from fastapi import UploadFile
from pydantic import BaseModel, Field

class ModelForm(BaseModel):
    file: UploadFile
    name: str

class ModelCreate(BaseModel):
    user_id: int
    filepath: str
    name: str
    uploadedAt: datetime.datetime = Field(default_factory=lambda: datetime.datetime.utcnow())


class ModelModel(ModelCreate):
    id: int
    deleted: bool
