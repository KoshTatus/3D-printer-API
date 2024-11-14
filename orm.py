import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database.db import Base


class GroupsOrm(Base):
    __tablename__ = "groups"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    canPrintWthtLimits: Mapped[bool]
    canPlaceOrder: Mapped[bool]
    canViewOrderQueue: Mapped[bool]
    canDeleteOrderFromQueue: Mapped[bool]
    canCreateGroup: Mapped[bool]
    canUpdateGroup: Mapped[bool]
    canManageOrder: Mapped[bool]
    canGiveGroup: Mapped[bool]
    canMonitorPrinting: Mapped[bool]
    canAddPrinter: Mapped[bool]
    canUpdatePrinter: Mapped[bool]

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
    queue_id: Mapped[int] = mapped_column(ForeignKey("queues.id"))
    createdAt: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow())
    status: Mapped[str] = mapped_column(default="В обработке")
    filepath: Mapped[str]
    occupancy: Mapped[float]
    notes: Mapped[str]

class QueuesOrm(Base):
    __tablename__ = "queues"
    id: Mapped[int] = mapped_column(primary_key=True)

