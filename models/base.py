from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Bd_Connect@localhost:5432/push_and_get"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

Session = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)
Base = declarative_base()
