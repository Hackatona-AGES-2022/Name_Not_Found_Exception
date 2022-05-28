from email.policy import default
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float
import uuid

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, index=True)
    password = Column(String, index=True)
    name = Column(String, index=True)
    photo_link = Column(String, default="", index=True)


class Store(Base):
    __tablename__ = "stores"

    cnpj = Column(String, primary_key=True, index=True)

    email = Column(String, index=True)
    password = Column(String, index=True)
    name = Column(String, index=True)
    photo_link = Column(String, default="", index=True)
    address = Column(String, index=True)
    description = Column(String, default="", index=True)


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String, ForeignKey("stores.cnpj"))

    title = Column(String, index=True)
    target_amount = Column(Integer, index=True)
    expiration_date = Column(String, index=True)
    current_amount = Column(Integer, default=0, index=True)
    target_price = Column(Float, index=True)
    default_price = Column(Float, index=True)
    photo_link = Column(String, default="", index=True)
    status = Column(Integer, default=1, index=True)


class UserSale(Base):
    __tablename__ = "users_sales"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"))
    sale_id = Column(String, ForeignKey("sales.id"))

    amount_purchased = Column(Integer, index=True)
