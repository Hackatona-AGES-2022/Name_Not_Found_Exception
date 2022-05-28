from typing import Union
from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str
    name: str
    photo_link: Union[str, None] = None


class UserAuthorization(BaseModel):
    email: str
    password: str


class StoreCreate(BaseModel):
    cnpj: str
    email: str
    password: str
    name: str
    photo_link: Union[str, None] = None
    address: str
    description: Union[str, None] = None


class StoreAuthorization(BaseModel):
    email: str
    password: str


class SaleCreate(BaseModel):
    cnpj: str
    title: str
    target_amount: int
    expiration_date: str
    target_price: float
    default_price: float
    photo_link: Union[str, None] = None


class UserSaleCreate(BaseModel):
    user_id: int
    sale_id: int
    amount_purchased: int


class User(UserCreate):
    id: int

    class Config:
        orm_mode = True


class Store(StoreCreate):
    pass


class Sale(SaleCreate):
    id: int

    class Config:
        orm_mode = True


class UserSale(UserSaleCreate):
    id: int

    class Config:
        orm_mode = True
