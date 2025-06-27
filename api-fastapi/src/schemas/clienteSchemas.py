from pydantic import BaseModel, constr, field_validator
from typing import Optional


class ClienteBase(BaseModel):
    nome: constr(min_length=1, max_length=30)
    endereco: constr(min_length=1, max_length=30)
    telefone: constr(min_length=1, max_length=30)


class ClienteCreate(ClienteBase):
    pass


class ClienteRead(ClienteBase):
    codigo_cliente: int

    class Config:
        from_attributes = True