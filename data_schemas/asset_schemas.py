from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class AssetBase(BaseModel):
    asset_num: str
    descript: str
    location: str
    remarks: Optional[str]
    mod_by: str


class NewAssetSchema(AssetBase):
    pass


class AssetEditSchema(AssetBase):
    __annotations__ = {
        key: Optional[value] for key, value in AssetBase.__annotations__.items()
    }


class AssetSchema(AssetBase):
    id: int
    date_in: datetime
    mod_date: datetime

    class config:
        from_attributes = True
