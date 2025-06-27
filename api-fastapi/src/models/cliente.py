from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from . import Base

class Cliente(Base):
    __tablename__ = 'cliente'

    codigo_cliente = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    endereco = Column(String)
    telefone = Column(String)
    created_at = Column(DateTime, server_default=func.now())

    fretes = relationship("Frete", back_populates="cliente")