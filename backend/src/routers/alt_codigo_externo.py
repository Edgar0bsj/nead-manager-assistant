from typing import Optional

from fastapi import APIRouter, Depends, status, Path

from src.apps.alt_codigo_externo.alt_codigo_externo_controller import (
    AlteracaoCodigoExternoController,
)
from src.apps.alt_codigo_externo.alt_codigo_externo_dto import (
    AlteracaoCodigoExternoOutput,
    AlteracaoCodigoExternoInput,
)

router = APIRouter(prefix="/alt-codigos-externos")


def get_depends():
    return AlteracaoCodigoExternoController()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=AlteracaoCodigoExternoOutput,
)
def create(
    payload: AlteracaoCodigoExternoInput,
    controller: AlteracaoCodigoExternoController = Depends(get_depends),
):
    return controller.create(payload)


@router.get("/to-csv", status_code=status.HTTP_200_OK)
def save_to_csv(
    filter_status: Optional[bool] = True,
    filter_sistema: Optional[str] = None,
    filter_unidade: Optional[str] = None,
    controller: AlteracaoCodigoExternoController = Depends(get_depends),
):
    return controller.save_to_csv(filter_status, filter_sistema, filter_unidade)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=AlteracaoCodigoExternoOutput,
)
def read_one(
    id: int = Path(..., title="ID do codigo", ge=1),
    controller: AlteracaoCodigoExternoController = Depends(get_depends),
):
    return controller.read_one(id)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[AlteracaoCodigoExternoOutput],
)
def read_all(
    name_entity: Optional[str] = None,
    controller: AlteracaoCodigoExternoController = Depends(get_depends),
):
    return controller.read_all(name_entity)


@router.put(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=AlteracaoCodigoExternoOutput,
)
def update(
    payload: AlteracaoCodigoExternoInput,
    id: int = Path(..., title="ID do codigo", ge=1),
    controller: AlteracaoCodigoExternoController = Depends(get_depends),
):
    return controller.update(id, payload)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    id: int = Path(..., title="ID do codigo", ge=1),
    controller: AlteracaoCodigoExternoController = Depends(get_depends),
):
    return controller.delete(id)
