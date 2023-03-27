from pydantic import BaseModel, Field


class Client(BaseModel):
    full_name: str = Field(str, max_length=120)
    cpf_cnpj: str = Field(str, max_length=18) 
    address: str = Field(str, max_length=320)

    class Config:
        orm_mode = True


class ClientUpdateScheme(BaseModel):
    id: int
    full_name: str = Field(str, max_length=120)
    cpf_cnpj: str = Field(str, max_length=18) 
    address: str = Field(str, max_length=320)

    class Config:
        orm_mode = True
