from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from . import Base

class Cidade(Base):
    __tablename__ = 'cidade'

    codigo_cidade = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    UF = Column(String)
    taxa = Column(Float)
    created_at = Column(DateTime, server_default=func.now())

    fretes = relationship("Frete", back_populates="cidade")