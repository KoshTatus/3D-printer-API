import datetime

from pydantic import BaseModel, Field


class ModelCreate(BaseModel):
    user_id: int
    filepath: str
    createdAt: datetime.datetime = Field(default=datetime.datetime.utcnow())

class ModelModel(ModelCreate):
    id: int