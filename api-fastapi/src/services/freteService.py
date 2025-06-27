from src.schemas.freteSchemas import FreteBase
from src.models.frete import Frete
from src.repositories.clienteRepository import ClienteRepository
from src.repositories.cidadeRepository import CidadeRepository
from src.repositories.freteRepository import FreteRepository
from sqlalchemy.exc import NoResultFound


class FreteService:
    VALOR_FIXO = 10.0

    def __init__(self, db):
        self.db = db
        self.frete_repo = FreteRepository(db)
        self.cliente_repo = ClienteRepository(db)
        self.cidade_repo = CidadeRepository(db)

    def cadastrar_frete(self, frete_data: FreteBase) -> Frete:

        cliente = self.cliente_repo.get_by_id(frete_data.codigo_cliente)
        if not cliente:
            raise ValueError("Cliente não encontrado")

        cidade = self.cidade_repo.get_by_id(frete_data.codigo_cidade)
        if not cidade:
            raise ValueError("Cidade não encontrada")

        valor_frete = frete_data.peso * self.VALOR_FIXO + cidade.taxa

        frete_data.valor = valor_frete

        return self.frete_repo.add(frete_data)

    def frete_maior_valor(self) -> Frete:
        return self.frete_repo.get_maior_valor()

    def cidade_com_mais_fretes(self):
        return self.frete_repo.get_cidade_com_mais_fretes()