from datetime import datetime, date
from uuid import uuid4
from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey, Date
from sqlalchemy.dialects.postgresql import UUID

from db.db_man import Base


class AssetModel(Base):
    __tablename__ = "assets"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    asset_num: Mapped[str] = mapped_column(
        String(45), nullable=False, unique=True, index=True
    )
    desc: Mapped[str] = mapped_column(String(240), nullable=False)
    location: Mapped[str] = mapped_column(Text, nullable=False)
    remarks: Mapped[str] = mapped_column(Text, nullable=True)
    date_in: Mapped[datetime] = mapped_column(default=datetime.utcnow, nullable=False)
    mod_date: Mapped[datetime] = mapped_column(default=datetime.utcnow, nullable=False)
    mod_by: Mapped[str] = mapped_column(String(150), nullable=False)

    transfers: Mapped[List["TransferModel"]] = relationship(back_populates="asset")


class TransferModel(Base):
    __tablename__ = "transfers"
    id: Mapped[uuid4] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid4, index=True
    )
    asset_num: Mapped[str] = mapped_column(
        String(45),
        ForeignKey("assets.asset_num", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    desc: Mapped[str] = mapped_column(String(240), nullable=True)
    qty: Mapped[int] = mapped_column(nullable=False)
    current_loc: Mapped[str] = mapped_column(Text, nullable=False)
    new_loc: Mapped[str] = mapped_column(Text, nullable=False)
    reasons: Mapped[str] = mapped_column(Text, nullable=False)
    move_date: Mapped[date] = mapped_column(Date, nullable=False)
    moved_by: Mapped[str] = mapped_column(String(150), nullable=False)

    asset: Mapped[AssetModel] = relationship(back_populates="transfers")
