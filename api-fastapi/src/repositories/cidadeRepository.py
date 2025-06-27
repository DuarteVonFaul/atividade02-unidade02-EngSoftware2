from ..models.cidade import Cidade
from ..schemas.cidadeSchemas import CidadeBase 


class CidadeRepository:

    def __init__(self, conn):
        self.conn = conn

    def add(self, cidade: CidadeBase) -> Cidade:
        nova_cidade = Cidade(**cidade.dict())
        self.conn.add(nova_cidade)
        self.conn.commit()
        self.conn.refresh(nova_cidade)
        return nova_cidade
    
    def get_by_id(self, cidade_id: int) -> Cidade | None:
        return self.conn.query(Cidade).filter(Cidade.codigo_cidade == cidade_id).first()

    def search_by_name(self, name: str) -> Cidade | None:
        return self.conn.query(Cidade).filter(Cidade.nome == name).first()