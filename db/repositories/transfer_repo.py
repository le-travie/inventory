from typing import List

from sqlalchemy import select, insert, update, delete
from pydantic import UUID4

from db.db_man import MasterSession
from data_schemas.transfer_schemas import (
    NewTransferSchema,
    TransferEditSchema,
    TransferSchema,
)
from db.models.asset_models import TransferModel as Transfer


def new_transfer(data: NewTransferSchema) -> None:
    session = MasterSession()
    query = insert(Transfer).values(data.model_dump(exclude_unset=True))
    with session as conn:
        conn.execute(query)
        conn.commit()


def all_transfers() -> List[TransferSchema]:
    session = MasterSession()
    query = select(Transfer)
    transfers = session.execute(query).all()
    session.close()

    return transfers


def get_transfer(transfer_id: UUID4) -> TransferSchema:
    session = MasterSession()
    query = select(Transfer).where(Transfer.id == transfer_id)
    results = session.scalar(query)
    return TransferSchema.model_validate(results)


def update_transfer(transfer_id: UUID4, update_data: TransferEditSchema) -> None:
    session = MasterSession()
    query = (
        update(Transfer)
        .where(Transfer.id == transfer_id)
        .values(**update_data.model_dump(exclude_unset=True))
    )
    with session as conn:
        conn.execute(query)
        conn.commit()


def delete_transfer(transfer_id: UUID4) -> None:
    session = MasterSession()
    query = delete(Transfer).where(Transfer.id == transfer_id)
    with session as conn:
        conn.execute(query)
        conn.commit()
