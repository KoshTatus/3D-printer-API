import datetime

from pydantic import BaseModel, Field, field_validator


class OrderForm(BaseModel):
    occupancy: float
    notes: str

    @field_validator("occupancy")
    @classmethod
    def occupancy_range(cls, occupancy: float):
        if 0 <= occupancy <= 1:
            return occupancy
        raise ValueError("occupancy should be in the range from 0 to 1 ")

class OrderCreate(OrderForm):
    filepath: str
    user_id: int
    #  queue_id: int

class OrderModel(OrderCreate):
    id: int
    createdAt: datetime.datetime
    status: str
