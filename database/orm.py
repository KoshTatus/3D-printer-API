import datetime
from dataclasses import dataclass

from pydantic import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, composite
from database.db import Base


@dataclass
class Size:
    width: int
    length: int
    heigth: int

class GroupsOrm(Base):
    __tablename__ = "groups"
    id: Mapped[int] = mapped_column(primary_key=True)
    isAdmin: Mapped[bool]

class UsersOrm(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id", ondelete="SET NULL"), nullable=True)
    name: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str]
    password_hash: Mapped[str]

class OrdersOrm(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    userId: Mapped[int] = mapped_column(ForeignKey("users.id"), name="user_id")
    modelId: Mapped[int] = mapped_column(ForeignKey("models.id"), name="model_id")
    printerId: Mapped[int] = mapped_column(ForeignKey("printers.id"), name="printer_id")
    name: Mapped[str]
    occupancy: Mapped[int]
    createdAt: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow(), name="created_at")
    state: Mapped[int] = mapped_column(default=0)

class ModelsOrm(Base):
    __tablename__ = "models"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    filepath: Mapped[str]
    name: Mapped[str]
    uploadedAt: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow())
    deleted: Mapped[bool] = mapped_column(default=False)

class PrintersOrm(Base):
    __tablename__ = "printers"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    size: Mapped[Size] = composite(
        mapped_column("width"),
        mapped_column("length"),
        mapped_column("heigth")
    )
    remainPlastic: Mapped[int]
    state: Mapped[int]
