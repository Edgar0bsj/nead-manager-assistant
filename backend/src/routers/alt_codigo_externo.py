from fastapi import APIRouter, Depends, status, Path
from src.apps.alt_codigo_externo.alt_codigo_externo_dto import (
    AlteracaoCodigoExternoInput,
)
from src.apps.alt_codigo_externo.alt_codigo_externo_controller import (
    AlteracaoCodigoExternoController,
)
from src.apps.alt_codigo_externo.alt_codigo_externo_dto import (
    AlteracaoCodigoExternoOutput,
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
def save_to_csv(controller: AlteracaoCodigoExternoController = Depends(get_depends)):
    return controller.save_to_csv()


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
    controller: AlteracaoCodigoExternoController = Depends(get_depends),
):
    return controller.read_all()


@router.post(
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
