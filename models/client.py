from typing import List
from sqlalchemy import Integer, String, Column

from .base import Base


class Client(Base):
    __tablename__ = "client"

    id = Column(
        Integer, primary_key=True, index=True
    )
    cpf_cnpj = Column(
        String(length=18), index=True
    )
    full_name = Column(
        String(length=120)
    )
    address = Column(
        String(length=320)
    )

    def _table(self):
        return self

