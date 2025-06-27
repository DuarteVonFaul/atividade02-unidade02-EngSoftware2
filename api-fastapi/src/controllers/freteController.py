from fastapi import HTTPException, status
from typing import List

from src.schemas.freteSchemas import FreteBase, FreteRead, CidadeMaisFrete
from src.services.freteService import FreteService


def resource(router, db):
    @router.post("/frete", response_model=FreteRead, status_code=status.HTTP_201_CREATED)
    def incluir_frete(frete_data: FreteBase):
        service = FreteService(db)
        try:
            frete = service.cadastrar_frete(frete_data)
            return frete
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))


    @router.get("/frete/cliente/{cliente_id}", response_model=List[FreteRead])
    def consultar_fretes_por_cliente(cliente_id: int):
        service = FreteService(db)
        fretes = service.frete_repo.search_findAll_by_buyer(cliente_id)
        return fretes


    @router.get("/frete/maior-valor", response_model=FreteRead)
    def frete_mais_caro():
        service = FreteService(db)
        frete = service.frete_maior_valor()
        if not frete:
            raise HTTPException(status_code=404, detail="Nenhum frete encontrado")
        return frete


    @router.get("/frete/cidade-maior-frete", response_model=CidadeMaisFrete)
    def cidade_com_mais_fretes():
        service = FreteService(db)
        cidade = service.cidade_com_mais_fretes()
        if not cidade:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhuma cidade encontrada")
        return cidade