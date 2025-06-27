from . import *
import pytest
from pydantic import ValidationError

def test_cliente_database_insert(session):
    
    with session:
        reposity = ClienteRepository(session)
        cliente_data = ClienteBase(nome="João", endereco="Rua A", telefone="123456")
        cliente = reposity.add(cliente_data)


    assert cliente.codigo_cliente == 1
    
    ...


def test_cliente_database_search_by_phoneNumber(session):
    
    with session:
        reposity = ClienteRepository(session)
        reposity.add(ClienteBase(nome="Maria", 
                                 endereco="Rua B", 
                                 telefone="999934"))
        reposity.add(ClienteBase(nome="Carla", 
                                 endereco="Rua B", 
                                 telefone="9991234"))
        reposity.add(ClienteBase(nome="Bruna", 
                                 endereco="Rua B", 
                                 telefone="123456"))
        
        cliente = reposity.search_by_phoneNumber('123456')


    assert cliente.codigo_cliente == 3
    
    ...

def test_cliente_schema_invalid_nome():
    with pytest.raises(ValidationError):
        ClienteBase(nome="", endereco="Rua A", telefone="123456")

def test_cliente_schema_invalid_endereco():
    with pytest.raises(ValidationError):
        ClienteBase(nome="Lucar", endereco="", telefone="123456")

def test_cliente_schema_invalid_telefone():
    with pytest.raises(ValidationError):
        ClienteBase(nome="Lucas", endereco="Rua A", telefone="")


def test_cidade_database_insert(session):
    with session:
        reposity = CidadeRepository(session)
        cidade_data = CidadeBase(nome="São Paulo", UF="SP", taxa=10.5)
        cidade = reposity.add(cidade_data)

    assert cidade.codigo_cidade is not None
    assert cidade.nome == "São Paulo"
    assert cidade.UF == "SP"
    assert cidade.taxa == 10.5

def test_cidade_database_search_by_name(session):
    with session:
        reposity = CidadeRepository(session)
        cidade_data = CidadeBase(nome="Curitiba", UF="PR", taxa=12.3)
        reposity.add(cidade_data)

    cidade = reposity.search_by_name("Curitiba")

    assert cidade is not None
    assert cidade.nome == "Curitiba"
    assert cidade.UF == "PR"


def test_cidade_schema_invalid_taxa():
    with pytest.raises(ValidationError):
        CidadeBase(nome="Rio", UF="RJ", taxa=-5.0)

def test_cidade_schema_invalid_nome():
    with pytest.raises(ValidationError):
        CidadeBase(nome="", UF="RJ", taxa=2.0)

def test_cidade_schema_invalid_uf():
    with pytest.raises(ValidationError):
        CidadeBase(nome="Belo Horizonte", UF="MGG", taxa=1.0)


def test_frete_database_insert(session):
    with session:
        repositoy = FreteRepository(session)
        frete_data = FreteBase(
            descricao="Carga 01",
            peso=10.0,
            valor=150.0,
            codigo_cliente=1,
            codigo_cidade=1
        )

        frete = repositoy.add(frete_data)

    assert frete.codigo_frete is not None
    assert frete.descricao == "Carga 01"
    assert frete.valor == 150.0
    assert frete.codigo_cliente == 1
    assert frete.codigo_cidade == 1

def test_frete_database_search_findAll_by_buyer(session):

    with session:
        repositoy = FreteRepository(session)

        repositoy.add(FreteBase(descricao="F1", peso=5, valor=100, codigo_cliente=2, codigo_cidade=1))
        repositoy.add(FreteBase(descricao="F2", peso=10, valor=200, codigo_cliente=2, codigo_cidade=2))
        repositoy.add(FreteBase(descricao="F3", peso=3, valor=50, codigo_cliente=3, codigo_cidade=1))

        fretes_cliente_2 = repositoy.search_findAll_by_buyer(2)

    assert len(fretes_cliente_2) == 2
    assert all(f.codigo_cliente == 2 for f in fretes_cliente_2)

def test_frete_schema_invalid_peso():
    with pytest.raises(ValidationError):
        FreteBase(
            descricao="Negativo",
            peso=-1.0,
            valor=100.0,
            codigo_cliente=1,
            codigo_cidade=1
        )

def test_frete_schema_invalid_valor():
    with pytest.raises(ValidationError):
        FreteBase(
            descricao="Negativo",
            peso=2.0,
            valor=-50.0,
            codigo_cliente=1,
            codigo_cidade=1
        )

def test_frete_schema_invalid_descricao():
    with pytest.raises(ValidationError):
        FreteBase(
            descricao="",
            peso=1.0,
            valor=10.0,
            codigo_cliente=1,
            codigo_cidade=1
        )