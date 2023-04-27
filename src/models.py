from typing import Optional, List
from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


# class User(Base):
#     __tablename__ = "user_account"
#     id = mapped_column(Integer, primary_key=True)
#     name = mapped_column(String(30))
