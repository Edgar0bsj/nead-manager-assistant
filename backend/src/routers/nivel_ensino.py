from typing import Optional
from fastapi import APIRouter, Depends, status, Path
from src.apps.nivel_ensino.nivel_ensino_dto import NivelEnsinoInput, NivelEnsinoOutput
from src.apps.nivel_ensino.nivel_ensino_controller import NivelEnsinoController

router = APIRouter(prefix="/nivel-ensino")


def get_depends():
    return NivelEnsinoController()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=NivelEnsinoOutput,
)
def create(
    payload: NivelEnsinoInput,
    controller: NivelEnsinoController = Depends(get_depends),
):
    return controller.create(payload)


@router.get("/export-csv", status_code=status.HTTP_200_OK)
def save_to_csv(
    filter_status: Optional[bool] = True,
    controller: NivelEnsinoController = Depends(get_depends),
):
    return controller.export_csv(filter_status)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=NivelEnsinoOutput,
)
def read_one(
    id: int = Path(..., title="ID do codigo", ge=1),
    controller: NivelEnsinoController = Depends(get_depends),
):
    return controller.read_one(id)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[NivelEnsinoOutput],
)
def read_all(
    controller: NivelEnsinoController = Depends(get_depends),
):
    return controller.read_all()


@router.post(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=NivelEnsinoOutput,
)
def update(
    payload: NivelEnsinoInput,
    id: int = Path(..., title="ID do codigo", ge=1),
    controller: NivelEnsinoController = Depends(get_depends),
):
    return controller.update(id, payload)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    id: int = Path(..., title="ID da entidade", ge=1),
    controller: NivelEnsinoController = Depends(get_depends),
):
    return controller.delete(id)
