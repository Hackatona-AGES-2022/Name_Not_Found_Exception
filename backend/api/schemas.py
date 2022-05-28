from typing import Union
from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str
    name: str
    photo_link: Union[str, None] = None


class UserSearchByEmail(BaseModel):
    email: str


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


class StoreSearchByCnpj(BaseModel):
    cnpj: str


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
    email: str
    cnpj: str
    amount_purchased: int


class User(UserCreate):
    pass


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
