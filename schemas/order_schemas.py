import datetime

from pydantic import BaseModel, field_validator, Field


class OrderForm(BaseModel):
    occupancy: int = Field(title="Заполненность", default=0)
    notes: str | None = Field(title="Заметки", default=None)

    @field_validator("occupancy")
    @classmethod
    def occupancy_range(cls, occupancy: int):
        if 0 <= occupancy <= 100:
            return occupancy
        raise ValueError("occupancy should be in the range from 0 to 100 ")

class OrderCreate(OrderForm):
    user_id: int
    queue_id: int
    model_id: int
    createdAt: datetime.datetime = Field(default=datetime.datetime.utcnow())
    status: str = Field(default="В обработке")
    occupancy: int
    notes: str | None

class OrderModel(OrderCreate):
    id: int
