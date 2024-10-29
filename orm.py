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
    id_group: Mapped[int] = mapped_column(ForeignKey("groups.id", ondelete="SET NULL"), nullable=True)
    name: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str]
    password_hash: Mapped[str]