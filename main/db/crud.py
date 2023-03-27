from sqlalchemy.orm import Session
from sqlalchemy import update, delete
from models.client import Client
from scheme.client import ClientUpdateScheme, Client as ClientScheme
from models.base import engine


def get_client(db: Session, client_id: int):
    result = db.query(Client).filter(Client.id == client_id).first()
    return result


def get_client_cpf_cnpj(db: Session, cpf_cnpj: str):
    result = db.query(Client).filter(Client.cpf_cnpj == cpf_cnpj).first()
    return result


def get_clients(db: Session, skip: int = 0, limit: int = 100):
    result = db.query(Client).offset(skip).limit(limit).all()
    return result


def create_client(db: Session, _client: ClientScheme):
    db_client = Client(**_client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def update_client(db: Session, client: ClientUpdateScheme):
    with engine.begin() as conn:
        conn.execute(
            update(Client).values(**client.dict())
            .where(Client.id == client.id)
        )
    result = get_client(db, client.id)
    return result


def delete_client(db: Session, client_id: int):
    result = get_client(db, client_id)
    if result:
        with engine.begin() as conn:
            conn.execute(delete(Client).where(Client.id == client_id))
    return result
