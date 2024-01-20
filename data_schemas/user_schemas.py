from typing import Optional

from pydantic import BaseModel

from db.models import user_model


class UserBase(BaseModel):
    fname: str
    lname: str
    username: str
    pwd: str
    gender: user_model.Gender
    role: user_model.Role
    title: Optional[str]


class NewUserSchema(UserBase):
    pass


class UserEditSchema(UserBase):
    __annotations__ = {
        key: Optional[value] for key, value in UserBase.__annotations__.items()
    }


class UserSchema(UserBase):
    id: int

    class config:
        from_attributes = True
