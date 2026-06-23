from fastapi import APIRouter, Depends, status, Path

from src.apps.polos.polos_controller import PoloController
from src.apps.polos.polos_dto import PoloOutput, PoloInput

router = APIRouter(prefix="/polo")


def get_depends():
    return PoloController()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=PoloOutput,
)
def create(
    payload: PoloInput,
    controller: PoloController = Depends(get_depends),
):
    return controller.create(payload)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=PoloOutput,
)
def read_one(
    id: int = Path(..., ge=1),
    controller: PoloController = Depends(get_depends),
):
    return controller.read_one(id)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[PoloOutput],
)
def read_all(controller: PoloController = Depends(get_depends)):
    return controller.read_all()


@router.put(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=PoloOutput,
)
def update(
    payload: PoloInput,
    id: int = Path(..., ge=1),
    controller: PoloController = Depends(get_depends),
):
    return controller.update(id, payload)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    id: int = Path(..., title="ID do Polo", ge=1),
    controller: PoloController = Depends(get_depends),
):
    return controller.delete(id)
