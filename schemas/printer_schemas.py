from pydantic import BaseModel, Field

from database.orm import Size


class PrinterCreate(BaseModel):
    name: str
    size: Size
    remainPlastic: int
    state: int = Field(default=1)

class PrinterModel(PrinterCreate):
    id: int