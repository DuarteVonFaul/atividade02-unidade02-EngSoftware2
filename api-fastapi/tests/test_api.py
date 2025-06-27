from http import HTTPStatus

def test_incluir_frete(client):
    frete_data = {
        "descricao": "Entrega teste",
        "peso": 5.0,
        "valor": 0.0,  # será calculado no serviço
        "codigo_cliente": 1,
        "codigo_cidade": 1
    }
    response = client.post("/frete", json=frete_data)
    assert response.status_code == HTTPStatus.CREATED
    data = response.json()
    assert data["descricao"] == frete_data["descricao"]
    assert data["codigo_cliente"] == frete_data["codigo_cliente"]
    assert data["codigo_cidade"] == frete_data["codigo_cidade"]
    assert data["valor"] > 0

def test_incluir_frete_cliente_invalido(client):
    frete_data = {
        "descricao": "Entrega teste",
        "peso": 5.0,
        "valor": 0.0,
        "codigo_cliente": 9999,  # cliente inexistente
        "codigo_cidade": 1
    }
    response = client.post("/frete", json=frete_data)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert "Cliente não encontrado" in response.json()["detail"]

def test_consultar_fretes_por_cliente(client):
    response = client.get("/frete/cliente/1")
    assert response.status_code == HTTPStatus.OK
    fretes = response.json()
    assert isinstance(fretes, list)
    # Se quiser, verifica se todos fretes são do cliente 1
    for frete in fretes:
        assert frete["codigo_cliente"] == 1

def test_frete_mais_caro(client):
    response = client.get("/frete/maior-valor")
    if response.status_code == HTTPStatus.NOT_FOUND:
        assert response.json()["detail"] == "Nenhum frete encontrado"
    else:
        assert response.status_code == HTTPStatus.OK
        data = response.json()
        assert "valor" in data
        assert data["valor"] >= 0

def test_cidade_com_mais_fretes(client):
    response = client.get("/frete/cidade-maior-frete")
    if response.status_code == HTTPStatus.NOT_FOUND:
        assert response.json()["detail"] == "Nenhuma cidade encontrada"
    else:
        assert response.status_code == HTTPStatus.OK
        data = response.json()
        assert "nome" in data
        assert "quantidade" in data
        assert data["quantidade"] >= 0