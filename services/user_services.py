from typing import Dict, List

import bcrypt
from pydantic import ValidationError

from data_schemas.user_schemas import UserEditSchema, UserSchema, NewUserSchema
from db.repositories import user_repo as Repo


def add_new_user(
    fname: str,
    lname: str,
    username: str,
    pwd: str,
    gender: str,
    role: str,
    title: str = None,
):
    try:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(pwd.encode("utf-8"), salt)

        new_user = NewUserSchema(
            fname=fname,
            lname=lname,
            username=username,
            pwd=hashed_password,
            gender=gender,
            role=role,
            title=title,
        )

        Repo.create_user(new_user)

    except ValidationError:
        print("Error user_services")


def edit_user(id: int, update: Dict[str]) -> None:
    try:
        update_data = UserEditSchema()
        update_data.model_validate(update)

        Repo.update_user(id, update_data)
    except ValidationError:
        print("Error user_services")
