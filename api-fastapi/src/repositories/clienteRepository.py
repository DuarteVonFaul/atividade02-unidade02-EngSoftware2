from ..models.cliente import Cliente
from ..schemas.clienteSchemas import ClienteBase 

class ClienteRepository:

    def __init__(self, conn):
        self.conn = conn

    def add(self, cliente_data: ClienteBase) -> Cliente:
        novo_cliente = Cliente(**cliente_data.dict()) 
        self.conn.add(novo_cliente)
        self.conn.commit()
        self.conn.refresh(novo_cliente)
        return novo_cliente
    
    def get_by_id(self, cliente_id: int) -> Cliente | None:
        return self.conn.query(Cliente).filter(Cliente.codigo_cliente == cliente_id).first()

    def search_by_phoneNumber(self, telefone: str) -> Cliente:
        return self.conn.query(Cliente).filter(Cliente.telefone == telefone).first()