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

@app.get("/")
async def read_root():
    item = {"Hello": "World"}
    return item

@app.post("/user")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user_email=user.email)
    if(db_user):
        raise HTTPException(status_code=400, detail="user já existe")
    return crud.create_user(db=db, user=db_user)

@app.post("/store")
def create_store(store: schemas.StoreCreate, db: Session = Depends(get_db)):
    db_store = crud.get_store_by_cnpj(db, store_cnpj=store.cnpj)
    if(db_store):
        raise HTTPException(status_code=400, detail="store já existe")
    return crud.create_store(db=db, store=db_store)

@app.post("/sale")
def create_sale(sale: schemas.SaleCreate, db: Session = Depends(get_db)):
    db_store = crud.get_store_by_id(db, sale_id=sale.id)
    if(db_store):
        raise HTTPException(status_code=400, detail="sale já existe")
    return crud.create_sale(db=db, sale=db_store)

@app.post("/users_sales")
def create_users_sales(users_sales: schemas.Users_salesCreate, db: Session = Depends(get_db)):
    db_users_sales = crud.get_users_sales_by_id(db, users_sales_id=users_sales.id)
    if(db_users_sales):
        raise HTTPException(status_code=400, detail="users_sales já existe")
    return crud.create_users_sales(db=db, users_sales=db_users_sales)

@app.get("/users", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/sales", response_model=List[schemas.Sales])
def read_sales(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sales = crud.get_sales(db, skip=skip, limit=limit)
    return sales

@app.get("/stores", response_model=List[schemas.User])
def read_stores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stores = crud.get_stores(db, skip=skip, limit=limit)
    return stores


@app.get("/user_sale", response_model=List[schemas.Users_sales])
def read_users_sales(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users_sales = crud.get_users_sales(db, skip=skip, limit=limit)
    return users_sales


#########################################################

@app.post("/turmas", response_model=schemas.Turma)
def create_turmas(turma: schemas.TurmaCreate, db: Session = Depends(get_db)):
    db_turma = crud.get_turma_by_num_turma(db, num_turma=turma.num_turma)
    if db_turma:
        raise HTTPException(status_code=400, detail="Turma já existe")
    return crud.create_turma(db=db, turma=turma)

@app.get("/turmas", response_model=List[schemas.Turma])
def read_turmas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    turmas = crud.get_turmas(db, skip=skip, limit=limit)
    return turmas


@app.post("/sale/{preco}", response_model=schemas.Aluno)
def create_alunos(aluno: schemas.AlunoCreate, db: Session = Depends(get_db)):
    db_aluno = crud.get_aluno_by_matricula(db, matricula=aluno.matricula)
    if db_aluno:
        raise HTTPException(status_code=400, detail="Aluno já existe")
    return crud.create_aluno(db=db, aluno=aluno)

@app.get("/alunos", response_model=List[schemas.Aluno])
def read_turmas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    alunos = crud.get_alunos(db, skip=skip, limit=limit)
    return alunos


@app.post("/horarios", response_model=schemas.Horario)
def create_horarios(horario: schemas.HorarioCreate, db: Session = Depends(get_db)):
    db_horario = crud.get_horario_by_dia_semana(db, dia_semana=horario.dia_semana)
    if db_horario:
        raise HTTPException(status_code=400, detail="Horário já existe")
    return crud.create_horario(db=db, horario=horario)

@app.get("/horarios", response_model=List[schemas.Horario])
def read_horarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    horarios = crud.get_horarios(db, skip=skip, limit=limit)
    return horarios