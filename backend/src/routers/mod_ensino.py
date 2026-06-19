from typing import Optional
from fastapi import APIRouter, Depends, status, Path
from src.apps.mod_ensino.mod_ensino_dto import ModEnsinoInput, ModEnsinoOutput
from src.apps.mod_ensino.mod_ensino_controller import ModEnsinoController

router = APIRouter(prefix="/mods-ensino")


def get_depends():
    return ModEnsinoController()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=ModEnsinoOutput,
)
def create(
    payload: ModEnsinoInput,
    controller: ModEnsinoController = Depends(get_depends),
):
    return controller.create(payload)


@router.get("/export-csv", status_code=status.HTTP_200_OK)
def save_to_csv(
    filter_status: Optional[bool] = True,
    controller: ModEnsinoController = Depends(get_depends),
):
    return controller.export_csv(filter_status)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ModEnsinoOutput,
)
def read_one(
    id: int = Path(..., title="ID do codigo", ge=1),
    controller: ModEnsinoController = Depends(get_depends),
):
    return controller.read_one(id)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[ModEnsinoOutput],
)
def read_all(
    controller: ModEnsinoController = Depends(get_depends),
):
    return controller.read_all()


@router.put(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ModEnsinoOutput,
)
def update(
    payload: ModEnsinoInput,
    id: int = Path(..., title="ID do codigo", ge=1),
    controller: ModEnsinoController = Depends(get_depends),
):
    return controller.update(id, payload)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    id: int = Path(..., title="ID da entidade", ge=1),
    controller: ModEnsinoController = Depends(get_depends),
):
    return controller.delete(id)
