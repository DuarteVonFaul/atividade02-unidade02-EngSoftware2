from ..models.cliente import Cliente


class ClienteRepository:

    def __init__(self, conn):
        pass

    def add(self, nome:str, endereco:str, telefone:str) -> Cliente :
        ...

    def search_by_phoneNumber(self, telefone:str) -> Cliente :
        ...