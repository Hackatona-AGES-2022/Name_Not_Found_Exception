import email
from sqlalchemy.orm import Session

from . import models, schemas


def create_user(db: Session, user: schemas.UserCreate):
    created_user = models.User(
        email=user.email,
        password=user.password,
        name=user.name,
        photo_link=user.photo_link
    )
    db.add(created_user)
    db.commit()
    db.refresh(created_user)
    return created_user


def create_store(db: Session, store: schemas.StoreCreate):
    created_store = models.Store(
        cnpj=store.cnpj,
        email=store.email,
        password=store.password,
        name=store.name,
        photo_link=store.photo_link,
        address=store.address,
        description=store.description
    )
    db.add(created_store)
    db.commit()
    db.refresh(created_store)
    return created_store


def get_all_stores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Store).offset(skip).limit(limit).all()


def create_sale(db: Session, sale: schemas.SaleCreate):
    created_sale = models.Sale(
        cnpj=sale.cnpj,
        title=sale.title,
        target_amount=sale.target_amount,
        expiration_date=sale.expiration_date,
        target_price=sale.target_amount,
        default_price=sale.default_price,
        photo_link=sale.photo_link
    )
    db.add(created_sale)
    db.commit()
    db.refresh(created_sale)
    return created_sale


def create_user_sale(db: Session, user_sale: schemas.UserSaleCreate):
    created_user_sale = models.UserSale(
        email=user_sale.email,
        cnpj=user_sale.cnpj,
        amount_purchased=user_sale.amount_purchased
    )
    db.add(created_user_sale)
    db.commit()
    db.refresh(created_user_sale)
    return created_user_sale
