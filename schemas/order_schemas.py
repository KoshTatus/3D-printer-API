import datetime

from pydantic import BaseModel, field_validator, Field


class OrderForm(BaseModel):
    modelId: int
    printerId: int
    name: str
    occupancy: int = Field(title="Заполненность", default=0)

    @field_validator("occupancy")
    @classmethod
    def occupancy_range(cls, occupancy: int):
        if 0 <= occupancy <= 100:
            return occupancy
        raise ValueError("occupancy should be in the range from 0 to 100 ")

class OrderModel(OrderForm):
    id: int
    userId: int
    createdAt: datetime.datetime = Field(default=datetime.datetime.utcnow())
    state: int = Field(default=0)