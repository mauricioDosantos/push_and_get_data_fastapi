from fastapi import HTTPException, Depends, FastAPI
from typing import List

from scheme.client import ClientUpdateScheme, Client as ClientScheme
from models.client import Client
from models.base import Base, engine, Session
from main.db.crud import (
    get_client, get_client_cpf_cnpj, get_clients,
    create_client, update_client, delete_client
)

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@app.get('/client/{client_id}', response_model=ClientScheme)
def get_client_(
    client_id: int,
    db: Session = Depends(get_db)
) -> ClientScheme:
    db_client = get_client(db, client_id) 
    if db_client is None:
        raise HTTPException(status_code=404, detail="client not found")
    return db_client


@app.post("/client/", response_model=ClientScheme)
def create_client_(
    _client: ClientScheme, db: Session = Depends(get_db)
) -> ClientScheme:
    db_client = get_client_cpf_cnpj(db, cpf_cnpj=_client.cpf_cnpj)
    if db_client:
        raise HTTPException(
            status_code=400, detail="CPF/CNPJ already registered"
        )
    return create_client(db=db, _client=_client)


@app.get("/clients/", response_model=List[ClientScheme])
def read_clients(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
) -> List[ClientScheme]:
    clients = get_clients(db, skip=skip, limit=limit)
    return clients


@app.delete('/client/{client_id}', response_model=ClientUpdateScheme)
def delete_clients(
    client_id: int, db: Session = Depends(get_db)
) -> ClientUpdateScheme:
    return delete_client(db, client_id)


@app.patch("/client/", response_model=ClientScheme)
def update_client_(
    _client: ClientUpdateScheme, db: Session = Depends(get_db)
) -> ClientScheme:
    result = update_client(db=db, client=_client)
    if result is None:
        raise HTTPException(status_code=404, detail="client not found")
    return ClientScheme.from_orm(result)
