from typing import List
from sqlalchemy.orm import Session

from fastapi import Depends, FastAPI, HTTPException

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost", "http://localhost:8080",
    "http://localhost:3000"
]

app = FastAPI()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# POSTS


@app.post("/user")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db=db, email=user.email)
    if(db_user):
        raise HTTPException(status_code=400, detail="User already exists.")
    return crud.create_user(db=db, user=user)


@app.post("/store")
def create_store(store: schemas.StoreCreate, db: Session = Depends(get_db)):
    db_store = crud.get_store_by_cnpj(db, cnpj=store.cnpj)
    if(db_store):
        raise HTTPException(status_code=400, detail="Store already exists.")
    return crud.create_store(db=db, store=store)


@app.post("/sale")
def create_sale(sale: schemas.SaleCreate, db: Session = Depends(get_db)):
    return crud.create_sale(db=db, sale=sale)


@app.post("/users_sales")
def create_user_sale(user_sale: schemas.UserSaleCreate, db: Session = Depends(get_db)):
    return crud.create_user_sale(db=db, user_sale=user_sale)


# GETS


@app.get("/sales")
def get_all_sales(db: Session = Depends(get_db)):
    sales = crud.get_all_sales(db=db)
    return sales


@app.get("/stores")
def get_all_stores(db: Session = Depends(get_db)):
    stores = crud.get_all_stores(db=db)
    return stores


@app.get("/user_sales")
def get_user_sales(user_search: schemas.UserSearchByEmail, db: Session = Depends(get_db)):
    users_sales = crud.get_user_sales(db=db, email=user_search.email)
    return users_sales


@app.get("/store_sales")
def get_user_sales(store_search: schemas.StoreSearchByCnpj, db: Session = Depends(get_db)):
    store_sales = crud.get_user_sales(db=db, cnpj=store_search.cnpj)
    return store_sales
