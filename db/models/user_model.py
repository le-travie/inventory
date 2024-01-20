from enum import StrEnum

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from db.db_man import Base


class Gender(StrEnum):
    Male = "Male"
    Female = "Female"


class Role(StrEnum):
    Admin = "Admin"
    User = "User"


class UserModel(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    fname: Mapped[str] = mapped_column(String(50), nullable=False)
    lname: Mapped[str] = mapped_column(String(50), nullable=False)
    username: Mapped[str] = mapped_column(
        String(150), nullable=False, unique=True, index=True
    )
    pwd: Mapped[str] = mapped_column(String(255), nullable=False)
    gender: Mapped[Gender] = mapped_column(nullable=False)
    role: Mapped[Role] = mapped_column(nullable=False)
    title: Mapped[str] = mapped_column(String(50), nullable=True)
