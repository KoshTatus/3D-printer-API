import datetime

from pydantic import BaseModel, field_validator, Field


class OrderForm(BaseModel):
    modelId: int
    printerId: int
    name: str
    occupancy: int = Field(title="Заполненность", default=0)
    createdAt: datetime.datetime = Field(default=datetime.datetime.utcnow())
    state: int = Field(default=0)

class OrderModel(OrderForm):
    id: int
    userId: int
