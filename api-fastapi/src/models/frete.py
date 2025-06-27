from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from . import Base


class Frete(Base):
    __tablename__ = 'frete'

    codigo_frete = Column(Integer, primary_key=True, autoincrement=True)
    codigo_cidade = Column(Integer, ForeignKey("cidade.codigo_cidade"))
    codigo_cliente = Column(Integer, ForeignKey("cliente.codigo_cliente"))
    descricao = Column(String)
    peso = Column(Float)
    valor = Column(Float)
    created_at = Column(DateTime, server_default=func.now())

    cliente = relationship("Cliente", back_populates="fretes")
    cidade = relationship("Cidade", back_populates="fretes")