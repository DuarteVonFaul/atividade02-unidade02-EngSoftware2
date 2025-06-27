from pydantic import BaseModel, constr, field_validator
from typing import Optional


class FreteBase(BaseModel):
    descricao: constr(min_length=1, max_length=30)
    peso: float
    valor: float
    codigo_cliente: int
    codigo_cidade: int

    @field_validator('peso', 'valor')
    def valores_positivos(cls, v):
        if v < 0:
            raise ValueError("Peso e valor devem ser positivos")
        return v


class FreteCreate(FreteBase):
    pass


class FreteRead(FreteBase):
    codigo_frete: int

    class Config:
        from_attributes = True

    
class CidadeMaisFrete(BaseModel):
    nome:str
    quantidade:int