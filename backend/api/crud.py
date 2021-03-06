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


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


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


def get_store_by_cnpj(db: Session, cnpj: str):
    return db.query(models.Store).filter(models.Store.cnpj == cnpj).first()


def get_store_by_email(db: Session, email: str):
    return db.query(models.Store).filter(models.Store.email == email).first()


def get_all_stores(db: Session):
    return db.query(models.Store).all()


def create_sale(db: Session, sale: schemas.SaleCreate):
    created_sale = models.Sale(
        cnpj=sale.cnpj,
        title=sale.title,
        target_amount=sale.target_amount,
        expiration_date=sale.expiration_date,
        target_price=sale.target_price,
        default_price=sale.default_price,
        description=sale.description,
        photo_link=sale.photo_link
    )
    db.add(created_sale)
    db.commit()
    db.refresh(created_sale)
    return created_sale


def get_sale_by_id(db: Session, id: str):
    return db.query(models.Sale).filter(models.Sale.id == id).first()


def get_store_sales(db: Session, store_cnpj: str):
    return db.query(models.Sale, models.Store).filter(
        models.Sale.cnpj == store_cnpj
    ).join(
        models.Store,
        models.Store.cnpj == models.Sale.cnpj
    ).all()


def get_all_sales(db: Session):
    return db.query(models.Sale, models.Store).join(
        models.Store,
        models.Store.cnpj == models.Sale.cnpj
    ).all()


def create_user_sale(db: Session, user_sale: schemas.UserSaleCreate):
    created_user_sale = models.UserSale(
        user_id=user_sale.user_id,
        sale_id=user_sale.sale_id,
        amount_purchased=user_sale.amount_purchased
    )
    db.add(created_user_sale)
    db.commit()
    db.refresh(created_user_sale)
    return created_user_sale


def get_user_sales(db: Session, user_id: str):
    return db.query(
        models.UserSale,
        models.Sale,
        models.Store
    ).filter(
        models.UserSale.user_id == user_id
    ).join(
        models.Sale, models.Sale.id == models.UserSale.sale_id
    ).join(
        models.Store, models.Store.cnpj == models.Sale.cnpj
    ).all()
