from sqlalchemy import func
from ..models.cidade import Cidade

from ..models.frete import Frete
from ..schemas.freteSchemas import FreteBase, CidadeMaisFrete
from typing import List
        



class FreteRepository:

    def __init__(self, conn):
        self.conn = conn

    def add(self, frete_data: FreteBase) -> Frete:
        novo_frete = Frete(**frete_data.dict())
        self.conn.add(novo_frete)
        self.conn.commit()
        self.conn.refresh(novo_frete)
        return novo_frete

    def search_findAll_by_buyer(self, codigo_cliente: int) -> List[Frete]:
        return self.conn.query(Frete).filter(Frete.codigo_cliente == codigo_cliente).all()
    
    def get_maior_valor(self) -> Frete | None:
        return self.conn.query(Frete).order_by(Frete.valor.desc()).first()

    def get_cidade_com_mais_fretes(self) -> CidadeMaisFrete:


        result = (
            self.conn.query(Frete.codigo_cidade, func.count(Frete.codigo_frete).label("total"))
            .group_by(Frete.codigo_cidade)
            .order_by(func.count(Frete.codigo_frete).desc())
            .first()
        )

        if result:
            cidade_id, total = result
            cidade = self.conn.query(Cidade).filter(Cidade.codigo_cidade == cidade_id).first()
            return CidadeMaisFrete(nome = cidade.nome, quantidade = total)

        return None
    
    def search_findAll_by_buyer(self, codigo_cliente: int) -> list[Frete]:
        return self.conn.query(Frete).filter(Frete.codigo_cliente == codigo_cliente).all()