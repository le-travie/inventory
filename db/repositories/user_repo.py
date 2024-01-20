from typing import List

from sqlalchemy import insert, update, delete, select
from pydantic import ValidationError


from db.db_man import MasterSession
from db.models.user_model import UserModel as User
from data_schemas.user_schemas import NewUserSchema, UserEditSchema, UserSchema


def create_user(new_user: NewUserSchema) -> None:
    query = insert(User).values(
        **new_user.model_dump(exclude_unset=True, exclude_none=None)
    )
    session = MasterSession()
    with session as conn:
        conn.execute(query)
        conn.commit()


def all_users() -> List[UserSchema]:
    query = select(User)
    session = MasterSession()
    users = session.execute(query).all()
    session.close()

    return users


def get_user(username: str) -> UserSchema:
    session = MasterSession()
    try:
        query = select(User).where(User.username == username)
        results = session.scalar(query)
        user = UserSchema.model_validate(results)
    except ValidationError:
        raise ValueError("No valid user!")
    except Exception as e:
        raise ValueError(e)

    return user


def update_user(user_id: int, update_data: UserEditSchema) -> None:
    session = MasterSession()
    query = (
        update(User)
        .where(User.id == user_id)
        .values(**update_data.model_dump(exclude_unset=True, exclude_none=True))
    )
    with session as conn:
        conn.execute(query)
        conn.commit()


def delete_user(user_id: int) -> None:
    session = MasterSession()
    query = delete(User).where(User.id == user_id)
    with session as conn:
        conn.execute(query)
        conn.commit()
