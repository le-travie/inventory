from datetime import date
from typing import Optional

from pydantic import BaseModel, UUID4


class TransferBase(BaseModel):
    asset_num: str
    descript: str
    qty: int
    current_loc: str
    new_loc: str
    reasons: str
    move_date: date
    moved_by: str


class NewTransferSchema(TransferBase):
    pass


class TransferEditSchema(TransferBase):
    __annotations__ = {
        key: Optional[value] for key, value in TransferBase.__annotations__items()
    }


class TransferSchema(TransferBase):
    id: UUID4

    class config:
        from_attributes = True
