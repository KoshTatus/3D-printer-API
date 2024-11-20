import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database.db import Base


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
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    model_id: Mapped[int] = mapped_column(ForeignKey("models.id"))
    name: Mapped[str]
    createdAt: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow())
    state: Mapped[str] = mapped_column(default="В обработке")
    occupancy: Mapped[int]
    notes: Mapped[str | None]

class ModelsOrm(Base):
    __tablename__ = "models"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    filepath: Mapped[str]
    name: Mapped[str]
    uploadedAt: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow())

