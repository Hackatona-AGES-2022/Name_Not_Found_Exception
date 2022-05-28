from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    email = Column(String, primary_key=True, index=True)
    password = Column(String, index=True)
    name = Column(String, index=True)
    photo_link = Column(String, index=True)


class Store(Base):
    __tablename__ = "stores"

    cnpj = Column(String, primary_key=True, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)
    name = Column(String, index=True)
    photo_link = Column(String, index=True)
    address = Column(String, index=True)
    description = Column(String, index=True)


class Sale(Base):
    __tablename__ = "sales"

    id = Column(String, primary_key=True, index=True)
    cnpj = Column(String, ForeignKey("stores.cnpj"))

    title = Column(String, index=True)
    target_amount = Column(Integer, index=True)
    expiration_date = Column(Date, index=True)
    current_amount = Column(Integer, index=True)
    target_price = Column(Float, index=True)
    default_price = Column(Float, index=True)
    photo_link = Column(String, index=True)
    status = Column(Boolean, index=True)


class UserSale(Base):
    __tablename__ = "users_sales"

    id = Column(String, primary_key=True, index=True)
    email = Column(String, ForeignKey("users.email"))
    cnpj = Column(String, ForeignKey("stores.cnpj"))

    amount_purchased = Column(Integer, index=True)
