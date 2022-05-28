from typing import List
from sqlalchemy.orm import Session

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost", "http://localhost:8080",
    "http://localhost:3000"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists.")
    return crud.create_user(db=db, user=user)


@app.post("/user/authorization")
def user_authorization(auth: schemas.UserAuthorization, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db=db, email=auth.email)
    if db_user:
        if db_user.password == auth.password:
            return {
                "email": db_user.email,
                "name": db_user.name,
                "photo_link": db_user.photo_link
            }
        raise HTTPException(status_code=400, detail="Wrong password.")
    raise HTTPException(status_code=400, detail="E-mail does not exist.")


@app.post("/store")
def create_store(store: schemas.StoreCreate, db: Session = Depends(get_db)):
    db_store = crud.get_store_by_cnpj(db, cnpj=store.cnpj)
    if db_store:
        raise HTTPException(status_code=400, detail="Store already exists.")
    return crud.create_store(db=db, store=store)


@app.post("/store/authorization")
def store_authorization(auth: schemas.StoreAuthorization, db: Session = Depends(get_db)):
    db_store = crud.get_store_by_email(db=db, email=auth.email)
    if db_store:
        if db_store.password == auth.password:
            return {
                "cnpj": db_store.cnpj,
                "email": db_store.email,
                "name": db_store.name,
                "photo_link": db_store.photo_link,
                "address": db_store.address,
                "description": db_store.description,
            }
        raise HTTPException(status_code=400, detail="Wrong password.")
    raise HTTPException(status_code=400, detail="E-mail does not exist.")


@app.post("/sale")
def create_sale(sale: schemas.SaleCreate, db: Session = Depends(get_db)):
    return crud.create_sale(db=db, sale=sale)


@app.post("/user_sale")
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


@app.get("/user_sales/{user_id}")
def get_user_sales(user_id, db: Session = Depends(get_db)):
    users_sales = crud.get_user_sales(db=db, user_id=user_id)
    return users_sales


@app.get("/store_sales/{store_cnpj}")
def get_store_sales(store_cnpj, db: Session = Depends(get_db)):
    store_sales = crud.get_store_sales(db=db, store_cnpj=store_cnpj)
    return store_sales
