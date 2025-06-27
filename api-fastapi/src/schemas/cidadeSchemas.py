from pydantic import BaseModel, constr, field_validator
from typing import Optional

class CidadeBase(BaseModel):
    nome: constr(min_length=1, max_length=30)
    UF: constr(min_length=2, max_length=2)
    taxa: float

    @field_validator('taxa')
    def taxa_nao_negativa(cls, v):
        if v < 0:
            raise ValueError("Taxa não pode ser negativa")
        return v


class CidadeCreate(CidadeBase):
    pass


class CidadeRead(CidadeBase):
    codigo_cidade: int

    class Config:
        from_attributes = True