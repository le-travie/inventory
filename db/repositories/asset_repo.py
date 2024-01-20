from typing import List

from sqlalchemy import select, insert, update, delete

from db.db_man import MasterSession
from db.models.asset_models import AssetModel as Asset
from data_schemas.asset_schemas import NewAssetSchema, AssetEditSchema, AssetSchema


def new_asset(new_asset: NewAssetSchema) -> None:
    session = MasterSession()
    query = insert(Asset).values(**new_asset.model_dump(exclude_unset=True))
    with session as conn:
        conn.execute(query)
        conn.commit()


def all_assets(offset: int = 0, limit: int = 50) -> List[AssetSchema]:
    session = MasterSession()
    query = select(Asset).offset(offset).limit(limit).order_by(Asset.date_in.desc())
    results = session.scalars(query).all()
    session.close()
    return [AssetSchema.model_validate(result) for result in results]


def get_asset(asset_id: int) -> AssetSchema:
    session = MasterSession()
    query = select(Asset).where(Asset.id == asset_id)
    result = session.scalar(query)
    session.close()
    return AssetSchema.model_validate(result)


def update_asset(asset_id: int, update_data: AssetEditSchema) -> None:
    session = MasterSession()
    query = (
        update(Asset)
        .where(Asset.id == asset_id)
        .values(**update_data.model_dump(exclude_unset=True, exclude_none=True))
    )
    with session as conn:
        conn.execute(query)
        conn.commit()


def delete_asset(asset_id: int) -> None:
    session = MasterSession()
    query = delete(Asset).where(Asset.id == asset_id)
    with session as conn:
        conn.execute(query)
        conn.commit()


def search_asset(search_term: str, column: str) -> List[AssetSchema]:
    session = MasterSession()
    query = select(Asset).where(getattr(Asset, column).like(f"%{search_term}%"))
    results = session.scalars(query).all()
    session.close()
    return results
