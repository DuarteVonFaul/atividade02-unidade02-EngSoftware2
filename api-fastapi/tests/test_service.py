from . import *
import pytest
from pydantic import ValidationError


# ---------- Utilitários ---------- #

def criar_cliente(session):
    cliente = Cliente(nome="João", endereco="Rua A", telefone="123")
    session.add(cliente)
    session.commit()
    return cliente

def criar_cidade(session, nome="São Paulo", taxa=5.0):
    cidade = Cidade(nome=nome, UF="SP", taxa=taxa)
    session.add(cidade)
    session.commit()
    return cidade



# ---------- Testes ---------- #

def test_cadastrar_frete_com_cliente_ou_cidade_invalida(session):
    service = FreteService(session)

    frete_data = FreteBase(
        descricao="Teste",
        peso=2.0,
        valor=0.0,
        codigo_cliente=999,
        codigo_cidade=999
    )

    with pytest.raises(ValueError, match="Cliente não encontrado"):
        service.cadastrar_frete(frete_data)

    cliente = criar_cliente(session)
    frete_data.codigo_cliente = cliente.codigo_cliente

    with pytest.raises(ValueError, match="Cidade não encontrada"):
        service.cadastrar_frete(frete_data)

def test_cadastrar_frete_calculo_valor(session):
    service = FreteService(session)

    cliente = criar_cliente(session)
    cidade = criar_cidade(session, taxa=7.5)

    frete_data = FreteBase(
        descricao="Entrega TV",
        peso=3.0,
        valor=0.0,
        codigo_cliente=cliente.codigo_cliente,
        codigo_cidade=cidade.codigo_cidade
    )

    frete = service.cadastrar_frete(frete_data)

    assert frete.valor == pytest.approx(3.0 * 10.0 + 7.5)
    assert frete.descricao == "Entrega TV"

def test_frete_maior_valor(session):
    service = FreteService(session)
    cliente = criar_cliente(session)
    cidade = criar_cidade(session)


    f1 = Frete(
        descricao="Barato",
        peso=1.0,
        valor=20.0,
        codigo_cliente=cliente.codigo_cliente,
        codigo_cidade=cidade.codigo_cidade
    )

    f2 = Frete(
        descricao="Caro",
        peso=5.0,
        valor=60.0,
        codigo_cliente=cliente.codigo_cliente,
        codigo_cidade=cidade.codigo_cidade
    )

    session.add_all([f1, f2])
    session.commit()

    frete = service.frete_maior_valor()
    assert frete.descricao == "Caro"
    assert frete.valor == 60.0

def test_cidade_com_mais_fretes(session):
    service = FreteService(session)
    cliente = criar_cliente(session)

    cidade1 = criar_cidade(session, nome="Campinas")
    cidade2 = criar_cidade(session, nome="Ribeirão Preto")


    for _ in range(3):
        session.add(Frete(
            descricao="Entrega",
            peso=2,
            valor=25,
            codigo_cliente=cliente.codigo_cliente,
            codigo_cidade=cidade1.codigo_cidade
        ))


    for _ in range(2):
        session.add(Frete(
            descricao="Entrega",
            peso=2,
            valor=25,
            codigo_cliente=cliente.codigo_cliente,
            codigo_cidade=cidade2.codigo_cidade
        ))

    session.commit()

    result = service.cidade_com_mais_fretes()
    assert isinstance(result, CidadeMaisFrete)
    assert result.nome == "Campinas"
    assert result.quantidade == 3